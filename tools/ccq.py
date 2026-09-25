#!/usr/bin/env python3
"""Lit le Code civil du Quebec quand legisquebec.gouv.qc.ca est hors service.

    python tools/ccq.py 1726 1739 2925      affiche ces articles
    python tools/ccq.py --chercher "vice cache"   cherche dans tout le code
    python tools/ccq.py --maj                 force le retelechargement

Pourquoi ce fichier existe. Le 25 septembre 2026, legisquebec.gouv.qc.ca a
repondu 502 pendant toute une journee de redaction. Quatre redacteurs ont
retire des citations du Code civil plutot que de les ecrire de memoire, ce qui
etait la bonne decision mais a laisse des articles plus faibles que la voix du
site. CanLII repond 403, et ccq.lexum.com est une coquille JavaScript.

La route qui marche est une capture datee de web.archive.org de la page
officielle. Une archive de la page officielle reste la page officielle: citez
l URL canonique de LegisQuebec, et dites dans le JOSN de meta que vous l avez
lue par archive, avec la date de la capture.

Deux pieges qui ont coute du temps:
  - l URL doit porter le suffixe `id_` apres l horodatage, sinon Wayback
    reinjecte sa barre d outils dans la page;
  - la reponse est gzippee, donc curl a besoin de `--compressed`. Sans lui on
    recupere 633 ko de binaire qui ressemble a une page vide.

Le cache local est gitignore: c est une copie d un texte de loi, elle n a rien
a faire dans le depot.
"""

import gzip
import html
import io
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "state" / "reference_cache" / "ccq.json"
CANONIQUE = "https://www.legisquebec.gouv.qc.ca/fr/document/lc/CCQ-1991"
CAPTURE = "20260310"
SOURCE = "https://web.archive.org/web/%sid_/%s" % (CAPTURE, CANONIQUE)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")


def telecharger():
    req = urllib.request.Request(SOURCE, headers={
        "User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=180) as r:
        brut = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            brut = gzip.decompress(brut)
    return brut.decode("utf-8", errors="replace")


def decouper(page):
    """Rend {numero: texte}. Sur cette page, le numero vit dans son propre
    element et le texte suit dans les elements d apres."""
    t = re.sub(r"<[^>]+>", "\n", page)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    lignes = [l.strip() for l in t.split("\n")]
    lignes = [l for l in lignes if l]

    positions = {}
    for i, l in enumerate(lignes):
        m = re.fullmatch(r"(\d{1,4}(?:\.\d+)?)\s*\.?", l)
        if m and m.group(1) not in positions:
            positions[m.group(1)] = i

    ordre = sorted(positions.items(), key=lambda kv: kv[1])
    arts = {}
    for n, (num, i) in enumerate(ordre):
        fin = ordre[n + 1][1] if n + 1 < len(ordre) else len(lignes)
        corps = " ".join(lignes[i + 1:fin]).lstrip(". ").strip()
        # Couper a la premiere reference de sanction, qui clot l article et
        # est suivie de la chaine des modifications puis parfois d un titre
        # de section appartenant deja a l article suivant.
        coupe = re.search(r"\s*\d{4}, c\. \d+,? a\. [\d.]+", corps)
        if coupe:
            corps = corps[:coupe.start()].strip()
        if corps:
            arts[num] = corps
    return arts


def charger(maj=False):
    if CACHE.is_file() and not maj:
        return json.loads(CACHE.read_text(encoding="utf-8"))
    arts = decouper(telecharger())
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(arts, ensure_ascii=False), encoding="utf-8")
    return arts


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    args = sys.argv[1:]
    maj = "--maj" in args
    args = [a for a in args if a != "--maj"]

    arts = charger(maj)

    if maj and not args:
        print("%d articles en cache." % len(arts))
        return

    if args and args[0] == "--chercher":
        besoin = " ".join(args[1:]).lower()
        if not besoin:
            print("Donnez un terme a chercher.")
            return
        n = 0
        for num, txt in arts.items():
            if besoin in txt.lower():
                print("art %s: %s" % (num, txt[:220]))
                n += 1
                if n >= 25:
                    print("... (limite a 25)")
                    break
        if not n:
            print("Rien trouve pour: %s" % besoin)
        return

    if not args:
        print(__doc__)
        print("%d articles en cache." % len(arts))
        return

    for num in args:
        txt = arts.get(num)
        print("\n=== Code civil du Quebec, article %s ===" % num)
        print(txt if txt else "NON TROUVE. Verifiez le numero.")
    print("\nSource a citer: %s" % CANONIQUE)
    print("Lu par capture web.archive.org du %s-%s-%s."
          % (CAPTURE[:4], CAPTURE[4:6], CAPTURE[6:]))


if __name__ == "__main__":
    main()
