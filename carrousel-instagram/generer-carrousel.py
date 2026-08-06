# -*- coding: utf-8 -*-
"""Carrousel Instagram 1080x1350 pour l inscription 28 rue St-Hilaire.

Genere 8 slides JPG numerotes dans l ordre de publication.
Couleurs echantillonnees directement dans le logo RE/MAX DU CARTIER.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SLUG = "28-rue-st-hilaire-longueuil"

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PHOTOS = os.path.join(ROOT, "static", "images", "listings", SLUG)
ASSETS = os.path.join(ROOT, "static", "images")
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, SLUG)
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350
M = 72                                  # marge laterale

RED = (230, 20, 5)
RED_PURE = (255, 18, 0)
BLUE = (0, 55, 214)
NAVY = (0, 14, 53)
INK = (22, 27, 43)
GREY = (112, 120, 136)
LINE = (227, 231, 238)
WHITE = (255, 255, 255)
CREAM = (250, 249, 247)


# ---------------------------------------------------------------- polices
def playfair(size, weight=700):
    f = ImageFont.truetype(os.path.join(FONTS, "Playfair.ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def inter(size, weight=400, opsz=None):
    f = ImageFont.truetype(os.path.join(FONTS, "Inter.ttf"), size)
    f.set_variation_by_axes([opsz if opsz else min(32, max(14, size)), weight])
    return f


# ---------------------------------------------------------------- texte
def tw(draw, s, font, track=0):
    if not track:
        return draw.textlength(s, font=font)
    return sum(draw.textlength(c, font=font) for c in s) + track * (len(s) - 1)


def tracked(draw, xy, s, font, fill, track=4, align="l"):
    x, y = xy
    if align == "c":
        x -= tw(draw, s, font, track) / 2
    elif align == "r":
        x -= tw(draw, s, font, track)
    for c in s:
        draw.text((x, y), c, font=font, fill=fill)
        x += draw.textlength(c, font=font) + track


def wrap(draw, s, font, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, s, font, fill, maxw, leading, align="l"):
    x, y = xy
    for ln in wrap(draw, s, font, maxw):
        draw.text((x, y), ln, font=font, fill=fill,
                  anchor={"l": "la", "c": "ma", "r": "ra"}[align])
        y += leading
    return y


# ---------------------------------------------------------------- images
def cover(path, w, h, fy=0.5):
    """Recadre en remplissant la boite. fy = centre d interet vertical."""
    im = Image.open(path).convert("RGB")
    r = max(w / im.width, h / im.height)
    im = im.resize((max(w, int(im.width * r + .5)), max(h, int(im.height * r + .5))),
                   Image.LANCZOS)
    x = (im.width - w) // 2
    y = int(round((im.height - h) * min(1.0, max(0.0, fy))))
    return im.crop((x, y, x + w, y + h))


def round_mask(w, h, r):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], r, fill=255)
    return m


def shadow(canvas, box, r, blur=26, alpha=42, dy=12):
    x0, y0, x1, y1 = box
    lay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).rounded_rectangle([x0, y0 + dy, x1, y1 + dy], r,
                                          fill=(0, 14, 53, alpha))
    canvas.alpha_composite(lay.filter(ImageFilter.GaussianBlur(blur)))


def photo(canvas, name, box, r=22, shad=True, fy=0.5):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    if shad and r:
        shadow(canvas, box, r)
    im = cover(os.path.join(PHOTOS, name), w, h, fy).convert("RGBA")
    if r:
        im.putalpha(round_mask(w, h, r))
    canvas.alpha_composite(im, (x0, y0))


def gradient(canvas, y0, y1, alpha=225, top=False):
    """Voile sombre pour rendre le texte lisible sur photo."""
    g = Image.new("L", (1, y1 - y0))
    px = g.load()
    n = y1 - y0
    for i in range(n):
        t = i / max(1, n - 1)
        px[0, i] = int(alpha * (1 - t) if top else alpha * t)
    g = g.resize((canvas.width, n))
    lay = Image.new("RGBA", (canvas.width, n), NAVY + (0,))
    lay.putalpha(g)
    canvas.alpha_composite(lay, (0, y0))


def _logo_img(white):
    src = "remax-ducartier-blanc.png" if white else "remax-logo.png"
    im = Image.open(os.path.join(ASSETS, src)).convert("RGBA")
    return im.crop(im.getchannel("A").getbbox())


def logo_w(box_h, white=False):
    im = _logo_img(white)
    return int(im.width * box_h / im.height)


def logo(canvas, box_h, xy, white=False):
    im = _logo_img(white)
    w = int(im.width * box_h / im.height)
    canvas.alpha_composite(im.resize((w, box_h), Image.LANCZOS),
                           (int(xy[0]), int(xy[1])))
    return w


# ---------------------------------------------------------------- icones
ICONS = {
    "bed": [("l", 2, 5, 2, 20), ("l", 2, 9, 19, 9), ("l", 19, 9, 22, 12),
            ("l", 22, 12, 22, 20), ("l", 2, 16, 22, 16), ("c", 7, 12.5, 2.1)],
    "bath": [("l", 2, 12, 22, 12), ("a", 3, 5, 21, 21, 0, 180),
             ("l", 6.5, 19.5, 5, 22), ("l", 17.5, 19.5, 19, 22),
             ("l", 7, 12, 7, 6), ("a", 5, 3, 11, 8, 180, 300)],
    "car": [("r", 2, 11, 22, 17, 3), ("p", [(5, 11), (7.5, 5.5), (16.5, 5.5), (19, 11)]),
            ("c", 6.5, 17.5, 1.9), ("c", 17.5, 17.5, 1.9)],
    "land": [("p", [(3, 8), (3, 3), (8, 3)]), ("p", [(16, 3), (21, 3), (21, 8)]),
             ("p", [(21, 16), (21, 21), (16, 21)]), ("p", [(8, 21), (3, 21), (3, 16)]),
             ("l", 8, 12, 16, 12)],
    "cal": [("r", 3, 5, 21, 21, 3), ("l", 3, 10.5, 21, 10.5),
            ("l", 8, 2.5, 8, 7), ("l", 16, 2.5, 16, 7), ("c", 8.5, 15.5, 1.2)],
    "area": [("r", 3, 3, 21, 21, 2), ("l", 3, 3, 21, 21),
             ("p", [(3, 8), (3, 3), (8, 3)]), ("p", [(21, 16), (21, 21), (16, 21)])],
    "check": [("p", [(4.5, 12.5), (10, 18), (19.5, 5.5)])],
    "pin": [("a", 4, 2, 20, 18, 180, 360), ("p", [(4, 10), (12, 21.5), (20, 10)]),
            ("c", 12, 9.8, 3.1)],
    "bag": [("r", 4, 7, 20, 21, 3), ("a", 8, 2.5, 16, 11, 180, 360)],
    "tree": [("c", 12, 8.5, 6), ("l", 12, 14.5, 12, 22),
             ("l", 12, 18, 8, 14.5), ("l", 12, 18, 16, 14.5)],
    "train": [("r", 5, 2.5, 19, 17, 4), ("l", 5, 11, 19, 11),
              ("c", 8.8, 14, 1.2), ("c", 15.2, 14, 1.2),
              ("l", 8, 17, 5, 22), ("l", 16, 17, 19, 22)],
    "phone": [("r", 7, 2, 17, 22, 3), ("l", 10.5, 19, 13.5, 19)],
    "mail": [("r", 2, 5, 22, 19, 2), ("p", [(2.5, 6), (12, 14), (21.5, 6)])],
    "globe": [("c", 12, 12, 9.6), ("l", 2.4, 12, 21.6, 12),
              ("a", 7, 2.4, 17, 21.6, 0, 360)],
}


def icon(canvas, name, xy, size, color, sw=None):
    k = size / 24.0
    sw = sw or max(2, int(round(size / 12.0)))
    ss = 4                                    # supersampling
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
            for p in op[1]:
                x, y = P(*p)
                d.ellipse([x - S / 2, y - S / 2, x + S / 2, y + S / 2], fill=color)
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


# ---------------------------------------------------------------- blocs
def base(bg=WHITE):
    return Image.new("RGBA", (W, H), bg + (255,))


def badge(canvas, xy, text, fill, fg=WHITE, pad=(26, 14), size=26, track=3):
    d = ImageDraw.Draw(canvas)
    f = inter(size, 800)
    w = tw(d, text, f, track) + pad[0] * 2
    h = size + pad[1] * 2
    x, y = xy
    d.rounded_rectangle([x, y, x + w, y + h], h / 2, fill=fill + (255,))
    tracked(d, (x + pad[0], y + pad[1] - size * 0.12), text, f, fg, track)
    return w, h


def eyebrow(canvas, xy, text, color=BLUE, align="l", size=23, track=5):
    tracked(ImageDraw.Draw(canvas), xy, text, inter(size, 800), color, track,
            align)


def signature(canvas, y, dark=False):
    """Signature obligatoire: logo, nom, titre et nom de l agence."""
    d = ImageDraw.Draw(canvas)
    fg = WHITE if dark else NAVY
    sub = (255, 255, 255, 185) if dark else GREY
    acc = (255, 140, 125) if dark else RED
    lw = logo(canvas, 88, (M, y), white=dark)
    x = M + lw + 26
    d.text((x, y + 2), "GEORGES MATAR", font=inter(29, 800), fill=fg)
    d.text((x, y + 37), "Courtier immobilier résidentiel", font=inter(22, 400),
           fill=sub)
    d.text((x, y + 65), "RE/MAX DU CARTIER INC.", font=inter(22, 700), fill=acc)
    return y + 88


def save(canvas, name):
    p = os.path.join(OUT, name)
    canvas.convert("RGB").save(p, quality=92, subsampling=0, optimize=True)
    print("  ", name)


# ================================================================ SLIDE 1
def slide1():
    c = base()
    photo(c, "03.jpg", (0, 0, W, H), r=0, shad=False)
    gradient(c, 0, 360, 155, top=True)
    gradient(c, 600, H, 252)
    d = ImageDraw.Draw(c)

    badge(c, (M, 64), "À VENDRE", RED)
    tracked(d, (W - M, 78), "CENTRIS 26368231", inter(23, 700),
            (255, 255, 255, 220), 4, "r")

    y = 820
    eyebrow(c, (M, y), "NOUVELLE INSCRIPTION", (255, 138, 124))
    y += 52
    d.text((M, y), "28, rue St-Hilaire", font=playfair(84, 700), fill=WHITE)
    y += 106
    d.text((M, y), "Vieux-Longueuil", font=inter(38, 400),
           fill=(255, 255, 255, 205))
    y += 62
    d.line([M, y + 10, M + 5, y + 68], fill=RED_PURE + (255,), width=6)
    d.text((M + 26, y), "499 000 $", font=playfair(64, 800), fill=WHITE)

    d.line([M, 1152, W - M, 1152], fill=(255, 255, 255, 70), width=2)
    signature(c, 1186, dark=True)
    return c


# ================================================================ SLIDE 2
def slide2():
    c = base()
    d = ImageDraw.Draw(c)
    eyebrow(c, (M, 92), "LA PROPRIÉTÉ")
    d.text((M, 134), "Découvrez votre", font=playfair(72, 700), fill=NAVY)
    d.text((M, 218), "prochaine maison", font=playfair(72, 700), fill=NAVY)

    photo(c, "06.jpg", (M, 336, W - M, 836))

    items = [("bed", "2", "Chambres"),
             ("bath", "1 + 1", "Salle de bain / salle d'eau"),
             ("car", "2", "Stationnements"),
             ("land", "371 m²", "Terrain (4 000 pi²)"),
             ("area", "25 x 25 pi", "Dimensions du bâtiment"),
             ("cal", "1949", "Année de construction")]
    x0, y0, cw, rh = M, 900, (W - 2 * M) // 2, 96
    for i, (ic, val, lab) in enumerate(items):
        x = x0 + (i % 2) * cw
        y = y0 + (i // 2) * rh
        icon(c, ic, (x, y + 6), 42, RED + (255,))
        d.text((x + 58, y), val, font=inter(31, 800), fill=NAVY)
        d.text((x + 58, y + 38), lab, font=inter(24, 400), fill=GREY)

    d.rounded_rectangle([M, 1194, W - M, 1310], 20, fill=RED + (255,))
    tracked(d, (M + 34, 1222), "PRIX DEMANDÉ", inter(23, 800),
            (255, 210, 205), 5)
    d.text((W - M - 34, 1216), "499 000 $", font=playfair(58, 800), fill=WHITE,
           anchor="ra")
    return c


# ================================================================ SLIDE 3
def slide3():
    c = base()
    photo(c, "09.jpg", (0, 0, W, 640), r=0, shad=False)
    d = ImageDraw.Draw(c)

    y = 696
    eyebrow(c, (M, y), "LA CUISINE")
    y += 46
    d.text((M, y), "Une cuisine pensée", font=playfair(66, 700), fill=NAVY)
    d.text((M, y + 78), "pour recevoir", font=playfair(66, 700), fill=NAVY)
    y += 192

    for t in ["Îlot central avec rangement",
              "Armoires blanches pleine hauteur",
              "Électroménagers en acier inoxydable",
              "Grandes fenêtres sur la cour arrière"]:
        icon(c, "check", (M, y + 2), 34, RED + (255,))
        d.text((M + 52, y), t, font=inter(30, 500), fill=INK)
        y += 62

    signature(c, 1196)
    return c


# ================================================================ SLIDE 4
def slide4():
    c = base()
    photo(c, "25.jpg", (0, 0, W, 600), r=0, shad=False, fy=0.28)
    d = ImageDraw.Draw(c)

    y = 656
    eyebrow(c, (M, y), "CE QUI A DÉJÀ ÉTÉ FAIT")
    y += 46
    d.text((M, y), "Les points forts", font=playfair(70, 700), fill=NAVY)
    y += 130

    items = ["Toiture refaite en 2014", "Plomberie et électricité 2014",
             "Plancher sablé en 2026", "Piscine hors terre 2023",
             "Terrasse en bois et cabanon", "Borne de recharge électrique"]
    cw, rh = (W - 2 * M) // 2, 108
    for i, t in enumerate(items):
        x = M + (i % 2) * cw
        yy = y + (i // 2) * rh
        icon(c, "check", (x, yy + 2), 32, RED + (255,))
        para(d, (x + 46, yy), t, inter(27, 500), INK, cw - 70, 36)

    signature(c, 1196)
    return c


# ================================================================ SLIDE 5
def slide5():
    c = base()
    d = ImageDraw.Draw(c)
    eyebrow(c, (M, 92), "VISITE INTÉRIEURE")
    d.text((M, 134), "Chaque détail compte", font=playfair(70, 700), fill=NAVY)

    photo(c, "12.jpg", (M, 268, W - M, 700))
    d.text((M, 716), "Chambre principale", font=inter(25, 700), fill=NAVY)

    gap = 28
    hw = (W - 2 * M - gap) // 2
    photo(c, "22.jpg", (M, 782, M + hw, 1118))
    photo(c, "24.jpg", (M + hw + gap, 782, W - M, 1118), fy=0.62)
    d.text((M, 1134), "Salle de bain", font=inter(25, 700), fill=NAVY)
    d.text((M + hw + gap, 1134), "Terrasse", font=inter(25, 700), fill=NAVY)

    signature(c, 1196)
    return c


# ================================================================ SLIDE 6
def slide6():
    c = base()
    photo(c, "04.jpg", (0, 0, W, 620), r=0, shad=False)
    d = ImageDraw.Draw(c)

    y = 680
    eyebrow(c, (M, y), "LE VIEUX-LONGUEUIL")
    y += 46
    d.text((M, y), "Un emplacement", font=playfair(66, 700), fill=NAVY)
    d.text((M, y + 78), "exceptionnel", font=playfair(66, 700), fill=NAVY)
    y += 194

    for ic, t in [("pin", "Écoles primaires et secondaires du secteur"),
                  ("bag", "Commerces de la rue Saint-Charles"),
                  ("tree", "Parcs et pistes cyclables"),
                  ("train", "Métro Longueuil et pont Jacques-Cartier")]:
        icon(c, ic, (M, y - 2), 40, BLUE + (255,))
        para(d, (M + 60, y), t, inter(29, 500), INK, W - 2 * M - 60, 36)
        y += 66

    signature(c, 1196)
    return c


# ================================================================ SLIDE 7
def slide7():
    c = base()
    photo(c, "07.jpg", (0, 0, W, H), r=0, shad=False, fy=0.45)
    gradient(c, 0, 300, 130, top=True)
    gradient(c, 700, H, 245)
    d = ImageDraw.Draw(c)

    d.line([W // 2 - 46, 820, W // 2 + 46, 820], fill=RED_PURE + (255,), width=5)
    d.text((W // 2, 876), "Imaginez-vous", font=playfair(80, 700), fill=WHITE,
           anchor="ma")
    d.text((W // 2, 972), "vivre ici.", font=playfair(80, 700), fill=WHITE,
           anchor="ma")
    tracked(d, (W // 2, 1094), "28, RUE ST-HILAIRE   ·   499 000 $",
            inter(25, 700), (255, 255, 255, 215), 4, "c")

    # logo place dans le degrade sombre du bas, sinon il disparait au plafond
    logo(c, 132, ((W - logo_w(132, True)) / 2, 1160), white=True)
    return c


# ================================================================ SLIDE 8
def slide8():
    c = base(CREAM)
    d = ImageDraw.Draw(c)

    d.rectangle([0, 0, W, 10], fill=RED + (255,))

    # portrait rond
    ph = Image.open(os.path.join(ASSETS, "georges-matar.png")).convert("RGB")
    s = 300
    r = max(s / ph.width, s / ph.height)
    ph = ph.resize((int(ph.width * r + .5), int(ph.height * r + .5)), Image.LANCZOS)
    ph = ph.crop(((ph.width - s) // 2, 0, (ph.width - s) // 2 + s, s)).convert("RGBA")
    m = Image.new("L", (s, s), 0)
    ImageDraw.Draw(m).ellipse([0, 0, s - 1, s - 1], fill=255)
    ph.putalpha(m)
    px = (W - s) // 2
    shadow(c, (px, 96, px + s, 96 + s), s // 2, blur=22, alpha=48)
    c.alpha_composite(ph, (px, 96))

    y = 440
    eyebrow(c, (W // 2, y), "PARLONS-EN", RED, "c")
    y += 46
    d.text((W // 2, y), "Cette propriété", font=playfair(66, 700), fill=NAVY,
           anchor="ma")
    d.text((W // 2, y + 78), "vous intéresse?", font=playfair(66, 700), fill=NAVY,
           anchor="ma")
    y += 216

    rows = [("phone", "(438) 372-0102"),
            ("mail", "georges.matar@remax-quebec.com"),
            ("globe", "georgesmatar.ca")]
    fnt = inter(29, 500)
    for ic, t in rows:
        wtot = 40 + 22 + d.textlength(t, font=fnt)
        x = (W - wtot) // 2
        icon(c, ic, (int(x), y), 40, RED + (255,))
        d.text((x + 62, y + 3), t, font=fnt, fill=INK)
        y += 66

    y += 18
    bh = 104
    d.rounded_rectangle([M, y, W - M, y + bh], bh / 2, fill=RED + (255,))
    d.text((W // 2, y + bh / 2 - 16), "Planifiez votre visite",
           font=inter(33, 800), fill=WHITE, anchor="mm")
    tracked(d, (W // 2, y + bh / 2 + 6), "DÈS AUJOURD'HUI", inter(21, 700),
            (255, 205, 200), 4, "c")

    y += bh + 46
    d.line([M, y, W - M, y], fill=LINE + (255,), width=2)
    y += 36

    lh = 84
    lw = logo_w(lh, False)
    f1, f2, f3 = inter(29, 800), inter(22, 400), inter(22, 700)
    tmax = max(d.textlength("GEORGES MATAR", font=f1),
               d.textlength("Courtier immobilier résidentiel", font=f2),
               d.textlength("RE/MAX DU CARTIER INC.", font=f3))
    lx = (W - (lw + 26 + tmax)) / 2
    logo(c, lh, (lx, y), white=False)
    tx = lx + lw + 26
    d.text((tx, y + 2), "GEORGES MATAR", font=f1, fill=NAVY)
    d.text((tx, y + 38), "Courtier immobilier résidentiel", font=f2, fill=GREY)
    d.text((tx, y + 66), "RE/MAX DU CARTIER INC.", font=f3, fill=RED)

    tracked(d, (W // 2, 1290), "CENTRIS 26368231", inter(21, 600), GREY, 4, "c")
    return c


# ---------------------------------------------------------------- run
if __name__ == "__main__":
    # nettoie l ancien lot pour eviter les fichiers orphelins
    for f in os.listdir(OUT):
        if f.lower().endswith(".jpg"):
            os.remove(os.path.join(OUT, f))
    print("Carrousel ->", OUT)
    for i, (fn, name) in enumerate([
            (slide1, "01-couverture.jpg"), (slide2, "02-caracteristiques.jpg"),
            (slide3, "03-cuisine.jpg"), (slide4, "04-points-forts.jpg"),
            (slide5, "05-details.jpg"), (slide6, "06-emplacement.jpg"),
            (slide7, "07-coup-de-coeur.jpg"), (slide8, "08-contact.jpg")], 1):
        save(fn(), name)
    print("OK")
