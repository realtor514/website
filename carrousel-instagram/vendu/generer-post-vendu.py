# -*- coding: utf-8 -*-
"""Publication VENDU | SOLD. Une image 4:5 par propriete vendue.

    python "carrousel-instagram/vendu/generer-post-vendu.py"           les deux
    python "carrousel-instagram/vendu/generer-post-vendu.py" mirabel   une seule

Le visuel courant du marche montrealais, monte comme une pancarte RE/MAX:
trois aplats, les trois couleurs du ballon, et rien d autre.

1. l en-tete bleu, le nom du courtier et la pastille de l agence
2. la facade en plein cadre, barree du bandeau rouge VENDU | SOLD
3. le pied creme: le portrait, le titre, l adresse

Le bleu et le rouge ne sont pas choisis a l oeil: ils sont echantillonnes
dans `static/images/remax-logo.png`, comme le fait deja le generateur des
carrousels. Le ballon donne #0043ff et #ff1200, et ce bleu est exactement le
`--blue` de `static/css/main.css`: la pancarte, le site et le profil parlent
la meme langue. Playfair pour le nom, Inter pour le reste.

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

# ------------------------------------- palette, echantillonnee dans le logo
# remax-logo.png donne ces deux valeurs au pixel pres. Le bleu est aussi le
# --blue de main.css: le site a ete construit sur le meme echantillon.
BLEU = (0, 67, 255)                     # #0043ff, le ballon et --blue
ROUGE = (255, 18, 0)                    # #ff1200, le ballon
NAVY = (0, 14, 53)                      # #000e35, le fonce du logo
CREME = (247, 245, 238)                 # --off-white du site
TEXTE = (26, 35, 50)                    # --text
GRIS = (107, 114, 128)                  # --gray
GRIS_PALE = (152, 159, 172)
BLANC = (255, 255, 255)

COURTIER = "Georges Matar"
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
    """L en-tete bleu: le nom du courtier, puis la pastille de l agence.

    Le ballon est pose sur une pastille blanche a coins arrondis, comme le
    fait le site dans son eyebrow: sans elle, la moitie bleue du ballon se
    fondrait dans le bleu du fond.
    """
    d = ImageDraw.Draw(c)
    d.rectangle([0, 0, W, ENTETE_H], fill=BLEU + (255,))
    d.text((W // 2, 74), COURTIER, font=playfair(86, 700), fill=BLANC,
           anchor="ma")

    cote, pad = 82, 9
    lh = cote - 2 * pad
    lw = logo_w(lh, False)
    fl = inter(24, 700)
    lbl = "RE/MAX DU CARTIER INC."
    total = cote + 22 + tw(d, lbl, fl, 3)
    x = (W - total) / 2
    y = 206
    d.rounded_rectangle([x, y, x + cote, y + cote], 12, fill=BLANC + (255,))
    logo(c, lh, (x + (cote - lw) / 2, y + pad), white=False)
    tracked(d, (x + cote + 22, y + cote / 2 - 13), lbl, fl, BLANC, 3)


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
    # aplat plein, sans filet ni transparence: une pancarte, pas un calque
    d.rectangle([0, haut, W, bas], fill=ROUGE + (255,))

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
    c = Image.new("RGBA", (W, H), CREME + (255,))
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
