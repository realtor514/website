# Lot 9, consignes de traduction par article

Regles generales: `state/BRIEF_TRADUCTION.md`, a lire en entier d abord.
Cartes de liens: `state/internal_links_en.md`, `_es.md`, `_ar.md`.

**La seule source de verite est le fichier francais.** Les listes « a preserver »
ont ete extraites mecaniquement du texte francais. Si un element listé ne s y
trouve pas, ne l inventez pas: signalez-le et traduisez ce qui est ecrit.

**Avant d ecrire un fichier, verifiez qu il n existe pas deja avec un autre
`translationKey`.** Au lot 8, un slug que j avais donne pointait sur un article
publie. Les six slugs de ce lot ont ete verifies libres le 25 septembre, mais
verifiez quand meme: c est votre derniere barriere avant un ecrasement.

**Les six articles portent la meme categorie**, `Guide pratique`:
en `Practical Guide`, es `Guía práctica`, ar `دليل عملي`.

**Cinq des six portent `needs_expert_review: true`.** Seul E3 ne le porte pas.
Recopiez ce qui est dans le francais, jamais autre chose.

**Le drapeau draft.** Ecrivez `draft: true`. Une etape automatisee passera
ensuite les fichiers en `draft: false`. Ne le remettez jamais a true, et ne
retouchez pas `lastmod` apres l avoir ecrit.

**Aucun lien entre les six articles de ce lot.** Ils sont tous en brouillon,
donc un lien entre eux renvoie 404.

**Absolu:** zero tiret long, demi-cadratin ou double tiret. Longueur a 15 % du
francais, sauf l arabe ou 80 % suffit. Chiffres en caracteres latins en arabe.
Section Questions frequentes gardee, titre dans la langue cible. Noms
d organismes, formulaires, reglements et termes juridiques gardes en francais,
glose a la premiere occurrence. CTA du formulaire: `/en/form/`,
`/es/formulario/`, `/ar/istimara/`.

## Ce qui est commun aux six, et qui compte plus que le reste

Ces six articles reposent sur des **reglements municipaux nommes par leur
numero**. Un numero de reglement ne se traduit pas, ne se reformule pas et ne
s arrondit pas: `15-069`, `12-005`, `RCG 25-011`, `RCG 12-003`, `L-13252`,
`11-010`, `L-11870`. Gardez-les tels quels.

Et surtout: **ces reglements appartiennent a une ville precise.** Montreal et
Laval n ont ni les memes seuils, ni les memes dates, ni les memes amendes. Le
francais le dit article par article. Une traduction qui presente une regle
montrealaise comme une regle quebecoise est fausse et expose Georges.

Enfin, plusieurs de ces articles disent franchement **qu aucune source ne
chiffre quelque chose**. Ces aveux sont le coeur de la voix du site. Ne les
transformez pas en estimation prudente, ne les supprimez pas pour gagner de la
place.

---

## E1. cabanon-abri-auto-garage-permis-quebec

- translationKey `article-cabanon-abri-garage-permis`, date et lastmod **2026-08-26**
- `needs_expert_review: true` present
- fichiers: `content/en/articles/shed-carport-garage-permit-quebec.md`,
  `content/es/articles/permiso-cobertizo-garaje-quebec.md`,
  `content/ar/articles/shed-carport-garage-permit-quebec.md`
- voix: `content/{lang}/articles/renovations-dont-add-value.md`
- a preserver: les montants 92 $, 133 $, 167,40 $, 259,90 $, 400 $, 800 $,
  1 000 $, 1 630,00 $, 2,50 $, 9,80 $ et 20 000 $, chacun rattache a la meme
  ville que dans le francais; la date du 1er juillet 2024; les deux tableaux.
- l expression **construction accessoire** est le pivot du texte: c est le mot
  qui decide si un permis est exige. Gardez le terme francais avec une glose.
- **aucune marge de recul, superficie maximale ni hauteur pour Laval.** L outil
  Info-reglements de Laval est inaccessible a un agent. Le francais explique a
  la place la manoeuvre pour lire sa propre fiche de zonage. N inventez aucun
  chiffre de zonage, et ne transposez pas les chiffres de Montreal a Laval.
- rien sur les distances d un abri d hiver lavallois: elles ne sont publiees
  qu en schemas illustres, sans texte.
- aucun pourcentage de couverture d assurance pour une dependance, et aucun
  chiffre d effet d un cabanon sur le role d evaluation. Les deux aveux restent.

## E2. poele-foyer-bois-reglement-assurance-quebec

- translationKey `article-poele-foyer-bois-reglement`, date et lastmod **2026-09-01**
- `needs_expert_review: true` present
- fichiers: `content/en/articles/wood-stove-rules-insurance-quebec.md`,
  `content/es/articles/estufa-lena-reglamento-seguro-quebec.md`,
  `content/ar/articles/wood-stove-rules-insurance-quebec.md`
