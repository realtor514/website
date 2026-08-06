# Carrousels Instagram

Slides 1080 x 1350 px (format 4:5, celui qui occupe le plus d espace dans le
fil Instagram). Identite RE/MAX: rouge, blanc, bleu, echantillonnes directement
dans le fichier `static/images/remax-ducartier-blanc.png`.

## 28, rue St-Hilaire, Longueuil (Centris 26368231)

Publier dans cet ordre exact. Instagram conserve l ordre d ajout des fichiers.

| # | Fichier | Contenu |
|---|---------|---------|
| 1 | `01-couverture.jpg` | Facade, badge A VENDRE, adresse, prix |
| 2 | `02-caracteristiques.jpg` | Salon, 6 caracteristiques, bande de prix |
| 3 | `03-cuisine.jpg` | Cuisine, 4 points |
| 4 | `04-points-forts.jpg` | Cour, 6 travaux deja realises |
| 5 | `05-details.jpg` | Chambre, salle de bain, terrasse |
| 6 | `06-emplacement.jpg` | Rue, 4 elements de proximite |
| 7 | `07-coup-de-coeur.jpg` | Salle a manger, Imaginez-vous vivre ici |
| 8 | `08-contact.jpg` | Portrait, coordonnees, appel a l action |

### Legende a copier-coller

```
NOUVELLE INSCRIPTION | 28, rue St-Hilaire, Vieux-Longueuil | 499 000 $

Maison à deux étages sur un terrain clôturé de près de 4 000 pi², dans un
secteur recherché du Vieux-Longueuil. Proximité des services, des écoles et
des accès vers le pont Jacques-Cartier.

Ce qui est déjà fait, et qui retire une bonne partie de l'incertitude:
Toiture refaite en 2014
Plomberie et électricité mises à jour en 2014
Plancher du rez-de-chaussée sablé en 2026
Piscine hors terre installée en 2023
Terrasse en bois, cabanon et borne de recharge pour véhicule électrique

2 chambres | 1 salle de bain + 1 salle d'eau | 2 stationnements
Terrain de 371 m² | Construite en 1949
Évaluation municipale 2026: 437 100 $
Taxes municipales: 2 899 $ | Taxes scolaires: 334 $

Glissez jusqu'à la fin pour les détails et pour planifier une visite.

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC.
438-372-0102 | georgesmatar.ca
Centris 26368231
```

### Mots-cles

```
#vieuxlongueuil #longueuil #rivesud #montreal #maisonavendre #avendre
#immobilierquebec #courtierimmobilier #remax #remaxducartier #centris
#maisonquebec #proprietearendre #immobilier #premiereMaison
```

### Notes avant publication

- Le premier commentaire est le meilleur endroit pour le lien vers la fiche.
  Instagram ne rend pas les liens cliquables dans la legende.
- La fiche officielle indique un co-courtage. Verifier si la mention de la
  courtiere collaboratrice doit apparaitre sur la slide 8.
- Quand la propriete se vend: changer le badge de la slide 1 pour VENDU et
  regenerer. Une publication VENDU performe mieux qu une suppression.

## Regenerer

```
python carrousel-instagram/generer-carrousel.py
```

Le script lit les photos dans `static/images/listings/<slug>/` et ecrit les
slides dans `carrousel-instagram/<slug>/`. Les anciens JPG du dossier sont
effaces a chaque execution.

Pour une nouvelle propriete: changer `SLUG` en haut du fichier, puis ajuster
les textes et les numeros de photo dans les fonctions `slide1` a `slide8`.
Le parametre `fy` de `photo()` deplace le recadrage vertical, entre 0 (haut de
la photo) et 1 (bas).

Polices: Playfair Display et Inter, les memes que le site web, sous licence
SIL Open Font License. Elles sont dans `fonts/`, aucune installation requise.
