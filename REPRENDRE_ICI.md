# REPRENDRE ICI

Fiche de reprise du moteur de contenu du blogue. Ecrite le 2026-09-25 pour
qu une session neuve puisse continuer sans rien redecouvrir. Lire ce fichier en
entier avant d agir.

---

## 1. Ou en est le travail

**58 articles ecrits, traduits en 4 langues et EN LIGNE.** Le site est passe de
**63 a 121 articles par langue**, soit 484 fichiers publies au lieu de 252.

- Depot: `realtor514/website`, branche de travail `auto/blogue-content`, fusionnee
  et poussee dans `main`. Le site se deploie par GitHub Actions a chaque push sur
  `main`, en environ 30 secondes.
- Repertoire du projet:
  `C:\Users\georg\OneDrive\A_personal\career\ciq25\ciqq\remax du cartier\website`
- `hugo` n est PAS installe sur ce poste. `tools/validate.py` remplace le build.

Etat chiffre a tout moment:

```
python tools/status.py --nouveaux
```

---

## 2. La chose a faire en premier

**Cinq articles francais sont ecrits, passent les six portes, ont leur image, et
attendent uniquement leurs traductions en, es et ar.** Leurs traducteurs ont ete
coupes par la limite de session du 2026-09-24.

| slug francais | translationKey | date | categorie | needs_expert_review |
|---|---|---|---|---|
| `acheter-pour-demolir-permis-quebec` | `article-demolition-reconstruction` | 2026-08-29 | Investissement | oui |
| `renover-hiver-permis-montreal-laval` | `article-renovation-hiver-permis` | 2026-09-13 | Guide pratique | oui |
| `cle-en-main-ou-a-renover-quebec` | `article-turnkey-vs-fixer` | 2026-09-24 | Guide de l'acheteur | oui |
| `vrai-cout-piscine-residentielle-quebec` | `article-pool-true-cost` | 2026-09-24 | Guide pratique | oui |
| `troubles-de-voisinage-quebec` | `article-neighbour-disputes` | 2026-09-25 | Guide pratique | oui |

Pour chacun, lancer UN agent de traduction (voir la consigne type en section 5),
puis:

```
python tools/release.py --check     # montre ce qui est publiable
python tools/release.py             # valide, aligne lastmod, publie, refait les cartes
git add -A content/ state/ && git commit && git push origin main
```

Trois de ces cinq ont perdu leur journal de sources a la coupure. Leurs fichiers
`meta/fr/*.json` le disent explicitement au lieu de faire semblant. Ne pas
inventer de journal.

---

## 3. La boucle de production, une fois par article

1. **Choisir un sujet** dans `state/content_plan.json` avec `status: clear`.
   Les plus utiles d abord, voir section 7.
2. **Reclamer** le sujet, ce qui fait passer la porte 2:
   `python tools/plan_gate.py claim t123`
3. **Lancer un agent redacteur.** Consigne type en section 4.
4. **Attendre que l agent signale sa fin.** Ne jamais publier avant: un agent
   qui peaufine encore reecrit son fichier, et on publie alors un instantane.
   Le signe fiable est la presence de `meta/fr/<slug>.json`.
5. **Passer les portes puis copier dans `content/`:**
   ```
   python tools/publish.py check --slugs <slug>
   python tools/publish.py run --slugs <slug>
   mv drafts/fr/<slug>.md drafts/fr/publies/<slug>.md
   ```
6. **Telecharger l image:** `python tools/fetch_images.py`
7. **Lancer un agent de traduction.** Consigne type en section 5.
8. **Publier:** `python tools/release.py`, puis commit et push.

Un agent bloque ou tue se nettoie avec
`python tools/plan_gate.py release t123`, qui libere le claim, le slug, le
mot-cle ET le titre. Oublier les deux derniers fait que le sujet se bloque
contre lui-meme a la tentative suivante.

---

## 4. Consigne type pour un agent redacteur

Un agent, un article. Garder la consigne courte: le detail vit dans les fichiers.

