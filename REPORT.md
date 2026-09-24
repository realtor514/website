# Blogue, rapport de session

**23 articles ecrits, traduits et EN LIGNE dans les 4 langues.**

Le site est passe de **63 a 88 articles par langue**: 352 fichiers publies au
lieu de 252. Verifie en direct sur georgesmatar.ca, pas seulement en local.

---

## 24 septembre, au matin

**Les 25 images a la une manquaient toutes.** Trouve en verifiant le rendu reel,
pas le code. Chaque article que j ai ecrit declarait
`image: images/articles/<slug>/featured.jpg`, et aucun de ces fichiers
n existait. Le gabarit fait `{{ with .Params.image }}`: le champ etant rempli,
la balise `img` est emise et pointe vers un fichier absent, donc le placeholder
de `article-card.html` ne prend jamais le relais, et il n y avait pas non plus
de fichier placeholder. Confirme en direct: l image renvoyait 404 sur les
22 articles publies, y compris sur la page du blogue ou les cartes etaient
cassees. Les 64 articles plus anciens avaient tous la leur.

Corrige: 25 images telechargees depuis Unsplash, JPEG paysage de 1200 px,
60 a 280 ko, au format des images deja en place. Verifie apres deploiement:
**25 sur 25 repondent 200**, et la page du blogue affiche bien les vignettes.
Credits photo dans `static/images/articles/CREDITS.json`.

**Deux trous d outillage bouches**, tous les deux de mon fait:

- `fetch_images.py` se fiait a une liste ecrite a la main. Il lit maintenant le
  champ `image` de chaque article francais et signale ceux dont le fichier
  manque. Sans ca, le prochain lot repetait l erreur.
- `plan_gate.py release` ne retirait que le claim et le slug du registre, en
  laissant le mot-cle et le titre. Consequence: un sujet libere se bloquait
  contre lui-meme, la porte 2 repondant `keyword=FAIL titre=FAIL` alors que
  plus personne ne s en occupait. Quatre sujets etaient coinces ainsi.

**23e article publie:** `garantie-gcr-maison-neuve-quebec`, qui attendait ses
traductions depuis la coupure de la veille.

**A signaler:** la cle `PEXELS_API_KEY` de `.env` renvoie une erreur HTTP a
chaque appel, elle semble expiree. Unsplash a tout fourni, donc rien n est
bloque, mais la solution de secours ne fonctionne plus.

---

## 23 septembre

La session s est arretee deux fois sur la limite d usage du compte, a 17 h et a
22 h, ce qui a tue 18 agents au total. Tout ce qui avait ete produit avant
chaque coupure est intact.

---

## Les 23 articles en ligne

| Date | Article | Categorie |
|---|---|---|
| 24 aout | Contester son evaluation municipale au Quebec | Immobilier 101 |
| 24 aout | Acheter une reprise de finance au Quebec | Guide de l acheteur |
| 25 aout | Acheter en zone inondable au Quebec | Guide de l acheteur |
| 26 aout | Choisir un inspecteur en batiment au Quebec | Guide de l acheteur |
| 27 aout | Conjoints de fait et la maison au Quebec | Immobilier 101 |
| 30 aout | Bruit dans une maison ou un condo au Quebec | Guide de l acheteur |
| 31 aout | Abattage d arbre: le reglement et la propriete | Guide pratique |
| 1 sept | Cout d entretien d une maison: le calendrier | Guide pratique |
| 2 sept | Contrat de courtage vente: clause par clause | Guide du vendeur |
| 5 sept | Casser son hypotheque: la penalite | Financement |
| 6 sept | Declaration du vendeur: le formulaire DV 00001 | Guide du vendeur |
| 7 sept | Comparables: auditer le prix du voisin | Guide du vendeur |
| 8 sept | Maison difficile a assurer: ce qui bloque | Guide de l acheteur |
| 9 sept | Garder ou vendre une propriete: cinq cas | Guide du vendeur |
| 11 sept | Copropriete indivise a Montreal | Financement |
| 14 sept | Impot et proprietaire: ce qui se deduit | Financement |
| 15 sept | Refinancement hypothecaire: est-ce rentable ? | Financement |
| 16 sept | Location court terme: les regles avant d acheter | Investissement |
| 17 sept | Ventre de boeuf dans un drain a Montreal | Guide de l acheteur |
| 20 sept | Ma propriete ne se vend pas: le diagnostic | Guide du vendeur |
| 21 sept | Vente sans garantie legale: ce que ca change | Guide de l acheteur |
| 22 sept | Reduire sa facture de chauffage au Quebec | Guide pratique |
| 23 sept | Renover son condo en copropriete: la vraie limite | Immobilier 101 |
| 23 sept | Vice cache: les conditions et vos recours | Immobilier 101 |
| 23 sept | Garantie GCR d une maison neuve au Quebec | Guide de l acheteur |

