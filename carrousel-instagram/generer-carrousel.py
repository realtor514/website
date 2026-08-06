# -*- coding: utf-8 -*-
"""Carrousel Instagram 1080x1350 pour l inscription 28 rue St-Hilaire.

Genere 8 slides JPG numerotes dans l ordre de publication.
Couleurs echantillonnees directement dans le logo RE/MAX DU CARTIER.
Inscription en collaboration avec l Equipe Pistoli: les deux courtiers
apparaissent sur la slide de contact.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SLUG = "28-rue-st-hilaire-longueuil"

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PHOTOS = os.path.join(ROOT, "static", "images", "listings", SLUG)
ASSETS = os.path.join(ROOT, "static", "images")
SOURCES = os.path.join(HERE, "sources")
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, SLUG)
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350
M = 72                                  # marge laterale

RED = (230, 20, 5)
RED_PURE = (255, 18, 0)
BLUE = (0, 55, 214)
NAVY = (0, 14, 53)                      # #000e35, navy du one pager RE/MAX
NAVY_SOFT = (152, 166, 198)             # navy eclairci pour les sous-titres
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


def photo(canvas, name, box, r=22, shad=True, fy=0.5, folder=None):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    if shad and r:
        shadow(canvas, box, r)
    im = cover(os.path.join(folder or PHOTOS, name), w, h, fy).convert("RGBA")
    if r:
        im.putalpha(round_mask(w, h, r))
    canvas.alpha_composite(im, (x0, y0))


def circle_photo(canvas, path, xy, size, fy=0.0):
    im = cover(path, size, size, fy).convert("RGBA")
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse([0, 0, size - 1, size - 1], fill=255)
    im.putalpha(m)
    shadow(canvas, (xy[0], xy[1], xy[0] + size, xy[1] + size), size // 2,
           blur=20, alpha=44)
    canvas.alpha_composite(im, xy)


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
    "check": [("p", [(4.5, 12.5), (10, 18), (19.5, 5.5)])],
    "pin": [("a", 4, 2, 20, 18, 180, 360), ("p", [(4, 10), (12, 21.5), (20, 10)]),
            ("c", 12, 9.8, 3.1)],
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


def badge(canvas, xy, text, fill=None, fg=WHITE, outline=None, size=26,
          track=3, pad=(26, 14), r=None):
    """Pastille pleine (fill) ou contour (outline). Renvoie sa largeur.

    r = rayon des coins. Par defaut la pastille est arrondie complete; le
    one pager RE/MAX utilise plutot un rectangle a coins doux (r=6).
    """
    d = ImageDraw.Draw(canvas)
    f = inter(size, 800)
    w = tw(d, text, f, track) + pad[0] * 2
    h = size + pad[1] * 2
    x, y = xy
    rad = h / 2 if r is None else r
    if fill:
        d.rounded_rectangle([x, y, x + w, y + h], rad, fill=fill + (255,))
    else:
        d.rounded_rectangle([x, y, x + w, y + h], rad, outline=outline, width=3)
    tracked(d, (x + pad[0], y + pad[1] - size * 0.12), text, f, fg, track)
    return w


def eyebrow(canvas, xy, text, color=NAVY, align="l", size=23, track=5):
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
    """Couverture calquee sur le one pager RE/MAX: titre blanc pose au bas de
    la photo, pastille navy NOUVEAUTE, puis bandeau blanc avec le prix."""
    c = base()
    photo(c, "03.jpg", (0, 0, W, 900), r=0, shad=False)
    gradient(c, 420, 900, 232)
    d = ImageDraw.Draw(c)

    d.text((M, 566), "28, rue St-Hilaire", font=playfair(78, 700), fill=WHITE)
    d.text((M, 672), "Vieux-Longueuil", font=inter(34, 400),
           fill=(255, 255, 255, 225))
    badge(c, (M, 748), "NOUVEAUTÉ", fill=NAVY, size=27, track=4,
          pad=(34, 17), r=6)

    eyebrow(c, (M, 962), "PRIX DEMANDÉ")
    d.text((M, 1000), "499 000 $", font=playfair(64, 800), fill=NAVY)
    tracked(d, (W - M, 962), "ÉQUIPE PISTOLI", inter(23, 800), NAVY, 5, "r")
    d.text((W - M, 1004), "Centris 26368231", font=inter(25, 400), fill=GREY,
           anchor="ra")

    d.line([M, 1136, W - M, 1136], fill=LINE + (255,), width=2)
    signature(c, 1172)
    return c


# ================================================================ SLIDE 2
def slide2():
    c = base()
    d = ImageDraw.Draw(c)
    eyebrow(c, (M, 92), "LA PROPRIÉTÉ")
    d.text((M, 134), "Découvrez votre", font=playfair(72, 700), fill=NAVY)
    d.text((M, 218), "prochaine maison", font=playfair(72, 700), fill=NAVY)

    photo(c, "06.jpg", (M, 336, W - M, 856))

    items = [("bed", "2", "Chambres"),
             ("bath", "1 + 1", "Salle de bain / eau"),
             ("car", "2", "Stationnements"),
             ("land", "371 m²", "Terrain")]
    x0, y0, cw, rh = M, 926, (W - 2 * M) // 2, 104
    for i, (ic, val, lab) in enumerate(items):
        x = x0 + (i % 2) * cw
        y = y0 + (i // 2) * rh
        icon(c, ic, (x, y + 6), 44, NAVY + (255,))
        d.text((x + 62, y), val, font=inter(33, 800), fill=NAVY)
        d.text((x + 62, y + 42), lab, font=inter(24, 400), fill=GREY)

    d.rounded_rectangle([M, 1176, W - M, 1292], 12, fill=NAVY + (255,))
    tracked(d, (M + 34, 1204), "PRIX DEMANDÉ", inter(23, 800),
            NAVY_SOFT, 5)
    d.text((W - M - 34, 1198), "499 000 $", font=playfair(58, 800), fill=WHITE,
           anchor="ra")
    return c


# ================================================================ SLIDE 3
def slide3():
    c = base()
    photo(c, "10.jpg", (0, 0, W, 700), r=0, shad=False)
    d = ImageDraw.Draw(c)

    y = 756
    eyebrow(c, (M, y), "LA CUISINE")
    y += 46
    d.text((M, y), "Une cuisine pensée", font=playfair(66, 700), fill=NAVY)
    d.text((M, y + 78), "pour recevoir", font=playfair(66, 700), fill=NAVY)
    y += 196

    for t in ["Îlot central avec rangement",
              "Armoires blanches pleine hauteur",
              "Électroménagers en acier inoxydable"]:
        icon(c, "check", (M, y + 2), 34, NAVY + (255,))
        d.text((M + 52, y), t, font=inter(30, 500), fill=INK)
        y += 62

    signature(c, 1196)
    return c


# ================================================================ SLIDE 4
def slide4():
    c = base()
    photo(c, "17.jpg", (0, 0, W, 700), r=0, shad=False, fy=0.5)
    d = ImageDraw.Draw(c)

    y = 756
    eyebrow(c, (M, y), "DÉJÀ FAIT")
    y += 46
    d.text((M, y), "Les points forts", font=playfair(70, 700), fill=NAVY)
    y += 122

    for t in ["Toiture refaite en 2014",
              "Plomberie et électricité 2014",
              "Piscine hors terre 2023",
              "Borne de recharge électrique"]:
        icon(c, "check", (M, y + 2), 34, NAVY + (255,))
        d.text((M + 52, y), t, font=inter(30, 500), fill=INK)
        y += 62

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
    """Photo de rue professionnelle. Les photos de la pancarte prise au
    telephone restent dans sources/ mais ne vont pas dans le carrousel."""
    c = base()
    photo(c, "05.jpg", (0, 0, W, 700), r=0, shad=False)
    d = ImageDraw.Draw(c)

    y = 756
    eyebrow(c, (M, y), "LE VIEUX-LONGUEUIL")
    y += 46
    d.text((M, y), "Un emplacement", font=playfair(66, 700), fill=NAVY)
    d.text((M, y + 78), "exceptionnel", font=playfair(66, 700), fill=NAVY)
    y += 196

    for ic, t in [("pin", "Écoles et services du secteur"),
                  ("tree", "Parcs et pistes cyclables"),
                  ("train", "Métro et pont Jacques-Cartier")]:
        icon(c, ic, (M, y - 2), 40, NAVY + (255,))
        d.text((M + 60, y), t, font=inter(30, 500), fill=INK)
        y += 62

    signature(c, 1196)
    return c


# ================================================================ SLIDE 7
def slide7():
    c = base()
    photo(c, "07.jpg", (0, 0, W, H), r=0, shad=False, fy=0.45)
    gradient(c, 0, 300, 130, top=True)
    gradient(c, 700, H, 245)
    d = ImageDraw.Draw(c)

    d.line([W // 2 - 46, 820, W // 2 + 46, 820], fill=WHITE + (255,), width=5)
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
    """Les deux courtiers de l inscription: Georges Matar et Rovena Pistoli."""
    c = base(CREAM)
    d = ImageDraw.Draw(c)
    d.rectangle([0, 0, W, 10], fill=NAVY + (255,))

    s, gap = 250, 60
    x0 = (W - (2 * s + gap)) // 2
    circle_photo(c, os.path.join(SOURCES, "rovena-pistoli.jpg"), (x0, 86), s,
                 fy=0.0)
    circle_photo(c, os.path.join(ASSETS, "georges-matar.png"),
                 (x0 + s + gap, 86), s)

    for cx, nom, titre in [
            (x0 + s // 2, "ROVENA PISTOLI",
             "Courtier immobilier résidentiel et commercial"),
            (x0 + s + gap + s // 2, "GEORGES MATAR",
             "Courtier immobilier résidentiel")]:
        d.text((cx, 368), nom, font=inter(26, 800), fill=NAVY, anchor="ma")
        para(d, (cx, 404), titre, inter(19, 400), GREY, s + 40, 26, "c")

    eyebrow(c, (W // 2, 500), "ÉQUIPE PISTOLI", NAVY, "c")
    d.text((W // 2, 542), "Cette propriété", font=playfair(62, 700), fill=NAVY,
           anchor="ma")
    d.text((W // 2, 616), "vous intéresse?", font=playfair(62, 700), fill=NAVY,
           anchor="ma")

    y = 728
    fnt = inter(29, 500)
    for ic, t in [("phone", "(438) 372-0102"),
                  ("mail", "georges.matar@remax-quebec.com"),
                  ("globe", "georgesmatar.ca")]:
        wtot = 40 + 22 + d.textlength(t, font=fnt)
        x = (W - wtot) // 2
        icon(c, ic, (int(x), y), 40, NAVY + (255,))
        d.text((x + 62, y + 3), t, font=fnt, fill=INK)
        y += 62

    y += 18
    bh = 104
    d.rounded_rectangle([M, y, W - M, y + bh], 12, fill=NAVY + (255,))
    d.text((W // 2, y + bh / 2 - 16), "Planifiez votre visite",
           font=inter(33, 800), fill=WHITE, anchor="mm")
    tracked(d, (W // 2, y + bh / 2 + 6), "DÈS AUJOURD'HUI", inter(21, 700),
            NAVY_SOFT, 4, "c")

    y += bh + 40
    d.line([M, y, W - M, y], fill=LINE + (255,), width=2)
    y += 26
    lh = 66
    lw = logo_w(lh, False)
    f = inter(24, 700)
    lbl = "RE/MAX DU CARTIER INC."
    lx = (W - (lw + 20 + d.textlength(lbl, font=f))) / 2
    logo(c, lh, (lx, y), white=False)
    d.text((lx + lw + 20, y + lh / 2), lbl, font=f, fill=NAVY, anchor="lm")

    tracked(d, (W // 2, 1296), "CENTRIS 26368231", inter(21, 600), GREY, 4, "c")
    return c


# ---------------------------------------------------------------- run
if __name__ == "__main__":
    # nettoie l ancien lot pour eviter les fichiers orphelins
    for f in os.listdir(OUT):
        if f.lower().endswith(".jpg"):
            os.remove(os.path.join(OUT, f))
    print("Carrousel ->", OUT)
    for fn, name in [
            (slide1, "01-couverture.jpg"), (slide2, "02-caracteristiques.jpg"),
            (slide3, "03-cuisine.jpg"), (slide4, "04-points-forts.jpg"),
            (slide5, "05-details.jpg"), (slide6, "06-emplacement.jpg"),
            (slide7, "07-coup-de-coeur.jpg"), (slide8, "08-contact.jpg")]:
        save(fn(), name)
    print("OK")
