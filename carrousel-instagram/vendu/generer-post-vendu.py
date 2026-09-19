# -*- coding: utf-8 -*-
"""Visuels VENDU | SOLD. Deux formats par propriete vendue.

    python "carrousel-instagram/vendu/generer-post-vendu.py"           les deux
    python "carrousel-instagram/vendu/generer-post-vendu.py" mirabel   une seule

| Fichier | Format | Ou il sert |
|---------|--------|------------|
| `publication-vendu.jpg` | 1080 x 1350, 4:5 | la publication dans le fil |
| `couverture-vendu.jpg` | 1080 x 1920, 9:16 | la couverture du reel |

Les deux disent la meme chose et se ressemblent, mais ils ne peuvent pas etre
le meme fichier. Instagram recadre une image 4:5 posee en couverture de reel:
il garde les 70 pour cent du milieu et coupe 15 pour cent de chaque cote. Le
nom et l adresse, qui commencent sur la marge de gauche, s y font manger. La
couverture est donc dessinee en 9:16, et tout ce qui compte tient dans la
bande centrale que la grille du profil recadre en 3:4.

Le visuel courant du marche montrealais, monte comme une pancarte RE/MAX:
trois aplats et rien d autre.

1. l en-tete navy, le nom du courtier et la pastille de l agence
2. la facade en plein cadre, barree du bandeau rouge VENDU | SOLD
3. le pied creme: le portrait a droite, le nom et l adresse a gauche

Les couleurs suivent la charte RE/MAX DU CARTIER, et surtout sa hierarchie.
Navy #000E35 et creme #F7F5EE sont les principales: ce sont elles qui portent
les grands aplats. Bleu #0043FF, bordeaux #600000 et rouge #FF1200 sont
secondaires: elles n accentuent. Le bandeau rouge est la seule exception a
cette regle, et c est voulu: c est lui qui dit VENDU, et il doit se lire dans
une vignette de fil.

Playfair pour le nom, Inter pour le reste, comme sur le site.

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

W = 1080
MARGE = 72

# ------------------------------------------ palette RE/MAX DU CARTIER
# La charte distingue deux principales et trois secondaires, et cet ordre
# se voit: les grands aplats sont navy et creme, les secondaires ne servent
# qu a accentuer. Le bandeau rouge est la seule exception, et c est voulu:
# c est lui qui dit VENDU.
NAVY = (0, 14, 53)                      # #000E35   principale, l en-tete
CREME = (247, 245, 238)                 # #F7F5EE   principale, le pied
BLEU = (0, 67, 255)                     # #0043FF   secondaire, le filet
ROUGE = (255, 18, 0)                    # #FF1200   secondaire, le bandeau
BORDEAUX = (96, 0, 0)                   # #600000   secondaire, non utilise ici

GRIS = (107, 114, 128)                  # --gray du site, pour le titre
GRIS_PALE = (152, 159, 172)

COURTIER = "Georges Matar"
TITRE = "Courtier immobilier résidentiel"
# l attribution a l Equipe Pistoli est due, mais elle n a pas a concurrencer
# le nom du courtier: elle reste dans le pied, en gris pale, sous le titre
EQUIPE = "Équipe Pistoli"
CONTACT = "438 372-0102   ·   WWW.GEORGESMATAR.CA"


# Les deux geometries. Sur la publication, `bandeau` est la valeur par
# defaut, une propriete peut la corriger pour que le rouge ne coupe pas la
# maison.
#
# Sur la couverture, `bandeau` est le meme pour toutes les proprietes, sans
# exception: les reels VENDU se suivent dans la grille du profil, et un rouge
# qui saute d une vignette a l autre se voit tout de suite. C est la photo
# qui se recadre autour du bandeau, avec `cadrage_couverture`, jamais
# l inverse. La grille recadre le 9:16 en 3:4, soit la bande de 240 a 1680.
# Le bandeau passe a 960, un peu sous le milieu de cette bande: plus haut, il
# coupait la galerie de Longueuil, que le cadrage ne peut plus remonter.
#
# `nom` et `pastille` sont des hauteurs absolues et non un centrage: sur la
# couverture, elles descendent volontairement sous la ligne des 240 px, la
# ou commence le recadrage de la grille. Centrees, elles tombaient hors
# vignette et la grille du profil n affichait qu une bande navy vide.
FORMATS = {
    "publication": dict(fichier="publication-vendu.jpg", h=1350, entete=330,
                        nom=82, pastille=216, photo=(330, 970), bandeau=596,
                        portrait=468),
    "couverture":  dict(fichier="couverture-vendu.jpg", h=1920, entete=560,
                        nom=300, pastille=432, photo=(560, 1440), bandeau=960,
                        portrait=560),
}


# zoom: 1.0 garde la photo entiere sur la largeur. Au dela, on se rapproche
# du sujet, et fx, fy disent de quel cote on garde ce qui reste.
# `cadrage_couverture` corrige ces trois valeurs pour la couverture seule.
PROPRIETES = [
    # bandeau: la hauteur ou passe le rouge sur la publication, la ou il ne
    # coupe pas la maison. Sur la couverture, le bandeau ne bouge pas, et
    # la photo remonte pour que toute la galerie passe au dessus du rouge.
    dict(slug="28-rue-st-hilaire-longueuil",
         photo=os.path.join(STH, "03.jpg"), zoom=1.30, fx=0.53, fy=0.54,
         bandeau=700, cadrage_couverture=dict(fy=0.80),
         adresse=["28, RUE ST-HILAIRE", "LONGUEUIL (VIEUX-LONGUEUIL)"],
         adresse_courte=["28, RUE ST-HILAIRE", "VIEUX-LONGUEUIL"]),

    # la vue de la rue plutot que la facade: le grand pin et le rang disent
    # la campagne en une seconde, et la facade de cote montrait la
    # bonbonne de propane et la generatrice. Sur la couverture, la photo
    # descend un peu pour que le rez de chaussee passe sous le rouge.
    dict(slug="4071-rang-saint-hyacinthe-mirabel",
         photo="23-Vue de la rue.png", zoom=1.0, fx=0.5, fy=0.50,
         cadrage_couverture=dict(zoom=1.06, fy=0.0),
         adresse=["4071, RANG SAINT-HYACINTHE",
                  "MIRABEL (SAINT-HERMAS)"],
         adresse_courte=["4071, RANG SAINT-HYACINTHE",
                         "SAINT-HERMAS, MIRABEL"]),
]


def entete(c, g):
    """L en-tete navy: le nom du courtier, puis la pastille de l agence.

    Navy et creme, les deux principales de la charte, et rien d autre. Le
    ballon est pose sur une pastille creme a coins arrondis, comme le fait le
    site dans son eyebrow: sans elle, la moitie foncee du ballon se fondrait
    dans le fond.
    """
    d = ImageDraw.Draw(c)
    d.rectangle([0, 0, W, g["entete"]], fill=NAVY + (255,))

    d.text((W // 2, g["nom"]), COURTIER, font=playfair(86, 700), fill=CREME,
           anchor="ma")

    cote, pad = 82, 9
    lh = cote - 2 * pad
    lw = logo_w(lh, False)
    fl = inter(24, 700)
    lbl = "RE/MAX DU CARTIER INC."
    total = cote + 22 + tw(d, lbl, fl, 3)
    x = (W - total) / 2
    y = g["pastille"]
    d.rounded_rectangle([x, y, x + cote, y + cote], 12, fill=CREME + (255,))
    logo(c, lh, (x + (cote - lw) / 2, y + pad), white=False)
    tracked(d, (x + cote + 22, y + cote / 2 - 13), lbl, fl, CREME, 3)


def bande_photo(c, prop, g, cle):
    """La facade, pleine largeur, a peine assombrie: le bandeau rouge suffit
    a porter le texte, inutile d etouffer la photo."""
    r = dict(prop)
    if cle == "couverture":
        r.update(prop.get("cadrage_couverture", {}))
    y0, y1 = g["photo"]
    h = y1 - y0
    z = r.get("zoom", 1.0)
    im = remplir(moteur._ouvrir(r["photo"]), int(W * z), int(h * z),
                 r.get("fx", 0.5), r.get("fy", 0.5))
    if z != 1.0:                        # on recadre au centre du sujet vise
        x = int((im.width - W) * r.get("fx", 0.5))
        y = int((im.height - h) * r.get("fy", 0.5))
        im = im.crop((x, y, x + W, y + h))
    im = im.filter(ImageFilter.UnsharpMask(2, 48, 3)).convert("RGBA")
    im.alpha_composite(Image.new("RGBA", (W, h), NAVY + (34,)))
    c.alpha_composite(im, (0, y0))


def bandeau_vendu(c, prop, g, cle):
    """Le bandeau rouge en travers de la photo.

    Un aplat rouge pleine largeur plutot qu un texte pose sur la photo: c est
    le seul traitement qui reste lisible dans une vignette de fil, et c est
    le code couleur que tout le monde associe deja a RE/MAX.
    """
    # la couverture ignore toute correction: meme hauteur pour tous les reels
    haut = prop.get("bandeau") if cle == "publication" else None
    haut = haut or g["bandeau"]
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
    tracked(d, (x, y), "VENDU", f, CREME, track)
    d.rectangle([x + wv + ecart, y + 10, x + wv + ecart + filet, y + 92],
                fill=CREME + (200,))
    tracked(d, (x + wv + ecart + filet + ecart, y), "SOLD", f, CREME, track)


def _portrait(c, g):
    """Le decoupe, cale en bas a droite. Il mord sur la photo: c est ce
    chevauchement qui empeche l image de se couper en deux."""
    p = Image.open(os.path.join(moteur.SOURCES, "georges-matar-decoupe.png"))
    p = p.crop(p.getchannel("A").getbbox())
    ph = g["portrait"]
    pw = int(p.width * ph / p.height)
    c.alpha_composite(p.resize((pw, ph), Image.LANCZOS),
                      (W - 18 - pw, g["h"] - ph))
    return pw


def pied_publication(c, prop, g):
    """Le pied creme de la publication: tout y est, jusqu aux coordonnees.

    Le pied reste clair alors que l en-tete est navy: le portrait est un
    decoupe en complet sombre, il disparaitrait sur un fond fonce.
    """
    H = g["h"]
    d = ImageDraw.Draw(c)
    d.rectangle([0, g["photo"][1], W, H], fill=CREME + (255,))
    pw = _portrait(c, g)

    # le texte garde son alignement a gauche, sur la marge de la page: c est
    # le bord que l oeil suit, et le portrait ferme le bloc a droite
    d = ImageDraw.Draw(c)
    x = MARGE
    dispo = (W - 18 - pw) - 34 - x
    d.text((x, 1014), COURTIER, font=inter(38, 800), fill=NAVY)
    y = 1066
    for ln in wrap(d, TITRE, inter(25, 400), dispo):
        d.text((x, y), ln, font=inter(25, 400), fill=GRIS)
        y += 34
    d.text((x, y + 2), EQUIPE, font=inter(23, 400), fill=GRIS_PALE)
    y += 38

    # le filet d accent est bleu et non rouge: le rouge est deja pris par le
    # bandeau, et le bleu est la seule secondaire qui ne sert nulle part
    # ailleurs que dans le ballon
    y = max(y + 16, 1148)
    d.rectangle([x, y, x + 64, y + 5], fill=BLEU + (255,))
    y += 28
    for ln in prop["adresse"]:
        for bout in wrap(d, ln, inter(27, 700), dispo):
            d.text((x, y), bout, font=inter(27, 700), fill=NAVY)
            y += 38

    # la ligne de coordonnees se pose sous l adresse, jamais dessus, et se
    # resserre jusqu a tenir dans la largeur restante plutot que de deborder
    taille, track = 21, 3
    while taille > 16 and tw(d, CONTACT, inter(taille, 600), track) > dispo:
        taille -= 1
        track = 2
    tracked(d, (x, max(y + 24, H - 82)), CONTACT, inter(taille, 600), GRIS,
            track)


def pied_couverture(c, prop, g):
    """Le pied creme de la couverture, volontairement plus maigre.

    Une couverture est d abord une vignette. Le telephone et le site n y
    servent a rien, ils sont dans la bio et dans la legende, et le bas de
    l ecran est de toute facon recouvert par l interface d Instagram pendant
    la lecture. Il reste le nom, le titre et l adresse, en version courte.
    """
    d = ImageDraw.Draw(c)
    d.rectangle([0, g["photo"][1], W, g["h"]], fill=CREME + (255,))
    pw = _portrait(c, g)

    d = ImageDraw.Draw(c)
    x = MARGE
    dispo = (W - 18 - pw) - 30 - x
    d.text((x, 1478), COURTIER, font=inter(34, 800), fill=NAVY)
    y = 1524
    for ln in wrap(d, TITRE, inter(22, 400), dispo):
        d.text((x, y), ln, font=inter(22, 400), fill=GRIS)
        y += 30

    y = max(y + 22, 1580)
    d.rectangle([x, y, x + 56, y + 5], fill=BLEU + (255,))
    y += 26
    for ln in prop.get("adresse_courte", prop["adresse"]):
        for bout in wrap(d, ln, inter(24, 700), dispo):
            d.text((x, y), bout, font=inter(24, 700), fill=NAVY)
            y += 34


def fabriquer(prop, cle):
    g = FORMATS[cle]
    c = Image.new("RGBA", (W, g["h"]), CREME + (255,))
    entete(c, g)
    bande_photo(c, prop, g, cle)
    bandeau_vendu(c, prop, g, cle)
    if cle == "publication":
        pied_publication(c, prop, g)
    else:
        pied_couverture(c, prop, g)
    return c.convert("RGB")


def main():
    filtre = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    for prop in PROPRIETES:
        if filtre and filtre not in prop["slug"]:
            continue
        dossier = os.path.join(HERE, prop["slug"])
        os.makedirs(dossier, exist_ok=True)
        for cle, g in FORMATS.items():
            chemin = os.path.join(dossier, g["fichier"])
            fabriquer(prop, cle).save(chemin, quality=94, subsampling=0)
            print("%-12s -> %s" % (cle, chemin))


if __name__ == "__main__":
    main()
