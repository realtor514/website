#!/usr/bin/env python3
"""Etat du blogue en une commande.

    python tools/status.py            vue d ensemble
    python tools/status.py --nouveaux seulement les articles ajoutes par le moteur

Montre, pour chaque article recent: sa date, s il est en ligne ou en brouillon,
dans quelles langues il existe, et s il attend une relecture de specialiste.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ["fr", "en", "es", "ar"]


def read(path):
    raw = path.read_text(encoding="utf-8")
    end = raw.find("\n---", 3)
    meta = {}
    for line in raw[3:end if end > 0 else 0].splitlines():
        if ":" in line and not line.startswith((" ", "-", "#")):
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def main():
    only_new = "--nouveaux" in sys.argv
    groups = defaultdict(dict)
    counts = {}
    for lang in LANGS:
        folder = ROOT / "content" / lang / "articles"
        files = [p for p in folder.glob("*.md") if p.stem != "_index"]
        counts[lang] = len(files)
        for p in files:
            meta = read(p)
            key = meta.get("translationKey") or p.stem
            groups[key][lang] = {
                "slug": p.stem,
                "date": meta.get("date", ""),
                "draft": meta.get("draft", "false").lower() == "true",
                "review": meta.get("needs_expert_review", "false").lower() == "true",
                "title": meta.get("title", ""),
            }

    plan_path = ROOT / "state" / "content_plan.json"
    session = set()
    if plan_path.is_file():
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        session = {t["translationKey"] for t in plan["topics"]
                   if t.get("status", "").startswith("written_draft") or t.get("status") == "in_progress"}

    rows = []
    for key, langs in groups.items():
        fr = langs.get("fr") or next(iter(langs.values()))
        rows.append((fr["date"], key, fr, langs))
    rows.sort(reverse=True)

    print("%-12s %-6s %-6s %-5s %s" % ("date", "etat", "langues", "revue", "article"))
    print("-" * 104)
    shown = 0
    for date, key, fr, langs in rows:
        if only_new and key not in session:
            continue
        online = sum(1 for v in langs.values() if not v["draft"])
        etat = "ligne" if online == len(langs) and len(langs) == 4 else (
            "partiel" if online else "brouil")
        have = "".join(l if l in langs else "." for l in LANGS)
        review = "oui" if fr["review"] else ""
        print("%-12s %-6s %-6s %-5s %s" % (date, etat, have, review, fr["title"][:58]))
        shown += 1

    print()
    print("Articles par langue: " + ", ".join("%s %d" % (l, counts[l]) for l in LANGS))
    total_groups = len(groups)
    complete = sum(1 for g in groups.values() if len(g) == 4)
    online = sum(1 for g in groups.values()
                 if len(g) == 4 and all(not v["draft"] for v in g.values()))
    draft_files = sum(1 for g in groups.values() for v in g.values() if v["draft"])
    review_n = sum(1 for g in groups.values()
                   if any(v["review"] for v in g.values()))
    print("Groupes de traduction: %d, complets dans les 4 langues: %d" % (total_groups, complete))
    print("En ligne dans les 4 langues: %d" % online)
    print("Fichiers encore en draft: %d" % draft_files)
    print("Articles marques needs_expert_review: %d" % review_n)
    if only_new:
        print("Affiches: %d articles produits par le moteur" % shown)


if __name__ == "__main__":
    main()
