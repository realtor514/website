#!/usr/bin/env python3
"""Publie d un coup tout article complet dans les 4 langues.

    python tools/release.py --check   montre ce qui serait publie, ne touche rien
    python tools/release.py           valide, aligne lastmod, puis publie

Un groupe est publiable quand ses 4 langues existent, qu au moins une version
est encore en draft, et que les 4 fichiers passent tools/validate.py sans
erreur. Un groupe incomplet ou invalide est laisse tel quel et explique.

Ce script remplace la sequence manuelle validate, approve, alignement de
lastmod et linkmap, repetee une fois par article.
"""

import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import validate  # noqa: E402

LANGS = ["fr", "en", "es", "ar"]


def groups():
    out = defaultdict(dict)
    for lang in LANGS:
        folder = ROOT / "content" / lang / "articles"
        if not folder.is_dir():
            continue
        for p in folder.glob("*.md"):
            if p.stem == "_index":
                continue
            meta, _, _ = validate.parse(p)
            if not meta:
                continue
            key = meta.get("translationKey") or p.stem
            out[key][lang] = {"path": p, "meta": meta,
                              "draft": meta.get("draft", "false").lower() == "true"}
    return out


def align_lastmod(files):
    for f in files:
        s = f["path"].read_text(encoding="utf-8")
        m = re.search(r"^date:\s*(\S+)", s, re.M)
        if not m:
            continue
        s2 = re.sub(r"^lastmod:.*$", "lastmod: " + m.group(1), s, count=1, flags=re.M)
        if s2 != s:
            f["path"].write_text(s2, encoding="utf-8")


def publish(files):
    n = 0
    for f in files:
        s = f["path"].read_text(encoding="utf-8")
        s2 = re.sub(r"^draft:\s*true\s*$", "draft: false", s, count=1, flags=re.M)
        if s2 != s:
            f["path"].write_text(s2, encoding="utf-8")
            n += 1
    return n


def main():
    check = "--check" in sys.argv
    ready, incomplete, invalid = [], [], []

    for key, langs in sorted(groups().items()):
        if not any(v["draft"] for v in langs.values()):
            continue
        fr = langs.get("fr") or next(iter(langs.values()))
        name = fr["path"].stem
        if len(langs) < 4:
            incomplete.append((name, "".join(l for l in LANGS if l in langs)))
            continue
        files = [langs[l] for l in LANGS]
        errs = []
        for f in files:
            _, e, _ = validate.check(f["path"])
            errs += ["%s: %s" % (f["path"].name, x) for x in e]
        if errs:
            invalid.append((name, errs))
        else:
            ready.append((name, key, files))

    for name, langs in incomplete:
        print("incomplet  %-46s %s" % (name, langs))
    for name, errs in invalid:
        print("INVALIDE   %s" % name)
        for e in errs[:4]:
            print("             x %s" % e)

    if not ready:
        print("\nRien a publier.")
        return

    print()
    for name, key, files in ready:
        print("%s  %s" % ("a publier " if check else "publie    ", name))
        if check:
            continue
        align_lastmod(files)
        publish(files)

    if not check:
        subprocess.run([sys.executable, str(ROOT / "tools" / "linkmap.py")],
                       capture_output=True)
        print("\n%d article(s) publie(s) dans les 4 langues. Cartes de liens rafraichies."
              % len(ready))
    else:
        print("\n%d article(s) prets. Relancez sans --check pour publier." % len(ready))


if __name__ == "__main__":
    main()
