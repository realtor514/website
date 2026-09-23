# Ce qui demande une decision de Georges

Mis a jour le 2026-09-23, session 1, branche `auto/blogue-content`.

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

**Le risque est neutralise.** Tous les nouveaux articles sont en `draft: true`,
donc invisibles sur le site. De plus, `tools/approve.py` **refuse** de publier un
article francais tant que les versions en, es et ar n existent pas. Il faut
`--fr-seulement` pour passer outre, volontairement.

Aucune action requise tant que vous publiez avec `tools/approve.py`.

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
| 2026-08-24 | `acheter-reprise-de-finance-quebec` | brouillon | 0 |
| 2026-08-25 | `acheter-zone-inondable-quebec` | en ligne | 4 |
| 2026-08-26 | `choisir-inspecteur-batiment-quebec` | en ligne | 3 |
| 2026-08-27 | `conjoints-de-fait-maison-quebec` | brouillon | 4 |
| 2026-09-02 | `contrat-courtage-vente-quebec` | en ligne | 2 |
| 2026-09-05 | `casser-hypotheque-penalite-quebec` | brouillon | 0 |
| 2026-09-06 | `declaration-du-vendeur-quebec` | en ligne | 3 |
| 2026-09-11 | `copropriete-indivise-cooperative-montreal` | brouillon | 0 |
| 2026-09-14 | `impot-proprietaire-quebec` | en ligne | 5 |
| 2026-09-16 | `location-court-terme-quebec-regles` | en ligne | 4 |
| 2026-09-21 | `vente-sans-garantie-legale-quebec` | en ligne | 4 |
| 2026-09-23 | `vice-cache-conditions-recours-quebec` | brouillon | 0 |

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

Pour retirer un article publie, l inverse n existe pas dans approve.py: mettez
`draft: true` dans les 4 fichiers, puis commit et push.

## 6. Sujets parques ou deja couverts

Aucun pour l instant. La porte 1 a classe les 14 premiers sujets en `clear`.

Cette section listera: le sujet, l article existant le plus proche, et le score
de similarite qui a motive la decision.
