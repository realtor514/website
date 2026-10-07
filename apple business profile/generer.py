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


def banniere(chemin, W=2400, H=1600):
    """Couverture dans l esprit de draft/aa1.jpg, demandee par Georges:
    panneau navy avec le portrait, colonne creme avec le nom, le titre et
    les coordonnees, logo de l agence, salon en fondu a droite.

    ATTENTION: Apple demande une couverture sans texte ni montage. Celle-ci
    risque d etre refusee; couverture-1-reception.jpg reste le plan B.

    Format 1,5:1 (Wallet). Plans recadre en 2,5:1 au centre: tout le
    contenu utile tient entre y = 320 et y = 1280."""
    c = Image.new("RGBA", (W, H), CREME + (255,))
    haut, bas = 320, 1280

    # Salon a droite, en fondu vers le creme.
    salon = Image.open(os.path.join(ROOT, "facebook", "sources", "interieur-salon.jpg")).convert("RGB")
    sw = 560
    sh = H
    sx = round(salon.width * 0.58)  # cadrage sur la baie vitree et le canape
    ratio = sh / salon.height
    salon = salon.resize((round(salon.width * ratio), sh), Image.LANCZOS)
    sx = min(max(0, round(sx * ratio) - sw // 2), salon.width - sw)
    salon = salon.crop((sx, 0, sx + sw, sh)).convert("RGBA")
    fondu = Image.new("L", (sw, 1))
    for x in range(sw):
        fondu.putpixel((x, 0), int(255 * min(1.0, max(0.0, (x - 40) / 360)) ** 1.4))
    salon.putalpha(fondu.resize((sw, sh)))
    c.alpha_composite(salon, (W - sw, 0))

    # Panneau navy a gauche.
    px = 900
    ImageDraw.Draw(c).rectangle((0, 0, px, H), fill=NAVY + (255,))

    # Portrait detoure, pied en bas, tete dans la bande que Plans conserve.
    p = Image.open(os.path.join(HERE, "draft", "Georges Matar sans mains_sans arriere plan.png")).convert("RGBA")
    p = p.crop(p.getchannel("A").getbbox())
    ph = H - 420
    pw = round(p.width * ph / p.height)
    p = p.resize((pw, ph), Image.LANCZOS)
    x0 = px + 110 - pw  # le visage dans le panneau, l epaule droite deborde a peine
    ombre = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ombre.paste((0, 4, 18, 150), (x0 + 22, H - ph + 18), p)
    from PIL import ImageFilter
    c.alpha_composite(ombre.filter(ImageFilter.GaussianBlur(30)))
    c.alpha_composite(p, (x0, H - ph))

    d = ImageDraw.Draw(c)
    colonne = (px + 110 + (W - sw + 40)) / 2  # centre de la colonne creme

    def centre(y, s, f, track=0, fill=NAVY):
        larg = [d.textlength(ch, font=f) for ch in s]
        tot = sum(larg) + track * (len(s) - 1)
        x = colonne - tot / 2
        for ch, w in zip(s, larg):
            d.text((x, y), ch, font=f, fill=fill)
            x += w + track

    centre(haut + 50, "Georges", playfair(150, 600))
    centre(haut + 235, "MATAR", playfair(128, 500), track=34)
    centre(haut + 420, "COURTIER IMMOBILIER RÉSIDENTIEL", inter(33, 500), track=6)
    centre(haut + 495, "(438) 372-0102", inter(58, 500))
    centre(haut + 580, "georges.matar@remax-quebec.com", inter(42, 400))

    # Logo de l agence, en navy comme dans aa1: le noir du fichier officiel
    # devient navy, le ballon garde ses couleurs.
    lg = Image.open(os.path.join(ROOT, "marketing tools by Daniella et Yassine",
                                 "logos", "logo-ducartier-noir2.png")).convert("RGBA")
    lg = lg.crop(lg.getchannel("A").getbbox())
    px_ = lg.load()
    for y in range(lg.height):
        for x in range(lg.width):
            r, g, b, a = px_[x, y]
            if a and max(r, g, b) < 90:
                px_[x, y] = NAVY + (a,)
    lh = 170
    lg = lg.resize((round(lg.width * lh / lg.height), lh), Image.LANCZOS)
    c.alpha_composite(lg, (round(colonne - lg.width / 2), bas - lh - 20))

    c = c.convert("RGB")
    c.save(chemin, quality=92, optimize=True, progressive=True)
    return c


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
    b = banniere(os.path.join(HERE, "couverture-banniere.jpg"))
    apercu(b, lg, os.path.join(APERCUS, "apercu-couverture-banniere.jpg"))
    print("ok")
