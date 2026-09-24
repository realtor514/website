#!/usr/bin/env python3
"""PORTE 1 (niveau sujet) et PORTE 2 (reclamation) du plan de contenu.

    python tools/plan_gate.py gate1        annote chaque sujet du plan
    python tools/plan_gate.py claim t01 t02 ...   reclame des sujets dans le registre

Porte 1 classe chaque sujet en:
    clear            aucun article existant ne le couvre
    parked           recouvrement partiel, a trancher par un humain
    already_covered  un article existant traite deja le sujet
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dedupe

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "state" / "content_plan.json"
REGISTRY = ROOT / "state" / "registry.json"


def load_plan():
    return json.loads(PLAN.read_text(encoding="utf-8"))


def save_plan(plan):
    PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")


def load_registry():
    if REGISTRY.is_file():
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {"claims": [], "slugs": [], "keywords": [], "titles": []}


def save_registry(reg):
    REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")


def gate1():
    plan = load_plan()
    index = dedupe.load_index()
    order = {"PASS": 0, "REVIEW": 1, "FAIL": 2}
    tally = {}

    # Un sujet deja ecrit, deja reclame ou deja tranche ne se rejuge pas.
    terminal = {"written_draft", "written_draft_review", "in_progress", "done",
                "already_covered", "failed_duplicate", "blocked_duplicate",
                "error_retry_later", "update_candidate"}

    for row in plan["topics"]:
        if row.get("status") in terminal:
            tally[row["status"]] = tally.get(row["status"], 0) + 1
            continue
        heads = row.get("planned_h2", [])
        checks = {
            "slug": dedupe.slug_check(row["slug"], index, "fr"),
            "title": dedupe.title_check(row["topic"], index, "fr"),
            "keyword": dedupe.keyword_check(row["target_keyword_fr"], index, "fr"),
            "topic": dedupe.topic_check(row["topic"], heads, index, "fr"),
        }
        worst = max((c["verdict"] for c in checks.values()), key=lambda v: order[v])
        status = {"PASS": "clear", "REVIEW": "parked", "FAIL": "already_covered"}[worst]
        row["gate1"] = {k: {"v": c["verdict"], "s": c["score"], "match": c["closest"]}
                        for k, c in checks.items()}
        row["status"] = status
        if status != "clear":
            row["closest_existing"] = max(checks.values(), key=lambda c: order[c["verdict"]])["closest"]
        tally[status] = tally.get(status, 0) + 1
        print("%-4s %-9s topic=%.2f titre=%.2f  %s" % (
            row["id"], status, checks["topic"]["score"], checks["title"]["score"], row["slug"]))
        if status != "clear":
            print("       proche de: %s" % row.get("closest_existing"))

    save_plan(plan)
    print("\n" + json.dumps(tally, ensure_ascii=False))
    return tally


def claim(ids):
    """PORTE 2: revalide puis inscrit une reclamation avant de lancer un agent."""
    plan = load_plan()
    index = dedupe.load_index()
    reg = load_registry()
    claimed = {c["id"] for c in reg["claims"]}

    for row in plan["topics"]:
        if row["id"] not in ids or row["id"] in claimed:
            continue
        s = dedupe.slug_check(row["slug"], index, "fr", reg["slugs"])
        k = dedupe.keyword_check(row["target_keyword_fr"], index, "fr", reg["keywords"])
        t = dedupe.title_check(row["topic"], index, "fr", reg["titles"])
        if "FAIL" in (s["verdict"], k["verdict"], t["verdict"]):
            row["status"] = "blocked_duplicate"
            print("%s BLOQUE  slug=%s keyword=%s titre=%s" % (
                row["id"], s["verdict"], k["verdict"], t["verdict"]))
            continue
        reg["claims"].append({"id": row["id"], "slug": row["slug"],
                              "keyword": row["target_keyword_fr"], "state": "in_progress"})
        reg["slugs"].append(row["slug"])
        reg["keywords"].append(row["target_keyword_fr"])
        reg["titles"].append(row["topic"])
        row["status"] = "in_progress"
        print("%s reclame: %s" % (row["id"], row["slug"]))

    save_plan(plan)
    save_registry(reg)


def release(ids):
    """Libere completement une reclamation: claim, slug, mot-cle ET titre.

    Oublier les deux derniers laisse le sujet se bloquer contre lui-meme a la
    prochaine tentative, ce qui est arrive une fois: la porte 2 repondait
    keyword=FAIL titre=FAIL sur un sujet dont plus personne ne s occupait.
    """
    plan = load_plan()
    reg = load_registry()
    rows = [r for r in plan["topics"] if r["id"] in ids]
    slugs = {r["slug"] for r in rows}
    keywords = {r["target_keyword_fr"] for r in rows}
    titles = {r["topic"] for r in rows}

    reg["claims"] = [c for c in reg["claims"] if c["id"] not in ids]
    reg["slugs"] = [s for s in reg["slugs"] if s not in slugs]
    reg["keywords"] = [k for k in reg["keywords"] if k not in keywords]
    reg["titles"] = [t for t in reg["titles"] if t not in titles]
    for r in rows:
        if r.get("status") == "in_progress":
            r["status"] = "clear"

    save_registry(reg)
    save_plan(plan)
    for r in rows:
        print("%s libere: %s" % (r["id"], r["slug"]))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "gate1"
    if cmd == "gate1":
        gate1()
    elif cmd == "claim":
        claim(set(sys.argv[2:]))
    elif cmd == "release":
        release(set(sys.argv[2:]))
    else:
        print(__doc__)
