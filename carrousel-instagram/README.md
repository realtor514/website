# Carrousels Instagram

Slides 1080 x 1350 px (format 4:5, celui qui occupe le plus d espace dans le
fil Instagram). Identite RE/MAX: rouge, blanc, bleu, echantillonnes directement
dans le fichier `static/images/remax-ducartier-blanc.png`.

Un dossier par inscription. Chaque dossier contient ses huit slides, son
generateur et sa legende:

| Inscription | Dossier |
|-------------|---------|
| 28, rue St-Hilaire, Longueuil (Centris 26368231) | `28-rue-st-hilaire-longueuil/`, genere par `generer-carrousel.py` |
| 35, terrasse Jacques-Leonard, Montreal (Centris 15815581) | `35 terrasse jacques leonard/`, avec son propre `generer-carrousel.py` et son `README.md` |
| 4071, rang Saint-Hyacinthe, Mirabel (Centris 26269222) | `4071 rang saint-hyacinthe mirabel/`, avec son propre `generer-carrousel.py` et son `README.md` |

## 28, rue St-Hilaire, Longueuil (Centris 26368231)

Publier dans cet ordre exact. Instagram conserve l ordre d ajout des fichiers.

| # | Fichier | Contenu |
|---|---------|---------|
| 1 | `01-couverture.jpg` | Facade, pastilles A VENDRE et EQUIPE PISTOLI, adresse, prix |
| 2 | `02-caracteristiques.jpg` | Salon, 4 caracteristiques, bande de prix |
| 3 | `03-cuisine.jpg` | Cuisine, 3 points |
| 4 | `04-points-forts.jpg` | Cour, 4 travaux deja realises |
| 5 | `05-details.jpg` | Chambre, salle de bain, terrasse |
| 6 | `06-emplacement.jpg` | Rue, 3 elements de proximite |
| 7 | `07-coup-de-coeur.jpg` | Salle a manger, Imaginez-vous vivre ici |
| 8 | `08-contact.jpg` | Georges Matar et Rovena Pistoli, coordonnees, appel a l action |

### Equipe Pistoli

L inscription vient d un lead obtenu par Rovena Pistoli. Elle est mentionnee
a deux endroits:

- slide 1: pastille EQUIPE PISTOLI a cote de A VENDRE
- slide 8: sa photo, son nom et son titre a cote de ceux de Georges

Les photos de la pancarte prises au telephone ne vont PAS dans le carrousel:
seules les photos professionnelles de Centris sont utilisees.

Titre exact tire de sa fiche RE/MAX DU CARTIER: Courtier immobilier
residentiel et commercial. Entreprise: Rovena Pistoli Immobilier Inc.
Telephone: 514 910-4128. Fiche: remaxducartier.com/fr/courtiers/rovena-pistoli

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

Une inscription de l'Équipe Pistoli.
Georges Matar, courtier immobilier résidentiel
Rovena Pistoli, courtier immobilier résidentiel et commercial
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
- Identifier @ l Equipe Pistoli et Rovena Pistoli dans la publication, en plus
  de la mention dans la legende. Une identification rejoint ses abonnes a elle.
- Seules les coordonnees de Georges paraissent sur la slide 8. Si le telephone
  de Rovena doit y figurer aussi, le dire et je l ajoute.
- Quand la propriete se vend: changer le badge de la slide 1 pour VENDU et
  regenerer. Une publication VENDU performe mieux qu une suppression.

## Dossier sources

`sources/` contient les portraits des courtiers et les photos de chaque
inscription. Les trois generateurs lisent tous dans ce dossier:

| Fichier | Origine | Utilise |
|---------|---------|---------|
| `georges-matar-decoupe.png` | Portrait detoure, repose sur un fond studio par le script | Slide 8 des trois carrousels |
| `rovena-pistoli.jpg` | Portrait officiel, telecharge de sa fiche RE/MAX DU CARTIER | Slide 8 des trois carrousels |
| `pancarte-01.jpg`, `pancarte-02.jpg` | Photos du terrain du 28, rue St-Hilaire | Non |
| `4.png`, `5.png`, `6.png` | Photos du 28, rue St-Hilaire | Slides 1, 3 et 5 de ce carrousel |
| `0-façade.png` a `16-parc et piscine privés du domaine.png` | Photos du 35, terrasse Jacques-Leonard | Carrousel Jacques-Leonard |
| `01-Facade principale.png` a `29-Vue du terrain.png` | Photos du 4071, rang Saint-Hyacinthe | Carrousel Mirabel |

Les deux photos de pancarte sont conservees pour les publications simples
(story, publication unique le jour de l installation), pas pour le carrousel.

Les fichiers `georges-matar-decoupe - Copy.png` et `rovena-pistoli - Copy.jpg`
sont des doublons: aucun script ne les lit.

**Ne pas vider `sources/` en deposant les photos d une nouvelle inscription.**
Les trois generateurs y lisent leurs photos: effacer le contenu casse les
carrousels precedents. Les noms de fichiers des trois inscriptions ne se
marchent pas dessus, tout peut cohabiter dans le meme dossier.

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
