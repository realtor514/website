# -*- coding: utf-8 -*-
"""Logo et photo de couverture de la marque "Georges Matar" dans Apple Business.

Exigences d Apple (guide Apple Business, octobre 2026):
  - logo: carre 1:1, 1024 x 1024 px au minimum, 4864 au maximum. Apple
    l affiche dans un cercle: tout tient dans le cercle inscrit.
  - couverture: 1600 x 1040 px au minimum. Apple la recadre en 2,5:1 dans
    Plans et en 1,5:1 dans Wallet: le sujet doit rester au centre.
  - couverture: une seule vraie photo, sans texte, logo ajoute, montage ni
    filtre. D ou une photo reelle de la reception du bureau, seulement
    recadree et mise a la taille. La montgolfiere du tapis fait partie du
    decor, ce n est pas un logo ajoute.

Le logo n utilise pas la marque RE/MAX: la marque declaree a Apple est
"Georges Matar", que Georges possede; RE/MAX ne lui appartient pas.

Couleurs et polices: regle 3 de CLAUDE.md, voir COULEURS.md a cote.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTS = os.path.join(ROOT, "carrousel-instagram", "fonts")
OFFICE = os.path.join(ROOT, "static", "images", "office")
APERCUS = os.path.join(HERE, "apercus")

NAVY = (0, 14, 53)       # principale
CREME = (247, 245, 238)  # principale, texte sur fond sombre
ROUGE = (255, 18, 0)     # secondaire, accent seulement


def playfair(size, weight=700):
    f = ImageFont.truetype(os.path.join(FONTS, "Playfair.ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def inter(size, weight=500):
    f = ImageFont.truetype(os.path.join(FONTS, "Inter.ttf"), size)
    f.set_variation_by_axes([14, weight])
    return f


# ------------------------------------------------------------------ logo
def logo(chemin, cote=2048):
    im = Image.new("RGB", (cote, cote), NAVY)
    d = ImageDraw.Draw(im)
    c = cote / 2

    # Anneau creme fin, juste a l interieur du cercle d affichage d Apple.
    r = cote * 0.43
    ep = max(4, round(cote * 0.006))
    d.ellipse((c - r, c - r, c + r, c + r), outline=CREME, width=ep)

    # Monogramme GM.
    f = playfair(round(cote * 0.36), 700)
    texte = "GM"
    x0, y0, x1, y1 = d.textbbox((0, 0), texte, font=f)
    tw, th = x1 - x0, y1 - y0
    ty = c - th / 2 - y0 - cote * 0.045
    d.text((c - tw / 2 - x0, ty), texte, font=f, fill=CREME)

    # Filet rouge sous le monogramme, seul accent secondaire.
    fw, fh = cote * 0.16, max(6, round(cote * 0.011))
    fy = ty + y0 + th + cote * 0.06
    d.rectangle((c - fw / 2, fy, c + fw / 2, fy + fh), fill=ROUGE)

    # Nom en petites capitales espacees, lisible quand le logo est grand.
    g = inter(round(cote * 0.042), 600)
    nom = "GEORGES MATAR"
    esp = cote * 0.012
    largeurs = [d.textlength(ch, font=g) for ch in nom]
    total = sum(largeurs) + esp * (len(nom) - 1)
    x = c - total / 2
    ny = fy + fh + cote * 0.05
    for ch, w in zip(nom, largeurs):
        d.text((x, ny), ch, font=g, fill=CREME)
        x += w + esp

    im.save(chemin, optimize=True)
    return im


# ------------------------------------------------------------ couverture
def couverture(source, chemin, centre_x=0.5, largeur=1600, ratio=1.5):
    """Recadre une vraie photo en 1,5:1 autour de centre_x, puis la met a
    1600 px de large. Aucun filtre, aucun ajout: Apple refuse les photos
    retouchees."""
    im = Image.open(source).convert("RGB")
    w, h = im.size
    cw = min(w, round(h * ratio))
    ch = round(cw / ratio)
    cx = round(w * centre_x)
    x0 = min(max(0, cx - cw // 2), w - cw)
    y0 = (h - ch) // 2
    im = im.crop((x0, y0, x0 + cw, y0 + ch))
    hauteur = round(largeur / ratio)
    im = im.resize((largeur, hauteur), Image.LANCZOS)
    assert im.size[0] >= 1600 and im.size[1] >= 1040, im.size
    im.save(chemin, quality=92, optimize=True, progressive=True)
    return im


def apercu(cov, lg, chemin):
    """Montre la couverture comme Apple la recadre: 2,5:1 dans Plans,
    1,5:1 dans Wallet, avec le logo en rond par-dessus."""
    w, h = cov.size
    plans_h = round(w / 2.5)
    plans = cov.crop((0, (h - plans_h) // 2, w, (h - plans_h) // 2 + plans_h))
    rond = lg.resize((220, 220), Image.LANCZOS)
    masque = Image.new("L", rond.size, 0)
    ImageDraw.Draw(masque).ellipse((0, 0, 219, 219), fill=255)
    out = Image.new("RGB", (w, plans_h + h + 60), (235, 235, 235))
    out.paste(plans, (0, 0))
    out.paste(rond, (40, plans_h - 130), masque)
    out.paste(cov, (0, plans_h + 60))
    out.save(chemin, quality=85)


if __name__ == "__main__":
    os.makedirs(APERCUS, exist_ok=True)
    lg = logo(os.path.join(HERE, "logo-georges-matar.png"))
    c1 = couverture(os.path.join(OFFICE, "reception.png"),
                    os.path.join(HERE, "couverture-1-reception.jpg"), centre_x=0.5)
    # La salle de conference a ete essayee: trop sombre et floue, rien de
    # reconnaissable. La reception, avec son comptoir rouge et le tapis RE/MAX,
    # dit tout de suite de quel bureau il s agit.
    apercu(c1, lg, os.path.join(APERCUS, "apercu-couverture-1.jpg"))
    print("ok")
