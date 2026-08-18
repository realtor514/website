# 4071, rang Saint-Hyacinthe, Mirabel (Centris 26269222)

Carrousel Instagram, 8 slides de 1080 x 1350 px (format 4:5, celui qui occupe
le plus d espace dans le fil). Meme gabarit que les carrousels du 28, rue
St-Hilaire et du 35, terrasse Jacques-Leonard: identite RE/MAX rouge, blanc,
bleu, polices Playfair Display et Inter, signature sur chaque slide de contenu.

Publier dans cet ordre exact. Instagram conserve l ordre d ajout des fichiers.

| # | Fichier | Contenu | Photo source |
|---|---------|---------|--------------|
| 1 | `01-couverture.jpg` | Facade, pastille NOUVEAUTE, adresse, prix, Equipe Pistoli | `01-Facade principale.png` |
| 2 | `02-caracteristiques.jpg` | Salon, 4 caracteristiques, bande de prix | `04-Salon - RDC.png` |
| 3 | `03-cuisines.jpg` | Cuisine du rez-de-chaussee, les deux cuisines | `06-Cuisine - RDC.png` |
| 4 | `04-tranquillite.jpg` | Vue laterale, 5 travaux deja faits avec les annees | `25-Vue exterieure 2.png` |
| 5 | `05-details.jpg` | Chambre principale, chambre en pin, poele a combustion lente | `08`, `17`, `11` |
| 6 | `06-emplacement.jpg` | La grange, le terrain et le rang | `19-Grange - vue exterieure.png` |
| 7 | `07-coup-de-coeur.jpg` | Galerie vers les champs, Imaginez-vous vivre ici | `28-Galerie - vue vers la rue.png` |
| 8 | `08-contact.jpg` | Georges Matar et Rovena Pistoli, coordonnees, appel a l action | portraits |

La slide 4 porte cinq points au lieu de quatre: la photo est un peu plus
courte et l interligne un peu plus serre pour les faire entrer.

### Equipe Pistoli

Comme pour les deux autres inscriptions, Rovena Pistoli est mentionnee a
deux endroits:

- slide 1: mention EQUIPE PISTOLI a droite, au-dessus du numero Centris
- slide 8: sa photo, son nom et son titre a cote de ceux de Georges

### Legende a copier-coller

```
Bienvenue au 4071, rang Saint-Hyacinthe, à Saint-Hermas, Mirabel.

Une maison de campagne construite en 1935, dans la même famille depuis 1990, sur un terrain de 22 152 pi2 en bordure des champs.

4 chambres
2 salles de bain complètes
Deux cuisines, une par étage
Poêle à combustion lente au rez-de-chaussée
Vaste galerie de bois face aux champs
Grange-garage de bois sur deux étages

Revêtement extérieur de vinyle refait en 2024.
Thermopompe centrale de 2022 et génératrice neuve installée en 2025.
Panneau électrique de 200 ampères, puits et fosse septique récents.

Un rang tranquille, sans voisin vis-à-vis. Saint-Benoît et Sainte-Scholastique à quelques minutes, accès à la route 148 et à l'autoroute 50.

Vendue sans garantie légale de qualité, aux risques et périls de l'acheteur. Déclarations du vendeur et rapport d'inspection de février 2026 disponibles.

Écrivez-moi pour une visite.

449 000 $ - Centris 26269222

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC., avec l'Équipe Pistoli
438 372-0102
```

### Version longue, si la fiche complete est souhaitee

```
9 pièces sur deux étages, construite en 1935.
Chauffage central au propane à air pulsé, fenêtres de PVC à guillotine, comble isolé à la cellulose soufflée.
Adoucisseur d'eau et filtre à sédiment, service effectué en décembre 2025.

Évaluation municipale 2026: 507 400 $
Taxes municipales: 1 956 $ | Taxes scolaires: 372 $
Occupation: 60 jours après l'acceptation de la promesse d'achat
```

### Mots-cles

```
#mirabel #sainthermas #saintbenoit #saintescholastique #laurentides
#maisonavendre #avendre #maisondecampagne #fermette #grange #terrain
#immobilierquebec #courtierimmobilier #remax #remaxducartier #centris
#maisonquebec #proprieteavendre #immobilier #viealacampagne
```

### Notes avant publication

- Le premier commentaire est le meilleur endroit pour le lien vers la fiche.
  Instagram ne rend pas les liens cliquables dans la legende.
- Identifier @ l Equipe Pistoli et Rovena Pistoli dans la publication, en plus
  de la mention dans la legende.
- La mention sans garantie legale de qualite est dans la legende. Elle n est
  pas sur les slides: si elle doit y paraitre, le dire et je l ajoute.
- Le prix demande est sous l evaluation municipale 2026 (507 400 $). C est un
  argument fort, mais il est laisse hors des slides pour ne pas encombrer la
  couverture. Il est dans la version longue de la legende.
- Photos non utilisees dans le carrousel mais utiles en story ou en
  publication simple: la grange par l interieur (`20`, `21`), la vue
  d ensemble maison et grange (`27`), les vues de la rue (`23`, `24`) et le
  poulailler (`22`).
- Quand la propriete se vend: changer le badge de la slide 1 pour VENDU et
  regenerer.

### Regenerer

```
python "carrousel-instagram/4071 rang saint-hyacinthe mirabel/generer-carrousel.py"
```

Le script lit les photos dans `carrousel-instagram/sources/` et reecrit les
huit JPG de ce dossier. Les anciens JPG sont effaces a chaque execution.

Les textes, les numeros de photo et la hauteur de la couverture sont
regroupes en haut du fichier. Le parametre `fy` de `photo()` deplace le
recadrage vertical, entre 0 (haut de la photo) et 1 (bas). Le parametre
`crop` prend une zone relative (gauche, haut, droite, bas) prelevee avant le
recadrage.

Polices: Playfair Display et Inter, les memes que le site web, sous licence
SIL Open Font License. Elles sont dans `carrousel-instagram/fonts/`, aucune
installation requise.