```
Write ONE original French article for a Quebec real estate broker's Hugo blog.

Working directory: C:\Users\georg\OneDrive\A_personal\career\ciq25\ciqq\remax du cartier\website

READ FIRST: state\BRIEF.md, state\internal_links_fr.md (use ONLY those paths,
never link an article marked (brouillon); city pages are
/courtier-immobilier/<ville>/), and the object with "id":"tXX" in
state\content_plan.json (its unique_angle, planned_h2, slug, translationKey,
category and target_keyword_fr are the assignment). Read <1 or 2 published
articles that are adjacent> and link to them rather than repeating them.

date and lastmod: <aujourd hui>. Add needs_expert_review: true just before
draft: true  [seulement si juridique, fiscal, assurance ou hypothecaire]

FORBIDDEN: rovenapistoli.com or any competing broker blog. Sources: <lister les
sources primaires attendues>. Verify with WebSearch/WebFetch, curl via Bash if a
site blocks.

<3 a 6 lignes sur l angle exact, ce qu il faut couvrir, et ce qu il ne faut pas
repeter d un article voisin>

Never state a figure you have not sourced. Never promise a price or a delay.

DELIVERABLES per BRIEF.md section 10: drafts\fr\<slug>.md and
meta\fr\<slug>.json (5+ sources, each really opened).
1200 to 1800 words. ZERO em dashes, en dashes or double hyphens.

Return only: the two paths, the word count, 3 lines on your angle.
```

---

## 5. Consigne type pour un agent de traduction

```
Localize ONE French article into English, Spanish and Arabic.

Working directory: C:\Users\georg\OneDrive\A_personal\career\ciq25\ciqq\remax du cartier\website

Read in full: state\BRIEF_TRADUCTION.md (the French article is the ONLY source of
truth: if anything I name below is absent from it, flag it and do not add it),
then the general rules at the top of state\TRAD_LOT6.md.

Source: content\fr\articles\<slug>.md
Link maps: state\internal_links_en.md, state\internal_links_es.md, state\internal_links_ar.md
Voice: content\en\articles\<un article proche>.md and its es and ar counterparts.

WRITE EXACTLY THREE FILES:
- content\en\articles\<slug-en>.md
- content\es\articles\<slug-es>.md
- content\ar\articles\<slug-ar, reprend le slug anglais>.md

FRONT MATTER, copying the French schema and field order:
- translationKey: "<cle>" identical in all three
- date and lastmod: <date du francais> in all three
- category: en "<...>", es "<...>", ar "<...>"     [table de conversion dans BRIEF_TRADUCTION.md]
- image: unchanged from the French
- needs_expert_review copie du francais, jamais ajoute
- draft: true

PRESERVE EXACTLY: <lister les numeros d articles de loi, les chiffres, les dates,
les refus de chiffrer, et tout ce qui porte l article>

Return only: the three paths and each word count.
```

Verifier d abord que les slugs cibles sont libres:
`ls content/*/articles/<slug>.md`

---

## 6. Les outils, et ce que chacun fait

| Outil | Role |
|---|---|
| `tools/dedupe.py` | index des articles et six controles de doublon. `selftest` doit passer. |
| `tools/validate.py` | remplace le build Hugo. Front matter, dates, categories par langue, longueur, liens resolus, CTA par langue, et refus d un lien vers un article en draft. |
| `tools/plan_gate.py` | `gate1` classe les sujets, `claim` reserve, `release` libere completement. |
| `tools/publish.py` | porte 4 puis copie vers `content/`, avec repartition des dates sur le dernier mois. `--slugs` cible des articles nommes. |
| `tools/fetch_images.py` | telecharge l image a la une manquante depuis Unsplash. Lit le champ `image` de chaque article, ne se fie a aucune liste. |
| `tools/linkmap.py` | refait les 4 cartes de liens depuis le contenu reel. A relancer apres chaque lot. |
| `tools/release.py` | publie d un coup tout article complet dans les 4 langues, apres validation. |
| `tools/status.py` | l etat du blogue en une commande. |
| `tools/approve.py` | **pour Georges seulement.** Ne jamais le lancer soi-meme sauf pour publier un lot verifie. |

---

## 7. Le reservoir de sujets

`state/content_plan.json`: **107 sujets en `status: clear`**, chacun avec son
angle quebecois et son plan de sections. Ils viennent des 619 articles releves
sur rovenapistoli.com, tries et reancres sur le Quebec.

Les plus utiles en tete de file:

```
t146  acheter-sans-mise-de-fonds-quebec          Financement
t147  bruit-copropriete-recours-montreal         Guide pratique
t148  louer-son-condo-syndicat-tal               Investissement
t151  renouvellement-hypotheque-choc-paiement    Financement
t154  hypotheque-legale-quebec-vente             Immobilier 101
t163  regle-anti-flip-365-jours-quebec           Investissement
t165  aider-son-enfant-acheter-quebec            Financement
t168  empietement-servitude-certificat-localisation  Immobilier 101
```

Liste complete, triee par etape d entonnoir:

```
python -c "import json;p=json.load(open('state/content_plan.json',encoding='utf-8'));rows=[r for r in p['topics'] if r['status']=='clear'];print(len(rows));[print(r['id'],r['slug'],r['category']) for r in rows]"
```

---

## 8. Ce qui a deja mordu, a ne pas refaire

