# Reels VENDU

Un reel vertical par propriété vendue, 1080 x 1920 (9:16), 30 images par
seconde, 33,2 secondes, H.264. Même montage et même identité visuelle que les
reels d'inscription de `reels/`, mais le texte de vente est retiré et remplacé
par le résultat obtenu pour les vendeurs.

| Propriété | Dossier | Résultat annoncé |
|-----------|---------|------------------|
| 28, rue St-Hilaire, Longueuil (Centris 26368231) | `28-rue-st-hilaire-longueuil/` | Vendu en 28 jours, près de 20 000 $ de plus que le prix attendu |
| 4071, rang Saint-Hyacinthe, Mirabel (Centris 26269222) | `4071-rang-saint-hyacinthe-mirabel/` | Vendu en 10 jours, à un prix plus élevé que les attentes |
| 35, terrasse Jacques-Léonard, Montréal (Centris 15815581) | `35-terrasse-jacques-leonard/` | en attente des chiffres de vente |

Pour la propriété en attente, il manque deux informations: le délai de vente
en jours, et l'écart avec le prix attendu par les vendeurs. Dès qu'elles sont
connues, remplir `delai`, `accroche`, `resultat` et les phrases dans
`generer-vendu.py`, puis relancer le script.

## Ce qui change par rapport au reel d'inscription

| Reel d'inscription | Reel VENDU |
|--------------------|------------|
| Pastille NOUVEAUTÉ | Pastille rouge VENDU, du premier au dernier plan |
| Prix demandé, 499 000 $ | Délai de vente, 28 jours |
| Chaque pièce nommée en bas de l'écran | Une phrase un plan sur deux, sur le résultat |
| Écran des travaux déjà faits | Écran du résultat obtenu |
| Planifiez votre visite | Évaluation gratuite et sans engagement |

Le raisonnement: un reel de résultat n'est pas une visite. La personne qui le
regarde ne cherche pas à acheter cette maison, elle est déjà vendue. Elle
regarde ce qu'un courtier a obtenu. Nommer les pièces la ramènerait vers une
annonce, et le mot VENDU perdrait sa place.

## Les phrases

C'est la piste qui porte le reel. Des phrases courtes, une chute en deux
temps, un plan sur deux. Les plans muets ne sont pas un oubli: ils laissent
respirer l'image et rendent la phrase suivante plus forte.

**28, rue St-Hilaire**

```
Quatre semaines. Pas quatre mois.
Le prix espéré par les vendeurs? Dépassé.
Près de 20 000 $ de plus que prévu.
Et aux conditions qu'ils voulaient.
Pas juste vendu. Bien vendu.
```

**4071, rang Saint-Hyacinthe**

```
Dix jours. Pas dix semaines.
Une maison de 1935 qui n'a pas attendu.
Le prix espéré par les vendeurs? Dépassé.
Plus cher que prévu. Plus vite que prévu.
Pas juste vendu. Bien vendu.
```

« Pas juste vendu. Bien vendu. » ferme les deux reels, sur la dernière vue
large. C'est la ligne qui se retient et qui se répète d'une propriété à
l'autre: à force, elle devient la signature du profil.

Tout se change dans `generer-vendu.py`, dans les tuples `plans` et `cadres`.
Un plan est `(photo, mouvement, fx, fy, phrase)`, un cadre
`(photo, crop, fy, phrase)`. Mettre `None` à la place d'une phrase rend le
plan muet. Le `\n` dans une phrase force la coupure de ligne: c'est là que
tombe la chute, et pas là où le dernier mot ne rentrait plus. Un plan qui
porte une phrase dure 2,9 s au lieu de 2,4 s, le temps de la lire.

## Le montage

1. **L'ouverture, 4,6 s.** La façade, un mouvement d'arc, et le résultat en
   clair dès la première seconde. Puis la pastille VENDU, l'adresse, le
   secteur, le délai de vente à la place du prix, et le numéro Centris.
2. **La visite, 8 plans.** Les pièces défilent, une phrase sur deux plans. Le
   logo et la pastille VENDU restent à opacité constante pendant que les
   phrases entrent et sortent: ils sont peints sous le calque de texte, pas
   dedans, et ne clignotent donc jamais avec lui.
3. **Le résultat, 5,6 s.** Les trois lignes qui comptent, une à une.
4. **Le contact, 5 s.** Les deux courtiers, le téléphone, et l'appel à
   l'action qui va avec un VENDU: l'évaluation gratuite.

## Les chiffres annoncés

Le reel affiche exactement ce qui a été convenu, sans arrondi vers le haut.

28, rue St-Hilaire:

- vendu en 28 jours
- près de 20 000 $ de plus que le prix attendu par les vendeurs
- selon les conditions souhaitées par les vendeurs

4071, rang Saint-Hyacinthe:

- vendu en 10 jours
- à un prix de vente plus élevé que les attentes des vendeurs

Aucun montant n'est annoncé pour le 4071: seul l'écart est connu, pas le
chiffre. Le jour où il l'est, l'ajouter dans `accroche` et dans le premier
point de `resultat` rendrait le reel plus fort.

## Regénérer

```
python "carrousel-instagram/vendu/generer-vendu.py"              tous
python "carrousel-instagram/vendu/generer-vendu.py" hilaire      un seul
python "carrousel-instagram/vendu/generer-vendu.py" mirabel      un seul
```

Environ 90 secondes par reel. Le script lit les photos dans
`static/images/listings/<slug>/` et dans `carrousel-instagram/sources/`, et
utilise le moteur de rendu `reels/moteur.py`. Rien à installer: si ffmpeg
n'est pas sur le poste, le moteur prend celui du paquet `imageio-ffmpeg`
(`pip install imageio-ffmpeg`).

Les `reel-vendu.mp4` ne sont pas suivis par Git, comme les autres reels: 16 Mo
par version alourdiraient le dépôt pour toujours et le fichier se refabrique
en 90 secondes. Les couvertures, elles, sont suivies.

## Légende du reel: 28, rue St-Hilaire

```
VENDU | 28, rue St-Hilaire, Vieux-Longueuil

Vendu en 28 jours, à près de 20 000 $ de plus que le prix attendu par les vendeurs, et selon les conditions qu'ils souhaitaient.

Pas juste vendu. Bien vendu.

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

## Légende du reel: 4071, rang Saint-Hyacinthe

```
VENDU | 4071, rang Saint-Hyacinthe, Saint-Hermas, Mirabel

Dix jours. Pas dix semaines. Et à un prix plus élevé que ce que les vendeurs attendaient.

Une maison de 1935 avec sa grange, sur 22 152 pi² en bordure des champs, dans la même famille depuis 1990.

Pas juste vendu. Bien vendu.

Merci à mes clients pour leur confiance.

Vous pensez vendre à Mirabel ou dans les Laurentides? L'évaluation est gratuite et sans engagement.

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC., avec l'Équipe Pistoli
438 372-0102

Centris 26269222
```

```
#vendu #mirabel #sainthermas #saintbenoit #laurentides #immobilierquebec
#courtierimmobilier #remax #remaxducartier #centris #evaluationgratuite
#maisondecampagne #fermette #maisonvendue #resultat
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
- Publier après la signature chez le notaire. Avant, c'est la story promesse
  d'achat acceptée de `PAC stories/` qui s'applique.
- Le même fichier passe sans retouche en story, sur Facebook et en YouTube
  Shorts.
