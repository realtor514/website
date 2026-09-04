# Stories: promesse d'achat acceptée

Une story Instagram par propriété, au format 1080 x 1920 (9:16), à publier le
jour où la promesse d'achat est acceptée. C'est le contenu qui rapporte le plus
de mandats: il montre un résultat, pas une intention.

| Propriété | Dossier | Fichier |
|-----------|---------|---------|
| 28, rue St-Hilaire, Longueuil (Centris 26368231) | `28-rue-st-hilaire-longueuil/` | `story-promesse-achat-acceptee.jpg` |
| 4071, rang Saint-Hyacinthe, Mirabel (Centris 26269222) | `4071-rang-saint-hyacinthe-mirabel/` | `story-promesse-achat-acceptee.jpg` |

## Ce que la story raconte

De haut en bas, dans l'ordre où l'oeil la lit en trois secondes:

1. **La photo de façade**, plein cadre, avec la pastille rouge PROMESSE
   D'ACHAT et le mot ACCEPTÉE en gros. Le prix demandé est à droite: c'est
   l'information que le voisinage cherche.
2. **L'adresse, le secteur et le numéro Centris**, pour que la propriété soit
   identifiable et vérifiable.
3. **Trois photos de la propriété**, la cuisine, une pièce de vie et
   l'extérieur, pour rappeler ce qui a été vendu.
4. **La relance.** MERCI POUR VOTRE CONFIANCE d'un côté, ÉVALUATION GRATUITE
   de l'autre, puis "Votre propriété mérite le même résultat." La story ne
   sert pas seulement à annoncer, elle demande le prochain mandat.
5. **Les coordonnées**: portrait, nom, titre, téléphone et site, sur la carte
   navy. Le courriel et l'agence sont en bas.

Les couleurs, les polices et le logo sont ceux des carrousels et des reels:
navy `#000e35`, rouge RE/MAX, crème, Playfair pour les titres et Inter pour le
reste. Le profil garde ainsi une seule identité visuelle.

## La zone sûre

Tout le contenu utile tient entre 250 px du haut et 1670 px du bas. Au-dessus,
Instagram affiche le nom du compte; en dessous, la barre de réponse. La
signature sous la carte de contact est volontairement dans cette zone: elle
est décorative, rien d'important n'y est caché.

## Regénérer

```
python "PAC stories/generer-stories.py"              les deux
python "PAC stories/generer-stories.py" mirabel      une seule, par bout de nom
```

Quelques secondes par image. Le script lit les photos dans
`static/images/listings/<slug>/`, les mêmes que la fiche du site, et le
portrait détouré dans `carrousel-instagram/sources/`.

Tout se règle en haut de `generer-stories.py`: l'adresse, le secteur, le prix,
le numéro Centris, la photo de couverture, les trois photos du bandeau et les
deux lignes de texte propres à la propriété. Une photo est un triplet
`(fichier, fx, fy)`, où `fx` et `fy` donnent le point d'intérêt du recadrage:
`fy=0.28` remonte le cadre vers le haut de la photo, `fy=0.5` reste au centre.

Pour une nouvelle propriété: copier un bloc de `PROPRIETES`, changer le slug,
les textes et les photos. Le dossier de sortie se crée tout seul.

## Légende de la story: 28, rue St-Hilaire

Instagram ne rend pas les liens cliquables dans une story sans le sticker
Lien. Ajouter le sticker vers la fiche, et coller ce texte dans un sticker de
texte ou en publication si la story est reprise en carrousel.

```
Promesse d'achat acceptée sur le 28, rue St-Hilaire, dans le Vieux-Longueuil.

Merci à mes clients pour leur confiance.

Vous pensez vendre? L'évaluation est gratuite et sans engagement.

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC., avec l'Équipe Pistoli
438 372-0102
```

## Légende de la story: 4071, rang Saint-Hyacinthe

```
Promesse d'achat acceptée sur le 4071, rang Saint-Hyacinthe, à Saint-Hermas, Mirabel.

Une maison de 1935 avec sa grange, sur 22 152 pi² en bordure des champs. Merci à mes clients pour leur confiance.

Vous pensez vendre dans les Laurentides ou à Mirabel? L'évaluation est gratuite et sans engagement.

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC., avec l'Équipe Pistoli
438 372-0102
```

## Avant de publier

- Attendre que la promesse d'achat soit **signée et acceptée** par le vendeur.
  Avant, l'annonce est prématurée; après le notaire, on passe plutôt au visuel
  VENDU.
- Ajouter un **sticker de musique** dans l'application: une story avec un son
  tendance sort davantage du cercle des abonnés.
- Ajouter le **sticker de lien** vers la fiche Centris ou vers
  georgesmatar.ca.
- Identifier @ l'Équipe Pistoli et Rovena Pistoli.
- Épingler la story **à la une** dans un dossier "Vendu" du profil: c'est la
  preuve sociale qu'un vendeur regarde avant d'appeler.
- Le même fichier passe sans retouche en story Facebook et en publication
  9:16.