- voix: `content/{lang}/articles/hard-to-insure-home-quebec.md`
- a preserver: les reglements **15-069** et **12-005** de Montreal et leurs
  articles 3, 4, 4.1, 5, 6, 7, 8, 10 et 11; les montants 100 $, 500 $,
  1 000 $ et 2 000 $; les dates 17 aout 2015, 1er octobre 2018, 10 mai 2021,
  18 octobre 2021, 15 janvier 2024 et **1er octobre 2026**; les deux tableaux.
- **les deux villes n ont pas la meme regle, c est la moitie de l article.**
  Montreal: seuil de 2,5 g/h, declaration en 120 jours, 19 arrondissements
  seulement. Laval: reglement propre, declaration en 160 jours, et interdiction
  d utiliser au-dela de 7,5 g/h a compter du 1er octobre 2026. Ne fusionnez
  jamais les deux regimes.
- le point le plus utile a un acheteur: la demarche de Montreal etend le delai
  de 120 jours **a l achat de la maison**, ce que le texte du reglement ne dit
  pas. Gardez cette nuance et gardez l attribution a la page de demarche.
- aucune frequence de ramonage presentee comme une obligation: le Code national
  de prevention des incendies n est pas diffuse librement. Le francais s en
  tient a ce que le service de securite incendie publie.
- le francais dit que seules Montreal et Laval ont ete verifiees et interdit la
  transposition aux autres municipalites. Gardez cet avertissement.

## E3. prevention-incendie-assurance-habitation-quebec

- translationKey `article-prevention-incendie-assurance`, date et lastmod **2026-09-07**
- **pas de `needs_expert_review`** dans le francais: ne l ajoutez pas.
- fichiers: `content/en/articles/smoke-alarm-obligation-insurance-quebec.md`,
  `content/es/articles/detector-humo-obligacion-seguro-quebec.md`,
  `content/ar/articles/smoke-alarm-obligation-insurance-quebec.md`
- voix: `content/{lang}/articles/hard-to-insure-home-quebec.md`
- a preserver: le reglement **RCG 12-003**; les articles 1854 et 1866 du Code
  civil du Quebec; les montants 80 $, 250 $, 400 $, 600 $, 1 000 $, 2 000 $ et
  4 000 $; le tableau qui compare Montreal et Laval.
- le pivot du texte: **le formulaire Declarations du vendeur DV 00001 ne parle
  ni d avertisseur, ni de fumee, ni de monoxyde de carbone.** Seule la question
  D14.1 parle d incendie. C est verifie sur les 13 pages du formulaire. Ne
  laissez pas la traduction suggerer une obligation de declaration qui
  n existe pas.
- deuxieme nuance a ne pas perdre: le chapitre Batiment du Code de securite de
  la Regie du batiment **ne vise pas la maison unifamiliale detachee**. Pour
  celle-la, seul le reglement municipal decide. Il n y a donc pas d obligation
  provinciale uniforme d avertisseur de monoxyde de carbone.
- le bail obligatoire du Tribunal administratif du logement contient a sa
  section B une clause sur les avertisseurs de fumee, citee textuellement.
  Gardez la citation et gardez le nom francais du bail.
- le francais ne donne aucune statistique sur la proportion d incendies mortels
  sans avertisseur fonctionnel: la source n a pas pu etre ouverte. N ajoutez
  aucun pourcentage.
- ne dites jamais qu un manquement annule automatiquement une couverture.

## E4. sinistres-frequents-couverture-habitation-quebec

- translationKey `article-sinistres-frequents-couverture`, date et lastmod **2026-09-13**
- `needs_expert_review: true` present
- fichiers: `content/en/articles/common-home-insurance-claims-quebec.md`,
  `content/es/articles/siniestros-frecuentes-seguro-hogar-quebec.md`,
  `content/ar/articles/common-home-insurance-claims-quebec.md`
- voix: `content/{lang}/articles/hard-to-insure-home-quebec.md`
- a preserver: les articles 2408, 2410, 2411, 2466, 2467, 2468, 2470, 2472,
  2473 et 2475 du Code civil, chacun rattache au meme sujet que dans le
  francais; le renvoi 3.03.02 et le reglement 11-010; les montants 40 $, 200 $,
  300 $, 400 $, 600 $, 800 $, 1 000 $, 5 000 $, 25 000 $, 23 550 $ et
  500 000 $; les deux tableaux.
- **la distinction centrale, et elle est technique:** les articles 2408 a 2411
  visent la **declaration initiale** du risque, les articles 2466 a 2468 visent
  l **aggravation** du risque en cours de contrat. Le francais les cite
  separement, exprès. Ne les melangez pas en un seul bloc.
