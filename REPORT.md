# Blogue, rapport de session

**Session 1, 2026-09-23. Etat: EN COURS. 5 articles EN LIGNE dans les 4 langues.**

---

## En ligne sur georgesmatar.ca

20 fichiers publies, `draft: false`, verifies en direct sur le site.

| Date | Article | fr | en | es | ar |
|---|---|---|---|---|---|
| 2026-08-24 | Contester son evaluation municipale | oui | oui | oui | oui |
| 2026-09-01 | Cout d entretien d une maison | oui | oui | oui | oui |
| 2026-09-08 | Maison difficile a assurer | oui | oui | oui | oui |
| 2026-09-15 | Refinancement hypothecaire | oui | oui | oui | oui |
| 2026-09-23 | Renover son condo en copropriete | oui | oui | oui | oui |

Dates reparties sur le dernier mois, comme demande. Le site compte maintenant
**68 articles par langue**, contre 63 au debut de la session.

**Verifie en direct, pas seulement en local:**
- `https://georgesmatar.ca/articles/maison-difficile-assurer-quebec/` repond, titre correct, date du 8 septembre affichee.
- `https://georgesmatar.ca/en/articles/hard-to-insure-home-quebec/` repond, et ses balises hreflang pointent bien vers les versions fr, es et ar. Les 4 versions sont donc reliees pour Google.

**Resultat des portes, 5 articles sur 5:** slug, titre, mot-cle, sujet, contenu
et comparaison au site de reference, tous PASS. Recoupement avec les articles
de reference: **0,000**. Les 20 fichiers passent la validation sans erreur.

---

## Deux vraies erreurs attrapees en cours de route

**1. Le site localise plus que je ne le croyais.** Mon brief de traduction
disait de garder la categorie en francais et d utiliser `/en/formulaire/`.
Les deux etaient faux: la categorie est traduite (`Buyer's Guide`,
`Guía del Comprador`, `دليل المشتري`), et le formulaire a un slug par langue
(`/en/form/`, `/es/formulario/`, `/ar/istimara/`). Corrige aupres des cinq
agents en cours de travail, puis dans le validateur et dans le brief, pour que
ca ne revienne pas. Deux agents avaient de leur cote signale l erreur.

**2. Les agents ont remis mes publications en brouillon.** En terminant apres
la mise en ligne, trois agents ont vu `draft: false` sur leurs fichiers, ont
conclu a une corruption et ont remis `draft: true`. Le raisonnement etait bon,
l alerte etait la bonne chose a faire, mais le passage en ligne etait voulu.
Repasse en `draft: false` une fois tous les agents arretes, puis verifie
fichier par fichier.

---

## Ce qui tourne en ce moment

10 agents redacteurs, deux lots de cinq:
impot du proprietaire, zone inondable, facture de chauffage, arbres et
reglements, comparables, garder ou vendre, vente sans garantie legale,
location court terme, choisir un inspecteur, contrat de courtage.

---

## Le reservoir de sujets

**121 sujets `clear`**, chacun avec son angle quebecois et son plan de
sections, tires des 619 articles releves sur le site de reference.

La porte 1 a rejete 2 sujets proposes en double des articles deja ecrits dans
cette session, ce qui est exactement son role.

Un lot de 155 titres reste a planifier (`state/reference_topics/chunk-2.txt`).

---

## Phase 0

| Element | Resultat |
|---|---|
| Mode multilingue | `by_dir`, 4 langues, francais a la racine |
| Articles au depart | 63 par langue, 252 au total |
| Schema de front matter | appris sur vos 5 articles les plus recents |
| Auto-test du detecteur | PASS |
| Sujets de reference releves | 619 uniques, 124 pages d index |

---

## Builds

`hugo` n est pas installe sur ce poste. `tools/validate.py` le remplace en
local et resout chaque lien interne contre les fichiers reels, dans les
4 langues. Le vrai build tourne dans GitHub Actions a chaque push sur `main`,
et il est passe: les pages repondent en ligne.

---

## Depot

- `main` et `auto/blogue-content` sont a jour et pousses
- Aucun fichier existant modifie ou supprime, uniquement des ajouts
- Vos propres commits (hugo.toml, pages de quartier) sont intacts

Voir `NEEDS_HUMAN.md` pour les points qui demandent votre avis. Aucun ne
bloque la production.