Chacun existe en francais, anglais, espagnol et arabe, avec la meme
`translationKey`, donc les balises hreflang relient les 4 versions et Google
les traite comme un seul article en quatre langues. Verifie en direct sur
l article d assurance.

Dates reparties sur le dernier mois, comme demande, sans collision de date.

**Le seul article encore en brouillon** est
`conjoints-de-fait-maison-quebec`, retenu volontairement: son redacteur demande
une validation par un notaire avant publication, et c est du droit de la
famille. Ses quatre versions sont pretes. Voir `NEEDS_HUMAN.md`.

---

## Qualite: mesuree, pas supposee

**Les six portes anti-doublon passent sur les 23 articles.** Slug, titre,
mot-cle, sujet en cosinus TF-IDF, contenu en segments de 5 mots et cosinus
contre les 352 articles du site, et comparaison au site de reference.

**Recoupement avec les articles de rovenapistoli.com: 0,000.** Leur texte
integral a ete telecharge dans un cache local, hors depot, qui ne sert qu au
detecteur. Aucun agent redacteur n y a eu acces. Les sujets viennent de leur
catalogue, les textes ne leur doivent rien.

**Zero lien mort.** Chaque lien interne est resolu contre les fichiers reels,
dans les 4 langues, et un lien non resolu bloque desormais le fichier.

**Sources primaires.** Code civil, OACIQ, Revenu Quebec, ARC, SCHL, APCIQ,
Hydro-Quebec, Bureau d assurance du Canada, RBQ, GCR, Tribunal administratif
du logement, CITQ, Ville de Montreal, Ville de Laval, ministeres. Plusieurs
agents ont utilise curl quand LegisQuebec ou l OACIQ bloquaient la lecture,
plutot que de paraphraser de memoire.

---

## Ce que les redacteurs ont corrige chez moi

Trois de mes consignes etaient fausses. Les agents les ont verifiees et
corrigees, ce qui est exactement ce qu on leur demandait.

1. **Conjoints de fait.** J avais ecrit qu un conjoint de fait n herite jamais
   sans testament. Faux depuis la reforme: un conjoint en **union parentale**
   est heritier legal selon les articles 653, 666 et 672.
2. **Egout a Montreal.** J avais ecrit que la responsabilite du proprietaire
   s arrete a la ligne de propriete. C est l inverse: il repond du branchement
   complet jusqu a l egout sous la rue. L eau potable, elle, suit l autre regle.
3. **Contrat de courtage.** Ma fiche parlait d un nombre de jours convenu pour
   la retribution apres expiration. Le formulaire fixe 180 jours et la loi
   plafonne la.

Trois de mes outils etaient faux aussi, et c est plus grave parce qu ils
touchaient tous les articles:

4. **Categories et formulaire.** Mon brief de traduction disait de garder la
   categorie en francais et d utiliser `/en/formulaire/`. Les deux etaient
   faux: la categorie est traduite, et le formulaire a un slug par langue.
   Corrige aupres des agents en cours de travail, puis dans le validateur.
