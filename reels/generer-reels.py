# -*- coding: utf-8 -*-
"""Reels Instagram des inscriptions. Un fichier MP4 vertical par propriete.

    python reels/generer-reels.py              tous les reels
    python reels/generer-reels.py mirabel      un seul, par bout de nom

Le montage est toujours le meme, parce qu il fonctionne: une accroche qui
retient dans les trois premieres secondes, une visite rythmee ou chaque plan
est nomme, un ecran de points forts, puis l appel a l action. Les photos et
les textes changent, la structure non.

Mouvements possibles pour un plan plein ecran: zoom, recul, droite, gauche,
descente, montee, arc, arc_inverse. Un plan en cadre garde la photo entiere
sur un fond flou: a reserver aux vues larges.
"""
import os
import sys
import time

import moteur
from moteur import (ClipPhoto, ClipCadre, ClipCarte, ClipOutro,
                    habillage_accroche, habillage_plan, rendre)

HERE = os.path.dirname(os.path.abspath(__file__))
STH = os.path.join(moteur.ROOT, "static", "images", "listings",
                   "28-rue-st-hilaire-longueuil")

# le montage des trois photos du domaine Bonneville: on y preleve deux zones
PARC = (0.0, 0.0, 1.0, 0.552)
AERIEN = (0.0, 0.567, 0.489, 1.0)

DUREE_PLAN = 2.4
DUREE_ACCROCHE = 4.4
DUREE_CARTE = 4.8
DUREE_OUTRO = 5.0


PROPRIETES = [
    # ------------------------------------------------ 28, rue St-Hilaire
    dict(
        slug="28-rue-st-hilaire-longueuil",
        titre1="28, rue", titre2="St-Hilaire",
        secteur="Vieux-Longueuil", prix="499 000 $", centris="26368231",
        accroche="Toiture, plomberie et électricité déjà refaites. "
                 "Terrain clôturé de près de 4 000 pi².",
        ouverture=dict(photo=os.path.join(STH, "03.jpg"), mouvement="arc",
                       fy=0.42),
        plans=[
            (os.path.join(STH, "06.jpg"), "LE REZ-DE-CHAUSSÉE", "Le salon",
             "zoom", 0.50, 0.50),
            (os.path.join(STH, "07.jpg"), "LE REZ-DE-CHAUSSÉE",
             "La salle à manger", "droite", 0.50, 0.50),
            (os.path.join(STH, "09.jpg"), "LE REZ-DE-CHAUSSÉE", "La cuisine",
             "gauche", 0.45, 0.50),
            (os.path.join(STH, "12.jpg"), "L'ÉTAGE", "La chambre principale",
             "zoom", 0.50, 0.50),
            (os.path.join(STH, "13.jpg"), "L'ÉTAGE", "La deuxième chambre",
             "descente", 0.50, 0.45),
            (os.path.join(STH, "17.jpg"), "LE SOUS-SOL",
             "Aménagé, avec salle de bain", "droite", 0.50, 0.50),
            (os.path.join(STH, "23.jpg"), "À L'ARRIÈRE", "La véranda",
             "zoom", 0.50, 0.50),
            (os.path.join(STH, "24.jpg"), "À L'ARRIÈRE",
             "La terrasse en bois", "arc_inverse", 0.50, 0.50),
        ],
        cadres=[
            (os.path.join(STH, "25.jpg"), "LE TERRAIN",
             "Clôturé, près de 4 000 pi²", None, 0.5),
        ],
        carte=dict(photo=os.path.join(STH, "04.jpg"), eyebrow="DÉJÀ FAIT",
                   titre="Tranquillité d'esprit", fy=0.45,
                   points=["Toiture refaite en 2014",
                           "Plomberie et électricité 2014",
                           "Plancher du rez-de-chaussée sablé en 2026",
                           "Piscine hors terre 2023",
                           "Borne de recharge pour véhicule électrique"]),
    ),

    # ------------------------------------- 35, terrasse Jacques-Leonard
    dict(
        slug="35-terrasse-jacques-leonard",
        titre1="35, terrasse", titre2="Jacques-Léonard",
        secteur="Rivière-des-Prairies, Montréal", prix="380 000 $",
        centris="15815581",
        accroche="Piscine, parc et centre communautaire privés. "
                 "Une maison de ville au Domaine Bonneville.",
        ouverture=dict(photo="0-façade.png", mouvement="arc", fx=0.60,
                       fy=0.45),
        plans=[
            ("2-salon-rdc.png", "LE REZ-DE-CHAUSSÉE", "Le salon", "zoom",
             0.50, 0.50),
            ("3-salle à manger- rdc.png", "LE REZ-DE-CHAUSSÉE",
             "La salle à manger", "droite", 0.50, 0.50),
            ("4-cuisine- RDC.png", "LE REZ-DE-CHAUSSÉE", "La cuisine",
             "gauche", 0.45, 0.50),
            ("5-chambre à coucher principale- 2ème étage.jpg", "L'ÉTAGE",
             "La chambre principale", "zoom", 0.50, 0.50),
            ("8-salle de bain 2ème étage.jpg", "L'ÉTAGE", "La salle de bain",
             "descente", 0.45, 0.50),
            ("11-Salon sous sol.jpg", "LE SOUS-SOL",
             "Complet, avec cuisine et chambre", "droite", 0.50, 0.50),
            ("14-deck extérieur.png", "À L'ARRIÈRE", "La terrasse couverte",
             "arc_inverse", 0.50, 0.50),
        ],
        cadres=[
            ("15-backyard.png", "À L'ARRIÈRE", "La cour privée et clôturée",
             None, 0.5),
            ("16-parc et piscine privés du domaine.png", "LE DOMAINE",
             "Le parc, réservé aux résidents", PARC, 0.5),
        ],
        carte=dict(photo="16-parc et piscine privés du domaine.png",
                   crop=AERIEN, eyebrow="LE DOMAINE BONNEVILLE",
                   titre="Tout un milieu de vie",
                   points=["Piscine et pataugeoire privées",
                           "Parc, aire de jeux et centre communautaire",
                           "Charges communes: toiture et maçonnerie",
                           "Balcons, déneigement et fonds de prévoyance"]),
    ),

    # --------------------------------- 4071, rang Saint-Hyacinthe, Mirabel
    dict(
        slug="4071-rang-saint-hyacinthe-mirabel",
        titre1="4071, rang", titre2="Saint-Hyacinthe",
        secteur="Saint-Hermas, Mirabel", prix="449 000 $",
        centris="26269222",
        accroche="22 152 pi² de terrain, une grange de bois "
                 "et pas un voisin en face.",
        ouverture=dict(photo="01-Facade principale.png", mouvement="arc",
                       fy=0.52),
        plans=[
            ("06-Cuisine - RDC.png", "LE REZ-DE-CHAUSSÉE",
             "La cuisine, 14 x 13 pieds", "zoom", 0.42, 0.50),
            ("04-Salon - RDC.png", "LE REZ-DE-CHAUSSÉE", "Le salon",
             "droite", 0.50, 0.50),
            ("11-Escalier vers le 2e etage - RDC.png", "LE REZ-DE-CHAUSSÉE",
             "Le poêle à combustion lente", "gauche", 0.36, 0.50),
            ("08-Chambre principale - RDC.png", "LE REZ-DE-CHAUSSÉE",
             "La chambre principale", "zoom", 0.50, 0.50),
            ("13-Deuxieme cuisine - 2e etage.png", "L'ÉTAGE",
             "Une seconde cuisine", "droite", 0.44, 0.50),
            ("17-Chambre 4 - 2e etage.png", "L'ÉTAGE", "Une chambre en pin",
             "descente", 0.50, 0.50),
            ("28-Galerie - vue vers la rue.png", "À L'EXTÉRIEUR",
             "La galerie, face aux champs", "arc_inverse", 0.50, 0.50),
        ],
        cadres=[
            ("23-Vue de la rue.png", "SAINT-HERMAS, MIRABEL",
             "Un rang bordé de champs", None, 0.5),
            ("19-Grange - vue exterieure.png", "LE TERRAIN",
             "La grange, sur deux étages", None, 0.5),
        ],
        carte=dict(photo="25-Vue exterieure 2.png", eyebrow="DÉJÀ FAIT",
                   titre="Tranquillité d'esprit", fy=0.55,
                   points=["Revêtement de vinyle refait en 2024",
                           "Thermopompe centrale Goodman de 2022",
                           "Génératrice neuve installée en 2025",
                           "Panneau électrique de 200 ampères",
                           "Puits et fosse septique récents"]),
    ),
]


