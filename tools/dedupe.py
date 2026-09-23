#!/usr/bin/env python3
"""Detecteur de doublons pour le blogue georgesmatar.ca.

Hors ligne, bibliotheque standard uniquement. Aucune dependance a installer.

Usage:
    python tools/dedupe.py index          reconstruit state/existing_blogue_index.json
    python tools/dedupe.py selftest       lance l auto-test obligatoire
    python tools/dedupe.py check FICHIER  passe un brouillon a toutes les portes

Seuils (definis par MASTER_PROMPT.md):
    slug identique                      FAIL
    titre >= 0.85 FAIL, 0.70-0.85 REVIEW
    mot-cle deja cible par un article   FAIL
    sujet (cosinus titre + H2) >= 0.75 FAIL, 0.60-0.75 REVIEW
    contenu shingle >= 0.15 ou cosinus >= 0.80 FAIL
    contre la reference shingle >= 0.10 FAIL
"""

import json
import math
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
STATE = ROOT / "state"
LANGS = ["fr", "en", "es", "ar"]

# Mots vides francais, anglais et espagnols: ils faussent la comparaison de titres.
STOPWORDS = set("""
le la les un une des du de d a au aux et ou ou est sont ce cet cette ces
en dans sur pour par avec sans sous vers chez que qui quoi dont ne pas plus
moins tres son sa ses leur leurs mon ma mes votre vos notre nos il elle ils
elles on nous vous je tu se y il-y-a c est quel quelle quels quelles
the a an of in on for to with without and or is are be by at from as it its
this that these those what which how why when where do does your you we they
el los las lo y o es son en para por con sin sobre como que se su sus del al
""".split())


# ---------------------------------------------------------------- normalisation

def strip_accents(text):
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(c for c in decomposed if unicodedata.category(c) != "Mn")


def normalize(text):
    """Minuscules, sans accents, sans ponctuation, espaces reduits."""
    text = strip_accents(str(text or "")).lower()
    text = re.sub(r"[^a-z0-9؀-ۿ\s]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokens(text, drop_stopwords=True):
    words = normalize(text).split()
    if drop_stopwords:
        words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    return words


# ---------------------------------------------------------------- front matter

def parse_front_matter(raw):
    """Parseur YAML plat suffisant pour le schema du site (cle: valeur)."""
    if not raw.startswith("---"):
        return {}, raw
    end = raw.find("\n---", 3)
    if end == -1:
        return {}, raw
    block, body = raw[3:end], raw[end + 4:]
    meta = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) > 1 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        meta[key.strip()] = value
    return meta, body


def strip_markdown(body):
    """Retire le balisage pour ne comparer que la prose."""
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", body)
    body = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", body)
    body = re.sub(r"^\s*\|.*\|\s*$", " ", body, flags=re.M)   # tableaux
    body = re.sub(r"[#>*_`~-]+", " ", body)
    return re.sub(r"\s+", " ", body).strip()


def headings(body):
    return [h.strip() for h in re.findall(r"^#{2,3}\s+(.+)$", body, flags=re.M)]


def keyword_of(meta, title, body):
    """Mot-cle cible: le champ explicite s il existe, sinon deduit du slug."""
    for field in ("target_keyword", "keywords", "keyword"):
        if meta.get(field):
            return normalize(meta[field].split(",")[0])
    slug = meta.get("slug") or ""
    if slug:
        return normalize(slug.replace("-", " "))
    return " ".join(tokens(title)[:5])


# ---------------------------------------------------------------- inventaire

def load_post(path, lang):
    raw = path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(raw)
    title = meta.get("title", "")
    slug = meta.get("slug") or path.stem
    prose = strip_markdown(body)
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "lang": lang,
        "slug": slug,
        "url": ("/articles/%s/" % slug) if lang == "fr" else ("/%s/articles/%s/" % (lang, slug)),
        "translationKey": meta.get("translationKey", ""),
        "draft": meta.get("draft", "false").lower() == "true",
        "title": title,
        "description": meta.get("description", ""),
        "category": meta.get("category", ""),
        "headings": headings(body),
        "keyword": keyword_of(meta, title, body),
        "excerpt": " ".join(prose.split()[:300]),
        "word_count": len(prose.split()),
        "text": prose,
    }


