# Reels VENDU

Un reel vertical par propriété vendue, 1080 x 1920 (9:16), 30 images par
seconde, environ 31 secondes, H.264. Même montage et même identité visuelle
que les reels d'inscription de `reels/`, mais le texte de vente est retiré et
remplacé par le résultat obtenu pour les vendeurs.

| Propriété | Dossier | Statut |
|-----------|---------|--------|
| 28, rue St-Hilaire, Longueuil (Centris 26368231) | `28-rue-st-hilaire-longueuil/` | `reel-vendu.mp4`, 30,7 s |
| 35, terrasse Jacques-Léonard, Montréal (Centris 15815581) | `35-terrasse-jacques-leonard/` | en attente des chiffres de vente |
| 4071, rang Saint-Hyacinthe, Mirabel (Centris 26269222) | `4071-rang-saint-hyacinthe-mirabel/` | en attente des chiffres de vente |

Pour les deux propriétés en attente, il manque deux informations: le délai de
vente en jours, et l'écart avec le prix attendu par les vendeurs. Dès qu'elles
sont connues, remplir `delai`, `accroche` et `resultat` dans
`generer-vendu.py` et relancer le script.

## Ce qui change par rapport au reel d'inscription

| Reel d'inscription | Reel VENDU |
|--------------------|------------|
| Pastille NOUVEAUTÉ | Pastille rouge VENDU, du premier au dernier plan |
| Prix demandé, 499 000 $ | Délai de vente, 28 jours |
| Chaque pièce nommée en bas de l'écran | Aucune légende: logo et mention VENDU, rien d'autre |
| Écran des travaux déjà faits | Écran du résultat obtenu |
| Planifiez votre visite | Évaluation gratuite et sans engagement |

Le raisonnement derrière la visite muette: un reel de résultat n'est pas une
visite. La personne qui le regarde ne cherche pas à acheter cette maison, elle
est déjà vendue. Elle regarde ce qu'un courtier a obtenu. Nommer les pièces la
ramènerait vers une annonce, et le mot VENDU perdrait sa place.

## Le montage: 28, rue St-Hilaire

1. **L'ouverture, 4,6 s.** La façade, un mouvement d'arc, et le résultat en
   clair dès la première seconde: vendu en 28 jours, près de 20 000 $ de plus
   que le prix attendu. Puis la pastille VENDU, l'adresse, le secteur, le
   délai et le numéro Centris.
2. **La visite, 8 plans de 2,4 s.** Les pièces défilent sans légende. Le logo
   et la pastille VENDU restent en place, à opacité constante.
3. **Le résultat, 5,6 s.** Les trois lignes qui comptent, une à une:
   l'écart de prix, les conditions souhaitées par les vendeurs, le
   remerciement.
4. **Le contact, 5 s.** Les deux courtiers, le téléphone, et l'appel à
   l'action qui va avec un VENDU: l'évaluation gratuite.

## Les chiffres annoncés

Le reel affiche exactement ce qui a été convenu, sans arrondi vers le haut:

- vendu en 28 jours
- près de 20 000 $ de plus que le prix attendu par les vendeurs
- selon les conditions souhaitées par les vendeurs

La mention des conditions n'est pas une formule: elle dit qu'au delà du prix,
la transaction s'est faite selon les modalités que les vendeurs voulaient,
date d'occupation comprise. C'est souvent ce qu'un vendeur qui hésite cherche
à entendre.

## Regénérer

```
python "carrousel-instagram/vendu/generer-vendu.py"              tous
python "carrousel-instagram/vendu/generer-vendu.py" hilaire      un seul
```

Environ 80 secondes par reel. Le script lit les photos dans
`static/images/listings/<slug>/` et dans `carrousel-instagram/sources/`, et
utilise le moteur de rendu `reels/moteur.py`. Rien à installer: si ffmpeg
n'est pas sur le poste, le moteur prend celui du paquet `imageio-ffmpeg`
(`pip install imageio-ffmpeg`).

Tout se règle en haut de `generer-vendu.py`: les textes, les photos, l'ordre
des plans, les mouvements et les durées. Un plan est un tuple
`(photo, mouvement, fx, fy)`, où `fx` et `fy` donnent le point d'intérêt du
mouvement.

Les `reel-vendu.mp4` ne sont pas suivis par Git, comme les autres reels: 16 Mo
par version alourdiraient le dépôt pour toujours et le fichier se refabrique
en 80 secondes. Les couvertures, elles, sont suivies.

## Légende du reel: 28, rue St-Hilaire

```
VENDU | 28, rue St-Hilaire, Vieux-Longueuil

Vendu en 28 jours, à près de 20 000 $ de plus que le prix attendu par les vendeurs, et selon les conditions qu'ils souhaitaient.

Merci à mes clients pour leur confiance.

Vous pensez vendre? L'évaluation est gratuite et sans engagement, et elle commence par une discussion honnête sur ce que votre propriété vaut aujourd'hui.

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC., avec l'Équipe Pistoli
438 372-0102

Centris 26368231
```

```
#vendu #vieuxlongueuil #longueuil #rivesud #montreal #immobilierquebec
#courtierimmobilier #remax #remaxducartier #centris #evaluationgratuite
#vendresamaison #maisonvendue #resultat
```

## Avant de publier

- Publier en **reel**, pas en publication simple.
- Ajouter un **son tendance** dans l'application, avant de publier. Le fichier
  ne contient qu'une piste muette, exprès.
- Choisir `couverture.jpg` comme couverture, pour que la grille du profil
  reste cohérente.
- Identifier @ l'Équipe Pistoli et Rovena Pistoli.
- Épingler le reel **à la une** dans un dossier "Vendu" du profil: c'est la
  preuve sociale qu'un vendeur regarde avant d'appeler.
- Publier après la signature chez le notaire. Avant, c'est la story
  promesse d'achat acceptée de `PAC stories/` qui s'applique.
- Le même fichier passe sans retouche en story, sur Facebook et en YouTube
  Shorts.
