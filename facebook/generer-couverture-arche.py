# -*- coding: utf-8 -*-
"""Photo de couverture Facebook, portrait et texte dans la zone mobile.

Sortie 2556 x 946 px, soit trois fois le format d affichage Facebook
(852 x 315). Le triple garde le texte net sur les ecrans Retina.

Zones mortes, mesurees sur deux captures reelles de l application:

  Mobile. Facebook met l image a la hauteur de la bande et rogne les
  cotes: seule la tranche x 567 a 1991 reste visible, 56 pour cent de
  la largeur. La photo de profil pose un disque de rayon 319 centre en
  (1277, 768), qui mange tout le bas du centre.

  Bureau. La photo de profil se pose en bas a gauche, elle couvre
  environ x 50 a 580 et y > 616, c est a dire le bas du bandeau navy.

Toute la composition tient donc dans la tranche mobile, en deux
colonnes de part et d autre du disque: le portrait a gauche, assez
grand pour que le visage se lise, le texte a droite, le logo dans
l angle bas droit. La photo d interieur et le bord gauche du bandeau
ne sont visibles que sur ordinateur, ils ne portent aucune
information.

verifier() controle apres coup que chaque bloc tient dans la tranche
et evite le disque. apercu_mobile() redessine le rognage.

Couleurs: charte RE/MAX DU CARTIER uniquement (voir CHARTE-COULEURS.md).
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

MOBILE = (567, 1991)                         # tranche visible sur telephone
DISQUE = (1277, 768, 319)                    # photo de profil, mobile
MARGE = 24                                   # garde autour des zones mortes

BANDE = 1210                                 # largeur du bandeau navy
TETE_X = 840                                 # axe du visage
CX = 1660                                    # axe de la colonne de texte

boites = []                                  # tout ce qui doit rester visible


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


def centre(draw, y, s, font, fill, track=0, cx=CX, anchor="mt", nom=""):
    """Ecrit la chaine centree sur cx, interlettrage optionnel.

    y est lu selon anchor: mt pour le haut de la boite, ms pour la
    ligne de base. La boite tracee est ajoutee a la liste de controle.
    """
    lg = largeur(draw, s, font, track)
    mt, ds = font.getmetrics()
    haut = y if anchor[1] == "t" else y - mt
    boites.append((nom or s[:18], cx - lg / 2, haut, cx + lg / 2, haut + mt + ds))
    if not track:
        draw.text((cx, y), s, font=font, fill=fill, anchor=anchor)
        return
    # lettre a lettre, toujours cale sur la ligne de base: un ancrage
    # par le haut ferait descendre les capitales accentuees, le É
    # debordant du jambage superieur
    base = y + mt if anchor[1] == "t" else y
    x = cx - lg / 2
    for c in s:
        draw.text((x, base), c, font=font, fill=fill, anchor="ls")
        x += draw.textlength(c, font=font) + track


# ---------------------------------------------------------------- bandeau
def bandeau(canvas):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(lay).rectangle([0, 0, BANDE, H], fill=NAVY + (255,))
    canvas.alpha_composite(lay)


# ---------------------------------------------------------------- portrait
def portrait(canvas):
    """Portrait detoure, cale pour que le visage tombe dans la tranche
    mobile, a gauche du disque de la photo de profil."""
    im = Image.open(os.path.join(ASSETS, "georges-matar-3.png")).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    w = 912
    h = int(im.height * w / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    x0, y0 = TETE_X - w // 2, H - h

    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.paste((0, 4, 18, 150), (x0 + 18, y0 + 16), im)
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
    canvas.alpha_composite(im, (x0, y0))

    # le visage occupe le quart haut du detourage, c est lui qui doit
    # rester visible sur telephone
    boites.append(("visage", TETE_X - w * 0.19, y0 + h * 0.03,
                   TETE_X + w * 0.19, y0 + h * 0.30))


# ---------------------------------------------------------------- interieur
def interieur(canvas):
    """Photo d interieur a droite, fondue dans le creme vers la gauche.

    Hors tranche mobile: decor pour l affichage sur ordinateur.
    """
    x0 = 2010
    pw, ph = W - x0, H
    im = Image.open(os.path.join(SOURCES, "interieur-salon.jpg")).convert("RGB")
    e = max(pw / im.width, ph / im.height)
    im = im.resize((int(im.width * e) + 1, int(im.height * e) + 1), Image.LANCZOS)
    gx = int((im.width - pw) * 0.35)
    im = im.crop((gx, (im.height - ph) // 2, gx + pw, (im.height - ph) // 2 + ph))

    im = im.convert("RGBA")
    im.alpha_composite(Image.new("RGBA", (pw, ph), CREME + (46,)))

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
    x, y = int(xy[0] - w / 2), int(xy[1])
    canvas.alpha_composite(im, (x, y))
    boites.append(("logo", x, y, x + w, y + hauteur))


# ---------------------------------------------------------------- montage
def couverture():
    del boites[:]
    c = Image.new("RGBA", (W, H), CREME + (255,))
    interieur(c)
    bandeau(c)
    portrait(c)
    d = ImageDraw.Draw(c)

    centre(d, 56, NOM, playfair(92, 500), NAVY + (255,), track=6)
    centre(d, 176, PRENOM_NOM, playfair(78, 450), NAVY + (255,), track=20)

    # pas de filets de part et d autre: la ligne de titre occupe deja
    # toute la largeur disponible dans la tranche mobile
    centre(d, 296, TITRE, inter(29, 450), NAVY_DOUX + (255,), track=4)

    centre(d, 350, TEL, inter(34, 400), NAVY + (255,))
    centre(d, 400, COURRIEL, inter(27, 400), NAVY + (235,))

    logo(c, 150, (1782, 648))
    return c


# ---------------------------------------------------------------- controles
def verifier():
    """Chaque bloc doit tenir dans la tranche mobile et eviter le disque."""
    x0, x1 = MOBILE
    cx, cy, r = DISQUE
    ok = True
    for nom, a, b, e, f in boites:
        if a < x0 + MARGE or e > x1 - MARGE:
            print(f"   HORS TRANCHE  {nom}: x {a:.0f} a {e:.0f}")
            ok = False
        # point de la boite le plus proche du centre du disque
        px = min(max(cx, a), e)
        py = min(max(cy, b), f)
        if ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5 < r + MARGE:
            print(f"   SOUS LE DISQUE  {nom}: x {a:.0f} a {e:.0f}, "
                  f"y {b:.0f} a {f:.0f}")
            ok = False
    print("   zones mobiles: OK" if ok else "   zones mobiles: a corriger")
    return ok


def apercu_mobile(im, chemin):
    """Rejoue le rognage de Facebook sur telephone, disque en rouge."""
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
    verifier()
    print("OK", W, "x", H)
