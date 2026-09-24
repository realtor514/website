#!/usr/bin/env python3
"""Telecharge l image a la une des articles qui n en ont pas.

    python tools/fetch_images.py --check      liste ce qui manque, ne telecharge rien
    python tools/fetch_images.py              telecharge ce qui manque

Chaque article du site attend `static/images/articles/<slug>/featured.jpg`. Le
gabarit fait `{{ with .Params.image }}`, donc un champ rempli pointant vers un
fichier absent produit une image cassee, et le placeholder ne prend jamais le
relais. D ou ce script.

Les cles viennent de .env, jamais du code. Pexels en premier, Unsplash en
secours. On demande directement une largeur de 1200 px a l API, ce qui evite de
retraiter l image localement et respecte le format des 64 images deja en place:
JPEG paysage, 80 a 200 ko.
"""

import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "static" / "images" / "articles"

# Termes de recherche en anglais: les banques d images indexent en anglais.
# Choisis pour donner une photo credible pour un courtier, pas une illustration.
QUERIES = {
    "contester-evaluation-municipale-quebec": "property tax documents desk calculator",
    "cout-entretien-maison-quebec": "house roof maintenance repair",
    "maison-difficile-assurer-quebec": "older brick house exterior",
    "refinancement-hypothecaire-quebec": "mortgage documents signing pen",
    "renovation-condo-copropriete-quebec": "condo apartment renovation interior",
    "acheter-zone-inondable-quebec": "flooded residential street water",
    "arbres-propriete-reglements-quebec": "large mature tree residential yard",
    "comparables-prix-maison-voisin-quebec": "suburban houses neighbourhood street",
    "impot-proprietaire-quebec": "tax forms calculator paperwork",
    "reduire-facture-chauffage-quebec": "home thermostat heating winter",
    "choisir-inspecteur-batiment-quebec": "home inspector clipboard house",
    "contrat-courtage-vente-quebec": "signing real estate contract",
    "garder-ou-vendre-propriete-quebec": "house for sale sign lawn",
    "location-court-terme-quebec-regles": "furnished apartment living room",
    "vente-sans-garantie-legale-quebec": "old house inspection interior",
    "conjoints-de-fait-maison-quebec": "couple holding house keys",
    "declaration-du-vendeur-quebec": "filling out form paperwork desk",
    "propriete-ne-se-vend-pas-quebec": "for sale sign house winter",
    "acheter-reprise-de-finance-quebec": "empty vacant house interior",
    "bruit-maison-condo-quebec": "apartment building balconies facade",
    "casser-hypotheque-penalite-quebec": "calculator financial documents money",
    "copropriete-indivise-cooperative-montreal": "montreal triplex exterior staircase",
    "ventre-de-boeuf-drain-montreal": "basement plumbing pipes drain",
    "vice-cache-conditions-recours-quebec": "water damage wall ceiling stain",
    "garantie-gcr-maison-neuve-quebec": "new house construction framing",
}


def env(name):
    f = ROOT / ".env"
    if not f.is_file():
        return None
    for line in f.read_text(encoding="utf-8").splitlines():
        if line.startswith(name + "="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def get(url, headers=None, timeout=45):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def from_pexels(query, key):
    url = ("https://api.pexels.com/v1/search?query=%s&orientation=landscape&per_page=5"
           % urllib.parse.quote(query))
    data = json.loads(get(url, {"Authorization": key}))
    for photo in data.get("photos", []):
        src = photo["src"].get("large") or photo["src"].get("original")
        if src:
            sized = re.sub(r"[?&]w=\d+", "", src)
            sep = "&" if "?" in sized else "?"
            return get(sized + sep + "w=1200"), photo.get("photographer", ""), photo.get("url", "")
    return None, None, None


def from_unsplash(query, key):
    url = ("https://api.unsplash.com/search/photos?query=%s&orientation=landscape&per_page=5"
           % urllib.parse.quote(query))
    data = json.loads(get(url, {"Authorization": "Client-ID " + key}))
    for photo in data.get("results", []):
        raw = photo["urls"].get("raw")
        if raw:
            sep = "&" if "?" in raw else "?"
            return (get(raw + sep + "w=1200&fm=jpg&q=80"),
                    photo.get("user", {}).get("name", ""), photo.get("links", {}).get("html", ""))
    return None, None, None


def missing():
    out = []
    for slug in QUERIES:
        if not (IMG / slug / "featured.jpg").is_file():
            out.append(slug)
    return out


def main():
    todo = missing()
    print("%d image(s) manquante(s) sur %d articles suivis" % (len(todo), len(QUERIES)))
    if "--check" in sys.argv:
        for s in todo:
            print("  manque:", s)
        return
    if not todo:
        return

    pexels, unsplash = env("PEXELS_API_KEY"), env("UNSPLASH_API_KEY")
    if not pexels and not unsplash:
        print("Aucune cle dans .env, rien a faire.")
        sys.exit(1)

    credits = {}
    ok = fail = 0
    for slug in todo:
        q = QUERIES[slug]
        blob = who = where = None
        for name, fn, key in (("pexels", from_pexels, pexels), ("unsplash", from_unsplash, unsplash)):
            if not key:
                continue
            try:
                blob, who, where = fn(q, key)
                if blob and len(blob) > 20000:
                    source = name
                    break
                blob = None
            except Exception as e:
                print("  %-46s %s a echoue: %s" % (slug[:46], name, type(e).__name__))
                blob = None
        if not blob:
            print("  ECHEC %s" % slug)
            fail += 1
            continue
        d = IMG / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "featured.jpg").write_bytes(blob)
        credits[slug] = {"source": source, "photographe": who, "page": where, "recherche": q}
        print("  ok    %-46s %4d ko  %s" % (slug[:46], len(blob) // 1024, source))
        ok += 1

    if credits:
        path = ROOT / "static" / "images" / "articles" / "CREDITS.json"
        old = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
        old.update(credits)
        path.write_text(json.dumps(old, ensure_ascii=False, indent=1), encoding="utf-8")
        print("\nCredits ecrits dans static/images/articles/CREDITS.json")
    print("%d telechargee(s), %d echec(s)" % (ok, fail))


if __name__ == "__main__":
    main()
