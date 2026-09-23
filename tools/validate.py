#!/usr/bin/env python3
"""Validation de contenu, en remplacement du `hugo build` (hugo n est pas installe ici).

Le site est bati par GitHub Actions avec Hugo 0.155.0. En local, ce script verifie
tout ce qui peut casser une page ou enfreindre une regle du projet.

    python tools/validate.py drafts/fr/*.md
    python tools/validate.py content/fr/articles/mon-article.md

Sortie: une ligne par fichier, puis le total. Code de sortie 1 s il y a une erreur.
"""

import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
LANGS = ["fr", "en", "es", "ar"]
TODAY = datetime.date.today()

REQUIRED = ["title", "date", "lastmod", "translationKey", "category", "description", "image", "draft"]

# Les categories sont LOCALISEES sur ce site: un article anglais porte
# "Buyer's Guide", pas "Guide de l'acheteur". Valeurs relevees dans content/.
CATEGORIES = {
    "fr": {"Guide de l'acheteur", "Guide du vendeur", "Financement", "Investissement",
           "Immobilier 101", "Analyse de marché", "Analyse de marche", "Guide pratique",
           "Conseils honnêtes"},
    "en": {"Buyer's Guide", "Seller's Guide", "Finance", "Financing", "Investment",
           "Real Estate 101", "Immobilier 101", "Practical Guide", "Market Analysis",
           "Market Insights", "Honest Advice"},
    "es": {"Guía del Comprador", "Guía del Vendedor", "Financiamiento", "Inversión",
           "Inmobiliaria 101", "Guía práctica", "Análisis de Mercado"},
    "ar": {"دليل المشتري", "دليل البائع", "تمويل", "التمويل", "استثمار",
           "عقارات 101", "دليل عملي", "تحليل السوق", "نصيحة صادقة"},
}

# Le formulaire et la page contact ont un slug propre a chaque langue.
FORM_PATH = {"fr": "/formulaire/", "en": "/en/form/",
             "es": "/es/formulario/", "ar": "/ar/istimara/"}
CONTACT_PATH = {"fr": "/contact/", "en": "/en/contact/",
                "es": "/es/contacto/", "ar": "/ar/tawasul/"}

# Chemins hors /articles/ que le site expose vraiment.
STATIC_PATHS = {"/formulaire/", "/contact/", "/about/", "/buyer/", "/seller/", "/listings/",
                "/articles/", "/secteurs/", "/tools/", "/confidentialite/", "/merci/",
                "/tools/affordability/", "/tools/mortgage/", "/tools/closing-costs/",
                "/tools/home-estimate/", "/tools/rent-vs-buy/", "/tools/welcome-tax/",
                "/advantages/", "/advantages/integri-t/", "/advantages/tranquilli-t/",
                "/advantages/coproprie-t/", "/advantages/mes-rabais-remax/"}

DASHES = {"—": "em dash", "–": "en dash", "−": "signe moins", "‒": "tiret numerique"}


def parse(path):
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return None, raw, raw
    end = raw.find("\n---", 3)
    if end == -1:
        return None, raw, raw
    block, body = raw[3:end], raw[end + 4:]
    meta = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "-", "#")):
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body, raw


def known_slugs(lang):
    folder = CONTENT / lang / "articles"
    return {p.stem for p in folder.glob("*.md")} if folder.is_dir() else set()


def section_paths(lang):
    """Toutes les URLs de pages reellement presentes pour cette langue.

    Le francais vit a la racine, les autres langues sous /{lang}/. Une page qui
    declare son propre `url:` dans le front matter, comme le formulaire, fait foi.
    """
    prefix = "" if lang == "fr" else "/" + lang
    out = {prefix + p for p in STATIC_PATHS}
    out.add(FORM_PATH[lang])
    out.add(CONTACT_PATH[lang])
    base = CONTENT / lang
    if not base.is_dir():
        return out
    for path in base.rglob("*.md"):
        meta, _, _ = parse(path)
        if meta and meta.get("url"):
            url = meta["url"]
            out.add(url if url.endswith("/") else url + "/")
            continue
        rel = path.relative_to(base).as_posix()
        if rel.endswith("_index.md"):
            rel = rel[:-len("_index.md")]
        else:
            rel = rel[:-3] + "/"
        out.add("%s/%s" % (prefix, rel.lstrip("/")))
    return out


