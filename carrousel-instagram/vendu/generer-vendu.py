# -*- coding: utf-8 -*-
"""Reels VENDU. Le meme montage que les reels d inscription, sans le texte
de vente, avec le resultat obtenu pour les vendeurs a la place.

    python "carrousel-instagram/vendu/generer-vendu.py"              tous
    python "carrousel-instagram/vendu/generer-vendu.py" hilaire      un seul

Ce qui change par rapport au reel d inscription:

- la pastille NOUVEAUTE devient une pastille rouge VENDU, presente du premier
  au dernier plan
- le prix demande disparait: a sa place, le delai de vente
- les noms de pieces disparaissent. Pendant la visite, l image est nue: il ne
  reste que le logo et la mention VENDU. Un reel de resultat n est pas une
  visite, c est une preuve
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
        accroche="Vendu en 28 jours, près de 20 000 $ de plus que le prix "
                 "attendu par les vendeurs.",
        resultat=dict(
            eyebrow="LE RÉSULTAT",
            titre="Vendu en 28 jours",
            points=["Près de 20 000 $ de plus que le prix attendu "
                    "par les vendeurs",
                    "Selon les conditions souhaitées par les vendeurs",
                    "Merci à nos vendeurs pour leur confiance"],
            photo=os.path.join(STH, "04.jpg"), fy=0.45),
        ouverture=dict(photo=os.path.join(STH, "03.jpg"), mouvement="arc",
                       fy=0.42),
        plans=[
            (os.path.join(STH, "06.jpg"), "zoom", 0.50, 0.50),
            (os.path.join(STH, "07.jpg"), "droite", 0.50, 0.50),
            (os.path.join(STH, "09.jpg"), "gauche", 0.45, 0.50),
            (os.path.join(STH, "12.jpg"), "zoom", 0.50, 0.50),
            (os.path.join(STH, "17.jpg"), "droite", 0.50, 0.50),
            (os.path.join(STH, "23.jpg"), "zoom", 0.50, 0.50),
            (os.path.join(STH, "24.jpg"), "arc_inverse", 0.50, 0.50),
        ],
        cadres=[
            (os.path.join(STH, "25.jpg"), None, 0.5),
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
            ("2-salon-rdc.png", "zoom", 0.50, 0.50),
            ("3-salle à manger- rdc.png", "droite", 0.50, 0.50),
            ("4-cuisine- RDC.png", "gauche", 0.45, 0.50),
            ("5-chambre à coucher principale- 2ème étage.jpg", "zoom",
             0.50, 0.50),
            ("11-Salon sous sol.jpg", "droite", 0.50, 0.50),
            ("14-deck extérieur.png", "arc_inverse", 0.50, 0.50),
        ],
        cadres=[
            ("15-backyard.png", None, 0.5),
        ],
    ),

    # --------------------------------- 4071, rang Saint-Hyacinthe, Mirabel
    # Chiffres de vente a fournir, meme chose.
    dict(
        slug="4071-rang-saint-hyacinthe-mirabel",
        titre1="4071, rang", titre2="Saint-Hyacinthe",
        secteur="Saint-Hermas, Mirabel", centris="26269222",
        delai=None, accroche=None, resultat=None,
        ouverture=dict(photo="01-Facade principale.png", mouvement="arc",
                       fy=0.52),
        plans=[
            ("06-Cuisine - RDC.png", "zoom", 0.42, 0.50),
            ("04-Salon - RDC.png", "droite", 0.50, 0.50),
            ("11-Escalier vers le 2e etage - RDC.png", "gauche", 0.36, 0.50),
            ("08-Chambre principale - RDC.png", "zoom", 0.50, 0.50),
            ("13-Deuxieme cuisine - 2e etage.png", "droite", 0.44, 0.50),
            ("28-Galerie - vue vers la rue.png", "arc_inverse", 0.50, 0.50),
        ],
        cadres=[
            ("23-Vue de la rue.png", None, 0.5),
            ("19-Grange - vue exterieure.png", None, 0.5),
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
def habillage_ouverture(prop):
    """Premiere seconde: logo, le resultat en clair, l adresse, le delai."""
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(c).rectangle([0, 0, W, 600], fill=NAVY + (148,))
    degrade(c, 600, 820, 148, haut=True)
    degrade(c, 880, H, 238)
    d = ImageDraw.Draw(c)

    logo(c, 96, (MARGE, HAUT), white=True)
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


def habillage_muet():
    """Plans de visite: aucune legende. Le logo, la pastille, rien d autre."""
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    degrade(c, 0, 420, 130, haut=True)
    logo(c, 82, (MARGE, HAUT), white=True, alpha=225)
    pastille(c, (W - MARGE - _largeur_pastille(25, 5), HAUT + 12))
    return c


def _playfair_qui_tient(d, texte, maxw, base=72, mini=52):
    """Reduit le corps jusqu a ce que la ligne tienne dans la largeur."""
    taille = base
    while taille > mini and d.textlength(texte, font=playfair(taille, 700)) > maxw:
        taille -= 2
    return playfair(taille, 700)


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
    """Ouverture, visite muette, ecran du resultat, carte de contact."""
    o = prop["ouverture"]
    ouverture = ClipPhoto(o["photo"], DUREE_ACCROCHE, o.get("mouvement", "arc"),
                          o.get("fx", 0.5), o.get("fy", 0.5))
    ouverture.etapes.append((0.12, habillage_ouverture(prop)))

    muet = habillage_muet()

    plans = []
    for photo, mvt, fx, fy in prop["plans"]:
        cl = ClipPhoto(photo, DUREE_PLAN, mvt, fx, fy)
        # apparition datee avant le debut du plan: le logo et la pastille sont
        # deja a pleine opacite a la premiere image, sinon ils pulsent a
        # chaque changement de plan
        cl.etapes.append((-1.0, muet))
        cl.sortie = 0
        plans.append(cl)

    larges = []
    for photo, crop, fy in prop["cadres"]:
        cl = ClipCadre(photo, DUREE_PLAN, crop, fy)
        cl.etapes.append((-1.0, muet))
        cl.sortie = 0
        larges.append(cl)

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
