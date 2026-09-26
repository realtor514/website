#!/usr/bin/env python3
"""Genere la fiche de faits d un article francais, pour une consigne de traduction.

    python tools/trad_spec.py mon-article                 un article
    python tools/trad_spec.py slug1 slug2 slug3           plusieurs
    python tools/trad_spec.py --tous-les-drafts           tous les brouillons fr

Pourquoi ce fichier existe. Les consignes de traduction des lots 7 a 10 ont ete
ecrites en listant les faits a preserver sous forme de listes plates: « les
articles 3, 4, 4.1, 5 », « les montants 96 $, 146 $, 500 $ ». A chaque lot, les
traducteurs ont trouve les memes erreurs, et toujours la meme classe d erreur:
**une liste plate perd le rattachement.** L article 4.1 se retrouve attribue a
Montreal alors qu il appartient au reglement de Laval, le 250 $ passe d une ville
a l autre, un numero d un autre article s invite dans la liste.

La sortie de ce script montre chaque fait **dans sa phrase**. Le traducteur voit
donc a quoi le numero se rattache, et ma liste ne peut plus le tromper. Les
quatre premiers lots ont coute environ une douzaine de corrections a envoyer en
cours de route; ce script les supprime a la source.

Ce script ne remplace pas le jugement: la consigne doit encore dire ce qui est
le coeur de l article, ce qu il ne faut pas aplatir, et quels aveux d ignorance
sont volontaires. Il remplace seulement la partie mecanique, celle que je faisais
mal.
"""

import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FR = ROOT / "content" / "fr" / "articles"
META = ROOT / "meta" / "fr"

CAT = {
    "Guide de l'acheteur": ("Buyer's Guide", "Guía del Comprador", "دليل المشتري"),
    "Guide du vendeur": ("Seller's Guide", "Guía del Vendedor", "دليل البائع"),
    "Financement": ("Finance", "Financiamiento", "تمويل"),
    "Investissement": ("Investment", "Inversión", "استثمار"),
    "Immobilier 101": ("Real Estate 101", "Inmobiliaria 101", "عقارات 101"),
    "Guide pratique": ("Practical Guide", "Guía práctica", "دليل عملي"),
    "Analyse de marche": ("Market Analysis", "Análisis de Mercado", "تحليل السوق"),
    "Analyse de marché": ("Market Analysis", "Análisis de Mercado", "تحليل السوق"),
}

# Ce qui doit survivre mot pour mot a une traduction.
MOTIFS = [
    ("article de loi", r"\barticles?\s+\d{1,4}(?:\.\d+)*(?:\s*(?:a|et|,)\s*\d{1,4}(?:\.\d+)*)*"),
    ("reglement", r"\b(?:RCG\s*)?(?:L-)?\d{2,3}-\d{3,4}\b"),
    ("norme", r"\b(?:BNQ|CAN/CSA|CSA|CTQ)[\s/-]?[A-Z]?[\d.-]{2,12}\b"),
    ("formulaire", r"\b(?:DV|CCVE|CCA|CCADI)\s*\d{5}\b|\bD\d{1,2}\.\d{1,2}\b"),
    ("montant", r"\d[\d  ]*(?:,\d+)?\s*\$"),
    ("pourcentage", r"\d+(?:,\d+)?\s*%"),
    ("date", r"(?:1er|\d{1,2})\s+(?:janvier|f[ée]vrier|mars|avril|mai|juin|juillet"
              r"|ao[uû]t|septembre|octobre|novembre|d[ée]cembre)\s+\d{4}"),
    # Les decimales et les fourchettes doivent etre captees ENTIERES. Une
    # premiere version cadrait sur `\b\d{1,4}`, donc « 10,3 mois » ressortait
    # « 3 mois » et « 4 a 6 heures » ressortait « 6 heures ». Un traducteur
    # lisant la fiche seule aurait recopie le mauvais chiffre.
    ("delai", r"\d{1,4}(?:[,.]\d+)?(?:\s*(?:a|à|ou|et)\s*\d{1,4}(?:[,.]\d+)?)?"
              r"\s+(?:jours?|mois|ans?|annees?|années?|semaines?|heures?|minutes?)\b"),
    ("unite", r"\d+(?:[,.]\d+)?(?:\s*(?:a|à)\s*\d+(?:[,.]\d+)?)?"
              r"\s*(?:¢/kWh|¢/jour|¢|g/h|\$/m2|m2|m²|kWh|mm|cm|BTU|°C)"),
]

# Un aveu d ignorance est un choix editorial, pas un oubli: il doit survivre.
AVEUX = re.compile(
    r"(aucune? (?:source|norme|donnee|statistique|bareme|tarif|etude|organisme|"
    r"page|regle|chiffre)[^.]{0,160}\.|"
    r"ne (?:permet|publie|chiffre|existe|precise|tranche)[^.]{0,160}\.|"
    r"je n ai pas (?:trouve|pu)[^.]{0,160}\.|"
    r"n est pas (?:public|chiffrable|verifiable)[^.]{0,160}\.)", re.I)


def parse(slug):
    p = FR / (slug + ".md")
    if not p.is_file():
        return None
    raw = p.read_text(encoding="utf-8")
    fin = raw.find("\n---", 3)
    fm, body = raw[3:fin], raw[fin + 4:]
    meta = {}
    for ligne in fm.splitlines():
        if ":" in ligne and not ligne.startswith((" ", "-", "#")):
            k, _, v = ligne.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    return meta, body


