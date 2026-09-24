# Brief de traduction et de localisation

Le site existe en 4 langues: francais (defaut, a la racine), anglais (`/en/`),
espagnol (`/es/`), arabe (`/ar/`). La regle 2 de `CLAUDE.md` est stricte: un
article ne vit pas dans une langue seule.

## Ce qu on vous demande

Pas une traduction litterale. Une **localisation**: le meme article, ecrit pour
un lecteur de cette langue qui vit au Quebec et qui cherche dans sa langue.

## La seule source de verite est l article francais

Si votre consigne vous demande de preserver un element qui ne se trouve pas
dans le fichier francais, **ne l inventez pas**. Signalez-le et traduisez ce qui
est reellement ecrit.

C est arrive trois fois: une consigne mentionnait un decret, une enquete datee
et un alinea de loi qui n existaient que dans le resume du redacteur, pas dans
son texte. Les trois traducteurs ont refuse d ajouter la donnee et l ont
signale. C etait la bonne reaction, et la regle est desormais ecrite ici.

## Ce qui ne change jamais

- Les faits, les chiffres, les articles de loi, les delais, les noms d organismes.
- La structure: memes sections, meme ordre, meme tableau.
- `translationKey`: **identique** a la version francaise. C est ce champ qui relie
  les 4 versions et qui alimente les balises hreflang de `layouts/partials/seo.html`.
- `date` et `lastmod`: identiques a la version francaise.
- `image`: meme chemin que la version francaise.
- `draft: true`.

## Ce qui change

### La categorie est traduite

C est une erreur facile: le site **localise** la categorie. Tableau de conversion,
valeurs relevees dans `content/`, a copier exactement:

| francais | en | es | ar |
|---|---|---|---|
| Guide de l'acheteur | Buyer's Guide | Guía del Comprador | دليل المشتري |
| Guide du vendeur | Seller's Guide | Guía del Vendedor | دليل البائع |
| Financement | Finance | Financiamiento | تمويل |
| Investissement | Investment | Inversión | استثمار |
| Immobilier 101 | Real Estate 101 | Inmobiliaria 101 | عقارات 101 |
| Guide pratique | Practical Guide | Guía práctica | دليل عملي |
| Analyse de marche | Market Analysis | Análisis de Mercado | تحليل السوق |

### Le formulaire n a pas le meme chemin dans les 4 langues

Deuxieme piege. Le formulaire et la page contact ont un slug propre a chaque
langue, parce que leur front matter declare son propre `url:`:

| | formulaire | contact |
|---|---|---|
| fr | `/formulaire/` | `/contact/` |
| en | `/en/form/` | `/en/contact/` |
| es | `/es/formulario/` | `/es/contacto/` |
| ar | `/ar/istimara/` | `/ar/tawasul/` |

Les pages d outils, elles, gardent leur slug anglais avec un prefixe de langue:
`/en/tools/mortgage/`, `/es/tools/mortgage/`, `/ar/tools/mortgage/`. Idem pour
`affordability`, `closing-costs`, `home-estimate`, `rent-vs-buy`, `welcome-tax`.

### Le reste

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
- Les liens vers les outils suivent la logique de prefixe. Le formulaire et la
  page contact ont leur propre slug par langue: voir les deux tableaux ci-dessus.

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
