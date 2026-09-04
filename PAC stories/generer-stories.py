# -*- coding: utf-8 -*-
"""Stories Instagram: promesse d achat acceptee. Une image par propriete.

    python "PAC stories/generer-stories.py"             les deux
    python "PAC stories/generer-stories.py" mirabel     une seule, par bout de nom

Format 1080 x 1920 (9:16), le format plein ecran d une story. Le contenu utile
reste entre 250 px du haut et 1700 px du bas: au dela, l interface d Instagram
(nom du compte en haut, barre de reponse en bas) recouvre l image.

La composition est toujours la meme: la nouvelle en haut sur la photo de
facade, trois photos de la propriete au milieu, la relance et les coordonnees
en bas. Les couleurs, les polices et le logo sont ceux des carrousels et des
reels, pour que la grille du profil reste coherente.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
M = 84                                  # marge laterale
HERO = 920                              # hauteur de la photo de couverture
BAS = 1670                              # au dela, la barre de reponse recouvre

RED = (230, 20, 5)
NAVY = (0, 14, 53)                      # navy du one pager RE/MAX
NAVY_SOFT = (152, 166, 198)
INK = (22, 27, 43)
GREY = (112, 120, 136)
LINE = (227, 231, 238)
WHITE = (255, 255, 255)
CREAM = (250, 249, 247)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PHOTOS = os.path.join(ROOT, "static", "images", "listings")
ASSETS = os.path.join(ROOT, "static", "images")
SOURCES = os.path.join(ROOT, "carrousel-instagram", "sources")
FONTS = os.path.join(ROOT, "carrousel-instagram", "fonts")


# ================================================================ contenu
CONTACT = dict(
    nom="GEORGES MATAR",
    titre="Courtier immobilier résidentiel",
    tel="(438) 372-0102",
    site="georgesmatar.ca",
    courriel="georges.matar@remax-quebec.com",
    agence="RE/MAX DU CARTIER INC.",
    equipe="AVEC L'ÉQUIPE PISTOLI",
)

PROPRIETES = [
    # ============================================== 28, rue St-Hilaire
    dict(
        slug="28-rue-st-hilaire-longueuil",
        adresse="28, rue St-Hilaire",
        secteur="Vieux-Longueuil, Longueuil",
        centris="26368231",
        hero=("03.jpg", 0.50, 0.42),
        strip=[("09.jpg", 0.50, 0.50),
               ("06.jpg", 0.50, 0.50),
               ("24.jpg", 0.50, 0.50)],
    ),

    # ======================================= 4071, rang Saint-Hyacinthe
    dict(
        slug="4071-rang-saint-hyacinthe-mirabel",
        adresse="4071, rang Saint-Hyacinthe",
        secteur="Saint-Hermas, Mirabel",
        centris="26269222",
        hero=("25.jpg", 0.44, 0.55),
        strip=[("06.jpg", 0.50, 0.50),
               ("27.jpg", 0.50, 0.55),
               ("28.jpg", 0.50, 0.28)],
    ),
]

EYEBROW = "MERCI POUR VOTRE CONFIANCE"
RELANCE = ["Votre propriété mérite", "le même résultat."]
TAG = "ÉVALUATION GRATUITE"


# ================================================================ polices
def playfair(size, weight=700):
    f = ImageFont.truetype(os.path.join(FONTS, "Playfair.ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def inter(size, weight=400, opsz=None):
    f = ImageFont.truetype(os.path.join(FONTS, "Inter.ttf"), size)
    f.set_variation_by_axes([opsz if opsz else min(32, max(14, size)), weight])
    return f


# ================================================================ texte
def tw(draw, s, font, track=0):
    if not track:
        return draw.textlength(s, font=font)
    return sum(draw.textlength(c, font=font) for c in s) + track * (len(s) - 1)


def tracked(draw, xy, s, font, fill, track=4, align="l"):
    """Texte lettre par lettre, avec interlettrage. Les petites capitales
    d une pastille ou d un sur titre ne respirent pas sans cela."""
    x, y = xy
    if align == "c":
        x -= tw(draw, s, font, track) / 2
    elif align == "r":
        x -= tw(draw, s, font, track)
    for c in s:
        draw.text((x, y), c, font=font, fill=fill)
        x += draw.textlength(c, font=font) + track


def wrap(draw, s, font, maxw):
    # decoupe sur l espace ordinaire seulement: l espace insecable des
    # nombres (4 000 pi²) doit rester colle
    words, lines, cur = s.split(" "), [], ""
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


# ================================================================ images
def cover(src, w, h, fx=0.5, fy=0.5):
    """Recadre en remplissant la boite. fx et fy donnent le point d interet."""
    im = src if isinstance(src, Image.Image) else Image.open(src)
    im = im.convert("RGB")
    r = max(w / im.width, h / im.height)
    im = im.resize((max(w, int(im.width * r + .5)),
                    max(h, int(im.height * r + .5))), Image.LANCZOS)
    x = int(round((im.width - w) * min(1.0, max(0.0, fx))))
    y = int(round((im.height - h) * min(1.0, max(0.0, fy))))
    return im.crop((x, y, x + w, y + h))


def round_mask(w, h, r):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], r, fill=255)
    return m


def shadow(canvas, box, r, blur=24, alpha=44, dy=12):
    x0, y0, x1, y1 = box
    lay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).rounded_rectangle([x0, y0 + dy, x1, y1 + dy], r,
                                          fill=(0, 14, 53, alpha))
    canvas.alpha_composite(lay.filter(ImageFilter.GaussianBlur(blur)))


def photo(canvas, path, box, r=18, shad=True, fx=0.5, fy=0.5):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    if shad and r:
        shadow(canvas, box, r)
    im = cover(path, w, h, fx, fy).convert("RGBA")
    if r:
        im.putalpha(round_mask(w, h, r))
    canvas.alpha_composite(im, (x0, y0))


def circle_photo(canvas, src, xy, size, fy=0.0, anneau=None):
    im = cover(src, size, size, 0.5, fy).convert("RGBA")
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse([0, 0, size - 1, size - 1], fill=255)
    im.putalpha(m)
    canvas.alpha_composite(im, xy)
    if anneau:
        ImageDraw.Draw(canvas).ellipse(
            [xy[0] - 3, xy[1] - 3, xy[0] + size + 2, xy[1] + size + 2],
            outline=anneau, width=4)


def studio_portrait(png, size=1200, head_top=0.08, zoom=1.14, dx=0.05):
    """Pose le portrait detoure sur un fond studio clair, comme sur le
    carrousel: mur lumineux derriere la tete, ombre douce derriere le sujet."""
    bg = Image.new("RGB", (size, size), (243, 244, 246))
    px = bg.load()
    cx, cy = size * 0.5, size * 0.34
    rmax = (size ** 2 * 2) ** 0.5
    for y in range(size):
        for x in range(0, size, 4):
            t = min(1.0, (((x - cx) ** 2 + (y - cy) ** 2) ** 0.5) /
                    (rmax * 0.62))
            v = tuple(int(a + (b - a) * t) for a, b in
                      ((246, 209), (247, 209), (249, 211)))
            for k in range(4):
                if x + k < size:
                    px[x + k, y] = v
    bg = bg.filter(ImageFilter.GaussianBlur(6))

    im = Image.open(png)
    im = im.crop(im.getchannel("A").getbbox())
    h = int(size * zoom)
    w = int(im.width * h / im.height)
    im = im.resize((w, h), Image.LANCZOS)
    x0, y0 = (size - w) // 2 + int(size * dx), int(size * head_top)

    sh = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sh.paste((176, 176, 180, 150), (x0 + int(size * 0.035), y0 + 10), im)
    bg = bg.convert("RGBA")
    bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(size // 26)))
    bg.alpha_composite(im, (x0, y0))
    return bg.convert("RGB")


def gradient(canvas, y0, y1, alpha=225, haut=False):
    """Voile navy progressif, pour que le texte tienne sur la photo."""
    n = y1 - y0
    g = Image.new("L", (1, n))
    px = g.load()
    for i in range(n):
        t = i / max(1, n - 1)
        px[0, i] = int(alpha * (1 - t) if haut else alpha * t)
    lay = Image.new("RGBA", (canvas.width, n), NAVY + (0,))
    lay.putalpha(g.resize((canvas.width, n)))
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


# ================================================================ icones
ICONS = {
    "check": [("p", [(4.5, 12.5), (10, 18), (19.5, 5.5)])],
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
                d.ellipse([x - S / 2, y - S / 2, x + S / 2, y + S / 2],
                          fill=color)
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


def pastille(canvas, xy, texte, fill=RED, fg=WHITE, size=30, track=5,
             pad=(32, 18), r=8, ic="check"):
    """Pastille pleine avec une icone en tete. Renvoie sa largeur."""
    d = ImageDraw.Draw(canvas)
    f = inter(size, 800)
    isz = int(size * 1.15)
    icw = isz + 18 if ic else 0
    w = int(pad[0] * 2 + icw + tw(d, texte, f, track))
    h = int(size + pad[1] * 2)
    x, y = int(xy[0]), int(xy[1])
    d.rounded_rectangle([x, y, x + w, y + h], r, fill=fill + (255,))
    if ic:
        icon(canvas, ic, (x + pad[0], y + (h - isz) // 2), isz, fg + (255,),
             sw=max(3, isz // 9))
    tracked(d, (x + pad[0] + icw, y + pad[1] - size * 0.14), texte, f, fg,
            track)
    return w


# ================================================================ story
def story(p):
    c = Image.new("RGBA", (W, H), CREAM + (255,))
    d = ImageDraw.Draw(c)

    # ---- la photo de couverture, plein cadre
    nom, fx, fy = p["hero"]
    hero = cover(os.path.join(PHOTOS, p["slug"], nom), W, HERO, fx, fy)
    c.alpha_composite(hero.convert("RGBA"), (0, 0))
    gradient(c, 0, 380, 128, haut=True)     # le logo doit tenir sur un ciel
    gradient(c, 386, HERO, 242)
    d = ImageDraw.Draw(c)

    logo(c, 86, (M, 258), white=True)

    # ---- la nouvelle
    pastille(c, (M, 482), "PROMESSE D'ACHAT")
    d.text((M - 6, 562), "ACCEPTÉE", font=playfair(118, 800), fill=WHITE)

    d.line([M, 748, W - M, 748], fill=(255, 255, 255, 96), width=2)
    d.text((M, 772), p["adresse"], font=playfair(52, 700), fill=WHITE)
    d.text((M, 846), p["secteur"], font=inter(28, 400),
           fill=(255, 255, 255, 222))
    tracked(d, (W - M, 852), "CENTRIS " + p["centris"], inter(22, 600),
            (255, 255, 255, 176), 4, "r")

    # ---- trois photos de la propriete, en bandeau
    gap, top, bh = 16, 976, 212
    pw = (W - 2 * M - 2 * gap) // 3
    for i, (nom, fx, fy) in enumerate(p["strip"]):
        x = M + i * (pw + gap)
        photo(c, os.path.join(PHOTOS, p["slug"], nom),
              (x, top, x + pw, top + bh), r=14, fx=fx, fy=fy)

    # ---- la relance: c est la que la story travaille pour le prochain mandat
    y = 1272
    d.rectangle([M, y, M + 64, y + 5], fill=RED + (255,))
    tracked(d, (M, y + 28), EYEBROW, inter(22, 800), NAVY, 5)
    tracked(d, (W - M, y + 28), TAG, inter(22, 800), RED, 5, "r")
    d.text((M, y + 70), RELANCE[0], font=playfair(48, 700), fill=NAVY)
    d.text((M, y + 126), RELANCE[1], font=playfair(48, 700), fill=NAVY)

    # ---- les coordonnees
    ch = 184
    cy = BAS - ch
    shadow(c, (M, cy, W - M, cy + ch), 18, blur=26, alpha=38, dy=10)
    d.rounded_rectangle([M, cy, W - M, cy + ch], 18, fill=NAVY + (255,))

    ps = 132
    circle_photo(c, studio_portrait(os.path.join(SOURCES,
                                                 "georges-matar-decoupe.png")),
                 (M + 36, cy + 30), ps, fy=0.0, anneau=(255, 255, 255, 40))
    x = M + 36 + ps + 32
    d.text((x, cy + 34), CONTACT["nom"], font=inter(31, 800), fill=WHITE)
    d.text((x, cy + 76), CONTACT["titre"], font=inter(21, 400), fill=NAVY_SOFT)

    f = inter(27, 600)
    yy = cy + 122
    for ic, txt in [("phone", CONTACT["tel"]), ("globe", CONTACT["site"])]:
        icon(c, ic, (int(x), yy), 32, WHITE + (255,))
        d.text((x + 44, yy + 2), txt, font=f, fill=WHITE)
        x += 44 + d.textlength(txt, font=f) + 40

    lh = 46
    logo(c, lh, (W - M - 34 - logo_w(lh, True), cy + 38), white=True)

    # ---- la signature, dans la zone que la barre de reponse recouvre
    d.line([M, 1716, W - M, 1716], fill=LINE + (255,), width=2)
    tracked(d, (W // 2, 1742),
            "%s   ·   %s" % (CONTACT["agence"], CONTACT["equipe"]),
            inter(21, 700), NAVY, 4, "c")
    d.text((W // 2, 1782), CONTACT["courriel"], font=inter(23, 400), fill=GREY,
           anchor="ma")
    return c


# ================================================================ run
def main():
    filtre = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    for p in PROPRIETES:
        if filtre and filtre not in p["slug"]:
            continue
        out = os.path.join(HERE, p["slug"])
        os.makedirs(out, exist_ok=True)
        f = os.path.join(out, "story-promesse-achat-acceptee.jpg")
        story(p).convert("RGB").save(f, quality=93, subsampling=0,
                                     optimize=True)
        print("Story ->", f)


if __name__ == "__main__":
    main()
