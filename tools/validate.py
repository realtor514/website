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
CATEGORIES = {"Guide de l'acheteur", "Guide du vendeur", "Financement", "Investissement",
              "Immobilier 101", "Analyse de marché", "Analyse de marche", "Guide pratique",
              "Conseils honnêtes"}

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
    """Toutes les URLs de pages reellement presentes pour cette langue."""
    out = set(STATIC_PATHS)
    base = CONTENT / lang
    if not base.is_dir():
        return out
    for path in base.rglob("*.md"):
        rel = path.relative_to(base).as_posix()
        if rel.endswith("_index.md"):
            rel = rel[:-len("_index.md")]
        else:
            rel = rel[:-3] + "/"
        out.add("/" + rel if not rel.startswith("/") else rel)
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
    if cat and cat not in CATEGORIES:
        errors.append("categorie inconnue: %s" % cat)

    for field in ("date", "lastmod"):
        value = meta.get(field, "")
        if value:
            try:
                d = datetime.date.fromisoformat(value)
                if d > TODAY:
                    errors.append("%s dans le futur: %s" % (field, value))
            except ValueError:
                errors.append("%s illisible: %s" % (field, value))

    slug = path.stem
    if meta.get("image") and slug not in meta["image"]:
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
            warnings.append("lien non verifie: %s" % target)

    if "/formulaire/" not in body:
        errors.append("aucun appel a l action vers /formulaire/")

    internal = len(re.findall(r"\]\(/articles/", body))
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
