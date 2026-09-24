#!/usr/bin/env python3
"""PORTE 4 (au moment d ecrire) puis copie des brouillons vers content/.

    python tools/publish.py check                verifie sans rien copier
    python tools/publish.py run                  copie les brouillons valides
    python tools/publish.py run --lang en

Ce script ne publie rien en ligne: il depose l article dans content/ avec
`draft: true`. Seul tools/approve.py, lance par Georges, retire le draft.

DATES
Les articles ne portent pas tous la date du jour. Ils sont repartis sur le
dernier mois, du plus ancien sujet au plus recent, sans jamais depasser
aujourd hui. `--fenetre N` change la largeur de la fenetre (30 jours par defaut).
"""

import argparse
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dedupe
import validate

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"
TODAY = datetime.date.today()


def taken_dates(lang="fr"):
    """Dates deja occupees par un article de cette langue."""
    folder = ROOT / "content" / lang / "articles"
    used = set()
    if not folder.is_dir():
        return used
    for path in folder.glob("*.md"):
        m = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", path.read_text(encoding="utf-8"), re.M)
        if m:
            used.add(m.group(1))
    return used


def spread_dates(count, window=30, end=None, avoid=()):
    """Repartit `count` dates sur les `window` derniers jours, bornees a aujourd hui.

    `avoid` liste les dates deja prises: en cas de collision on glisse d un jour,
    puis de deux, sans jamais sortir de la fenetre ni depasser aujourd hui. Deux
    articles le meme jour restent possibles si la fenetre est pleine.
    """
    end = end or TODAY
    if count <= 0:
        return []
    start = end - datetime.timedelta(days=window)
    step = window / (count - 1) if count > 1 else 0
    avoid = set(avoid)
    out = []
    for i in range(count):
        d = start + datetime.timedelta(days=round(i * step)) if count > 1 else end
        for shift in (0, -1, 1, -2, 2, -3, 3):
            c = d + datetime.timedelta(days=shift)
            if start <= c <= end and c.isoformat() not in avoid:
                d = c
                break
        avoid.add(d.isoformat())
        out.append(d)
    return sorted(out)


def set_date(raw, date):
    raw = re.sub(r"^date:.*$", "date: %s" % date.isoformat(), raw, count=1, flags=re.M)
    raw = re.sub(r"^lastmod:.*$", "lastmod: %s" % date.isoformat(), raw, count=1, flags=re.M)
    return raw


def load_plan():
    return json.loads((STATE / "content_plan.json").read_text(encoding="utf-8"))


def save_plan(plan):
    (STATE / "content_plan.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")


def gate4(path, index, lang, siblings):
    """Dernier controle avant d ecrire dans content/."""
    report = dedupe.check_draft(path, index=index, lang=lang, extra_drafts=siblings)
    _, errors, warnings = validate.check(path)
    report["validation_errors"] = errors
    report["validation_warnings"] = warnings
    if errors:
        report["overall"] = "FAIL"
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["check", "run"])
    ap.add_argument("--lang", default="fr")
    ap.add_argument("--fenetre", type=int, default=30)
    ap.add_argument("--slugs", nargs="*", default=None,
                    help="ne traiter que ces slugs. Sans ca, tous les brouillons du "
                         "dossier, ce qui ramasse aussi ceux qu un agent est encore "
                         "en train d ecrire.")
    args = ap.parse_args()

    lang = args.lang
    drafts_dir = ROOT / "drafts" / lang
    target_dir = ROOT / "content" / lang / "articles"
    files = sorted(p for p in drafts_dir.glob("*.md"))
    if args.slugs:
        wanted = set(args.slugs)
        files = [p for p in files if p.stem in wanted]
        absents = wanted - {p.stem for p in files}
        if absents:
            print("introuvable dans drafts/%s: %s" % (lang, ", ".join(sorted(absents))))
    if not files:
        print("Aucun brouillon dans %s" % drafts_dir)
        return

    # PORTE 4: l index est reconstruit maintenant, pour attraper tout fichier
    # apparu dans content/ depuis le debut de la session.
    index = dedupe.build_index()
    print("Index reconstruit: %d articles (%s)\n" % (index["total"], index["counts"]))

    results = []
    for path in files:
        siblings = [str(p) for p in files if p != path]
        report = gate4(path, index, lang, siblings)
        results.append((path, report))
        checks = " ".join("%s=%s" % (c["check"], c["verdict"]) for c in report["checks"])
        print("%-8s %-44s %d mots" % (report["overall"], path.name, report["word_count"]))
        print("         %s" % checks)
        for e in report["validation_errors"]:
            print("         x %s" % e)
        for w in report["validation_warnings"]:
            print("         . %s" % w)
        worst = [c for c in report["checks"] if c["verdict"] != "PASS"]
        for c in worst:
            print("         ! %s %s: %s" % (c["check"], c["verdict"], c["closest"]))

    ok = [(p, r) for p, r in results if r["overall"] == "PASS"]
    review = [(p, r) for p, r in results if r["overall"] == "REVIEW"]
    fail = [(p, r) for p, r in results if r["overall"] == "FAIL"]
    print("\n%d PASS, %d REVIEW, %d FAIL" % (len(ok), len(review), len(fail)))

    if args.cmd == "check":
        return

    # Les REVIEW passent aussi en content/ mais restent en draft et sont signales.
    movable = ok + review
    if not movable:
        print("Rien a copier.")
        return

    dates = spread_dates(len(movable), window=args.fenetre, avoid=taken_dates(lang))
    plan = load_plan()
    by_slug = {t["slug"]: t for t in plan["topics"]}

    print("\nDates reparties du %s au %s:" % (dates[0], dates[-1]))
    for (path, report), date in zip(movable, dates):
        dest = target_dir / path.name
        if dest.exists():
            print("  [existe deja] %s" % dest.name)
            continue
        raw = set_date(path.read_text(encoding="utf-8"), date)
        dest.write_text(raw, encoding="utf-8")
        row = by_slug.get(path.stem)
        if row:
            row["status"] = "written_draft" if report["overall"] == "PASS" else "written_draft_review"
            row["published_path"] = str(dest.relative_to(ROOT)).replace("\\", "/")
            row["date"] = date.isoformat()
        print("  %s  %s" % (date, dest.name))

    save_plan(plan)
    dedupe.build_index()
    print("\nCopie terminee. Tout reste en draft: true.")


if __name__ == "__main__":
    main()
