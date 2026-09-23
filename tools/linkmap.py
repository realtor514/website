#!/usr/bin/env python3
"""Reconstruit les cartes de liens internes donnees aux redacteurs.

    python tools/linkmap.py

Ecrit state/internal_links_{fr,en,es,ar}.md a partir de ce qui existe
REELLEMENT dans content/. A relancer apres chaque lot publie, sinon les
redacteurs ne peuvent pas pointer vers les articles du lot precedent.

Les chemins hors articles ne sont jamais devines: ils sont lus dans le front
matter des pages, parce que plusieurs declarent leur propre `url:`. C est ainsi
qu on evite d annoncer /secteurs/laval/, qui n existe pas, au lieu de
/courtier-immobilier/laval/.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
LANGS = {"fr": "francais", "en": "English", "es": "Espanol", "ar": "Arabic"}

INTRO = {
    "fr": ("# Articles existants en francais: cibles autorisees pour les liens internes",
           "Utilisez EXACTEMENT ces chemins. Ne jamais inventer une URL. Style de lien du "
           "site: [texte descriptif](/articles/slug/)"),
    "en": ("# English articles: allowed internal link targets",
           "Copy these paths exactly. A link to a page that does not exist fails the check."),
    "es": ("# Articulos en espanol: destinos permitidos para enlaces internos",
           "Copie estas rutas exactamente. Un enlace a una pagina inexistente falla la revision."),
    "ar": ("# Arabic articles: allowed internal link targets",
           "Copy these paths exactly. A link to a page that does not exist fails the check."),
}


def page_url(path, lang):
    """L URL reelle d une page: son `url:` declare, sinon son chemin."""
    meta, _, _ = validate.parse(path)
    if meta and meta.get("url"):
        u = meta["url"]
        return u if u.endswith("/") else u + "/"
    prefix = "" if lang == "fr" else "/" + lang
    rel = path.relative_to(CONTENT / lang).as_posix()
    rel = rel[:-len("_index.md")] if rel.endswith("_index.md") else rel[:-3] + "/"
    return "%s/%s" % (prefix, rel.lstrip("/"))


def build(lang):
    folder = CONTENT / lang / "articles"
    rows = []
    for p in sorted(folder.glob("*.md")):
        if p.stem == "_index":
            continue
        meta, _, _ = validate.parse(p)
        if not meta:
            continue
        rows.append((meta.get("category", ""), meta.get("title", p.stem),
                     page_url(p, lang), meta.get("description", "")[:105],
                     meta.get("draft", "false").lower() == "true"))
    rows.sort()

    title, note = INTRO[lang]
    out = [title, "", note, "",
           "Un article marque (brouillon) n est pas encore visible: ne le liez pas.", ""]
    cat = None
    for c, t, url, desc, draft in rows:
        if c != cat:
            cat = c
            out += ["", "## " + (cat or "Sans categorie")]
        out.append("- [%s](%s)%s : %s" % (t, url, " (brouillon)" if draft else "", desc))

    # Pages hors articles, lues telles qu elles se declarent.
    out += ["", "## Pages outils et conversion", ""]
    seen = set()
    for p in sorted((CONTENT / lang).rglob("*.md")):
        rel = p.relative_to(CONTENT / lang).as_posix()
        if rel.startswith("articles/") or rel.startswith("listings/"):
            continue
        meta, _, _ = validate.parse(p)
        if not meta:
            continue
        url = page_url(p, lang)
        if url in seen:
            continue
        seen.add(url)
        out.append("- %s : %s" % (url, meta.get("title", "")[:70]))

    path = ROOT / "state" / ("internal_links_%s.md" % lang)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return len(rows), len(seen)


if __name__ == "__main__":
    for lang in LANGS:
        n, pages = build(lang)
        print("%s: %d articles, %d autres pages" % (lang, n, pages))
