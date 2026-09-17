# Fiches hors marche

Les fiches retirees du site, gardees intactes pour le jour ou la propriete
revient sur le marche.

Ce dossier est en dehors de `content/`, donc Hugo ne le voit pas et ne le
construit jamais. Rien ici n'est publie, rien ici n'apparait dans
`/listings/`, et aucune de ces pages n'existe sur georgesmatar.ca. C'est une
armoire, pas une vitrine.

| Propriete | Dossier | Retiree le | Raison |
|-----------|---------|------------|--------|
| 35, terrasse Jacques-Leonard, Montreal (Centris 15815581) | `35-terrasse-jacques-leonard/` | 16 septembre 2026 | Hors marche pour le moment |

## Ce qu'un dossier contient

Les quatre versions linguistiques de la fiche, telles qu'elles etaient en
ligne le jour du retrait: `fr.md`, `en.md`, `es.md`, `ar.md`. Le texte, les
prix, les taxes, l'evaluation municipale, le numero Centris et la liste des
photos, rien n'a ete touche.

Les photos, elles, ne sont pas copiees ici. Elles restent a leur place
habituelle, `static/images/listings/<slug>/`, pour deux raisons: elles sont
deja suivies par Git donc deja sauvegardees, et les scripts de
`carrousel-instagram/` vont les chercher a cet endroit precis. Les dupliquer
alourdirait le depot sans rien proteger de plus.

## Remettre une fiche en ligne

Un fichier par langue, remis a sa place, et c'est fait. Le nom du fichier
dans `content/` est le slug, pas la langue.

```
cp "archives/fiches-hors-marche/35-terrasse-jacques-leonard/fr.md" content/fr/listings/35-terrasse-jacques-leonard.md
cp "archives/fiches-hors-marche/35-terrasse-jacques-leonard/en.md" content/en/listings/35-terrasse-jacques-leonard.md
cp "archives/fiches-hors-marche/35-terrasse-jacques-leonard/es.md" content/es/listings/35-terrasse-jacques-leonard.md
cp "archives/fiches-hors-marche/35-terrasse-jacques-leonard/ar.md" content/ar/listings/35-terrasse-jacques-leonard.md
```

Les quatre langues ensemble, jamais une seule: c'est la regle 2 du
`CLAUDE.md`. Une fiche qui existe en francais mais pas en anglais laisse un
trou dans le selecteur de langue.

Avant de pousser, deux choses a verifier sur la fiche qui revient:

- **Le prix.** Celui du fichier est celui du jour du retrait. Une propriete
  qui revient apres quelques mois revient rarement au meme prix.
- **Le statut.** `status: "A vendre"` en francais, `For sale`, `En venta`,
  `للبيع`. C'est ce qui donne la pastille rouge sur la carte.

Le `git push` sur `main` declenche le deploiement, et la fiche est en ligne
deux a trois minutes plus tard.

## Si le dossier disparaissait

Tout est aussi dans l'historique Git, et l'historique est sur GitHub. La
version en ligne juste avant le retrait se recupere ainsi:

```
git show a147927^:content/fr/listings/35-terrasse-jacques-leonard.md
```

`a147927` est le commit du retrait. `a147927^` est donc le dernier etat ou la
fiche etait encore publiee.
