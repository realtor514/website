# Ce qui demande une decision de Georges

Mis a jour le 2026-09-24. Branche de travail `auto/blogue-content`, fusionnee dans `main`.

Rien dans ce fichier ne bloque la production. Tout ce qui est liste ici a ete
contourne proprement et la production a continue.

---

## 1. Hugo n est pas installe sur ce poste

`hugo` est introuvable en ligne de commande ici. Le site est bati par GitHub
Actions avec Hugo 0.155.0 (`.github/workflows/deploy.yml`), donc la commande
`hugo list all` et la verification de build locale du plan automatise ne peuvent
pas tourner.

**Ce qui a ete fait a la place.** `tools/validate.py` verifie chaque fichier:
front matter complet et lisible, dates non futures, categorie connue, longueur
de la description, nombre de mots, hierarchie des titres, presence du CTA, et
surtout **chaque lien interne est resolu contre les fichiers reellement presents
dans `content/`**. Un lien mort fait echouer le fichier. Sur du contenu qui
n ajoute que des fichiers markdown, cette verification attrape davantage qu un
build.

**Ce que vous pouvez faire.** Rien d urgent. Si vous voulez la verification de
build en local: `winget install Hugo.Hugo.Extended`, puis
`hugo --gc --minify -D --destination /tmp/hugo_check`.

---

## 2. La regle des 4 langues et les brouillons francais

`CLAUDE.md` regle 2 exige que toute modification de contenu soit faite dans les
4 langues. La production commence par le francais, les traductions suivent en
phase 3.

**La regle est tenue.** Aucun article n est passe en ligne avant que ses quatre
versions existent. `tools/approve.py` **refuse** de publier un article francais
tant que les versions en, es et ar manquent, et il faut `--fr-seulement` pour
passer outre, volontairement. Rien n a eu besoin de cette option.

Verifiable a tout moment:

```
python tools/status.py --nouveaux
```

La colonne `langues` affiche `frenesar` quand les quatre versions sont la, et
un point a la place d une langue manquante.

---

## 3. Pas de schema FAQ en JSON-LD

`layouts/partials/seo.html` produit du JSON-LD `BlogPosting` et `BreadcrumbList`
pour les articles, mais pas de `FAQPage`. Les articles existants n ont pas de
champ `faq` dans leur front matter.

**Choix retenu.** La section Questions frequentes est ecrite dans le corps de
l article, en H2, comme du contenu visible. Le front matter reste exactement
celui de vos articles existants, et aucun layout n est touche.

**Si vous voulez le JSON-LD FAQ un jour.** Il faudrait ajouter un fichier
`layouts/shortcodes/faq-schema.html` et un champ `faq` au front matter, dans les
4 langues. C est un changement de theme, donc il ne sera pas fait sans votre
accord.

---

## 4. Le site de reference et le droit d auteur

Les 619 sujets recoltes sur rovenapistoli.com servent de carte des sujets, rien
de plus. Aucun agent redacteur n a recu le texte de ces articles.

Un cache texte de 14 articles de reference existe dans `state/reference_cache/`.
Il sert **uniquement** au detecteur de plagiat de `tools/dedupe.py`, qui rejette
tout brouillon dont le recoupement de segments de 5 mots depasse 10 %.

Si vous preferez que ce cache disparaisse du depot, ajoutez
`state/reference_cache/` a `.gitignore`. La detection ne fonctionnera alors plus
qu en local.

---

## 5. Articles a faire relire par un specialiste

Ces articles portent `needs_expert_review: true`. Ils sont sources et passent
tous les controles, et chacun dit lui-meme ou s arrete ce qu il peut demontrer,
en renvoyant au notaire, au comptable, a l assureur ou a la municipalite.

La plupart sont **en ligne**, parce que vous avez demande de tout publier. Ceux
qui restent en brouillon le sont pour une raison precise, indiquee plus bas.

| Date | Article | Etat | Points a revalider |
|---|---|---|---|
| 2026-08-24 | `acheter-reprise-de-finance-quebec` | en ligne | 3 |
| 2026-08-25 | `acheter-zone-inondable-quebec` | en ligne | 4 |
| 2026-08-26 | `choisir-inspecteur-batiment-quebec` | en ligne | 3 |
| 2026-08-27 | `conjoints-de-fait-maison-quebec` | brouillon | 4 |
| 2026-09-02 | `contrat-courtage-vente-quebec` | en ligne | 2 |
| 2026-09-05 | `casser-hypotheque-penalite-quebec` | en ligne | 3 |
| 2026-09-06 | `declaration-du-vendeur-quebec` | en ligne | 3 |
| 2026-09-11 | `copropriete-indivise-cooperative-montreal` | en ligne | 4 |
| 2026-09-14 | `impot-proprietaire-quebec` | en ligne | 5 |
| 2026-09-16 | `location-court-terme-quebec-regles` | en ligne | 4 |
| 2026-09-21 | `vente-sans-garantie-legale-quebec` | en ligne | 4 |
| 2026-09-23 | `garantie-gcr-maison-neuve-quebec` | en ligne | 0 |
| 2026-09-23 | `vice-cache-conditions-recours-quebec` | en ligne | 3 |