def monter(prop):
    """Construit la suite des plans. Les vues larges s intercalent entre les
    plans pleine page pour casser la monotonie du cadrage serre."""
    o = prop["ouverture"]
    ouverture = ClipPhoto(o["photo"], DUREE_ACCROCHE, o.get("mouvement", "arc"),
                          o.get("fx", 0.5), o.get("fy", 0.5))
    ouverture.etapes.append((0.12, habillage_accroche(prop, prop["accroche"])))

    plans = []
    for photo, eyebrow, titre, mvt, fx, fy in prop["plans"]:
        cl = ClipPhoto(photo, DUREE_PLAN, mvt, fx, fy)
        cl.etapes.append((0.06, habillage_plan(eyebrow, titre)))
        plans.append(cl)

    larges = []
    for photo, eyebrow, titre, crop, fy in prop["cadres"]:
        cl = ClipCadre(photo, DUREE_PLAN, crop, fy)
        cl.etapes.append((0.06, habillage_plan(eyebrow, titre)))
        larges.append(cl)

    # une vue large environ tous les trois plans, la derniere juste avant
    # l ecran des points forts
    suite, i = [], 0
    for k, cl in enumerate(plans):
        suite.append(cl)
        if i < len(larges) - 1 and (k + 1) % 3 == 0:
            suite.append(larges[i])
            i += 1
    while i < len(larges):
        suite.append(larges[i])
        i += 1

    c = prop["carte"]
    carte = ClipCarte(c["photo"], DUREE_CARTE, c["eyebrow"], c["titre"],
                      c["points"], c.get("crop"), c.get("fy", 0.5))
    return [ouverture] + suite + [carte, ClipOutro(DUREE_OUTRO, prop)]


def main():
    filtre = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    for prop in PROPRIETES:
        if filtre and filtre not in prop["slug"]:
            continue
        dossier = os.path.join(HERE, prop["slug"])
        os.makedirs(dossier, exist_ok=True)
        mp4 = os.path.join(dossier, "reel.mp4")
        jpg = os.path.join(dossier, "couverture.jpg")
        print("Reel ->", prop["slug"])
        t0 = time.time()
        duree = rendre(monter(prop), mp4, cover=jpg)
        print("   %.1f s de video, rendu en %.0f s" % (duree, time.time() - t0))
        print("   ", mp4)


if __name__ == "__main__":
    main()