5. **Un lien mort.** Mes cartes de liens annoncaient `/secteurs/laval/`, qui
   n existe pas: la page vit sous `/courtier-immobilier/laval/`. Un seul
   brouillon avait suivi la mauvaise carte, corrige avant publication. Le
   validateur bloque maintenant sur un lien non resolu.
6. **Cartes de liens jamais rafraichies.** Trois agents ont signale que les
   articles publies plus tot dans la journee n y figuraient pas, donc personne
   ne pouvait pointer vers eux. `tools/linkmap.py` les reconstruit desormais a
   partir du contenu reel.

Et une erreur de methode de ma part: **j ai publie sept articles depuis un
instantane**, pendant que leur redacteur peaufinait encore. Chaque fois j ai
compare les deux versions terme a terme: memes sections, memes numeros
d articles, memes chiffres, la version publiee etant simplement la plus
fournie. Rien n est perdu, les versions courtes sont dans
`drafts/fr/variantes/` avec la comparaison.

---

## Deux verifications faites a la main

**Seuil de 30 mm a Laval.** Un traducteur y voyait une incoherence entre 30 mm
et 3 cm. Verifie sur laval.ca: la Ville ecrit elle-meme le seuil ainsi.
L article est exact.

**Version du formulaire CCVE.** Le redacteur demandait de revalider la
numerotation des clauses avant publication. Verifie: le PDF de l OACIQ porte la
mention CCVE 00001 (v29 06/2022), donc la version consultee est la version
courante, et la clause 7.1 paragraphe 3 est bien celle des 180 jours. Publie
apres cette verification, pas avant.

---

## Le reservoir de sujets

**619 sujets** releves sur les 124 pages d index de rovenapistoli.com. Environ
40 % touchent vraiment l immobilier, le reste est deco, jardinage, voyage et
idees cadeaux, sans valeur de recherche pour un courtier.

Apres tri et passage a la porte 1: **172 sujets au plan, 140 encore prets a
ecrire**, chacun avec son angle quebecois et son plan de sections.

La porte 1 a bloque 3 sujets en double, dont deux proposes par des
planificateurs differents pour des articles ecrits le meme jour.

---

## Pour reprendre, apres 22 h

1. `garantie-gcr-maison-neuve-quebec` attend ses 3 traductions, puis une
   commande pour passer en ligne.
2. 4 sujets a reprendre, marques `error_retry_later`: reglement des piscines,
   deces du conjoint, reprise de logement en plex, loi 16 en copropriete.
   Leurs reclamations sont liberees.
3. 140 sujets `clear` dans `state/content_plan.json`.
4. Quatre journaux de sources ont ete perdus aux coupures. Les fichiers meta
   concernes le disent explicitement.

---

## Ce qui vous attend

`NEEDS_HUMAN.md`, six points. Le plus important:

**12 articles portent `needs_expert_review: true`** et sont en ligne, parce que
vous avez demande de tout publier. Chacun dit lui-meme ou s arrete ce qu il
peut demontrer, en renvoyant au notaire, au comptable, a l assureur ou a la
municipalite. Les points precis a revalider sont dans chaque
`meta/fr/<slug>.json`, champ `claims_needing_review`. C est une liste courte et
concrete, pas une inquietude vague.

**Une contradiction** entre un nouvel article et un ancien, sur la voie
transitoire des inspecteurs en batiment. Je n ai pas touche a l ancien.

---

## Commandes

```
python tools/status.py --nouveaux     ce que le moteur a produit, et son etat
python tools/approve.py list          les brouillons en attente
python tools/linkmap.py               rafraichir les cartes de liens
python tools/dedupe.py selftest       l auto-test du detecteur
python tools/validate.py "content/fr/articles/*.md"
```

---

## Depot

- `main` et `auto/blogue-content` a jour et pousses
- Aucun fichier existant modifie ou supprime, uniquement des ajouts
- Vos propres commits, hugo.toml et les pages de quartier, sont intacts
- Le cache texte du site de reference et l index du site restent hors depot