La colonne **Points a revalider** compte les elements que le redacteur a
lui-meme signales dans `meta/fr/<slug>.json`, champ `claims_needing_review`.
C est la liste exacte a verifier, pas une inquietude vague. Un zero signifie
que l agent n avait pas encore ecrit son journal au moment du relevé.

**Retenu volontairement:** `conjoints-de-fait-maison-quebec`. Son redacteur
demande explicitement une validation par un notaire avant publication, et c est
du droit de la famille, ou une erreur coute cher au lecteur. Ses traductions
sont pretes. Une seule commande le met en ligne:

```
python tools/approve.py approve conjoints-de-fait-maison-quebec
```

**Si vous le publiez, un lien est a remettre.** L article
`deces-conjoint-proteger-propriete-quebec` renvoyait naturellement vers lui a
deux endroits. J ai retire les deux liens, parce qu un lien vers un article en
draft renvoie 404 en production: Hugo ne rend pas les brouillons. Une fois
`conjoints-de-fait-maison-quebec` en ligne, ces deux renvois valent la peine
d etre remis, dans les 4 langues.

Le validateur bloque desormais ce cas de lui-meme: `tools/validate.py` refuse un
lien vers un article encore en draft, alors qu avant il se contentait de
verifier que le fichier existait sur le disque.

Pour retirer un article publie, l inverse n existe pas dans approve.py: mettez
`draft: true` dans les 4 fichiers, puis commit et push.

### Une contradiction tranchee: c est mon article qui avait tort

Sur la voie transitoire du certificat RBQ d inspecteur, mon article
`choisir-inspecteur-batiment-quebec` affirmait que trois ans d experience plus
une preuve d assurance suffisaient. Votre article deja en ligne
`home-inspection-checklist-montreal` parlait, lui, d une formation de mise a
niveau. J avais signale la contradiction en supposant que le vieux texte etait
le fautif.

**Verification faite a la source, c est l inverse.** La RBQ decrit deux voies
transitoires, ouvertes jusqu au 2 aout 2027, et **les deux passent par la
formation de mise a niveau**. L experience s ajoute seulement pour qui n a pas
d attestation collegiale commencee en 2020 ou apres: trois ans sur cinq en
categorie 1, cinq ans sur huit en categorie 2, avec une assurance propre a
l activite d inspecteur. L experience seule ne suffit jamais.

Le passage a ete reecrit dans les 4 langues le 2026-09-24. Votre ancien article
n a pas ete touche: il etait substantiellement exact, il ne mentionne
simplement pas la condition d experience. Rien a corriger de votre cote.

Source: https://www.rbq.gouv.qc.ca/en/you-are/inspector-pre-purchase/obtaining-a-residential-building-inspector-certificate/

### Deux limites assumees par les redacteurs

- `acheter-zone-inondable-quebec`: les interdictions de construction par classe
  n ont pas ete detaillees, parce que LegisQuebec bloquait la lecture du
  reglement et que l agent a refuse de le paraphraser de memoire. C est la
  bonne decision. Si vous voulez ce detail, il faut lire le reglement.
- `choisir-inspecteur-batiment-quebec`: l affirmation qu aucun ordre
  professionnel n encadre les inspecteurs repose sur l absence d ordre plus le
  caractere encore volontaire du certificat, pas sur une page qui l affirme
  noir sur blanc.

---

## 6. Sujets bloques par la porte anti-doublon

La porte 1 a refuse trois sujets proposes par les planificateurs, chacun parce
qu un article couvrait deja le terrain. C est le comportement attendu, rien a
corriger. La liste est dans `state/content_plan.json`, statut `already_covered`.

| Sujet propose | Bloque parce que |
|---|---|
| `maison-difficile-a-assurer-quebec` | doublon de l article ecrit le meme jour |
| `preparer-refinancement-hypothecaire-quebec` | doublon de l article ecrit le meme jour |
| `declarations-vendeur-formulaire-quebec` | doublon de `declaration-du-vendeur-quebec` |

Deux planificateurs differents ont propose les memes sujets sans le savoir,
puisqu ils travaillaient sur des tranches separees du catalogue de reference.
La porte les a rattrapes au moment de la reclamation.
