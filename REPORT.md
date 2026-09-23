# Blogue, rapport de session

**Session 1, 2026-09-23. Branche `auto/blogue-content`. Etat: INTERROMPUE.**

La session s est arretee sur une limite d usage du compte, pas sur une erreur du
travail. Onze agents tournaient en parallele et ont tous ete coupes en meme
temps. Tout ce qui avait ete produit avant la coupure est intact et verifie.

---

## 5 articles francais produits, verifies, deposes en brouillon

Chacun a passe les six controles de doublon et la validation complete. Aucun
n est visible sur le site: ils portent tous `draft: true`.

| Date | Article | Mots | Categorie |
|---|---|---|---|
| 2026-08-24 | Contester son evaluation municipale au Quebec | 1 684 | Immobilier 101 |
| 2026-09-01 | Cout d entretien d une maison au Quebec: le calendrier | 1 823 | Guide pratique |
| 2026-09-08 | Maison difficile a assurer au Quebec: ce qui bloque | 1 834 | Guide de l acheteur |
| 2026-09-15 | Refinancement hypothecaire au Quebec: est-ce rentable ? | 1 900 | Financement |
| 2026-09-23 | Renover son condo en copropriete au Quebec: la vraie limite | 1 803 | Immobilier 101 |

Total: 9 044 mots. Dates reparties sur le dernier mois, comme demande.

**Resultat des portes, 5 articles sur 5:**

```
slug=PASS  titre=PASS  mot-cle=PASS  sujet=PASS  contenu=PASS  reference=PASS
5 PASS, 0 REVIEW, 0 FAIL
```

Le controle `reference` compare chaque texte aux articles du site de reference,
segment de 5 mots par segment de 5 mots. Recoupement mesure: **0,000**. Ces
articles ne doivent rien au site de reference au-dela du sujet.

---

## Ce qui a ete coupe en vol

| Travail | Etat | Ou ca reprend |
|---|---|---|
| 5 articles (impot proprietaire, zone inondable, facture de chauffage, arbres, comparables) | agents tues pendant la recherche | sujets remis a `error_retry_later`, reclamations liberees dans le registre |
| Plan de sujets, lots 1, 2 et 4 | agents tues avant d ecrire | `state/reference_topics/chunk-1.txt`, `chunk-2.txt`, `chunk-4.txt` sont prets a rejouer |
| Journal de sources de 4 articles | perdu | voir plus bas |

**Le journal de sources.** Quatre agents ont fini leur article mais ont ete
coupes avant d ecrire leur fichier `meta/fr/*.json`. Les articles citent leurs
sources dans le corps du texte, souvent entre guillemets et nommement. Les
fichiers meta correspondants le disent explicitement plutot que de faire semblant.
Seul `contester-evaluation-municipale-quebec.json` contient le journal complet,
avec 2 affirmations signalees par son auteur comme derivees plutot que lues.

---

## Phase 0, terminee

| Element | Resultat |
|---|---|
| Mode multilingue | `by_dir`, 4 langues, francais a la racine |
| Articles existants | 63 par langue, 252 au total, deux methodes de comptage d accord a 0 % |
| Schema de front matter | appris sur vos 5 articles les plus recents, reproduit a l identique |
| Style de lien interne | chemin markdown simple, pas de shortcode |
| Auto-test du detecteur | PASS |
| Sujets de reference releves | 619 uniques, sur les 124 pages d index |
| Sujets planifies et passes a la porte 1 | 14 clear, plus 42 du lot 3 en attente |

---

## Le site de reference

619 sujets releves sur `rovenapistoli.com/fr/articles`. Environ 40 % touchent
vraiment l immobilier, le reste est de la deco, du jardinage, du voyage et des
idees cadeaux, sans valeur de recherche pour un courtier.

Le texte integral de 14 articles de reference est dans `state/reference_cache/`,
**hors depot** (un `.gitignore` local l exclut, le depot est public). Il ne sert
qu au detecteur de plagiat. Aucun agent redacteur n y a eu acces.

---

## Builds Hugo

Aucun. `hugo` n est pas installe sur ce poste, le site est bati par GitHub
Actions avec Hugo 0.155.0. `tools/validate.py` le remplace en local: les
5 articles passent, y compris la resolution de **chaque lien interne** contre
les fichiers reellement presents dans `content/`.

---

## Pour reprendre

La limite se libere a 17 h, heure de Toronto. Il n y a rien a reparer avant.

1. 5 sujets deja ecrits et deposes, rien a refaire.
2. 5 sujets a reprendre: ils sont en `error_retry_later` dans
   `state/content_plan.json`, leurs reclamations sont liberees.
3. 4 sujets encore `clear` dans le plan: bruit, particularites des maisons
   quebecoises, garder ou vendre, valeur du terrain.
4. 42 sujets prets dans `state/reference_topics/plan-3.json`, a passer a la porte 1.
5. Les lots 1, 2 et 4 de sujets restent a planifier.
6. Phase 3, traductions en, es et ar: rien de commence. Tant qu elles manquent,
   `tools/approve.py` refuse de publier les articles francais.

---

## Ce qui vous attend, vous

`NEEDS_HUMAN.md`, 6 points. Aucun ne bloque la production.

Le plus important: **rien n est en ligne**. Pour publier apres relecture:

```
python tools/approve.py list
python tools/approve.py show maison-difficile-assurer-quebec
python tools/approve.py approve maison-difficile-assurer-quebec
```

Deux articles portent `needs_expert_review: true` dans le plan et ne sont pas
encore ecrits: impot du proprietaire et zone inondable.

---

## Depot

- Branche: `auto/blogue-content`, jamais `main`
- Dernier commit d outillage: `bc8e9fc`
- Aucun fichier existant modifie ou supprime. Uniquement des ajouts.
- Non pousse vers `origin` pour l instant.
