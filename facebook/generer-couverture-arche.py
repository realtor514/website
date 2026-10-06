# -*- coding: utf-8 -*-
"""Photo de couverture Facebook, bandeau navy et colonne de texte.

Sortie 2556 x 946 px, soit trois fois le format d affichage Facebook
(852 x 315). Le triple garde le texte net sur les ecrans Retina.

Composition, de gauche a droite:
  - bandeau navy a fond perdu, le portrait detoure devant,
    qui deborde sur le creme
  - colonne de texte: nom sur deux lignes, titre, coordonnees
  - photo d interieur a droite, fondue dans le creme par un degrade
  - logo de l agence en bas a droite

Zones mortes, mesurees sur une capture reelle de l application:

  Mobile. Facebook met l image a la hauteur de la bande et rogne les
  cotes: seule la tranche x 555 a 2025 reste visible, 57 pour cent de
  la largeur. La photo de profil pose un disque de rayon 329 centre en
  (1287, 791), donc tout le bas du centre disparait. Le texte vit en
  consequence au dessus de y = 455, et le logo passe a droite du
  disque, apres x = 1650.

  Bureau. La photo de profil se pose en bas a gauche, elle couvre
  environ x 50 a 580 et y > 616, c est a dire le bas du bandeau navy.

La fonction apercu_mobile() redessine ces deux contraintes par dessus
l image, pour verifier d un coup d oeil apres chaque retouche.

Couleurs: charte RE/MAX DU CARTIER uniquement (voir CHARTE-COULEURS.md).
Le dore du modele de depart est remplace par du navy dilue, l or ne
figure pas dans la charte.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(ROOT, "static", "images")
FONTS = os.path.join(ROOT, "carrousel-instagram", "fonts")
LOGOS = os.path.join(ROOT, "marketing tools by Daniella et Yassine", "logos")
SOURCES = os.path.join(HERE, "sources")

W, H = 2556, 946

NAVY = (0, 14, 53)
CREME = (247, 245, 238)
NAVY_DOUX = (108, 120, 148)

NOM = "Georges"
PRENOM_NOM = "MATAR"
TITRE = "COURTIER IMMOBILIER RÉSIDENTIEL"
TEL = "(438) 372-0102"
COURRIEL = "georges.matar@remax-quebec.com"

CX = 1290                                    # axe de la colonne de texte

MOBILE = (555, 2025)                         # tranche visible sur telephone
DISQUE = (1287, 791, 329)                    # photo de profil, mobile
PLANCHER = 455                               # rien d essentiel plus bas au centre


# ---------------------------------------------------------------- polices
def playfair(size, weight=500):
    f = ImageFont.truetype(os.path.join(FONTS, "Playfair.ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def inter(size, weight=400):
    f = ImageFont.truetype(os.path.join(FONTS, "Inter.ttf"), size)
    f.set_variation_by_axes([min(32, max(14, size)), weight])
    return f


def largeur(draw, s, font, track=0):
    w = sum(draw.textlength(c, font=font) for c in s)
    return w + track * (len(s) - 1) if track else draw.textlength(s, font=font)


def centre(draw, y, s, font, fill, track=0, cx=CX, anchor="mt"):
    """Ecrit la chaine centree sur cx, interlettrage optionnel.

    y est lu selon anchor: mt pour le haut de la boite, ms pour la
    ligne de base.
    """
    if not track:
        draw.text((cx, y), s, font=font, fill=fill, anchor=anchor)
        return
    # lettre a lettre, toujours cale sur la ligne de base: un ancrage
    # par le haut ferait descendre les capitales accentuees, le É
    # debordant du jambage superieur
    base = y + font.getmetrics()[0] if anchor[1] == "t" else y
    x = cx - largeur(draw, s, font, track) / 2
    for c in s:
        draw.text((x, base), c, font=font, fill=fill, anchor="ls")
        x += draw.textlength(c, font=font) + track


# ---------------------------------------------------------------- bandeau
BANDE = 706                                  # largeur du bandeau navy


def bandeau(canvas):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(lay).rectangle([0, 0, BANDE, H], fill=NAVY + (255,))
    canvas.alpha_composite(lay)


# ---------------------------------------------------------------- portrait
def portrait(canvas):
    im = Image.open(os.path.join(ASSETS, "georges-matar-3.png")).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    h = 874
    w = int(im.width * h / im.height)
    im = im.resize((w, h), Image.LANCZOS)
    x0, y0 = 350 - w // 2, H - h

    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.paste((0, 4, 18, 150), (x0 + 18, y0 + 16), im)
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
    canvas.alpha_composite(im, (x0, y0))


# ---------------------------------------------------------------- interieur
def interieur(canvas):
    """Photo d interieur a droite, fondue dans le creme vers la gauche."""
    x0 = 2010
    pw, ph = W - x0, H
    im = Image.open(os.path.join(SOURCES, "interieur-salon.jpg")).convert("RGB")
    e = max(pw / im.width, ph / im.height)
    im = im.resize((int(im.width * e) + 1, int(im.height * e) + 1), Image.LANCZOS)
    gx = int((im.width - pw) * 0.35)
    im = im.crop((gx, (im.height - ph) // 2, gx + pw, (im.height - ph) // 2 + ph))

    # voile creme, pour que la photo reste en retrait du texte
    im = im.convert("RGBA")
    im.alpha_composite(Image.new("RGBA", (pw, ph), CREME + (46,)))

    # degrade d entree: invisible a gauche, pleine opacite a droite
    fondu = 300
    m = Image.new("L", (pw, 1), 255)
    mp = m.load()
    for x in range(fondu):
        t = x / fondu
        mp[x, 0] = int(255 * (t * t * (3 - 2 * t)))
    im.putalpha(m.resize((pw, ph)))

    canvas.alpha_composite(im, (x0, 0))


# ---------------------------------------------------------------- logo
def logo(canvas, hauteur, xy):
    im = Image.open(os.path.join(LOGOS, "logo-ducartier-noir2.png")).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    w = int(im.width * hauteur / im.height)
    im = im.resize((w, hauteur), Image.LANCZOS)

    # le texte noir passe en navy, le ballon garde ses couleurs
    px = im.load()
    for j in range(im.height):
        for i in range(im.width):
            r, g, b, a = px[i, j]
            if a and max(r, g, b) < 110 and max(r, g, b) - min(r, g, b) < 42:
                px[i, j] = NAVY + (a,)
    canvas.alpha_composite(im, (int(xy[0] - w / 2), int(xy[1])))


# ---------------------------------------------------------------- montage
def couverture():
    c = Image.new("RGBA", (W, H), CREME + (255,))
    interieur(c)
    bandeau(c)
    portrait(c)
    d = ImageDraw.Draw(c)

    centre(d, 78, NOM, playfair(116, 500), NAVY + (255,), track=8)
    centre(d, 218, PRENOM_NOM, playfair(96, 450), NAVY + (255,), track=26)

    # filets de part et d autre du titre
    ft = inter(40, 450)
    y = 334
    lt = largeur(d, TITRE, ft, 7)
    centre(d, y, TITRE, ft, NAVY_DOUX + (255,), track=7)
    for s in (-1, 1):
        x = CX + s * (lt / 2 + 36)
        d.line([(x, y + 27), (x + s * 64, y + 27)], fill=NAVY_DOUX + (150,),
               width=2)

    # telephone et courriel sur une seule ligne, pour tenir au dessus
    # du disque de la photo de profil
    fc = inter(34, 400)
    ligne = TEL + "    ·    " + COURRIEL
    centre(d, 396, ligne, fc, NAVY + (245,))

    # logo a droite du disque, seul endroit du bas visible sur telephone
    logo(c, 158, (1776, 686))
    return c


def apercu_mobile(im, chemin):
    """Rejoue le rognage de Facebook sur telephone, zones mortes en rouge."""
    x0, x1 = MOBILE
    vue = im.convert("RGBA").crop((x0, 0, x1, H))
    cx, cy, r = DISQUE
    masque = Image.new("RGBA", vue.size, (0, 0, 0, 0))
    ImageDraw.Draw(masque).ellipse([cx - r - x0, cy - r, cx + r - x0, cy + r],
                                   fill=(255, 18, 0, 150))
    vue.alpha_composite(masque)
    vue.convert("RGB").save(chemin, quality=92)


if __name__ == "__main__":
    im = couverture()
    png = os.path.join(HERE, "couverture-facebook-arche.png")
    jpg = os.path.join(HERE, "couverture-facebook-arche.jpg")
    im.convert("RGB").save(png, optimize=True)
    im.convert("RGB").save(jpg, quality=94, subsampling=0, optimize=True)
    apercu_mobile(im, os.path.join(HERE, "apercu-mobile.jpg"))
    for p in (png, jpg):
        print("  ", os.path.basename(p), f"{os.path.getsize(p)/1024:.0f} Ko")
    print("OK", W, "x", H)
