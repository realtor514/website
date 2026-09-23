# Blogue, rapport de session

**Session du 2026-09-23. 15 articles ecrits, traduits et EN LIGNE dans les 4 langues.**

Le site est passe de **63 a 78 articles par langue**, soit 312 fichiers publies
au lieu de 252. Tout est verifie en direct sur georgesmatar.ca.

---

## Ce qui est en ligne

| Date | Article | Categorie |
|---|---|---|
| 24 aout | Contester son evaluation municipale au Quebec | Immobilier 101 |
| 25 aout | Acheter en zone inondable au Quebec | Guide de l acheteur |
| 26 aout | Choisir un inspecteur en batiment au Quebec | Guide de l acheteur |
| 31 aout | Abattage d arbre au Quebec: le reglement et la propriete | Guide pratique |
| 1 sept | Cout d entretien d une maison au Quebec: le calendrier | Guide pratique |
| 2 sept | Contrat de courtage vente: clause par clause | Guide du vendeur |
| 7 sept | Comparables immobiliers: auditer le prix du voisin | Guide du vendeur |
| 8 sept | Maison difficile a assurer au Quebec: ce qui bloque | Guide de l acheteur |
| 9 sept | Garder ou vendre une propriete: cinq cas | Guide du vendeur |
| 14 sept | Impot et proprietaire au Quebec: ce qui se deduit | Financement |
| 15 sept | Refinancement hypothecaire: est-ce rentable ? | Financement |
| 16 sept | Location court terme: les regles avant d acheter | Investissement |
| 21 sept | Vente sans garantie legale: ce que ca change | Guide de l acheteur |
| 22 sept | Reduire sa facture de chauffage au Quebec | Guide pratique |
| 23 sept | Renover son condo en copropriete: la vraie limite | Immobilier 101 |

Chacun existe en francais, anglais, espagnol et arabe, avec la meme
`translationKey`, donc les balises hreflang relient bien les 4 versions.
Verifie en direct: la version anglaise de l article sur l assurance pointe
correctement vers ses versions fr, es et ar.

Dates reparties sur le dernier mois, comme demande, sans collision.

---

## Qualite: ce qui a ete mesure, pas suppose

**Les six portes anti-doublon passent sur les 15 articles.** Slug, titre,
mot-cle, sujet (cosinus TF-IDF sur titres et H2), contenu (segments de 5 mots
et cosinus contre les 312 articles du site), et comparaison au site de
reference.

**Recoupement avec les articles de rovenapistoli.com: 0,000.** Le texte
integral de leurs articles a ete telecharge dans un cache local, hors depot,
qui ne sert qu au detecteur. Aucun agent redacteur n y a eu acces. Les sujets
viennent de leur catalogue, les textes ne leur doivent rien.

**Chaque lien interne a ete resolu** contre les fichiers reellement presents,
dans les 4 langues. Aucun lien mort.

**Les sources sont primaires.** Code civil, OACIQ, Revenu Quebec, ARC, SCHL,
APCIQ, Hydro-Quebec, Bureau d assurance du Canada, RBQ, Ville de Montreal,
Ville de Laval, ministeres. Les fichiers `meta/fr/*.json` listent chaque
source avec ce qu elle appuie.

---

## Trois erreurs attrapees, dont deux etaient les miennes

**1. Le site localise plus que je ne le croyais.** Mon brief de traduction
disait de garder la categorie en francais et d utiliser `/en/formulaire/`. Les
deux etaient faux: la categorie est traduite, et le formulaire a un slug par
langue (`/en/form/`, `/es/formulario/`, `/ar/istimara/`). Corrige aupres des
agents en cours de travail, puis dans le validateur et le brief. Deux agents
l avaient signale de leur cote.

**2. J ai publie trois articles depuis un instantane.** Trois redacteurs
peaufinaient encore leur texte quand j ai copie leur fichier. J ai compare les
deux versions terme a terme: la version publiee contient tout ce que contient
la version courte, et parfois davantage. Rien n est perdu, les versions
courtes sont dans `drafts/fr/variantes/` avec l explication. Regle adoptee
ensuite: ne rien publier avant que le redacteur ait signale sa fin.

**3. Ma consigne sur les conjoints de fait etait fausse.** J avais ecrit qu un
conjoint de fait n herite jamais sans testament. Le redacteur a verifie et
corrige: un conjoint en **union parentale** est heritier legal selon les
articles 653, 666 et 672. La nuance est dans l article.

---

## Deux verifications faites a la main

**Le seuil de 30 mm a Laval.** Un traducteur y voyait une incoherence d unites
entre 30 mm et 3 cm. Verifie sur laval.ca: la Ville ecrit elle-meme le seuil
ainsi. L article est exact, aucune correction.

**La version du formulaire CCVE.** Le redacteur demandait de revalider la
numerotation des clauses avant publication. Verifie: le PDF publie par l OACIQ
porte la mention CCVE 00001 (v29 06/2022), donc la version consultee est bien
la version courante, et la clause 7.1 paragraphe 3 est bien celle des
180 jours. L article est parti en ligne apres cette verification, pas avant.

---

## Le reservoir de sujets

**619 sujets** releves sur les 124 pages d index de rovenapistoli.com. Environ
40 % touchent vraiment l immobilier, le reste est de la deco, du jardinage et
des idees cadeaux, sans valeur de recherche pour un courtier.

Apres tri et passage a la porte 1: **172 sujets au plan, 135 encore prets a
ecrire**, chacun avec son angle quebecois et son plan de sections.

La porte 1 a bloque 3 sujets en double, dont deux proposes par des
planificateurs differents pour des articles deja ecrits dans la journee.

---

## Ce qui tourne encore

3 articles francais de plus sont en `content/`, en brouillon, leurs traductions
en cours: conjoints de fait et la propriete, le formulaire Declarations du
vendeur, et la propriete qui ne se vend pas.

5 autres sont en redaction: vice cache, penalite pour casser une hypotheque,
ventre de boeuf dans le drain des plex montrealais, achat d une reprise de
finance, copropriete indivise.

---

## Ce qui vous attend

`NEEDS_HUMAN.md`. Rien n y bloque la production, mais deux points meritent
votre oeil:

1. **Six articles portent `needs_expert_review: true`.** Ils sont en ligne,
   parce que vous avez demande de tout publier, et chacun dit lui-meme ou
   s arrete ce qu il peut demontrer en renvoyant au notaire, au comptable ou a
   l assureur. Les points precis a revalider sont listes dans chaque
   `meta/fr/*.json`, champ `claims_needing_review`.
2. **Une contradiction entre un nouvel article et un ancien**, sur la voie
   transitoire des inspecteurs en batiment. Je n ai pas touche a l ancien.

---

## Commandes utiles

```
python tools/status.py --nouveaux     ce que le moteur a produit, et son etat
python tools/approve.py list          les brouillons en attente
python tools/dedupe.py selftest       l auto-test du detecteur de doublons
python tools/validate.py "content/fr/articles/*.md"
```

`tools/approve.py` refuse de publier un article francais tant que les versions
en, es et ar n existent pas, pour tenir la regle 2 de `CLAUDE.md`.

---

## Depot

- `main` et `auto/blogue-content` a jour et pousses
- Aucun fichier existant modifie ou supprime, uniquement des ajouts
- Vos propres commits, hugo.toml et les pages de quartier, sont intacts