- le coeur du texte: quatre origines de degat d eau, **une seule incluse dans
  la police de base**. Gardez les quatre origines distinctes et gardez les noms
  exacts des trois avenants.
- gardez les trois chiffres du cheque comme trois notions distinctes:
  franchise, montant de garantie de l avenant, valeur a neuf.
- deux aveux a garder tels quels: le francais dit qu aucune source ne confirme
  que les franchises de plusieurs avenants s additionnent lors d un meme
  sinistre, et qu aucune source officielle ne decrit un registre quebecois des
  reclamations tenu par adresse. **Ne comblez ni l un ni l autre.**

## E5. solarium-veranda-permis-evaluation-quebec

- translationKey `article-solarium-veranda-permis-evaluation`, date et lastmod **2026-09-19**
- `needs_expert_review: true` present
- fichiers: `content/en/articles/sunroom-veranda-permit-quebec.md`,
  `content/es/articles/solario-veranda-permiso-quebec.md`,
  `content/ar/articles/sunroom-veranda-permit-quebec.md`
- voix: `content/{lang}/articles/renovations-dont-add-value.md`
- a preserver: l article 16 tel qu il est attribue dans le francais et
  l article 2917 du Code civil; les montants 90 $, 92 $, 100 $, 167,40 $,
  300 $, 2,50 $, 9,80 $, 1 000 $, 20 000 $ et 500 000 $; les dates
  30 aout 2012, 28 novembre 2012 et 1er juillet 2024; les 30 jours contre
  50 jours selon trois ou quatre saisons; le tableau.
- **le pivot: un solarium est un agrandissement de l aire de plancher**, pas un
  projet d amenagement. Permis obligatoire, licence d entrepreneur obligatoire,
  aucun droit acquis. Ne l affaiblissez pas.
- trois saisons contre quatre saisons change le permis, le delai, l evaluation
  et le calcul de la superficie habitable. Gardez les quatre consequences.
- les seuls chiffres de marge cites appartiennent a l arrondissement de
  Riviere-des-Prairies-Pointe-aux-Trembles, et le francais le nomme. Gardez
  cette attribution, n en faites pas une regle montrealaise.
- **aucun pourcentage de plus-value.** Le francais dit qu aucune source
  publique quebecoise ne le chiffre, et traite a la place la hausse de
  l evaluation municipale et donc des taxes. Gardez ce choix.
- gardez le point pratique de la fin: un agrandissement sans permis cree un
  probleme au certificat de localisation et peut bloquer une vente.

## E6. systeme-alarme-domotique-assurance-quebec

- translationKey `article-systeme-alarme-domotique-assurance`, date et lastmod **2026-09-25**
- `needs_expert_review: true` present
- fichiers: `content/en/articles/alarm-system-insurance-discount-quebec.md`,
  `content/es/articles/sistema-alarma-descuento-seguro-quebec.md`,
  `content/ar/articles/alarm-system-insurance-discount-quebec.md`
- voix: `content/{lang}/articles/hard-to-insure-home-quebec.md`
- a preserver: le reglement **RCG 25-011** de Montreal, adopte le 15 mai 2025
  et en vigueur le 21 mai 2025, et le reglement **L-13252** de Laval; les
  articles 2408, 2410 et 2466 du Code civil, et les articles 35 et 36 pour la
  vie privee; les montants 96 $, 146 $, 191 $, 500 $ pour Montreal et 114 $,
  145 $, 177 $, 1 000 $ pour Laval, sans les melanger; les 250 $; le tableau.
- **le titre promet un rabais et l article commence par dire qu il n existe
  aucun chiffre public.** C est voulu. Le francais cite l Autorite des marches
  financiers, qui ecrit de demander le montant du rabais avant l installation,
  et le Bureau d assurance du Canada, qui parle de primes reduites sans
  pourcentage. **N ajoutez aucun pourcentage de rabais.** C est le point le plus
  facile a trahir dans ce lot.
- le compteur de fausses alarmes de Montreal se remet a zero apres un an,
  celui de Laval fonctionne dans une fenetre de 183 jours. Deux mecaniques
  differentes, a garder distinctes.
- ni Montreal ni Laval n exige d enregistrer le systeme, et Laval precise
  qu aucun permis n est requis. Gardez cette precision.
- correction juridique a preserver: la Loi sur la protection des
  renseignements personnels dans le secteur prive vise les **entreprises**, pas
  le voisin qui filme. Pour la camera d un particulier, le francais renvoie aux
  articles 35 et 36 du Code civil. Ne retablissez pas la version courante.
- le francais mentionne le Bureau de la securite privee, parce que la reponse
  d alarme exige un permis d agence et un permis d agent. Gardez le nom
  francais de l organisme avec une glose.
- deux autres aveux a garder: aucune source ne dit qu un vol sans effraction
  serait exclu d une police residentielle, et rien ne chiffre l effet d une
  serrure connectee.
