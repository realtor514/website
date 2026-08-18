# -*- coding: utf-8 -*-
"""Moteur de rendu des reels Instagram, 1080 x 1920, 30 images par seconde.

Fabrique une video a partir des photos fixes d une inscription. Les photos ne
bougent pas d elles-memes: le mouvement vient du cadrage, qui se deplace image
par image. Trois familles de mouvements:

- zoom avant et zoom arriere, lents, le classique du travelling
- panoramique horizontal ou vertical, comme une camera sur rail
- arc, une legere deformation de perspective en plus du zoom, qui donne la
  sensation d un drone qui contourne le sujet

Deux mises en page:

- plein: la photo remplit l ecran. Cinematographique, mais le format 9:16
  coupe une photo horizontale des deux cotes.
- cadre: la photo garde sa largeur entiere au centre, sur un fond flou tire de
  la meme photo. Rien n est coupe et l image reste nette. Reserve aux plans
  larges, ou couper serait dommage.

Le texte reste entre 250 px du haut et 1600 px du bas: c est la zone que
l interface d Instagram ne recouvre pas.

Aucune bande sonore n est ajoutee, seulement une piste muette pour que le
fichier soit accepte partout. La musique se choisit dans Instagram, au
montage: un son tendance y vaut beaucoup plus de portee qu une musique
importee.
"""
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
HAUT, BAS = 250, 1600                   # zone libre de l interface Instagram
MARGE = 84
FONDU = 0.36                            # duree des transitions, en secondes

NAVY = (0, 14, 53)
NAVY_SOFT = (152, 166, 198)
RED = (230, 20, 5)
INK = (22, 27, 43)
GREY = (112, 120, 136)
WHITE = (255, 255, 255)
CREAM = (250, 249, 247)
LINE = (227, 231, 238)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SOURCES = os.path.join(ROOT, "carrousel-instagram", "sources")
FONTS = os.path.join(ROOT, "carrousel-instagram", "fonts")
ASSETS = os.path.join(ROOT, "static", "images")


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


# ---------------------------------------------------------------- icones
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


# ---------------------------------------------------------------- logo
def _logo_img(white):
    src = "remax-ducartier-blanc.png" if white else "remax-logo.png"
    im = Image.open(os.path.join(ASSETS, src)).convert("RGBA")
    return im.crop(im.getchannel("A").getbbox())


def logo_w(box_h, white=False):
    im = _logo_img(white)
    return int(im.width * box_h / im.height)


