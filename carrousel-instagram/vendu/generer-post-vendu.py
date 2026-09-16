# -*- coding: utf-8 -*-
"""Publication VENDU | SOLD. Une image 4:5 par propriete vendue.

    python "carrousel-instagram/vendu/generer-post-vendu.py"           les deux
    python "carrousel-instagram/vendu/generer-post-vendu.py" mirabel   une seule

Le visuel courant du marche montrealais, mais habille aux couleurs du site
georgesmatar.ca plutot qu en blanc neutre. Les valeurs sont prises telles
quelles dans `static/css/main.css`, le fichier qui habille le site: navy
#0a1628, rouge #B00000, bleu #0043FF, creme #F7F5EE, Playfair pour les titres
et Inter pour le reste. Le profil Instagram et le site se repondent.

La structure, de haut en bas:

1. le triple filet rouge, blanc, bleu du ballon RE/MAX, sur fond navy
2. le nom du courtier, dont le patronyme en bleu, comme le hero du site
3. la facade en plein cadre, barree d un bandeau rouge VENDU | SOLD
4. le pied creme: le portrait, le titre, l adresse

Pas de prix, pas de caracteristiques. Ce n est pas une annonce, c est une
preuve, et elle doit se lire en une seconde dans un fil.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "reels"))

import moteur                                                   # noqa: E402
from moteur import (inter, playfair, logo, logo_w, remplir,      # noqa: E402
                    tracked, tw, wrap)
from PIL import Image, ImageDraw, ImageFilter                   # noqa: E402

STH = os.path.join(ROOT, "static", "images", "listings",
                   "28-rue-st-hilaire-longueuil")

W, H = 1080, 1350
MARGE = 72
ENTETE_H = 330                          # le bloc navy du haut
PHOTO_Y0, PHOTO_Y1 = 330, 970           # la bande de photo, pleine largeur

# --------------------------------------------- palette du site, main.css
NAVY = (10, 22, 40)                     # --navy
ROUGE = (176, 0, 0)                     # --red
BLEU = (0, 67, 255)                     # --blue
BLEU_VIF = (46, 107, 255)               # --blue-bright, lisible sur le navy
CREME = (247, 245, 238)                 # --off-white
TEXTE = (26, 35, 50)                    # --text
GRIS = (107, 114, 128)                  # --gray
GRIS_PALE = (152, 159, 172)
BLANC = (255, 255, 255)

COURTIER_PRENOM = "Georges "
COURTIER_NOM = "Matar"
COURTIER = COURTIER_PRENOM + COURTIER_NOM
TITRE = "Courtier immobilier résidentiel"
# l attribution a l Equipe Pistoli est due, mais elle n a pas a concurrencer
# le nom du courtier: elle reste dans le pied, en gris pale, sous le titre
EQUIPE = "Équipe Pistoli"
CONTACT = "438 372-0102   ·   WWW.GEORGESMATAR.CA"


# zoom: 1.0 garde la photo entiere sur la largeur. Au dela, on se rapproche
# du sujet, et fx, fy disent de quel cote on garde ce qui reste.
PROPRIETES = [
    # bandeau: la hauteur ou passe le bandeau rouge. Il se place la ou il ne
    # coupe pas la maison: sous elle a Longueuil, dans les arbres a Mirabel
    dict(slug="28-rue-st-hilaire-longueuil",
         photo=os.path.join(STH, "03.jpg"), zoom=1.30, fx=0.53, fy=0.54,
         bandeau=700,
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
    """Fond navy, filet RE/MAX, nom du courtier et agence."""
    d = ImageDraw.Draw(c)
    d.rectangle([0, 0, W, ENTETE_H], fill=NAVY + (255,))

    # le triple filet du ballon: rouge, blanc, bleu
    for i, couleur in enumerate([ROUGE, BLANC, BLEU]):
        d.rectangle([0, i * 5, W, i * 5 + 5], fill=couleur + (255,))

    # le patronyme en bleu, exactement comme le titre du hero sur le site
    f = playfair(86, 700)
    wp = d.textlength(COURTIER_PRENOM, font=f)
    wn = d.textlength(COURTIER_NOM, font=f)
    x = (W - (wp + wn)) / 2
    d.text((x, 92), COURTIER_PRENOM, font=f, fill=BLANC)
    d.text((x + wp, 92), COURTIER_NOM, font=f, fill=BLEU_VIF)

    lh = 56
    lw = logo_w(lh, False)
    fl = inter(23, 700)
    lbl = "RE/MAX DU CARTIER INC."
    total = lw + 20 + tw(d, lbl, fl, 3)
    x = (W - total) / 2
    logo(c, lh, (x, 222), white=False)
    tracked(d, (x + lw + 20, 222 + lh / 2 - 13), lbl, fl, BLANC, 3)


def bande_photo(c, prop):
    """La facade, pleine largeur, a peine assombrie: le bandeau rouge suffit
    a porter le texte, inutile d etouffer la photo."""
    h = PHOTO_Y1 - PHOTO_Y0
    z = prop.get("zoom", 1.0)
    im = remplir(moteur._ouvrir(prop["photo"]), int(W * z), int(h * z),
                 prop.get("fx", 0.5), prop.get("fy", 0.5))
    if z != 1.0:                        # on recadre au centre du sujet vise
        x = int((im.width - W) * prop.get("fx", 0.5))
        y = int((im.height - h) * prop.get("fy", 0.5))
        im = im.crop((x, y, x + W, y + h))
    im = im.filter(ImageFilter.UnsharpMask(2, 48, 3)).convert("RGBA")
    im.alpha_composite(Image.new("RGBA", (W, h), NAVY + (34,)))
    c.alpha_composite(im, (0, PHOTO_Y0))


def bandeau_vendu(c, prop):
    """Le bandeau rouge en travers de la photo.

    Un aplat rouge pleine largeur plutot qu un texte pose sur la photo: c est
    le seul traitement qui reste lisible dans une vignette de fil, et c est
    le code couleur que tout le monde associe deja a RE/MAX.
    """
    haut = prop.get("bandeau", 596)
    bas = haut + 158
    d = ImageDraw.Draw(c)
    d.rectangle([0, haut, W, bas], fill=ROUGE + (242,))
    d.rectangle([0, haut, W, haut + 4], fill=BLANC + (70,))
    d.rectangle([0, bas - 4, W, bas], fill=(0, 0, 0, 52))

    f = inter(88, 300)
    track = 9
    wv, ws = tw(d, "VENDU", f, track), tw(d, "SOLD", f, track)
    ecart, filet = 46, 3
    x = (W - (wv + ecart + filet + ecart + ws)) / 2
    y = haut + (bas - haut - 88) / 2 - 6
    tracked(d, (x, y), "VENDU", f, BLANC, track)
    d.rectangle([x + wv + ecart, y + 10, x + wv + ecart + filet, y + 92],
                fill=BLANC + (200,))
    tracked(d, (x + wv + ecart + filet + ecart, y), "SOLD", f, BLANC, track)


def pied(c, prop):
    """Le pied creme: le portrait a gauche, l adresse a droite.

    Le pied reste clair alors que l en-tete est navy: le portrait est un
    decoupe en complet sombre, il disparaitrait sur un fond fonce.
    """
    d = ImageDraw.Draw(c)
    d.rectangle([0, PHOTO_Y1, W, H], fill=CREME + (255,))

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
        d.text((x, y), ln, font=inter(25, 400), fill=GRIS)
        y += 34
    d.text((x, y + 2), EQUIPE, font=inter(23, 400), fill=GRIS_PALE)
    y += 38

    y = max(y + 16, 1148)
    d.rectangle([x, y, x + 64, y + 5], fill=ROUGE + (255,))
    y += 28
    for ln in prop["adresse"]:
        for bout in wrap(d, ln, inter(27, 700), dispo):
            d.text((x, y), bout, font=inter(27, 700), fill=TEXTE)
            y += 38

    # la ligne de coordonnees se pose sous l adresse, jamais dessus, et se
    # resserre jusqu a tenir dans la largeur restante plutot que de deborder
    taille, track = 21, 3
    while taille > 16 and tw(d, CONTACT, inter(taille, 600), track) > dispo:
        taille -= 1
        track = 2
    tracked(d, (x, max(y + 24, H - 82)), CONTACT, inter(taille, 600), GRIS,
            track)


def fabriquer(prop):
    c = Image.new("RGBA", (W, H), NAVY + (255,))
    entete(c)
    bande_photo(c, prop)
    bandeau_vendu(c, prop)
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
