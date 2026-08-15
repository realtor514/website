# 35, terrasse Jacques-Léonard, Montréal (Centris 15815581)

Carrousel Instagram, 8 slides de 1080 x 1350 px (format 4:5, celui qui occupe
le plus d espace dans le fil). Meme gabarit que le carrousel du 28, rue
St-Hilaire: identite RE/MAX rouge, blanc, bleu, polices Playfair Display et
Inter, signature obligatoire sur chaque slide de contenu.

Publier dans cet ordre exact. Instagram conserve l ordre d ajout des fichiers.

| # | Fichier | Contenu | Photo source |
|---|---------|---------|--------------|
| 1 | `01-couverture.jpg` | Facade, pastille NOUVEAUTE, adresse, prix, Equipe Pistoli | `0-façade.png` |
| 2 | `02-caracteristiques.jpg` | Salle a manger, 4 caracteristiques, bande de prix | `3-salle à manger- rdc.png` |
| 3 | `03-cuisine.jpg` | Cuisine, 3 points | `4-cuisine- RDC.png` |
| 4 | `04-domaine.jpg` | Parc du domaine, aires communes et charges communes | `16-parc et piscine privés du domaine.png` |
| 5 | `05-details.jpg` | Chambre principale, salon du sous-sol, terrasse couverte | `5`, `11`, `14` |
| 6 | `06-emplacement.jpg` | Vue aerienne du secteur, 3 elements de proximite | `16` (vue aerienne) |
| 7 | `07-coup-de-coeur.jpg` | Salon du rez-de-chaussee, Imaginez-vous vivre ici | `2-salon-rdc.png` |
| 8 | `08-contact.jpg` | Georges Matar et Rovena Pistoli, coordonnees, appel a l action | portraits |

La photo `16-parc et piscine privés du domaine.png` est un montage de trois
cliches. Le script y decoupe deux zones: la bande du haut (le parc au
couchant) pour la slide 4, la vue aerienne du bas a gauche pour la slide 6.

### Equipe Pistoli

Comme pour le 28, rue St-Hilaire, l inscription est partagee avec Rovena
Pistoli. Elle est mentionnee a deux endroits:

- slide 1: mention EQUIPE PISTOLI a droite, au-dessus du numero Centris
- slide 8: sa photo, son nom et son titre a cote de ceux de Georges

Titre exact tire de sa fiche RE/MAX DU CARTIER: Courtier immobilier
residentiel et commercial. Entreprise: Rovena Pistoli Immobilier Inc.
Telephone: 514 910-4128. Fiche: remaxducartier.com/fr/courtiers/rovena-pistoli

### Legende a copier-coller

```
Bienvenue au 35, terrasse Jacques-Léonard, Rivière-des-Prairies.

Une maison de ville sur trois niveaux au Domaine Bonneville, une enclave paisible de 250 maisons dans un site paysager mature.

4 chambres, dont 1 au sous-sol
2 salles de bain et 1 salle d'eau
Sous-sol complet avec cuisine, salon et chambre
Garage au sous-sol et allée à usage exclusif
Cour arrière privée et clôturée avec terrasse couverte

Piscine, pataugeoire, parc privé, aire de jeux et centre communautaire réservés aux résidents du domaine.

Les charges communes couvrent l'assurance, la toiture, la maçonnerie, les balcons, le déneigement et le fonds de prévoyance.

Écoles, parcs et pistes cyclables à distance de marche. Transport en commun et autoroute 40 à proximité.

Écrivez-moi pour une visite.

380 000 $ - Centris 15815581

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC., avec l'Équipe Pistoli
438 372-0102
```

### Version longue, si la fiche complete est souhaitee

```
Construite en 1972, brique et fondation de béton, chauffage électrique individuel.
9 pièces réparties sur 3 niveaux.

Évaluation municipale 2026: 412 300 $
Taxes municipales: 2 616 $ | Taxes scolaires: 314 $
Occupation: 90 jours après l'acceptation de la promesse d'achat
```

### Mots-cles

```
#rivieredesprairies #rdp #pointeauxtrembles #montrealest #montreal
#maisonavendre #avendre #maisondeville #immobilierquebec #courtierimmobilier
#remax #remaxducartier #centris #maisonquebec #proprieteavendre #immobilier
#domainebonneville #premiereMaison #familleaupairs
```

### Notes avant publication

- Le premier commentaire est le meilleur endroit pour le lien vers la fiche.
  Instagram ne rend pas les liens cliquables dans la legende.
- Identifier @ l Equipe Pistoli et Rovena Pistoli dans la publication, en plus
  de la mention dans la legende. Une identification rejoint ses abonnes a elle.
- Seules les coordonnees de Georges paraissent sur la slide 8. Si le telephone
  de Rovena doit y figurer aussi, le dire et je l ajoute.
- Le montant exact des charges communes n est pas publie sur Centris. Il n
  apparait donc nulle part dans le carrousel ni dans la legende. Si le montant
  doit y figurer, le fournir et je l ajoute a la slide 4.
- Centris affiche Stationnement total: Allee (1), alors que la description
  parle d un garage prive au sous-sol. La slide 2 dit Garage / Allee a usage
  exclusif, ce qui reprend la description. A corriger si la fiche change.
- Quand la propriete se vend: changer le badge de la slide 1 pour VENDU et
  regenerer. Une publication VENDU performe mieux qu une suppression.

### Regenerer

```
python "carrousel-instagram/35 terrasse jacques leonard/generer-carrousel.py"
```

Le script lit les photos dans `carrousel-instagram/sources/` et reecrit les
huit JPG de ce dossier. Les anciens JPG sont effaces a chaque execution.

Les textes, les numeros de photo et les zones de decoupe sont regroupes en
haut du fichier. Le parametre `fy` de `photo()` deplace le recadrage vertical,
entre 0 (haut de la photo) et 1 (bas). Le parametre `crop` prend une zone
relative (gauche, haut, droite, bas) prelevee avant le recadrage.

Polices: Playfair Display et Inter, les memes que le site web, sous licence
SIL Open Font License. Elles sont dans `carrousel-instagram/fonts/`, aucune
installation requise.
