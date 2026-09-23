# Brief de traduction et de localisation

Le site existe en 4 langues: francais (defaut, a la racine), anglais (`/en/`),
espagnol (`/es/`), arabe (`/ar/`). La regle 2 de `CLAUDE.md` est stricte: un
article ne vit pas dans une langue seule.

## Ce qu on vous demande

Pas une traduction litterale. Une **localisation**: le meme article, ecrit pour
un lecteur de cette langue qui vit au Quebec et qui cherche dans sa langue.

## Ce qui ne change jamais

- Les faits, les chiffres, les articles de loi, les delais, les noms d organismes.
- La structure: memes sections, meme ordre, meme tableau.
- `translationKey`: **identique** a la version francaise. C est ce champ qui relie
  les 4 versions et qui alimente les balises hreflang de `layouts/partials/seo.html`.
- `date` et `lastmod`: identiques a la version francaise.
- `category`: identique a la version francaise, en francais dans le texte, parce
  que c est la valeur que le site utilise partout.
- `image`: meme chemin que la version francaise.
- `draft: true`.

## Ce qui change

- `title` et `description`: rediges dans la langue cible, pas traduits mot a mot.
  Ils doivent contenir la formulation que le lecteur taperait vraiment.
- Le **slug**, donc le nom du fichier: dans la langue cible quand c est naturel.
  Le site accepte les deux, plusieurs articles existants gardent un slug anglais
  dans les 4 langues. Un slug localise est preferable pour l espagnol et l anglais.
  Pour l arabe, gardez le slug latin de la version anglaise: les URL du site ne
  sont pas en caracteres arabes.
- Les **liens internes**: ils pointent vers la version de la MEME langue.
  - francais: `/articles/slug/`
  - anglais: `/en/articles/slug/`
  - espagnol: `/es/articles/slug/`
  - arabe: `/ar/articles/slug/`
  Verifiez que le fichier cible existe vraiment dans cette langue. S il n existe
  pas, pointez vers la version francaise, ou retirez le lien. Jamais de lien mort.
- Les liens vers les outils et le formulaire suivent la meme logique de prefixe.

## Noms officiels: ne les traduisez pas

Ces organismes et documents gardent leur nom francais, avec au besoin une glose
entre parentheses la premiere fois:

OACIQ, Centris, APCIQ, Tribunal administratif du logement, Tribunal administratif
du Quebec, Regie du batiment du Quebec, Code civil du Quebec, Registre foncier,
Declarations du vendeur sur l immeuble, promesse d achat, certificat de
localisation, taxe de bienvenue (droits de mutation), CELIAPP, RAP, Hydro-Quebec,
Revenu Quebec, Autorite des marches financiers.

Exemple en anglais: `the Tribunal administratif du logement (Quebec's rental board)`.
Exemple en espagnol: `el Tribunal administratif du logement (el tribunal de vivienda de Quebec)`.

## Par langue

**Anglais.** Anglais canadien. Orthographe: neighbourhood, cheque, licence (nom).
Dollars en `$450,000`. Le lecteur type est un anglophone de Montreal ou un
nouvel arrivant: il connait le contexte quebecois, ne le lui expliquez pas comme
a un etranger.

**Espagnol.** Espagnol neutre d Amerique latine, vouvoiement `usted`. Le lecteur
type est un nouvel arrivant d Amerique latine: c est la langue ou une glose
courte sur une institution quebecoise aide le plus.

**Arabe.** Arabe standard moderne. Le theme gere la direction du texte, et
`layouts/partials/ar-numerals.html` s occupe des chiffres: ecrivez les nombres
en chiffres latins comme dans les articles arabes existants, ne les convertissez
pas a la main. Regardez un article arabe existant avant de commencer.

## Regles absolues

1. **Zero tiret long**, dans toutes les langues, front matter compris.
2. Ne rajoutez aucun fait absent de la version francaise. Si la version
   francaise se trompe, signalez-le, ne corrigez pas de votre cote.
3. `draft: true` reste.
4. Longueur a plus ou moins 15 % de la version francaise.

## Livrable

Un seul fichier: `content/{lang}/articles/{slug}.md`.

Avant de rendre, verifiez: `translationKey` identique au francais, chaque lien
interne existe dans la bonne langue, aucun tiret long, `draft: true` present.
