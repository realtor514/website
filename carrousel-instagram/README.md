# Carrousels Instagram

Slides 1080 x 1350 px (format 4:5, celui qui occupe le plus d espace dans le
fil Instagram). Identite RE/MAX: rouge, blanc, bleu, echantillonnes directement
dans le fichier `static/images/remax-ducartier-blanc.png`.

## 28, rue St-Hilaire, Longueuil (Centris 26368231)

Publier dans cet ordre exact. Instagram conserve l ordre d ajout des fichiers.

| # | Fichier | Contenu |
|---|---------|---------|
| 1 | `01-couverture.jpg` | Facade, pastilles A VENDRE et EQUIPE PISTOLI, adresse, prix |
| 2 | `02-caracteristiques.jpg` | Salon, 4 caracteristiques, bande de prix |
| 3 | `03-cuisine.jpg` | Cuisine, 3 points |
| 4 | `04-points-forts.jpg` | Cour, 4 travaux deja realises |
| 5 | `05-details.jpg` | Chambre, salle de bain, terrasse |
| 6 | `06-emplacement.jpg` | Pancarte Equipe Pistoli sur le terrain, 3 elements de proximite |
| 7 | `07-coup-de-coeur.jpg` | Salle a manger, Imaginez-vous vivre ici |
| 8 | `08-contact.jpg` | Georges Matar et Rovena Pistoli, coordonnees, appel a l action |

### Equipe Pistoli

L inscription vient d un lead obtenu par Rovena Pistoli. Elle est mentionnee
a trois endroits:

- slide 1: pastille EQUIPE PISTOLI a cote de A VENDRE
- slide 6: photo de la pancarte installee sur le terrain, ou son nom parait
- slide 8: sa photo, son nom et son titre a cote de ceux de Georges

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

`sources/` contient les fichiers qui ne viennent pas de Centris:

| Fichier | Origine |
|---------|---------|
| `pancarte-01.jpg` | Photo du terrain, pancarte vue de pres. Non utilisee, disponible en remplacement |
| `pancarte-02.jpg` | Photo du terrain, cadrage large. Utilisee sur la slide 6 |
| `rovena-pistoli.jpg` | Portrait officiel, telecharge de sa fiche RE/MAX DU CARTIER |

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
