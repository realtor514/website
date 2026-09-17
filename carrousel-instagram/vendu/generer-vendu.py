# -*- coding: utf-8 -*-
"""Reels VENDU. Le meme montage que les reels d inscription, sans le texte
de vente, avec le resultat obtenu pour les vendeurs a la place.

    python "carrousel-instagram/vendu/generer-vendu.py"              tous
    python "carrousel-instagram/vendu/generer-vendu.py" hilaire      un seul

Ce qui change par rapport au reel d inscription:

- la pastille NOUVEAUTE devient une pastille rouge VENDU, presente du premier
  au dernier plan
- le prix demande disparait: a sa place, le delai de vente
- les noms de pieces disparaissent. A leur place, une phrase courte un plan sur
  deux, qui raconte le resultat plutot que la maison. Un reel de resultat n est
  pas une visite, c est une preuve
- l ecran des travaux devient l ecran du resultat
- l appel a l action passe de "planifiez votre visite" a l evaluation
  gratuite: la personne qui regarde un VENDU est un vendeur potentiel

Les mouvements de camera, les durees et le moteur de rendu sont ceux de
`reels/moteur.py`.
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "reels"))

import moteur                                                  # noqa: E402
from moteur import (ClipPhoto, ClipCadre, ClipCarte, ClipOutro,  # noqa: E402
                    W, H, MARGE, HAUT, NAVY, NAVY_SOFT, RED, WHITE, CREAM,
                    INK, GREY, LINE, degrade, logo, logo_w, icon, inter,
                    playfair, tracked, tw, wrap, para, rendre)
from PIL import Image, ImageDraw                               # noqa: E402

STH = os.path.join(ROOT, "static", "images", "listings",
                   "28-rue-st-hilaire-longueuil")

DUREE_PLAN = 2.4
DUREE_PHRASE = 2.9                      # un plan qui porte une phrase, a lire
DUREE_ACCROCHE = 4.6
DUREE_CARTE = 5.6
DUREE_OUTRO = 5.0


PROPRIETES = [
    # ------------------------------------------------ 28, rue St-Hilaire
    dict(
        slug="28-rue-st-hilaire-longueuil",
        titre1="28, rue", titre2="St-Hilaire",
        secteur="Vieux-Longueuil", centris="26368231",
        # le resultat obtenu. C est tout le propos du reel.
        delai="28 jours",
        # les espaces de 20 000 $ sont insecables (U+00A0): le calibrage ne
        # doit jamais couper entre 20 et 000, ni laisser le $ tout seul au
        # debut de la ligne suivante. Meme chose pour 22 152 pi² plus bas.
        accroche="Vendu en 28 jours, près de 20 000 $ de plus que "
                 "le prix attendu par les vendeurs.",
        # la phrase d ouverture passe dans un panneau borde de pointilles:
        # c est le resultat, il doit frapper avant l adresse
        accroche_encadree=True,
        resultat=dict(
            eyebrow="LE RÉSULTAT",
            titre="Vendu en 28 jours",
            points=["Près de 20 000 $ de plus que le prix attendu "
                    "par les vendeurs",
                    "Selon les conditions souhaitées par les vendeurs",
                    "Merci à nos vendeurs pour leur confiance"],
            photo=os.path.join(STH, "04.jpg"), fy=0.45),
        ouverture=dict(photo=os.path.join(STH, "03.jpg"), mouvement="arc",
                       fy=0.42),
        # (photo, mouvement, fx, fy, phrase). None: le plan reste muet, et
        # c est voulu. Une phrase sur deux plans laisse respirer les images
        # et rend la suivante plus forte. Le \n coupe la phrase la ou la
        # chute doit tomber.
        plans=[
            (os.path.join(STH, "06.jpg"), "zoom", 0.50, 0.50,
             "Quatre semaines.\nPas quatre mois."),
            (os.path.join(STH, "07.jpg"), "droite", 0.50, 0.50, None),
            (os.path.join(STH, "09.jpg"), "gauche", 0.45, 0.50,
             "Le prix espéré par\nles vendeurs? Dépassé."),
            (os.path.join(STH, "12.jpg"), "zoom", 0.50, 0.50, None),
            (os.path.join(STH, "17.jpg"), "droite", 0.50, 0.50,
             "Près de 20 000 $\nde plus que prévu."),
            (os.path.join(STH, "23.jpg"), "zoom", 0.50, 0.50, None),
            (os.path.join(STH, "24.jpg"), "arc_inverse", 0.50, 0.50,
             "Et aux conditions\nqu'ils voulaient."),
        ],
        cadres=[
            (os.path.join(STH, "25.jpg"), None, 0.5,
             "Pas juste vendu.\nBien vendu."),
        ],
    ),

    # ------------------------------------- 35, terrasse Jacques-Leonard
    # Chiffres de vente a fournir: delai et ecart avec le prix attendu.
    # Tant que `resultat` vaut None, le reel n est pas fabrique.
    dict(
        slug="35-terrasse-jacques-leonard",
        titre1="35, terrasse", titre2="Jacques-Léonard",
        secteur="Rivière-des-Prairies, Montréal", centris="15815581",
        delai=None, accroche=None, resultat=None,
        ouverture=dict(photo="0-façade.png", mouvement="arc", fx=0.60,
                       fy=0.45),
        plans=[
            ("2-salon-rdc.png", "zoom", 0.50, 0.50, None),
            ("3-salle à manger- rdc.png", "droite", 0.50, 0.50, None),
            ("4-cuisine- RDC.png", "gauche", 0.45, 0.50, None),
            ("5-chambre à coucher principale- 2ème étage.jpg", "zoom",
             0.50, 0.50, None),
            ("11-Salon sous sol.jpg", "droite", 0.50, 0.50, None),
            ("14-deck extérieur.png", "arc_inverse", 0.50, 0.50, None),
        ],
        cadres=[
            ("15-backyard.png", None, 0.5, None),
        ],
    ),

    # --------------------------------- 4071, rang Saint-Hyacinthe, Mirabel
    dict(
        slug="4071-rang-saint-hyacinthe-mirabel",
        titre1="4071, rang", titre2="Saint-Hyacinthe",
        secteur="Saint-Hermas, Mirabel", centris="26269222",
        delai="22 jours",
        accroche="Vendu en 22 jours, à un prix qui dépasse les attentes "
                 "des vendeurs.",
        resultat=dict(
            eyebrow="LE RÉSULTAT",
            titre="Vendu en 22 jours",
            points=["Un prix de vente qui dépasse les attentes "
                    "des vendeurs",
                    "Une maison de 1935 avec sa grange, sur 22 152 pi²",
                    "Merci à nos vendeurs pour leur confiance"],
            photo="25-Vue exterieure 2.png", fy=0.55),
        ouverture=dict(photo="01-Facade principale.png", mouvement="arc",
                       fy=0.52),
        plans=[
            ("06-Cuisine - RDC.png", "zoom", 0.42, 0.50,
             "Vingt-deux jours.\nPas six mois."),
            ("04-Salon - RDC.png", "droite", 0.50, 0.50, None),
            ("11-Escalier vers le 2e etage - RDC.png", "gauche", 0.36, 0.50,
             "Une maison de 1935\nqui n'a pas attendu."),
            ("08-Chambre principale - RDC.png", "zoom", 0.50, 0.50,
             "Un prix qui dépasse\nles attentes des vendeurs."),
            ("13-Deuxieme cuisine - 2e etage.png", "droite", 0.44, 0.50, None),
            ("28-Galerie - vue vers la rue.png", "arc_inverse", 0.50, 0.50,
             "Plus cher que prévu.\nPlus vite que prévu."),
        ],
        cadres=[
            ("23-Vue de la rue.png", None, 0.5, None),
            ("19-Grange - vue exterieure.png", None, 0.5,
             "Pas juste vendu.\nBien vendu."),
        ],
    ),
]


# ---------------------------------------------------------------- pastille
def _largeur_pastille(taille, track):
    d = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    return int(tw(d, "VENDU", inter(taille, 800), track) + 64)


def pastille(canvas, xy, hauteur=58, taille=25, track=5):
    """Pastille rouge VENDU. Le seul mot qui doit rester lisible a 100 pour
    cent de vitesse de defilement."""
    d = ImageDraw.Draw(canvas)
    lg = _largeur_pastille(taille, track)
    d.rounded_rectangle([xy[0], xy[1], xy[0] + lg, xy[1] + hauteur], 6,
                        fill=RED + (255,))
    tracked(d, (xy[0] + 32, xy[1] + (hauteur - taille) / 2 - 3), "VENDU",
            inter(taille, 800), WHITE, track)
    return lg


# ---------------------------------------------------------------- habillage
def cadre_pointille(d, box, couleur, tiret=20, trou=13, ep=4):
    """Cadre en pointilles.

    Le pas est recalcule sur chaque cote pour que le premier et le dernier
    tiret tombent pile dans les coins: un pointille qui s arrete a trois
    pixels du coin se voit tout de suite.
    """
    x0, y0, x1, y1 = box

    def cote(fixe, debut, fin, horizontal):
        long = fin - debut
        n = max(2, int(round(long / (tiret + trou))))
        pas = long / n
        lg = pas * tiret / (tiret + trou)
        for i in range(n):
            a = debut + i * pas
            if horizontal:
                d.rectangle([a, fixe, a + lg, fixe + ep - 1], fill=couleur)
            else:
                d.rectangle([fixe, a, fixe + ep - 1, a + lg], fill=couleur)

    cote(y0, x0, x1, True)
    cote(y1 - ep, x0, x1, True)
    cote(x0, y0, y1, False)
    cote(x1 - ep, y0, y1, False)


def encadre_accroche(c, texte):
    """La phrase d ouverture, sur un panneau navy borde de pointilles.

    C est la premiere chose que l oeil attrape, avant meme l adresse. Le
    resultat doit se lire dans les trois premieres secondes, sinon le reel
    est regarde comme une annonce de plus et le pouce continue.
    """
    f = inter(52, 800)
    pad, interligne = 36, 66
    d = ImageDraw.Draw(c)
    lignes = wrap(d, texte, f, W - 2 * MARGE - 2 * pad)
    y0 = HAUT + 126
    h = len(lignes) * interligne + 2 * pad - 14
    c.alpha_composite(Image.new("RGBA", (W - 2 * MARGE, h), NAVY + (132,)),
                      (MARGE, y0))
    cadre_pointille(d, (MARGE, y0, W - MARGE, y0 + h), (255, 255, 255, 240))
    y = y0 + pad - 8
    for ln in lignes:
        d.text((MARGE + pad, y), ln, font=f, fill=WHITE)
        y += interligne


def habillage_ouverture(prop):
    """Premiere seconde: logo, le resultat en clair, l adresse, le delai."""
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(c).rectangle([0, 0, W, 600], fill=NAVY + (148,))
    degrade(c, 600, 820, 148, haut=True)
    degrade(c, 880, H, 238)
    d = ImageDraw.Draw(c)

    logo(c, 96, (MARGE, HAUT), white=True)
    if prop.get("accroche_encadree"):
        encadre_accroche(c, prop["accroche"])
    else:
        y = HAUT + 152
        f = inter(46, 800)
        for ln in wrap(d, prop["accroche"], f, W - 2 * MARGE - 40):
            d.text((MARGE, y), ln, font=f, fill=WHITE)
            y += 60

    y = 1006
    pastille(c, (MARGE, y))

    y += 92
    d.text((MARGE, y), prop["titre1"], font=playfair(88, 700), fill=WHITE)
    d.text((MARGE, y + 104), prop["titre2"], font=playfair(88, 700), fill=WHITE)
    y += 232
    d.text((MARGE, y), prop["secteur"], font=inter(34, 400),
           fill=(255, 255, 255, 224))
    y += 66
    d.line([MARGE, y, W - MARGE, y], fill=(255, 255, 255, 92), width=2)
    y += 26
    tracked(d, (MARGE, y), "VENDU EN", inter(24, 800), (255, 255, 255, 190), 5)
    d.text((MARGE, y + 34), prop["delai"], font=playfair(70, 800), fill=WHITE)
    tracked(d, (W - MARGE, y + 62), "CENTRIS " + prop["centris"],
            inter(23, 600), (255, 255, 255, 180), 4, "r")
    return c


def habillage_fixe():
    """Ce qui ne bouge jamais pendant la visite: le logo et la pastille.

    Ce calque n est pas dans `etapes`: il est peint sous les phrases, a chaque
    image, sans fondu. C est ce qui permet aux phrases d entrer et de sortir
    sans que la mention VENDU clignote avec elles.
    """
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    degrade(c, 0, 420, 130, haut=True)
    logo(c, 82, (MARGE, HAUT), white=True, alpha=225)
    pastille(c, (W - MARGE - _largeur_pastille(25, 5), HAUT + 12))
    return c


def habillage_phrase(phrase):
    """Une phrase courte en bas de l ecran, calee sur le bas de la zone sure.

    Le `\\n` d une phrase est une coupure voulue: une chute en deux temps se
    lit mieux quand la deuxieme ligne commence ou l auteur l a decide, et non
    la ou le dernier mot ne rentrait plus. Chaque morceau est quand meme
    repasse au calibrage, au cas ou il deborderait.

    Le bloc est ancre en bas: le point final tombe toujours a la meme hauteur
    d un plan a l autre, que la phrase prenne une ligne ou trois.
    """
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # voile plus soutenu que celui des reels d inscription: une cuisine
    # blanche plein cadre avalerait du texte blanc pose dessus
    degrade(c, 1040, H, 244)
    d = ImageDraw.Draw(c)
    f = playfair(60, 700)
    lignes = []
    for bout in phrase.split("\n"):
        lignes += wrap(d, bout, f, W - 2 * MARGE)
    y = 1566 - len(lignes) * 78
    d.rectangle([MARGE, y - 44, MARGE + 76, y - 38], fill=RED + (255,))
    for ln in lignes:
        d.text((MARGE, y), ln, font=f, fill=WHITE)
        y += 78
    return c


def _playfair_qui_tient(d, texte, maxw, base=72, mini=52):
    """Reduit le corps jusqu a ce que la ligne tienne dans la largeur."""
    taille = base
    while taille > mini and d.textlength(texte, font=playfair(taille, 700)) > maxw:
        taille -= 2
    return playfair(taille, 700)


class _AvecPastille:
    """Peint un calque permanent avant le calque de texte.

    `fixe` est prepare une fois pour tout le reel, en RGB et en alpha
    separes: une conversion par image sur 1080 x 1920 coute plus cher que
    tout le reste du plan.
    """

    fixe_rgb = fixe_a = None

    def image(self, i):
        t = i / moteur.FPS
        im = self.fond(t)
        if self.fixe_rgb is not None:
            im.paste(self.fixe_rgb, (0, 0), self.fixe_a)
        c = self.calque(t)
        if c is not None:
            im.paste(c.convert("RGB"), (0, 0), c.getchannel("A"))
        return im


class PlanVendu(_AvecPastille, ClipPhoto):
    pass


class CadreVendu(_AvecPastille, ClipCadre):
    pass


class ClipOutroVendu(ClipOutro):
    """Carte de contact d un reel VENDU: la preuve vient d etre montree, on
    demande le prochain mandat plutot qu une visite."""

    def preparer(self):
        p = self.prop
        c = Image.new("RGBA", (W, H), CREAM + (255,))
        d = ImageDraw.Draw(c)
        d.rectangle([0, 0, W, 14], fill=NAVY + (255,))

        s, gap = 268, 64
        x0 = (W - (2 * s + gap)) // 2
        self._rond(c, os.path.join(moteur.SOURCES, "rovena-pistoli.jpg"),
                   (x0, 330), s)
        self._rond(c, self._studio(os.path.join(moteur.SOURCES,
                                                "georges-matar-decoupe.png")),
                   (x0 + s + gap, 330), s)

        for cx, nom, titre in [
                (x0 + s // 2, "ROVENA PISTOLI",
                 "Courtier immobilier résidentiel et commercial"),
                (x0 + s + gap + s // 2, "GEORGES MATAR",
                 "Courtier immobilier résidentiel")]:
            d.text((cx, 632), nom, font=inter(28, 800), fill=NAVY, anchor="ma")
            para(d, (cx, 672), titre, inter(20, 400), GREY, s + 44, 28, "c")

        lignes = ["Votre propriété mérite", "le même résultat"]
        # un seul corps pour les deux lignes, celui que la plus longue permet
        f = _playfair_qui_tient(d, max(lignes, key=len), W - 2 * MARGE)
        for i, ligne in enumerate(lignes):
            d.text((W // 2, 772 + i * 86), ligne, font=f, fill=NAVY,
                   anchor="ma")

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
        d.text((W // 2, y + bh / 2 - 18), "Évaluation gratuite",
               font=inter(37, 800), fill=WHITE, anchor="mm")
        tracked(d, (W // 2, y + bh / 2 + 8), "ET SANS ENGAGEMENT",
                inter(23, 700), NAVY_SOFT, 4, "c")

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
                "VENDU EN %s   ·   %s" % (p["delai"].upper(),
                                          p["secteur"].upper()),
                inter(23, 600), GREY, 4, "c")
        self.plaque = c.convert("RGB")


# ---------------------------------------------------------------- montage
def monter(prop):
    """Ouverture, visite avec ses phrases, ecran du resultat, contact."""
    o = prop["ouverture"]
    ouverture = ClipPhoto(o["photo"], DUREE_ACCROCHE, o.get("mouvement", "arc"),
                          o.get("fx", 0.5), o.get("fy", 0.5))
    ouverture.etapes.append((0.12, habillage_ouverture(prop)))

    fixe = habillage_fixe()
    fixe_rgb, fixe_a = fixe.convert("RGB"), fixe.getchannel("A")

    def poser(cl, phrase):
        """Calque permanent dessous, phrase dessus.

        La phrase quitte l ecran avant le changement de plan: deux phrases
        superposees pendant un fondu, ca se lit mal. Le logo et la pastille,
        eux, ne partent jamais.
        """
        cl.fixe_rgb, cl.fixe_a = fixe_rgb, fixe_a
        if phrase:
            cl.etapes.append((0.06, habillage_phrase(phrase)))
        return cl

    plans = []
    for photo, mvt, fx, fy, phrase in prop["plans"]:
        duree = DUREE_PHRASE if phrase else DUREE_PLAN
        plans.append(poser(PlanVendu(photo, duree, mvt, fx, fy), phrase))

    larges = []
    for photo, crop, fy, phrase in prop["cadres"]:
        duree = DUREE_PHRASE if phrase else DUREE_PLAN
        larges.append(poser(CadreVendu(photo, duree, crop, fy), phrase))

    # une vue large tous les trois plans, la derniere juste avant le resultat
    suite, i = [], 0
    for k, cl in enumerate(plans):
        suite.append(cl)
        if i < len(larges) - 1 and (k + 1) % 3 == 0:
            suite.append(larges[i])
            i += 1
    while i < len(larges):
        suite.append(larges[i])
        i += 1

    r = prop["resultat"]
    carte = ClipCarte(r["photo"], DUREE_CARTE, r["eyebrow"], r["titre"],
                      r["points"], r.get("crop"), r.get("fy", 0.5))
    return [ouverture] + suite + [carte, ClipOutroVendu(DUREE_OUTRO, prop)]


def main():
    filtre = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    for prop in PROPRIETES:
        if filtre and filtre not in prop["slug"]:
            continue
        if not prop["resultat"]:
            print("Ignore ->", prop["slug"],
                  ": delai de vente et ecart de prix a fournir")
            continue
        dossier = os.path.join(HERE, prop["slug"])
        os.makedirs(dossier, exist_ok=True)
        mp4 = os.path.join(dossier, "reel-vendu.mp4")
        jpg = os.path.join(dossier, "couverture.jpg")
        print("Reel VENDU ->", prop["slug"])
        t0 = time.time()
        duree = rendre(monter(prop), mp4, cover=jpg)
        print("   %.1f s de video, rendu en %.0f s" % (duree, time.time() - t0))
        print("   ", mp4)


if __name__ == "__main__":
    main()
