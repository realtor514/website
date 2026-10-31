"""Signale a IndexNow (Bing, et par lui ChatGPT, Yandex, Seznam, Naver) les
pages modifiees depuis une date, pour qu elles soient explorees sans attendre.

Usage, depuis la racine du depot, apres le deploiement (la cle doit etre en
ligne a https://georgesmatar.ca/<cle>.txt):

    hugo --quiet -d %TEMP%\\gm-build
    python -I tools/indexnow.py %TEMP%\\gm-build 2026-10-31
    python -I tools/indexnow.py %TEMP%\\gm-build 2026-10-31 --dry-run

Les adresses viennent des sitemaps construits (une par langue) et de leur
balise lastmod: seules celles dont lastmod est egal ou posterieur a la date
sont envoyees. Une seule requete, 10 000 adresses au plus.
"""
import json
import os
import re
import sys
import urllib.request

HOST = "georgesmatar.ca"
KEY = "415bda2a956ce8319b21462f95b279df"
ENDPOINT = "https://api.indexnow.org/indexnow"


def urls_since(build_dir, since):
    found = {}
    for lang in ("fr", "en", "es", "ar"):
        path = os.path.join(build_dir, lang, "sitemap.xml")
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            xml = f.read()
        for block in re.findall(r"<url>(.*?)</url>", xml, re.S):
            loc = re.search(r"<loc>(.*?)</loc>", block)
            mod = re.search(r"<lastmod>(.*?)</lastmod>", block)
            if loc and mod and mod.group(1)[:10] >= since:
                found[loc.group(1).strip()] = True
    return list(found)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    build_dir, since = args
    urls = urls_since(build_dir, since)[:10000]
    print(f"{len(urls)} adresse(s) modifiee(s) depuis le {since}")
    if not urls or "--dry-run" in sys.argv:
        for u in urls[:20]:
            print("  " + u)
        return
    body = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{HOST}/{KEY}.txt",
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow: HTTP {r.status}")


if __name__ == "__main__":
    main()