def check(path):
    path = Path(path)
    lang = "fr"
    for candidate in LANGS:
        if ("/%s/" % candidate) in path.as_posix() or ("\\%s\\" % candidate) in str(path):
            lang = candidate
            break

    errors, warnings = [], []
    meta, body, raw = parse(path)
    if meta is None:
        return path, ["front matter illisible"], []

    # Regle 1 du projet: aucun tiret long.
    for char, name in DASHES.items():
        if char in raw:
            line = raw[:raw.index(char)].count("\n") + 1
            errors.append("%s a la ligne %d (regle 1)" % (name, line))
    for m in re.finditer(r"(?<!-)--(?!-)", raw):
        if not raw[max(0, m.start() - 60):m.start()].rstrip().endswith("|"):
            errors.append("double tiret a la ligne %d (regle 1)" % (raw[:m.start()].count("\n") + 1))
            break

    for key in REQUIRED:
        if key not in meta:
            errors.append("champ manquant: %s" % key)

    if meta.get("draft", "").lower() != "true":
        warnings.append("draft n est pas true")

    # Google tronque vers 155. Les articles existants du site vont jusqu a 218,
    # donc un depassement modeste est un avis, pas une erreur.
    desc = meta.get("description", "")
    if len(desc) > 175:
        errors.append("description de %d caracteres, maximum 155" % len(desc))
    elif len(desc) > 155:
        warnings.append("description de %d caracteres, vise 155" % len(desc))
    elif len(desc) < 70:
        warnings.append("description courte (%d caracteres)" % len(desc))

    title = meta.get("title", "")
    if len(title) > 75:
        warnings.append("titre de %d caracteres, vise moins de 60" % len(title))

    cat = meta.get("category", "")
    if cat and cat not in CATEGORIES.get(lang, set()):
        errors.append("categorie inconnue en %s: %s" % (lang, cat))

    for field in ("date", "lastmod"):
        value = meta.get(field, "")
        if value:
            try:
                d = datetime.date.fromisoformat(value)
                if d > TODAY:
                    errors.append("%s dans le futur: %s" % (field, value))
            except ValueError:
                errors.append("%s illisible: %s" % (field, value))

    # Une traduction partage le dossier d images de la version francaise, donc
    # son chemin d image porte le slug francais. On ne verifie qu en francais.
    slug = path.stem
    if lang == "fr" and meta.get("image") and slug not in meta["image"]:
        warnings.append("le chemin d image ne contient pas le slug")

    if re.search(r"^#\s+", body, flags=re.M):
        errors.append("titre H1 dans le corps, il doit rester dans le front matter")

    h2 = re.findall(r"^##\s+(.+)$", body, flags=re.M)
    if not 5 <= len(h2) <= 10:
        warnings.append("%d sections H2, vise 6 a 8" % len(h2))

    words = len(re.sub(r"[#>*_`|-]+", " ", body).split())
    if words < 1100:
        errors.append("%d mots, minimum 1200" % words)
    elif words > 2100:
        warnings.append("%d mots, vise 1800" % words)

    # Liens internes: chaque cible doit exister.
    valid = section_paths(lang)
    slugs = known_slugs(lang)
    prefix = "/articles/" if lang == "fr" else "/%s/articles/" % lang
    for target in re.findall(r"\]\((/[^)#\s]*)\)", body):
        target = target if target.endswith("/") else target + "/"
        if target.startswith(prefix):
            if target[len(prefix):].rstrip("/") not in slugs:
                errors.append("lien mort: %s" % target)
        elif target not in valid and target.rstrip("/") + "/" not in valid:
            # section_paths enumere toutes les pages reelles, y compris les url:
            # declarees en front matter. Une cible absente est donc un lien mort,
            # pas un doute. Cas vecu: /secteurs/laval/ n existe pas, la page
            # s appelle /courtier-immobilier/laval/.
            errors.append("lien mort: %s" % target)

    if FORM_PATH[lang] not in body:
        errors.append("aucun appel a l action vers %s" % FORM_PATH[lang])

    internal = len(re.findall(r"\]\(" + re.escape(prefix), body))
    if internal < 3:
        warnings.append("%d liens vers des articles, vise 3 a 5" % internal)

    return path, errors, warnings


def main():
    targets = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        targets.extend(sorted(p.parent.glob(p.name)) if "*" in arg else [p])
    if not targets:
        print("Aucun fichier. Exemple: python tools/validate.py drafts/fr/*.md")
        sys.exit(1)

    bad = 0
    for path in targets:
        if not path.is_file():
            print("ABSENT  %s" % path)
            bad += 1
            continue
        path, errors, warnings = check(path)
        flag = "ERREUR" if errors else ("avis  " if warnings else "ok    ")
        print("%s  %s" % (flag, path.name))
        for e in errors:
            print("        x %s" % e)
        for w in warnings:
            print("        . %s" % w)
        bad += 1 if errors else 0

    print("\n%d fichier(s), %d en erreur." % (len(targets), bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