Ces erreurs ont toutes ete commises une fois. Elles sont corrigees dans les
outils, mais le piege reste comprehensible.

1. **Les 25 images manquaient.** Chaque article declare
   `image: images/articles/<slug>/featured.jpg`, et le gabarit fait
   `{{ with .Params.image }}`: un champ rempli pointant vers un fichier absent
   emet une balise `img` cassee, et le placeholder ne prend jamais le relais.
   Toujours lancer `fetch_images.py` avant de publier.
2. **`/secteurs/laval/` n existe pas.** Les pages de ville declarent leur propre
   `url:` et vivent sous `/courtier-immobilier/laval/`. Ne jamais deviner un
   chemin: prendre `state/internal_links_fr.md`, refait par `linkmap.py`.
3. **Le site localise plus qu on ne croit.** La categorie est traduite, et le
   formulaire a un slug par langue: `/formulaire/`, `/en/form/`,
   `/es/formulario/`, `/ar/istimara/`. Tables de conversion dans
   `BRIEF_TRADUCTION.md`.
4. **Un lien vers un article en draft est un lien mort.** Hugo ne rend pas les
   brouillons. Le validateur le refuse desormais.
5. **Ne pas publier un brouillon avant que son agent ait signale sa fin.** Sept
   articles ont ete publies depuis un instantane. A chaque fois j ai compare les
   deux versions terme a terme avant de trancher; les versions courtes sont dans
   `drafts/fr/variantes/`.
6. **Ne jamais mettre dans une consigne de traduction un detail pris dans le
   resume d un redacteur.** C est arrive quatre fois: un decret, une enquete
   datee, un alinea, un terme. Les traducteurs ont refuse d inventer et l ont
   signale. La seule source de verite est l article francais.
7. **`release` doit liberer le mot-cle et le titre**, pas seulement le claim et
   le slug, sinon le sujet se bloque contre lui-meme.
8. **Georges a retire la promesse de service en espagnol le 2026-09-25.** Le site
   existe en espagnol, mais on ne promet que francais, anglais et arabe. Le brief
   est corrige.

Et quatre fois, un redacteur a corrige une de mes consignes fausses: l echeance
des piscines n est pas passee (30 septembre 2027), la responsabilite de l egout
a Montreal va jusqu a l egout sous la rue, la retribution apres expiration est
de 180 jours, et un conjoint en union parentale EST heritier legal.

---

## 9. Limites rencontrees

- **Limite d usage de session**, trois fois: 17 h, 22 h, puis en soiree, avec
  reset annonce a 16 h heure de Toronto. Elle tue tous les agents en cours d un
  coup. Les fichiers deja ecrits survivent.
- **Watchdog**: quatre agents se sont bloques sans rien produire. Meme reponse,
  `plan_gate.py release` puis relancer.
- **Concurrence**: 8 a 13 agents en parallele fonctionne. Au-dela, les blocages
  augmentent.
- **Sites qui bloquent la lecture**: LegisQuebec, OACIQ, Revenu Quebec, la
  Chambre des notaires et Hydro-Quebec renvoient souvent 403 a WebFetch. Les
  agents doivent passer par `curl` via Bash. C est dit dans les consignes.
- **La cle `PEXELS_API_KEY` de `.env` est expiree.** Unsplash fournit tout.

---

## 10. Ce qui attend une decision de Georges

`NEEDS_HUMAN.md` tient la liste a jour. Les deux points ouverts:

1. **45 articles portent `needs_expert_review: true`** et sont en ligne, parce
   que Georges a demande de tout publier. Chacun dit lui-meme ou s arrete ce
   qu il peut demontrer. Les points precis a revalider sont dans chaque
   `meta/fr/<slug>.json`, champ `claims_needing_review`.
2. **Un lien a remettre** si l article sur les conjoints de fait sert de
   reference: voir `NEEDS_HUMAN.md` section 5.

Rien d autre ne bloque la production.

---

## 11. Regles du projet a ne jamais enfreindre

Elles viennent de `CLAUDE.md` a la racine, qui prime sur tout le reste.

1. **Zero tiret long**, em dash, en dash ou double tiret, dans tout ce qui est
   produit, front matter compris.
2. **Les 4 langues.** Aucun article ne passe en ligne avant que ses versions fr,
   en, es et ar existent. `approve.py` refuse de publier un article francais seul.
3. **Ne jamais modifier ni supprimer un fichier existant du site.** Uniquement
   des ajouts. Une exception a ete faite une fois, sur accord explicite de
   Georges, pour corriger une faute factuelle dans un de MES articles.
4. Jamais de commit sur `main` sans que le contenu soit valide, ni de push force.
