# -*- coding: utf-8 -*-
"""Publication VENDU | SOLD. Une image carree 4:5 par propriete vendue.

    python "carrousel-instagram/vendu/generer-post-vendu.py"           les deux
    python "carrousel-instagram/vendu/generer-post-vendu.py" mirabel   une seule

Le visuel le plus courant du marche montrealais: en-tete au nom du courtier,
la facade en plein cadre barree d un VENDU | SOLD bilingue, et en bas le
portrait avec l adresse. Rien d autre. Ce n est pas une annonce, c est une
preuve, et elle doit se lire en une seconde dans un fil.

1080 x 1350, le format qui occupe le plus de hauteur dans le fil Instagram.
Memes couleurs et memes polices que les carrousels et les reels: navy, rouge
RE/MAX, Playfair pour le nom, Inter pour le reste.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "reels"))

import moteur                                                   # noqa: E402
from moteur import (NAVY, RED, WHITE, GREY, INK, inter, playfair,  # noqa: E402
                    logo, logo_w, remplir, tracked, tw, wrap)
from PIL import Image, ImageDraw, ImageFilter                   # noqa: E402

STH = os.path.join(ROOT, "static", "images", "listings",
                   "28-rue-st-hilaire-longueuil")

W, H = 1080, 1350
MARGE = 72
PHOTO_Y0, PHOTO_Y1 = 330, 970           # la bande de photo, pleine largeur

COURTIER = "Georges Matar"
TITRE = "Courtier immobilier résidentiel"
# l attribution a l Equipe Pistoli est due, mais elle n a pas a concurrencer
# le nom du courtier: elle descend dans le pied, en gris pale, sous le titre
EQUIPE = "Équipe Pistoli"
GRIS_PALE = (152, 159, 172)
CONTACT = "438 372-0102   ·   WWW.GEORGESMATAR.CA"


# zoom: 1.0 garde la photo entiere sur la largeur. Au dela, on se rapproche
# du sujet, et fx, fy disent de quel cote on garde ce qui reste.
PROPRIETES = [
    dict(slug="28-rue-st-hilaire-longueuil",
         photo=os.path.join(STH, "03.jpg"), zoom=1.30, fx=0.53, fy=0.54,
         adresse=["28, RUE ST-HILAIRE", "LONGUEUIL (VIEUX-LONGUEUIL)"]),

    # la vue de la rue plutot que la facade: le grand pin et le rang disent
    # la campagne en une seconde, et la facade de cote montrait la
    # bonbonne de propane et la generatrice
    dict(slug="4071-rang-saint-hyacinthe-mirabel",
         photo="23-Vue de la rue.png", zoom=1.0, fx=0.5, fy=0.50,
         adresse=["4071, RANG SAINT-HYACINTHE",
                  "MIRABEL (SAINT-HERMAS)"]),
]


def entete(c):
    """Le nom du courtier et l agence, comme un en-tete de papier a lettres."""
    d = ImageDraw.Draw(c)
    d.text((W // 2, 96), COURTIER, font=playfair(84, 700), fill=NAVY,
           anchor="ma")

    lh = 58
    lw = logo_w(lh, False)
    f = inter(24, 700)
    lbl = "RE/MAX DU CARTIER INC."
    total = lw + 20 + d.textlength(lbl, font=f)
    x = (W - total) / 2
    logo(c, lh, (x, 216), white=False)
    d.text((x + lw + 20, 216 + lh / 2), lbl, font=f, fill=NAVY, anchor="lm")


def bande_photo(c, prop):
    """La facade, pleine largeur, legerement assombrie pour porter le texte."""
    h = PHOTO_Y1 - PHOTO_Y0
    z = prop.get("zoom", 1.0)
    im = remplir(moteur._ouvrir(prop["photo"]), int(W * z), int(h * z),
                 prop.get("fx", 0.5), prop.get("fy", 0.5))
    if z != 1.0:                        # on recadre au centre du sujet vise
        x = int((im.width - W) * prop.get("fx", 0.5))
        y = int((im.height - h) * prop.get("fy", 0.5))
        im = im.crop((x, y, x + W, y + h))
    im = im.filter(ImageFilter.UnsharpMask(2, 48, 3)).convert("RGBA")
    im.alpha_composite(Image.new("RGBA", (W, h), NAVY + (58,)))
    c.alpha_composite(im, (0, PHOTO_Y0))


def vendu_sold(c):
    """VENDU | SOLD au centre de la photo.

    Deux mots, un filet entre les deux, et une ombre floue dessous: c est
    elle qui garantit la lisibilite sur une brique claire comme sur un ciel,
    sans avoir a noircir la photo davantage.
    """
    f = inter(94, 300)
    track = 9
    d = ImageDraw.Draw(c)
    wv, ws = tw(d, "VENDU", f, track), tw(d, "SOLD", f, track)
    ecart, filet = 48, 3
    total = wv + ecart + filet + ecart + ws
    x = (W - total) / 2
    y = PHOTO_Y0 + (PHOTO_Y1 - PHOTO_Y0) * 0.44

    def peindre(dessin, couleur):
        tracked(dessin, (x, y), "VENDU", f, couleur, track)
        dessin.rectangle([x + wv + ecart, y + 8,
                          x + wv + ecart + filet, y + 102], fill=couleur)
        tracked(dessin, (x + wv + ecart + filet + ecart, y), "SOLD", f,
                couleur, track)

    ombre = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    peindre(ImageDraw.Draw(ombre), (0, 6, 22, 168))
    c.alpha_composite(ombre.filter(ImageFilter.GaussianBlur(20)))
    peindre(d, WHITE + (255,))


def pied(c, prop):
    """Le portrait a gauche, l adresse a droite. Le portrait mord sur la
    photo: c est ce chevauchement qui empeche l image de se couper en deux."""
    p = Image.open(os.path.join(moteur.SOURCES, "georges-matar-decoupe.png"))
    p = p.crop(p.getchannel("A").getbbox())
    ph = 468
    pw = int(p.width * ph / p.height)
    c.alpha_composite(p.resize((pw, ph), Image.LANCZOS), (18, H - ph))

    d = ImageDraw.Draw(c)
    x = 18 + pw + 34
    dispo = W - MARGE - x
    d.text((x, 1014), COURTIER, font=inter(38, 800), fill=NAVY)
    y = 1066
    for ln in wrap(d, TITRE, inter(25, 400), dispo):
        d.text((x, y), ln, font=inter(25, 400), fill=GREY)
        y += 34
    d.text((x, y + 2), EQUIPE, font=inter(23, 400), fill=GRIS_PALE)
    y += 38

    y = max(y + 16, 1148)
    d.rectangle([x, y, x + 64, y + 5], fill=RED + (255,))
    y += 28
    for ln in prop["adresse"]:
        for bout in wrap(d, ln, inter(27, 700), dispo):
            d.text((x, y), bout, font=inter(27, 700), fill=INK)
            y += 38

    # la ligne de coordonnees se pose sous l adresse, jamais dessus, meme si
    # une adresse prend une ligne de plus, et se resserre jusqu a tenir dans
    # la largeur restante plutot que de deborder sur la marge
    taille, track = 21, 3
    while taille > 16 and tw(d, CONTACT, inter(taille, 600), track) > dispo:
        taille -= 1
        track = 2
    tracked(d, (x, max(y + 24, H - 82)), CONTACT, inter(taille, 600), GREY,
            track)


def fabriquer(prop):
    c = Image.new("RGBA", (W, H), (255, 255, 255, 255))
    entete(c)
    bande_photo(c, prop)
    vendu_sold(c)
    pied(c, prop)
    return c.convert("RGB")


def main():
    filtre = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    for prop in PROPRIETES:
        if filtre and filtre not in prop["slug"]:
            continue
        dossier = os.path.join(HERE, prop["slug"])
        os.makedirs(dossier, exist_ok=True)
        chemin = os.path.join(dossier, "publication-vendu.jpg")
        fabriquer(prop).save(chemin, quality=94, subsampling=0)
        print("Publication VENDU ->", chemin)


if __name__ == "__main__":
    main()