def build_index(save=True):
    posts = []
    for lang in LANGS:
        folder = CONTENT / lang / "articles"
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.stem == "_index":
                continue
            posts.append(load_post(path, lang))
    index = {
        "generated_from": "content/{lang}/articles/*.md",
        "languages": LANGS,
        "counts": {lang: sum(1 for p in posts if p["lang"] == lang) for lang in LANGS},
        "total": len(posts),
        "posts": posts,
    }
    if save:
        STATE.mkdir(exist_ok=True)
        (STATE / "existing_blogue_index.json").write_text(
            json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    return index


def load_index():
    path = STATE / "existing_blogue_index.json"
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return build_index()


# ---------------------------------------------------------------- similarite

def jaccard(a, b):
    a, b = set(a), set(b)
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def shingles(text, n=5):
    words = tokens(text, drop_stopwords=False)
    if len(words) < n:
        return set()
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def shingle_jaccard(a, b, n=5):
    return jaccard(shingles(a, n), shingles(b, n))


def tfidf_cosine(target, corpus):
    """Cosinus TF-IDF de `target` contre chaque document de `corpus`.

    L IDF est calcule sur corpus + target pour que les deux vecteurs
    partagent le meme espace.
    """
    docs = [tokens(d) for d in corpus]
    tgt = tokens(target)
    if not tgt:
        return [0.0] * len(corpus)
    total = len(docs) + 1
    df = Counter()
    for doc in docs + [tgt]:
        for term in set(doc):
            df[term] += 1

    def vector(doc):
        counts = Counter(doc)
        if not counts:
            return {}
        top = max(counts.values())
        return {t: (0.5 + 0.5 * c / top) * math.log(total / (1 + df[t]) + 1)
                for t, c in counts.items()}

    def cosine(v1, v2):
        if not v1 or not v2:
            return 0.0
        shared = set(v1) & set(v2)
        num = sum(v1[t] * v2[t] for t in shared)
        n1 = math.sqrt(sum(v * v for v in v1.values()))
        n2 = math.sqrt(sum(v * v for v in v2.values()))
        return num / (n1 * n2) if n1 and n2 else 0.0

    vt = vector(tgt)
    return [cosine(vt, vector(d)) for d in docs]


def title_similarity(a, b):
    """Melange Jaccard de jetons et ratio de sequence, insensible aux accents."""
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    import difflib
    seq = difflib.SequenceMatcher(None, " ".join(ta), " ".join(tb)).ratio()
    return max(jaccard(ta, tb), 0.5 * jaccard(ta, tb) + 0.5 * seq)


# ---------------------------------------------------------------- les portes

def verdict(score, fail_at, review_at=None):
    if score >= fail_at:
        return "FAIL"
    if review_at is not None and score >= review_at:
        return "REVIEW"
    return "PASS"


def _result(name, v, score, match):
    return {"check": name, "verdict": v, "score": round(score, 4), "closest": match}


def slug_check(slug, index, lang="fr", extra_slugs=()):
    slug = normalize(slug).replace(" ", "-")
    for post in index["posts"]:
        if post["lang"] == lang and normalize(post["slug"]).replace(" ", "-") == slug:
            return _result("slug", "FAIL", 1.0, post["url"])
    if slug in {normalize(s).replace(" ", "-") for s in extra_slugs}:
        return _result("slug", "FAIL", 1.0, "brouillon de cette session")
    return _result("slug", "PASS", 0.0, None)


def title_check(title, index, lang="fr", extra_titles=()):
    best, best_match = 0.0, None
    pool = [(p["title"], p["url"]) for p in index["posts"] if p["lang"] == lang]
    pool += [(t, "brouillon de cette session") for t in extra_titles]
    for other, url in pool:
        score = title_similarity(title, other)
        if score > best:
            best, best_match = score, url
    return _result("title", verdict(best, 0.85, 0.70), best, best_match)


def keyword_check(keyword, index, lang="fr", extra_keywords=()):
    key = set(tokens(keyword))
    best, best_match = 0.0, None
    pool = [(p["keyword"], p["url"]) for p in index["posts"] if p["lang"] == lang]
    pool += [(k, "brouillon de cette session") for k in extra_keywords]
    for other, url in pool:
        score = jaccard(key, set(tokens(other)))
        if score > best:
            best, best_match = score, url
    # Cannibalisation: un mot-cle identique est un echec, un fort recouvrement un examen.
    return _result("keyword", verdict(best, 0.90, 0.65), best, best_match)


def topic_check(title, heads, index, lang="fr", extra=()):
    target = title + " " + " ".join(heads)
    pool = [(p["title"] + " " + " ".join(p["headings"]), p["url"])
            for p in index["posts"] if p["lang"] == lang]
    pool += [(t, "brouillon de cette session") for t in extra]
    if not pool:
        return _result("topic", "PASS", 0.0, None)
    scores = tfidf_cosine(target, [c for c, _ in pool])
    best_i = max(range(len(scores)), key=lambda i: scores[i])
    return _result("topic", verdict(scores[best_i], 0.75, 0.60), scores[best_i], pool[best_i][1])


def content_check(text, index, lang="fr", extra=()):
    pool = [(p["text"], p["url"]) for p in index["posts"] if p["lang"] == lang]
    pool += [(t, "brouillon de cette session") for t in extra]
    if not pool:
        return _result("content", "PASS", 0.0, None)
    cosines = tfidf_cosine(text, [c for c, _ in pool])
    worst_v, worst_score, worst_match = "PASS", 0.0, None
    order = {"PASS": 0, "REVIEW": 1, "FAIL": 2}
    for (other, url), cos in zip(pool, cosines):
        sh = shingle_jaccard(text, other)
        v = "FAIL" if (sh >= 0.15 or cos >= 0.80) else (
            "REVIEW" if (sh >= 0.08 or cos >= 0.65) else "PASS")
        score = max(sh / 0.15, cos / 0.80)
        if order[v] > order[worst_v] or (order[v] == order[worst_v] and score > worst_score):
            worst_v, worst_score, worst_match = v, score, "%s (shingle %.3f, cosinus %.3f)" % (url, sh, cos)
    return _result("content", worst_v, worst_score, worst_match)


def reference_check(text, cache_dir=None):
    """Compare a un cache local d articles de reference.

    Ce cache ne sort jamais d ici: aucun agent redacteur ne le recoit.
    Absence de cache = PASS, aucun texte de reference n a ete copie.
    """
    cache_dir = Path(cache_dir or (STATE / "reference_cache"))
    if not cache_dir.is_dir():
        return _result("reference", "PASS", 0.0, "aucun cache de reference")
    worst, match = 0.0, None
    for path in cache_dir.glob("*.txt"):
        score = shingle_jaccard(text, path.read_text(encoding="utf-8"))
        if score > worst:
            worst, match = score, path.name
    return _result("reference", verdict(worst, 0.10, 0.05), worst, match)


def check_draft(path, index=None, lang=None, extra_drafts=()):
    """Passe un fichier de brouillon a toutes les portes. Retourne un rapport."""
    path = Path(path)
    lang = lang or path.parent.name
    index = index or load_index()
    raw = path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(raw)
    title = meta.get("title", "")
    slug = meta.get("slug") or path.stem
    prose = strip_markdown(body)

    others = [load_post(Path(p), lang) for p in extra_drafts if Path(p) != path]
    checks = [
        slug_check(slug, index, lang, [o["slug"] for o in others]),
        title_check(title, index, lang, [o["title"] for o in others]),
        keyword_check(keyword_of(meta, title, body), index, lang, [o["keyword"] for o in others]),
        topic_check(title, headings(body), index, lang,
                    [o["title"] + " " + " ".join(o["headings"]) for o in others]),
        content_check(prose, index, lang, [o["text"] for o in others]),
        reference_check(prose),
    ]
    order = {"PASS": 0, "REVIEW": 1, "FAIL": 2}
    overall = max((c["verdict"] for c in checks), key=lambda v: order[v])
    return {
        "file": str(path).replace("\\", "/"),
        "lang": lang,
        "slug": slug,
        "title": title,
        "word_count": len(prose.split()),
        "overall": overall,
        "checks": checks,
    }


# ---------------------------------------------------------------- auto-test

def selftest():
    """3 articles existants doivent ECHOUER contre eux-memes, 3 textes etrangers PASSER."""
    index = load_index()
    fr = [p for p in index["posts"] if p["lang"] == "fr"]
    if len(fr) < 3:
        print("SELFTEST FAIL: moins de 3 articles francais dans l index")
        return False

    ok = True
    for post in fr[:3]:
        c = content_check(post["text"], index, "fr")
        s = slug_check(post["slug"], index, "fr")
        t = title_check(post["title"], index, "fr")
        good = c["verdict"] == "FAIL" and s["verdict"] == "FAIL" and t["verdict"] == "FAIL"
        print("  %-46s contenu=%s slug=%s titre=%s  %s"
              % (post["slug"][:46], c["verdict"], s["verdict"], t["verdict"],
                 "OK" if good else "ECHEC"))
        ok = ok and good

    etrangers = [
        ("La fermentation du kimchi maison",
         "Le chou nappa se sale pendant deux heures, puis se rince trois fois. "
         "La pate de piment gochugaru se melange a l ail, au gingembre et a la sauce de poisson. "
         "La fermentation se fait a temperature ambiante pendant trois jours, puis au froid. "
         "Le sel tire l eau du chou par osmose et cree la saumure qui protege le legume. "
         "Les bacteries lactiques acidifient le milieu et empechent les moisissures de s installer."),
        ("Reparer une chambre a air de velo",
         "Demontez la roue, degonflez completement, puis inserez deux demonte-pneus a dix "
         "centimetres l un de l autre. Trouvez la perforation en immergeant la chambre dans l eau. "
         "Poncez la zone, appliquez la dissolution, attendez cinq minutes, posez la rustine. "
         "Verifiez l interieur du pneu avant de remonter, sinon le corps etranger perforera encore."),
        ("Les migrations de la sterne arctique",
         "La sterne arctique parcourt chaque annee la distance entre ses aires de nidification "
         "du cercle polaire et les eaux de l Antarctique. Le trajet suit les vents dominants et "
         "les zones de nourriture, ce qui allonge le parcours bien au dela de la ligne droite. "
         "L oiseau voit ainsi deux etes par an et plus de lumiere du jour que tout autre animal."),
    ]
    for title, text in etrangers:
        c = content_check(text, index, "fr")
        t = title_check(title, index, "fr")
        good = c["verdict"] == "PASS" and t["verdict"] == "PASS"
        print("  %-46s contenu=%s titre=%s  %s"
              % (title[:46], c["verdict"], t["verdict"], "OK" if good else "ECHEC"))
        ok = ok and good

    print("SELFTEST", "PASS" if ok else "FAIL")
    return ok


# ---------------------------------------------------------------- cli

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "selftest"
    if cmd == "index":
        idx = build_index()
        print(json.dumps({"total": idx["total"], "counts": idx["counts"]}, ensure_ascii=False))
    elif cmd == "selftest":
        sys.exit(0 if selftest() else 1)
    elif cmd == "check":
        extra = sys.argv[3:]
        report = check_draft(sys.argv[2], extra_drafts=extra)
        print(json.dumps(report, ensure_ascii=False, indent=1))
        sys.exit(0 if report["overall"] != "FAIL" else 2)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
