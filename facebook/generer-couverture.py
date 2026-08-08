# -*- coding: utf-8 -*-
"""Photo de couverture Facebook pour la page de Georges Matar.

Sortie 1640 x 624 px, soit le double du format d affichage Facebook
(820 x 312). Le double permet un rendu net sur les ecrans Retina.

Identite visuelle identique au carrousel Instagram: navy RE/MAX,
Playfair Display pour le nom, Inter pour le reste.

Zones a respecter:
  - la photo de profil se pose en bas a gauche: rien d important
    sous y = 520 ni a gauche de x = 400
  - le telephone recadre les cotes: le bloc de texte reste entre
    x = 420 et x = 1100
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(ROOT, "static", "images")
FONTS = os.path.join(ROOT, "carrousel-instagram", "fonts")

W, H = 1640, 624

NAVY = (0, 14, 53)
NAVY_LIGHT = (10, 34, 88)
NAVY_SOFT = (152, 166, 198)
RED = (230, 20, 5)
BLUE = (0, 55, 214)
WHITE = (255, 255, 255)


# ---------------------------------------------------------------- polices
def playfair(size, weight=700):
    f = ImageFont.truetype(os.path.join(FONTS, "Playfair.ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def inter(size, weight=400, opsz=None):
    f = ImageFont.truetype(os.path.join(FONTS, "Inter.ttf"), size)
    f.set_variation_by_axes([opsz if opsz else min(32, max(14, size)), weight])
    return f


def tw(draw, s, font, track=0):
    if not track:
        return draw.textlength(s, font=font)
    return sum(draw.textlength(c, font=font) for c in s) + track * (len(s) - 1)


def tracked(draw, xy, s, font, fill, track=4):
    x, y = xy
    for c in s:
        draw.text((x, y), c, font=font, fill=fill)
        x += draw.textlength(c, font=font) + track


# ---------------------------------------------------------------- fond
def lerp(a, b, t):
    return tuple(int(p + (q - p) * t) for p, q in zip(a, b))


def fond():
    """Degrade diagonal navy, plus une lueur derriere le portrait."""
    small = Image.new("RGB", (82, 32))
    px = small.load()
    for y in range(32):
        for x in range(82):
            t = min(1.0, x / 81 * 0.45 + y / 31 * 0.55)
            px[x, y] = lerp((7, 26, 74), (0, 8, 28), t)
    base = small.resize((W, H), Image.BICUBIC).convert("RGBA")

    # lueur circulaire derriere la tete du portrait
    gw, gh = 128, 64
    m = Image.new("L", (gw, gh), 0)
    mp = m.load()
    cx, cy, rad = gw * 0.79, gh * 0.42, gh * 0.62
    for y in range(gh):
        for x in range(gw):
            d = (((x - cx) / rad) ** 2 + ((y - cy) / rad) ** 2) ** 0.5
            mp[x, y] = int(255 * max(0.0, 1.0 - d) ** 1.6)
    glow = Image.new("RGBA", (W, H), NAVY_LIGHT + (0,))
    glow.putalpha(m.resize((W, H), Image.BICUBIC))
    base.alpha_composite(glow)
    return base


def filigrane(canvas):
    """Ballon RE/MAX en tres basse opacite, coin gauche, coupe par le bord.

    Cette zone est celle que la photo de profil recouvre: aucune
    information ne s y trouve, seulement de la texture.
    """
    im = Image.open(os.path.join(ASSETS, "remax-ducartier-ballon.png")).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    h = 1080
    im = im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
    im.putalpha(im.getchannel("A").point(lambda a: int(a * 0.075)))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lay.alpha_composite(im, (-330, -300))
    canvas.alpha_composite(lay.filter(ImageFilter.GaussianBlur(55)))


# ---------------------------------------------------------------- portrait
def portrait(canvas):
    im = Image.open(os.path.join(ASSETS, "georges-matar-3.png")).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    h = 596
    w = int(im.width * h / im.height)
    im = im.resize((w, h), Image.LANCZOS)
    x0, y0 = W - w + 40, H - h

    # ombre portee douce pour decoller le sujet du fond
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.paste((0, 4, 18, 165), (x0 - 16, y0 + 14), im)
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(26)))
    canvas.alpha_composite(im, (x0, y0))


# ---------------------------------------------------------------- logo
def logo(canvas, box_h, xy):
    im = Image.open(os.path.join(ASSETS, "remax-ducartier-blanc.png")).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    w = int(im.width * box_h / im.height)
    canvas.alpha_composite(im.resize((w, box_h), Image.LANCZOS),
                           (int(xy[0]), int(xy[1])))
    return w


# ---------------------------------------------------------------- icones
ICONS = {
    "phone": [("r", 7, 2, 17, 22, 3), ("l", 10.5, 19, 13.5, 19)],
    "mail": [("r", 2, 5, 22, 19, 2), ("p", [(2.5, 6), (12, 14), (21.5, 6)])],
    "globe": [("c", 12, 12, 9.6), ("l", 2.4, 12, 21.6, 12),
              ("a", 7, 2.4, 17, 21.6, 0, 360)],
}


def icon(canvas, name, xy, size, color, sw=None):
    k = size / 24.0
    sw = sw or max(2, int(round(size / 12.0)))
    ss = 4
    lay = Image.new("RGBA", (size * ss, size * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    S = sw * ss

    def P(x, y):
        return (x * k * ss, y * k * ss)

    for op in ICONS[name]:
        t = op[0]
        if t == "l":
            d.line([P(op[1], op[2]), P(op[3], op[4])], fill=color, width=S,
                   joint="curve")
        elif t == "p":
            d.line([P(*p) for p in op[1]], fill=color, width=S, joint="curve")
        elif t == "r":
            d.rounded_rectangle([P(op[1], op[2]), P(op[3], op[4])],
                                op[5] * k * ss, outline=color, width=S)
        elif t == "c":
            x, y = P(op[1], op[2])
            r = op[3] * k * ss
            d.ellipse([x - r, y - r, x + r, y + r], outline=color, width=S)
        elif t == "a":
            d.arc([P(op[1], op[2]), P(op[3], op[4])], op[5], op[6],
                  fill=color, width=S)
    canvas.alpha_composite(lay.resize((size, size), Image.LANCZOS), xy)


# ---------------------------------------------------------------- montage
def couverture():
    c = fond()
    filigrane(c)
    portrait(c)
    d = ImageDraw.Draw(c)

    X = 452                                   # colonne de texte, zone sure

    # barre d accent rouge, blanc, bleu, alignee sur le bloc de texte
    bx, by, bw = X - 38, 252, 6
    for col, y0, y1 in [(RED, 0, 104), (WHITE, 110, 146), (BLUE, 152, 266)]:
        d.rounded_rectangle([bx, by + y0, bx + bw, by + y1], bw / 2,
                            fill=col + (255,))

    logo(c, 118, (X, 62))

    d.text((X, 236), "Georges Matar", font=playfair(82, 700), fill=WHITE)
    d.text((X, 344), "Courtier immobilier résidentiel",
           font=inter(31, 500), fill=(214, 222, 240, 255))

    # coordonnees: telephone et site sur une ligne, courriel en dessous
    f = inter(28, 600)
    x = X
    for ic, t in [("phone", "(438) 372-0102"), ("globe", "georgesmatar.ca")]:
        icon(c, ic, (int(x), 424), 32, (255, 255, 255, 235), sw=3)
        d.text((x + 44, 425), t, font=f, fill=WHITE)
        x += int(44 + d.textlength(t, font=f) + 50)

    icon(c, "mail", (X, 486), 32, (255, 255, 255, 235), sw=3)
    d.text((X + 44, 487), "georges.matar@remax-quebec.com", font=f, fill=WHITE)

    return c


if __name__ == "__main__":
    im = couverture()
    png = os.path.join(HERE, "couverture-facebook.png")
    jpg = os.path.join(HERE, "couverture-facebook.jpg")
    im.convert("RGB").save(png, optimize=True)
    im.convert("RGB").save(jpg, quality=94, subsampling=0, optimize=True)
    for p in (png, jpg):
        print("  ", os.path.basename(p), f"{os.path.getsize(p)/1024:.0f} Ko")
    print("OK", W, "x", H)
