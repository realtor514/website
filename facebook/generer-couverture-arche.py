# -*- coding: utf-8 -*-
"""Photo de couverture Facebook, mise en page arche.

Sortie 2556 x 946 px, soit trois fois le format d affichage Facebook
(852 x 315). Le triple garde le texte net sur les ecrans Retina.

Composition, de gauche a droite:
  - bandeau navy a fond perdu, une arche tracee a l interieur,
    le portrait detoure devant, qui deborde sur le creme
  - colonne de texte centree: prenom calligraphie, nom en lettres
    espacees, titre, coordonnees, logo de l agence
  - photo d interieur a droite, fondue dans le creme par un degrade

Zones a respecter:
  - la photo de profil Facebook se pose en bas a gauche, elle couvre
    environ x < 600 et y > 540: rien d important dessous
  - le telephone recadre les cotes: le bloc de texte reste entre
    x = 700 et x = 1900

Couleurs: charte RE/MAX DU CARTIER uniquement (voir CHARTE-COULEURS.md).
Le filet dore du modele de depart est remplace par un creme et un navy
dilue, l or ne figure pas dans la charte.
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
CREME_FILET = (247, 245, 238, 150)

NOM = "Georges"
PRENOM_NOM = "MATAR"
TITRE = "COURTIER IMMOBILIER RÉSIDENTIEL"
TEL = "(438) 372-0102"
COURRIEL = "georges.matar@remax-quebec.com"

CX = 1300                                    # axe de la colonne de texte


# ---------------------------------------------------------------- polices
def allura(size):
    return ImageFont.truetype(os.path.join(FONTS, "Allura.ttf"), size)


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
    ligne de base, ce qui est le seul reglage fiable quand les
    jambages d une calligraphie debordent.
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
BANDE = 660                                  # largeur du bandeau navy


def bandeau(canvas):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(lay).rectangle([0, 0, BANDE, H], fill=NAVY + (255,))
    canvas.alpha_composite(lay)


def arche(canvas):
    """Arche a l interieur du bandeau, un filet creme tres fin."""
    ss = 3
    x0, x1, haut = 96, 566, 74
    lay = Image.new("RGBA", (W * ss, H * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    r = (x1 - x0) / 2
    d.arc([x0 * ss, haut * ss, x1 * ss, (haut + 2 * r) * ss], 180, 360,
          fill=CREME_FILET, width=4 * ss)
    for x in (x0, x1):
        d.line([(x * ss, (haut + r) * ss), (x * ss, H * ss)],
               fill=CREME_FILET, width=4 * ss)
    canvas.alpha_composite(lay.resize((W, H), Image.LANCZOS))


# ---------------------------------------------------------------- portrait
def portrait(canvas):
    im = Image.open(os.path.join(ASSETS, "georges-matar-3.png")).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    h = 806
    w = int(im.width * h / im.height)
    im = im.resize((w, h), Image.LANCZOS)
    x0, y0 = 326 - w // 2, H - h

    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.paste((0, 4, 18, 150), (x0 + 18, y0 + 16), im)
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
    canvas.alpha_composite(im, (x0, y0))


# ---------------------------------------------------------------- interieur
def interieur(canvas):
    """Photo d interieur a droite, fondue dans le creme vers la gauche."""
    x0 = 1636
    pw, ph = W - x0, H
    im = Image.open(os.path.join(SOURCES, "interieur-salon.jpg")).convert("RGB")
    e = max(pw / im.width, ph / im.height)
    im = im.resize((int(im.width * e) + 1, int(im.height * e) + 1), Image.LANCZOS)
    gx = int((im.width - pw) * 0.35)
    im = im.crop((gx, (im.height - ph) // 2, gx + pw, (im.height - ph) // 2 + ph))

    # voile creme, pour que la photo reste en retrait du texte
    voile = Image.new("RGBA", (pw, ph), CREME + (46,))
    im = im.convert("RGBA")
    im.alpha_composite(voile)

    # degrade d entree: invisible a gauche, pleine opacite a droite
    fondu = 420
    m = Image.new("L", (pw, 1), 255)
    mp = m.load()
    for x in range(fondu):
        t = x / fondu
        mp[x, 0] = int(255 * (t * t * (3 - 2 * t)))
    im.putalpha(m.resize((pw, ph)))

    canvas.alpha_composite(im, (x0, 0))


# ---------------------------------------------------------------- logo
def logo(canvas, hauteur, y):
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
    canvas.alpha_composite(im, (CX - w // 2, y))


# ---------------------------------------------------------------- montage
def couverture():
    c = Image.new("RGBA", (W, H), CREME + (255,))
    interieur(c)
    bandeau(c)
    arche(c)
    portrait(c)
    d = ImageDraw.Draw(c)

    centre(d, 216, NOM, allura(296), NAVY + (255,), anchor="ms")
    centre(d, 334, PRENOM_NOM, playfair(60, 450), NAVY + (255,), track=24)

    # filets de part et d autre du titre
    ft = inter(25, 500)
    y = 452
    lt = largeur(d, TITRE, ft, 7)
    centre(d, y, TITRE, ft, NAVY_DOUX + (255,), track=7)
    for s in (-1, 1):
        x = CX + s * (lt / 2 + 32)
        d.line([(x, y + 15), (x + s * 60, y + 15)], fill=NAVY_DOUX + (150,),
               width=2)

    centre(d, 522, TEL, inter(78, 300), NAVY + (255,))
    centre(d, 644, COURRIEL, inter(34, 400), NAVY + (235,))

    logo(c, 150, 732)
    return c


if __name__ == "__main__":
    im = couverture()
    png = os.path.join(HERE, "couverture-facebook-arche.png")
    jpg = os.path.join(HERE, "couverture-facebook-arche.jpg")
    im.convert("RGB").save(png, optimize=True)
    im.convert("RGB").save(jpg, quality=94, subsampling=0, optimize=True)
    for p in (png, jpg):
        print("  ", os.path.basename(p), f"{os.path.getsize(p)/1024:.0f} Ko")
    print("OK", W, "x", H)
