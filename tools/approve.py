#!/usr/bin/env python3
"""Passe des articles de `draft: true` a `draft: false`. A LANCER PAR GEORGES SEULEMENT.

Claude ne lance jamais ce script. Il sert a publier ce que vous avez relu.

    python tools/approve.py list                 montre les brouillons en attente
    python tools/approve.py show SLUG            affiche un brouillon pour relecture
    python tools/approve.py approve SLUG [SLUG]  publie ces articles
    python tools/approve.py approve --batch 5    publie les 5 plus anciens brouillons
    python tools/approve.py approve SLUG --fr-seulement   ignore la regle des 4 langues

REGLE DES 4 LANGUES (CLAUDE.md, regle 2)
Un article ne se publie pas en francais seul. Par defaut, ce script refuse de
publier un article francais tant que les versions en, es et ar n existent pas.
`--fr-seulement` force le passage, a utiliser en connaissance de cause.
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
LANGS = ["fr", "en", "es", "ar"]
TODAY = datetime.date.today().isoformat()


def articles(lang):
    folder = CONTENT / lang / "articles"
    return sorted(p for p in folder.glob("*.md") if p.stem != "_index") if folder.is_dir() else []


def front_matter(path):
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return {}, raw
    end = raw.find("\n---", 3)
    block = raw[3:end]
    meta = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, raw


def is_draft(path):
    meta, _ = front_matter(path)
    return meta.get("draft", "false").lower() == "true"


def drafts():
    out = []
    for lang in LANGS:
        for path in articles(lang):
            if is_draft(path):
                meta, _ = front_matter(path)
                out.append({"lang": lang, "path": path, "slug": path.stem,
                            "title": meta.get("title", ""), "date": meta.get("date", ""),
                            "key": meta.get("translationKey", "")})
    return out


def translations_of(key):
    """Quelles langues possedent deja un article portant cette translationKey."""
    found = {}
    if not key:
        return found
    for lang in LANGS:
        for path in articles(lang):
            meta, _ = front_matter(path)
            if meta.get("translationKey") == key:
                found[lang] = path
    return found


def cmd_list():
    rows = drafts()
    if not rows:
        print("Aucun brouillon en attente.")
        return
    by_key = {}
    for r in rows:
        by_key.setdefault(r["key"] or r["slug"], []).append(r)
    print("%-42s %-18s %s" % ("cle de traduction", "langues pretes", "titre francais"))
    print("-" * 100)
    for key, group in sorted(by_key.items()):
        langs = "".join(l if any(g["lang"] == l for g in group) else "." for l in LANGS)
        fr = next((g for g in group if g["lang"] == "fr"), group[0])
        print("%-42s %-18s %s" % (key[:42], langs, fr["title"][:60]))
    print("\n%d brouillons, %d articles distincts." % (len(rows), len(by_key)))
    print("Legende des langues: fr en es ar, un point signifie absent.")


def cmd_show(slug):
    for lang in LANGS:
        path = CONTENT / lang / "articles" / ("%s.md" % slug)
        if path.is_file():
            print("=" * 70)
            print(path)
            print("=" * 70)
            print(path.read_text(encoding="utf-8"))
            return
    print("Introuvable: %s" % slug)
    sys.exit(1)


def flip(path):
    raw = path.read_text(encoding="utf-8")
    if not re.search(r"^draft:\s*true\s*$", raw, flags=re.M):
        return False
    raw = re.sub(r"^draft:\s*true\s*$", "draft: false", raw, count=1, flags=re.M)
    if re.search(r"^lastmod:", raw, flags=re.M):
        raw = re.sub(r"^lastmod:.*$", "lastmod: %s" % TODAY, raw, count=1, flags=re.M)
    path.write_text(raw, encoding="utf-8")
    return True


def cmd_approve(slugs, batch, fr_only):
    rows = drafts()
    if batch:
        fr_rows = sorted([r for r in rows if r["lang"] == "fr"], key=lambda r: r["date"])
        slugs = [r["slug"] for r in fr_rows[:batch]]
    if not slugs:
        print("Rien a publier. Precisez des slugs ou --batch N.")
        return

    published = blocked = 0
    for slug in slugs:
        fr_path = CONTENT / "fr" / "articles" / ("%s.md" % slug)
        if not fr_path.is_file():
            hit = next((r for r in rows if r["slug"] == slug), None)
            if not hit:
                print("[introuvable] %s" % slug)
                continue
            fr_path = hit["path"]

        meta, _ = front_matter(fr_path)
        key = meta.get("translationKey", "")
        found = translations_of(key)
        missing = [l for l in LANGS if l not in found]

        if missing and not fr_only:
            print("[bloque]  %s : traductions manquantes (%s). "
                  "Relancez avec --fr-seulement pour passer outre."
                  % (slug, ", ".join(missing)))
            blocked += 1
            continue

        targets = list(found.values()) if found else [fr_path]
        done = [str(p.relative_to(ROOT)) for p in targets if flip(p)]
        if done:
            print("[publie]  %s : %d fichier(s)" % (slug, len(done)))
            for d in done:
                print("           %s" % d.replace("\\", "/"))
            published += 1
        else:
            print("[deja publie] %s" % slug)

    print("\n%d article(s) publie(s), %d bloque(s)." % (published, blocked))
    if published:
        print("Pensez a verifier le rendu, puis: git add content && git commit && git push")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("list")
    p_show = sub.add_parser("show")
    p_show.add_argument("slug")
    p_ok = sub.add_parser("approve")
    p_ok.add_argument("slugs", nargs="*")
    p_ok.add_argument("--batch", type=int, default=0)
    p_ok.add_argument("--fr-seulement", action="store_true", dest="fr_only")

    args = ap.parse_args()
    if args.cmd == "list" or args.cmd is None:
        cmd_list()
    elif args.cmd == "show":
        cmd_show(args.slug)
    elif args.cmd == "approve":
        cmd_approve(args.slugs, args.batch, args.fr_only)


if __name__ == "__main__":
    main()
