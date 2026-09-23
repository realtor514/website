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

Ces articles portent `needs_expert_review: true` dans leur front matter. Ils
restent en brouillon. Le contenu est sourcé, mais la matiere est fiscale,
juridique ou assurantielle et merite une relecture avant mise en ligne.

Ces articles sont sources et verifies, mais la matiere est fiscale, juridique
ou assurantielle. Ils restent en `draft: true` jusqu a votre feu vert, meme
quand leurs traductions sont pretes.

| Slug | Sujet | Qui devrait relire | Etat |
|---|---|---|---|
| impot-proprietaire-quebec | Residence principale, depenses deductibles, changement d usage | comptable ou fiscaliste | dans content/, brouillon |
| acheter-zone-inondable-quebec | Nouveau cadre des zones inondables, assurance, financement | assureur ou courtier hypothecaire | dans content/, brouillon |
| vente-sans-garantie-legale-quebec | Garantie legale de qualite et son exclusion | notaire | brouillon |
| contrat-courtage-vente-quebec | Clauses du contrat de courtage, dont la remuneration apres expiration | vous, puis l agence | brouillon |
| choisir-inspecteur-batiment-quebec | Certification RBQ des inspecteurs, clauses de limitation de responsabilite | vous | brouillon |
| conjoints-de-fait-maison-quebec | Union parentale depuis le 30 juin 2025, indivision, succession | notaire | en redaction |

**Une contradiction entre un nouvel article et un ancien:**

Sur la voie transitoire des inspecteurs en batiment, le nouvel article
`choisir-inspecteur-batiment-quebec` parle de trois ans d experience dans les
cinq dernieres annees plus une preuve d assurance. L article deja en ligne
`content/en/articles/home-inspection-checklist-montreal.md` parle, lui, d un
cours de mise a niveau. Les deux ne peuvent pas etre exacts en meme temps.

Le nouvel article est source et recent, l ancien ne l est pas forcement. Je n ai
pas touche a l ancien: la regle du projet est de ne jamais modifier l existant.
C est a trancher, puis a corriger dans les 4 langues de l article concerne.

**Deux points de vigilance signales par les redacteurs eux-memes:**

- `acheter-zone-inondable-quebec`: les interdictions de construction par classe
  n ont pas ete detaillees, parce que LegisQuebec bloquait la lecture du
  reglement et que l agent a refuse de le paraphraser de memoire. C est la
  bonne decision. Si vous voulez ce detail, il faut lire le reglement.
- `choisir-inspecteur-batiment-quebec`: l affirmation qu aucun ordre
  professionnel n encadre les inspecteurs repose sur l absence d ordre plus le
  caractere encore volontaire du certificat, pas sur une page qui l affirme
  noir sur blanc.

---

## 6. Sujets parques ou deja couverts

Aucun pour l instant. La porte 1 a classe les 14 premiers sujets en `clear`.

Cette section listera: le sujet, l article existant le plus proche, et le score
de similarite qui a motive la decision.