def phrases(body):
    """Decoupe en phrases, en gardant les cellules de tableau entieres.

    Une cellule de tableau n est pas une phrase mais elle porte souvent le
    rattachement le plus precis: « Laval (art. 8) | 160 jours | 500 $ ».
    """
    out, para = [], []

    def vider():
        if not para:
            return
        texte = " ".join(para)
        for ph in re.split(r"(?<=[.!?])\s+", texte):
            if ph.strip():
                out.append(("texte", ph.strip()))
        para.clear()

    for ligne in body.splitlines():
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#"):
            vider()
            continue
        if re.match(r"^\|[\s:|-]+\|$", ligne):
            vider()
            continue
        if ligne.startswith("|"):
            vider()
            out.append(("tableau", ligne))
            continue
        # Les lignes du corps sont coupees a 80 colonnes: il faut recoller le
        # paragraphe avant de decouper en phrases, sinon chaque fait apparait
        # dans un fragment tronque qui ne montre plus son rattachement.
        para.append(ligne)
    vider()
    return out


def fiche(slug):
    lu = parse(slug)
    if not lu:
        print("  introuvable: %s" % slug)
        return
    meta, body = lu
    cat = meta.get("category", "")
    trad = CAT.get(cat, ("?", "?", "?"))

    print("=" * 74)
    print("## %s" % slug)
    print()
    print("- translationKey `%s`, date et lastmod **%s**"
          % (meta.get("translationKey", "?"), meta.get("date", "?")))
    print("- categorie: en `%s`, es `%s`, ar `%s`" % trad)
    if meta.get("needs_expert_review", "").lower() == "true":
        print("- `needs_expert_review: true` present, a recopier")
    else:
        print("- **pas de `needs_expert_review`**: ne l ajoutez pas")

    ph = phrases(body)

    # Chaque fait, dans sa phrase. C est tout l interet du script.
    vus, lignes = set(), []
    for genre, texte in ph:
        trouves = []
        for nom, motif in MOTIFS:
            for m in re.finditer(motif, texte, re.I):
                v = re.sub(r"\s+", " ", m.group(0)).strip()
                if (nom, v) not in vus:
                    vus.add((nom, v))
                    trouves.append(v)
        if trouves:
            court = texte if len(texte) <= 300 else texte[:297] + "..."
            lignes.append((genre, court, trouves))

    print()
    print("### Faits a preserver, chacun dans sa phrase")
    print()
    print("Ne deplacez aucun de ces elements d une phrase a l autre. Le")
    print("rattachement compte autant que la valeur: une ville, un reglement, un")
    print("organisme. Si un element vous parait mal place, c est le francais qui")
    print("tranche, pas cette fiche.")
    print()
    for genre, texte, trouves in lignes:
        marque = "TABLEAU " if genre == "tableau" else ""
        print("- %s%s" % (marque, texte))
        print("  -> %s" % " | ".join(trouves))

    aveux = []
    for _, texte in ph:
        for m in AVEUX.finditer(texte):
            a = re.sub(r"\s+", " ", m.group(0)).strip()
            if a not in aveux:
                aveux.append(a)
    if aveux:
        print()
        print("### Aveux d ignorance, volontaires, a garder tels quels")
        print()
        print("Ce sont des choix editoriaux, pas des trous a combler. Une")
        print("traduction qui les remplace par une estimation prudente est fausse.")
        print()
        for a in aveux:
            print("- %s" % a)

    jp = META / (slug + ".json")
    if jp.is_file():
        try:
            j = json.loads(jp.read_text(encoding="utf-8"))
        except ValueError:
            j = {}
        cl = j.get("claims_needing_review") or []
        if cl:
            print()
            print("### Reserves consignees (%d)" % len(cl))
            print()
            print("Elles expliquent pourquoi certaines choses ne sont pas dites.")
            print()
            for c in cl:
                print("- %s" % re.sub(r"\s+", " ", str(c))[:240])

    liens = sorted(set(re.findall(r"\]\((/[^)]+)\)", body)))
    tableaux = sum(1 for l in body.splitlines()
                   if re.match(r"^\s*\|[\s:|-]+\|\s*$", l))
    print()
    print("### Structure")
    print()
    print("- %d H2, %d tableau(x): reproduisez ces nombres, pas un compte annonce"
          % (len(re.findall(r"^##\s", body, re.M)), tableaux))
    print("- liens du francais, a convertir vers votre langue: %s"
          % ", ".join(liens))
    print()


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    if args[0] == "--tous-les-drafts":
        slugs = []
        for p in sorted(FR.glob("*.md")):
            if re.search(r"^draft:\s*true", p.read_text(encoding="utf-8")[:900],
                         re.M):
                slugs.append(p.stem)
        if not slugs:
            print("Aucun brouillon francais.")
            return
    else:
        slugs = [a[:-3] if a.endswith(".md") else a for a in args]

    print("# Fiches de faits, generees par tools/trad_spec.py")
    print()
    print("Lisez `state/BRIEF_TRADUCTION.md` en entier avant de commencer.")
    print("**Le fichier francais reste la seule source de verite.**")
    print()
    for s in slugs:
        fiche(s)


if __name__ == "__main__":
    main()