def logo(canvas, box_h, xy, white=False, alpha=255):
    im = _logo_img(white)
    w = int(im.width * box_h / im.height)
    im = im.resize((w, box_h), Image.LANCZOS)
    if alpha < 255:
        a = im.getchannel("A").point(lambda v: v * alpha // 255)
        im.putalpha(a)
    canvas.alpha_composite(im, (int(xy[0]), int(xy[1])))
    return w


# ---------------------------------------------------------------- images
def _ouvrir(nom, crop=None):
    im = Image.open(os.path.join(SOURCES, nom)) if not os.path.isabs(nom) \
        else Image.open(nom)
    im = im.convert("RGB")
    if crop:
        im = im.crop((int(crop[0] * im.width), int(crop[1] * im.height),
                      int(crop[2] * im.width), int(crop[3] * im.height)))
    return im


def remplir(im, w, h, fx=0.5, fy=0.5):
    r = max(w / im.width, h / im.height)
    im = im.resize((max(w, int(im.width * r + .5)), max(h, int(im.height * r + .5))),
                   Image.LANCZOS)
    x = int(round((im.width - w) * min(1.0, max(0.0, fx))))
    y = int(round((im.height - h) * min(1.0, max(0.0, fy))))
    return im.crop((x, y, x + w, y + h))


def degrade(canvas, y0, y1, alpha=225, haut=False, couleur=NAVY):
    """Voile sombre progressif, pour que le texte tienne sur la photo."""
    n = y1 - y0
    g = Image.new("L", (1, n))
    px = g.load()
    for i in range(n):
        t = i / max(1, n - 1)
        px[0, i] = int(alpha * (1 - t) if haut else alpha * t)
    lay = Image.new("RGBA", (canvas.width, n), couleur + (0,))
    lay.putalpha(g.resize((canvas.width, n)))
    canvas.alpha_composite(lay, (0, y0))


# ---------------------------------------------------------------- courbes
def lisse(t):
    """Acceleration puis deceleration. Un mouvement de camera ne demarre
    jamais sec."""
    return t * t * (3 - 2 * t)


def sortie_cubique(t):
    return 1 - (1 - t) ** 3


def melange(a, b, t):
    return a + (b - a) * t


# ================================================================ clips
class Clip:
    """Un plan. duree en secondes, images produites a la demande."""

    def __init__(self, duree):
        self.duree = duree
        self.etapes = []                # (t_apparition, calque cumulatif RGBA)
        self.sortie = 0.30              # duree de la disparition du texte
        self._cache = (None, None)

    @property
    def n(self):
        return max(1, int(round(self.duree * FPS)))

    def preparer(self):
        pass

    def fond(self, t):
        raise NotImplementedError

    def calque(self, t):
        """Calque de texte au temps t, avec apparition en fondu."""
        j = -1
        for k, (ta, _) in enumerate(self.etapes):
            if t >= ta:
                j = k
        if j < 0:
            return None
        u = sortie_cubique(min(1.0, max(0.0, (t - self.etapes[j][0]) / 0.34)))
        # disparition: deux legendes superposees pendant un fondu, ca fait
        # brouillon. Le texte quitte l ecran avant que l image ne change.
        s = 0.0
        if self.sortie:
            debut = self.duree - FONDU - self.sortie
            if t > debut:
                s = sortie_cubique(min(1.0, (t - debut) / self.sortie))
        cle = (j, round(u, 3), round(s, 3))
        if self._cache[0] == cle:
            return self._cache[1]
        if u >= 0.999:
            out = self.etapes[j][1]
        else:
            base = self.etapes[j - 1][1] if j > 0 else \
                Image.new("RGBA", (W, H), (0, 0, 0, 0))
            out = Image.blend(base, self.etapes[j][1], u)
        if s > 0.001:
            out = Image.blend(out, Image.new("RGBA", (W, H), (0, 0, 0, 0)), s)
        self._cache = (cle, out)
        return out

    def image(self, i):
        t = i / FPS
        im = self.fond(t)
        c = self.calque(t)
        if c is not None:
            im.paste(c.convert("RGB"), (0, 0), c.getchannel("A"))
        return im


# Mouvements. z = serrage: 1 montre le champ le plus large, S les pixels
# natifs. dx et dy sont exprimes en fraction du cadre visible, pas de la
# photo: un panoramique de 0.42 fait donc toujours defiler 42 pour cent de
# l ecran, quelle que soit la taille de la photo.
MOUVEMENTS = {
    "zoom":        dict(z0=1.00, z1=1.13),
    "recul":       dict(z0=1.15, z1=1.00),
    "droite":      dict(z0=1.08, z1=1.13, dx=+0.42),
    "gauche":      dict(z0=1.08, z1=1.13, dx=-0.42),
    "descente":    dict(z0=1.14, z1=1.18, dy=+0.40),
    "montee":      dict(z0=1.14, z1=1.18, dy=-0.40),
    "arc":         dict(z0=1.00, z1=1.13, k0=-0.030, k1=+0.030),
    "arc_inverse": dict(z0=1.15, z1=1.00, k0=+0.030, k1=-0.030),
}


class ClipPhoto(Clip):
    """Photo plein ecran, cadrage mobile.

    La photo n est pas recadree a l avance: elle est seulement mise a
    l echelle. Le cadre 9:16 se promene ensuite dedans, ce qui permet un vrai
    panoramique d un bout a l autre d une photo horizontale. fx et fy donnent
    le point d interet, autour duquel le mouvement se joue.
    """

    S = 1.30                            # champ le plus large que l on montre

    def __init__(self, photo, duree, mouvement="zoom", fx=0.5, fy=0.5,
                 crop=None):
        super().__init__(duree)
        self.photo, self.mouvement, self.fx, self.fy = photo, mouvement, fx, fy
        self.crop = crop

    def preparer(self):
        im = _ouvrir(self.photo, self.crop)
        r = max(H * self.S / im.height, W * self.S / im.width)
        w, h = int(im.width * r + .5), int(im.height * r + .5)
        im = im.resize((w, h), Image.LANCZOS)
        # la photo a ete agrandie pour tenir en 9:16: on lui rend du mordant
        self.work = im.filter(ImageFilter.UnsharpMask(2, 62, 3))
        self.ws, self.hs = w, h
        self.p = dict(z0=1.0, z1=1.13, dx=0.0, dy=0.0, k0=0.0, k1=0.0)
        self.p.update(MOUVEMENTS.get(self.mouvement, {}))
        self._bornes()

    def _taille(self, z):
        ch = min(self.hs, H * self.S / z)
        cw = min(self.ws, ch * W / H)
        return cw, cw * H / W

    def _bornes(self):
        """Depart et arrivee du centre, deja ramenes dans la photo.

        On borne les deux extremites avant d interpoler: sinon un panoramique
        trop large viendrait buter contre le bord en cours de route, et le
        mouvement s arreterait net au milieu du plan.
        """
        p = self.p
        cw, ch = self._taille(min(p["z0"], p["z1"]))

        def borne(v, taille, total):
            return min(max(v, taille / 2), total - taille / 2)

        self.cx0 = borne(self.fx * self.ws - p["dx"] * cw / 2, cw, self.ws)
        self.cx1 = borne(self.fx * self.ws + p["dx"] * cw / 2, cw, self.ws)
        self.cy0 = borne(self.fy * self.hs - p["dy"] * ch / 2, ch, self.hs)
        self.cy1 = borne(self.fy * self.hs + p["dy"] * ch / 2, ch, self.hs)

    def _cadre(self, u):
        """Rectangle visible dans l image de travail, au temps relatif u."""
        p = self.p
        cw, ch = self._taille(melange(p["z0"], p["z1"], u))
        cx = melange(self.cx0, self.cx1, u)
        cy = melange(self.cy0, self.cy1, u)
        l = min(max(0.0, cx - cw / 2), self.ws - cw)
        top = min(max(0.0, cy - ch / 2), self.hs - ch)
        return l, top, cw, ch

    def fond(self, t):
        u = lisse(min(1.0, t / max(0.001, self.duree)))
        l, top, cw, ch = self._cadre(u)
        r, b = l + cw, top + ch
        k = melange(self.p["k0"], self.p["k1"], u)
        if abs(k) < 1e-4:
            return self.work.resize((W, H), Image.BICUBIC, box=(l, top, r, b))
        # le haut du cadre se resserre ou s ouvre: la scene bascule doucement
        dx = k * cw / 2
        m = abs(dx)
        l = min(max(m, l), self.ws - cw - m)
        r = l + cw
        quad = (l + dx, top, l - dx, b, r + dx, b, r - dx, top)
        return self.work.transform((W, H), Image.Transform.QUAD, quad,
                                   Image.BILINEAR)


class ClipCadre(Clip):
    """Photo entiere au centre, fond flou tire de la meme photo.

    Rien n est coupe et l image reste a sa resolution d origine. Le fond
    bouge plus vite que la photo: c est ce decalage qui donne la profondeur.
    """

    def __init__(self, photo, duree, crop=None, fy=0.5, sens=1):
        super().__init__(duree)
        self.photo, self.crop, self.fy, self.sens = photo, crop, fy, sens

    def preparer(self):
        im = _ouvrir(self.photo, self.crop)
        fh = int(W * im.height / im.width)
        self.avant = im.resize((W, fh), Image.LANCZOS) \
            .filter(ImageFilter.UnsharpMask(2, 45, 3))
        self.fh = fh
        f = remplir(im, int(W * 1.30), int(H * 1.30), 0.5, self.fy)
        self.arriere = f.filter(ImageFilter.GaussianBlur(46))
        voile = Image.new("RGBA", self.arriere.size, NAVY + (108,))
        a = self.arriere.convert("RGBA")
        a.alpha_composite(voile)
        self.arriere = a.convert("RGB")

    def fond(self, t):
        u = lisse(min(1.0, t / max(0.001, self.duree)))
        # fond: zoom lent
        zb = melange(1.0, 1.10, u)
        bw, bh = self.arriere.size
        cw, ch = bw / zb, bh / zb
        l = (bw - cw) / 2
        top = (bh - ch) / 2
        im = self.arriere.resize((W, H), Image.BILINEAR,
                                 box=(l, top, l + cw, top + ch))
        # photo: zoom plus faible, leger glissement vertical
        zf = melange(1.0, 1.035, u)
        pw, ph = int(W * zf), int(self.fh * zf)
        ph_im = self.avant.resize((pw, ph), Image.BICUBIC)
        y = int((H - ph) / 2 + self.sens * melange(-16, 16, u))
        im.paste(ph_im, (int((W - pw) / 2), y))
        return im


class ClipCarte(Clip):
    """Ecran de points forts, sur photo fortement assombrie."""

    def __init__(self, photo, duree, eyebrow, titre, points, crop=None,
                 fy=0.5):
        super().__init__(duree)
        self.photo, self.crop, self.fy = photo, crop, fy
        self.eyebrow, self.titre, self.points = eyebrow, titre, points

    def preparer(self):
        im = remplir(_ouvrir(self.photo, self.crop), int(W * 1.16),
                     int(H * 1.16), 0.5, self.fy)
        im = im.filter(ImageFilter.GaussianBlur(9))
        self.work = im
        self.ws, self.hs = im.size

        # calques cumulatifs: le titre, puis les points un a un
        base = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(base)
        logo(base, 82, (MARGE, HAUT), white=True, alpha=225)
        tracked(d, (MARGE, 560), self.eyebrow, inter(26, 800),
                (255, 255, 255, 205), 6)
        y = 610
        for ln in wrap(d, self.titre, playfair(78, 700), W - 2 * MARGE):
            d.text((MARGE, y), ln, font=playfair(78, 700), fill=WHITE)
            y += 96
        self.etapes.append((0.10, base))

        y = max(y + 46, 800)
        cur = base
        for i, p in enumerate(self.points):
            lay = cur.copy()
            dd = ImageDraw.Draw(lay)
            icon(lay, "check", (MARGE, y + 4), 40, (255, 255, 255, 255))
            para(dd, (MARGE + 62, y), p, inter(34, 500), WHITE,
                 W - 2 * MARGE - 62, 46)
            self.etapes.append((0.55 + i * 0.30, lay))
            cur = lay
            y += 96

    def fond(self, t):
        u = lisse(min(1.0, t / max(0.001, self.duree)))
        z = melange(1.0, 1.06, u)
        cw, ch = self.ws / z, self.hs / z
        l, top = (self.ws - cw) / 2, (self.hs - ch) / 2
        im = self.work.resize((W, H), Image.BILINEAR,
                              box=(l, top, l + cw, top + ch))
        a = im.convert("RGBA")
        a.alpha_composite(Image.new("RGBA", (W, H), NAVY + (188,)))
        return a.convert("RGB")


class ClipOutro(Clip):
    """Carte de contact: les deux courtiers, le telephone, l appel a l action."""

    def __init__(self, duree, prop):
        super().__init__(duree)
        self.prop = prop

    def preparer(self):
        p = self.prop
        c = Image.new("RGBA", (W, H), CREAM + (255,))
        d = ImageDraw.Draw(c)
        d.rectangle([0, 0, W, 14], fill=NAVY + (255,))

        s, gap = 268, 64
        x0 = (W - (2 * s + gap)) // 2
        self._rond(c, os.path.join(SOURCES, "rovena-pistoli.jpg"), (x0, 330), s)
        self._rond(c, self._studio(os.path.join(SOURCES,
                                                "georges-matar-decoupe.png")),
                   (x0 + s + gap, 330), s)

        for cx, nom, titre in [
                (x0 + s // 2, "ROVENA PISTOLI",
                 "Courtier immobilier résidentiel et commercial"),
                (x0 + s + gap + s // 2, "GEORGES MATAR",
                 "Courtier immobilier résidentiel")]:
            d.text((cx, 632), nom, font=inter(28, 800), fill=NAVY, anchor="ma")
            para(d, (cx, 672), titre, inter(20, 400), GREY, s + 44, 28, "c")

        d.text((W // 2, 772), "Cette propriété", font=playfair(72, 700),
               fill=NAVY, anchor="ma")
        d.text((W // 2, 858), "vous intéresse?", font=playfair(72, 700),
               fill=NAVY, anchor="ma")

        y = 986
        fnt = inter(33, 500)
        for ic, txt in [("phone", "(438) 372-0102"),
                        ("globe", "georgesmatar.ca")]:
            wtot = 44 + 24 + d.textlength(txt, font=fnt)
            x = (W - wtot) // 2
            icon(c, ic, (int(x), y), 44, NAVY + (255,))
            d.text((x + 68, y + 4), txt, font=fnt, fill=INK)
            y += 70

        y += 24
        bh = 118
        d.rounded_rectangle([MARGE, y, W - MARGE, y + bh], 14,
                            fill=NAVY + (255,))
        d.text((W // 2, y + bh / 2 - 18), "Planifiez votre visite",
               font=inter(37, 800), fill=WHITE, anchor="mm")
        tracked(d, (W // 2, y + bh / 2 + 8), "DÈS AUJOURD'HUI", inter(23, 700),
                NAVY_SOFT, 4, "c")

        y += bh + 48
        d.line([MARGE, y, W - MARGE, y], fill=LINE + (255,), width=2)
        y += 30
        lh = 72
        lw = logo_w(lh, False)
        f = inter(26, 700)
        lbl = "RE/MAX DU CARTIER INC."
        lx = (W - (lw + 22 + d.textlength(lbl, font=f))) / 2
        logo(c, lh, (lx, y), white=False)
        d.text((lx + lw + 22, y + lh / 2), lbl, font=f, fill=NAVY, anchor="lm")

        tracked(d, (W // 2, y + lh + 54),
                "%s   ·   CENTRIS %s" % (p["prix"].upper(), p["centris"]),
                inter(23, 600), GREY, 4, "c")
        self.plaque = c.convert("RGB")

    def _rond(self, canvas, src, xy, size):
        im = remplir(src if isinstance(src, Image.Image) else Image.open(src),
                     size, size, 0.5, 0.0).convert("RGBA")
        m = Image.new("L", (size, size), 0)
        ImageDraw.Draw(m).ellipse([0, 0, size - 1, size - 1], fill=255)
        im.putalpha(m)
        lay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        ImageDraw.Draw(lay).ellipse([xy[0], xy[1] + 10, xy[0] + size,
                                     xy[1] + size + 10], fill=(0, 14, 53, 44))
        canvas.alpha_composite(lay.filter(ImageFilter.GaussianBlur(20)))
        canvas.alpha_composite(im, xy)

    def _studio(self, png, size=1200, head_top=0.08, zoom=1.14, dx=0.05):
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

    def fond(self, t):
        # tres leger zoom, pour que la carte ne soit pas une image morte
        u = lisse(min(1.0, t / max(0.001, self.duree)))
        z = melange(1.0, 1.022, u)
        w, h = int(W * z), int(H * z)
        im = self.plaque.resize((w, h), Image.BILINEAR)
        return im.crop(((w - W) // 2, (h - H) // 2,
                        (w - W) // 2 + W, (h - H) // 2 + H))


# ---------------------------------------------------------------- habillage
def habillage_accroche(prop, accroche):
    """Calque de la premiere seconde: logo, accroche, adresse, prix."""
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # bandeau plein en haut, sinon l accroche disparait sur un mur clair
    ImageDraw.Draw(c).rectangle([0, 0, W, 600], fill=NAVY + (148,))
    degrade(c, 600, 820, 148, haut=True)
    degrade(c, 880, H, 238)
    d = ImageDraw.Draw(c)

    logo(c, 96, (MARGE, HAUT), white=True)
    y = HAUT + 152
    f = inter(46, 800)
    for ln in wrap(d, accroche, f, W - 2 * MARGE - 40):
        d.text((MARGE, y), ln, font=f, fill=WHITE)
        y += 60

    y = 1006
    dd = ImageDraw.Draw(c)
    f = inter(25, 800)
    bw = tw(dd, "NOUVEAUTÉ", f, 4) + 64
    dd.rounded_rectangle([MARGE, y, MARGE + bw, y + 58], 6, fill=NAVY + (255,))
    tracked(dd, (MARGE + 32, y + 14), "NOUVEAUTÉ", f, WHITE, 4)

    y += 92
    d.text((MARGE, y), prop["titre1"], font=playfair(88, 700), fill=WHITE)
    d.text((MARGE, y + 104), prop["titre2"], font=playfair(88, 700), fill=WHITE)
    y += 232
    d.text((MARGE, y), prop["secteur"], font=inter(34, 400),
           fill=(255, 255, 255, 224))
    y += 66
    d.line([MARGE, y, W - MARGE, y], fill=(255, 255, 255, 92), width=2)
    y += 26
    tracked(d, (MARGE, y), "PRIX DEMANDÉ", inter(24, 800),
            (255, 255, 255, 190), 5)
    d.text((MARGE, y + 34), prop["prix"], font=playfair(70, 800), fill=WHITE)
    tracked(d, (W - MARGE, y + 62), "CENTRIS " + prop["centris"],
            inter(23, 600), (255, 255, 255, 180), 4, "r")
    return c


def habillage_plan(eyebrow, titre):
    """Calque d un plan: logo en haut, nom de la piece en bas."""
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    degrade(c, 0, 420, 120, haut=True)
    degrade(c, 1120, H, 226)
    d = ImageDraw.Draw(c)
    logo(c, 82, (MARGE, HAUT), white=True, alpha=225)
    if eyebrow:
        tracked(d, (MARGE, 1372), eyebrow, inter(25, 800),
                (255, 255, 255, 200), 6)
    y = 1416
    for ln in wrap(d, titre, playfair(62, 700), W - 2 * MARGE):
        d.text((MARGE, y), ln, font=playfair(62, 700), fill=WHITE)
        y += 76
    return c


# ---------------------------------------------------------------- montage
def rendre(clips, sortie, cover=None):
    """Assemble les clips avec des fondus enchaines et encode en H.264."""
    for cl in clips:
        cl.preparer()
    clips[-1].sortie = 0                # la carte de contact reste a l ecran

    k = int(round(FONDU * FPS))
    cmd = ["ffmpeg", "-y", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (W, H),
           "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
           "-shortest",
           "-c:v", "libx264", "-preset", "medium", "-crf", "19",
           "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.1",
           "-c:a", "aac", "-b:a", "96k",
           "-movflags", "+faststart", sortie]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    if cover:
        clips[0].image(int(clips[0].n * 0.4)).save(cover, quality=92,
                                                   subsampling=0)
    total = 0
    queue = []                          # dernieres images du clip precedent
    for ci, cl in enumerate(clips):
        n = cl.n
        dernier = ci == len(clips) - 1
        tail = []
        print("      plan %d/%d" % (ci + 1, len(clips)), flush=True)
        for i in range(n):
            im = cl.image(i)
            if i < len(queue):          # fondu avec la fin du clip precedent
                im = Image.blend(queue[i], im, (i + 1) / (len(queue) + 1))
            if not dernier and i >= n - k:
                tail.append(im)         # servira au fondu du clip suivant
                continue
            p.stdin.write(im.tobytes())
            total += 1
        queue = tail
    p.stdin.close()
    p.wait()
    return total / FPS
