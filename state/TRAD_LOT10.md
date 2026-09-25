# Lot 10, consignes de traduction par article

Regles generales: `state/BRIEF_TRADUCTION.md`, a lire en entier d abord, y
compris la section sur le **separateur decimal en arabe**, ajoutee hier.
Cartes de liens: `state/internal_links_en.md`, `_es.md`, `_ar.md`.

**La seule source de verite est le fichier francais.** Les listes « a preserver »
sont extraites mecaniquement et **elles se trompent regulierement** sur la ville
ou l organisme auquel un numero se rattache. Au lot 9, les trois traducteurs ont
trouve les memes quatre erreurs dans ma consigne. Quand ma liste et le fichier
francais divergent, **suivez le francais et signalez-le.**

**Avant d ecrire un fichier, verifiez qu il n existe pas deja avec un autre
`translationKey`.** Les 18 slugs de ce lot ont ete verifies libres le
25 septembre, mais verifiez quand meme.

**`needs_expert_review: true` est present dans les six.** Recopiez-le.

**Le drapeau draft.** Ecrivez `draft: true`. Une etape automatisee passera
ensuite les fichiers en `draft: false`.

**Aucun lien entre les six articles de ce lot.** Ils sont tous en brouillon.

**Absolu:** zero tiret long, demi-cadratin ou double tiret. Longueur a 15 % du
francais, sauf l arabe ou 80 % suffit. Section Questions frequentes gardee.
Noms d organismes, formulaires, reglements et articles de loi gardes en
francais, glose a la premiere occurrence. CTA: `/en/form/`, `/es/formulario/`,
`/ar/istimara/`.

## Ce qui est commun aux six, et qui compte plus que le reste

**1. Les numeros d articles du Code civil ont ete lus, pour de vrai.** Ils
viennent de `tools/ccq.py`, qui lit le texte officiel par capture d archive.
Chaque numero est rattache a une regle precise dans le francais. Ne deplacez
aucun numero d un paragraphe a l autre, n en ajoutez aucun, n en retirez aucun.

**2. Les sections du formulaire Declarations du vendeur sont exactes et
verifiees page par page.** `D7.3`, `D3.1`, `D13.2` et les autres ont ete lues
dans le formulaire DV 00001 version 06/2022. Un redacteur a trouve que la
section `D5.4` que ma fiche annoncait **n existe pas**. Recopiez les codes tels
quels, ne les renumerotez pas, n en inventez aucun.

**3. Ces six articles disent souvent qu une chose n est pas chiffrable.** Aucun
cout de reparation de fondation, aucun seuil de largeur de fissure, aucun seuil
de concentration de moisissure, aucun tarif de deneigement, aucune plus-value
d adaptation, aucun pourcentage de depassement de budget. Ces aveux sont la voix
du site. Ne les transformez pas en estimation prudente.

**4. Deux mesures publiques sont fermees ou incertaines, avec leur date.** Ne
les presentez jamais comme ouvertes. Le francais donne la date et renvoie le
lecteur a la Ville: gardez les deux mouvements.

---

## F1. adapter-maison-vieillir-chez-soi-quebec

- translationKey `article-adaptation-domicile-aines`, date et lastmod **2026-08-26**
- categorie: en `Practical Guide`, es `Guía práctica`, ar `دليل عملي`
- fichiers: `content/en/articles/aging-in-place-home-adaptation-quebec.md`,
  `content/es/articles/adaptar-vivienda-envejecer-quebec.md`,
  `content/ar/articles/aging-in-place-home-adaptation-quebec.md`
- voix: `content/{lang}/articles/home-maintenance-cost-quebec.md`
- a preserver: les renvois 1029.8.61.5 et 1029.8.61.101 de la Loi sur les impots;
  la norme CAN/CSA-B613; les montants 250 $, 10 000 $, 12 000 $, 19 500 $,
  20 000 $, 25 500 $, 50 000 $, 72 465 $ et 117 395 $; les dates
  **1er avril 2025**, 13 juillet 2025, 30 juin 2026, **12 aout 2026** et
  30 juin 2027; le tableau.
- **le point le plus important de l article, et le plus facile a trahir:** le
  programme municipal d adaptation de domicile de Montreal **n accepte plus de
  nouvelles demandes depuis le 1er avril 2025**, l entente avec Quebec n ayant
  pas ete renouvelee. Tout passe par le programme de la Societe d habitation du
  Quebec. Une traduction qui laisse croire que la Ville traite encore des
  demandes envoie un aine au mauvais guichet.
- le programme de la SHQ **n a aucun critere d age**: il repose sur une
  incapacite significative et persistante. Ne le presentez pas comme une aide
  reservee aux aines, meme si l article parle de vieillir chez soi.
- il y a **quatre aides distinctes** et une seule paie les travaux. Gardez les
  quatre separees et gardez cette hierarchie.
- la sous-categorie de licence 14.2 vise l entrepreneur en appareils elevateurs
  pour personnes handicapees. Gardez le numero exact.
- le francais ne donne aucun taux de conversion pour le credit federal, parce
  que la page de l Agence du revenu du Canada ne le publie pas. N en ajoutez pas.
- aucune plus-value chiffree: le francais ecrit qu aucune source officielle ne
  permet de chiffrer l effet d une adaptation sur le prix de vente.

## F2. budget-grosse-renovation-financement-quebec

- translationKey `article-budget-grosse-renovation`, date et lastmod **2026-09-01**
- categorie: en `Finance`, es `Financiamiento`, ar `تمويل`
- fichiers: `content/en/articles/financing-major-renovation-quebec.md`,
  `content/es/articles/financiar-renovacion-mayor-quebec.md`,
  `content/ar/articles/financing-major-renovation-quebec.md`
- voix: `content/{lang}/articles/renovations-dont-add-value.md`
- a preserver: les articles 2107, 2108, 2109, 2111, 2114, 2125, 2129, 2724,
  2726, 2727, 2728 et 2952 du Code civil, chacun a sa place; les montants
  15 000 $, 15 000,01 $, 20 000 $, 40 000 $, 74 999,99 $, 75 000 $,
  99 999,99 $, 100 000 $ et 150 000 $; les deux tableaux.
- **les deux mecanismes qui font l article, et qui ne se recouvrent pas:**
  1. le cautionnement de licence de la Regie du batiment est un **plafond
     partage**, pas un remboursement: il indemnise tous les reclamants de la
     periode au prorata, le dossier reste ouvert six mois, et un cautionnement
     epuise ne donne plus rien. Il **exclut les creances des personnes qui ont
     participe aux travaux**, donc un sous-traitant impaye.
  2. l hypotheque legale de la construction passe **devant toute autre
     hypotheque publiee** pour la plus-value, article 2952.
  Ne fusionnez jamais les deux protections, et ne laissez pas entendre que le
  cautionnement rembourse integralement.
- l article 2114 attache une **presomption de reception** au paiement d une
  phase. C est une clause a ecrire au contrat, et c est presente comme tel.
- aucun pourcentage de depassement « typique », aucun taux de credit, aucun
  montant de reserve pour imprevus. Le francais le dit et s appuie seulement sur
  l exigence faite au preteur d evaluer la capacite a couvrir les depassements.

## F3. deneigement-chute-glace-responsabilite-quebec

- translationKey `article-deneigement-responsabilite`, date et lastmod **2026-09-07**
- categorie: en `Practical Guide`, es `Guía práctica`, ar `دليل عملي`
- fichiers: `content/en/articles/snow-removal-liability-quebec.md`,
  `content/es/articles/remocion-nieve-responsabilidad-quebec.md`,
  `content/ar/articles/snow-removal-liability-quebec.md`
- voix: `content/{lang}/articles/hard-to-insure-home-quebec.md`
- a preserver: les articles 976, 1457, 1465, 1467, 1474, 1854, 1864 et 2930 du
  Code civil; les reglements **L-6070** et **L-12767** de Laval; les montants
  107 $, 116 $, 29 $, 100 $, 4 000 $ et **2 000 000 $**; la date du
  26 fevrier 2025; les deux tableaux.
- **le coeur de l article est un tableau a trois regimes**, et il se perd
  facilement a la traduction: sous 1457 c est la victime qui prouve la faute,
  sous 1465 c est le gardien du bien qui doit prouver l absence de faute, et
  1467 vise la ruine meme partielle d un batiment. Gardez les trois charges de
  preuve distinctes: c est toute la valeur du texte.
- **les reglements municipaux ne visent que le domaine public.** Le francais dit
  explicitement qu ils n encadrent pas le depot de neige sur le terrain du
  voisin, et renvoie a 1457 et 976 pour ce cas. Ne laissez pas la traduction
  suggerer une amende municipale pour la neige poussee chez le voisin.
- Laval exige un **permis de tout deneigeur prive**, avec preuve d assurance
  responsabilite de 2 000 000 $ et vignette au pare-brise. Montreal a un regime
  different, d arrondissement. Ne les melangez pas.
- l amende de 100 $ a 4 000 $ est celle de **Saint-Leonard**, et le francais
  l attribue ainsi dans le tableau. Gardez l attribution.
- le francais ne chiffre aucun tarif de contrat de deneigement et aucune
  franchise de responsabilite civile, faute de source. Gardez les deux aveux.

## F4. fissures-affaissement-fondation-expertise-quebec

- translationKey `article-foundation-cracks-expertise`, date et lastmod **2026-09-13**
- categorie: en `Practical Guide`, es `Guía práctica`, ar `دليل عملي`
- fichiers: `content/en/articles/foundation-cracks-diagnosis-quebec.md`,
  `content/es/articles/grietas-cimientos-diagnostico-quebec.md`,
  `content/ar/articles/foundation-cracks-diagnosis-quebec.md`
- voix: `content/{lang}/articles/home-inspection-checklist-montreal.md`
- a preserver: les articles 1726, 1739, 2118, 2925 et 2926 du Code civil; les
  sections **D2.13, D2.14, D3.1, D3.2, D5.2, D13.2 et D15** du formulaire
  Declarations du vendeur, telles quelles; la graphie **CTQ M-200** de l OACIQ;
  les montants 5 000 $ et 35 000 $; la date du 21 mars 2025; le tableau.
- l article distingue **quatre causes**: argile, drainage, pyrite, pyrrhotite.
  Elles n ont pas le meme regime ni le meme recours. Gardez-les separees.
- **l article 2118 vise le batiment neuf**, avec les cinq ans du plan de
  garantie. Le vice cache et la denonciation ecrite visent le batiment usage.
  Deux regimes, deux sections: ne les melangez pas.
- **le pivot local, et il est contre-intuitif:** le volet maisons lezardees du
  programme Renovation Quebec a Laval exige que la cause de l affaissement soit
  liee au sol et **non** a un vice de construction. C est la preuve exactement
  inverse de celle d une reclamation contre un entrepreneur. Gardez cette
  opposition, c est le point le plus utile du texte.
- **ce programme n est peut-etre plus ouvert:** la derniere edition verifiable
  fermait le 21 mars 2025. Le francais le dit et renvoie a la Ville. Gardez les
  deux mouvements, ne le presentez jamais comme disponible.
- aucun cout de reparation, de pieutage ou d expertise, et aucune largeur de
  fissure servant de seuil de gravite: aucune source officielle n en publie.
  Gardez ces aveux.
- le francais ne resume aucun historique judiciaire de la pyrrhotite en
  Mauricie, faute de source primaire. N en ajoutez pas.

## F5. moisissure-maison-detection-recours-quebec

- translationKey `article-moisissure-maison-quebec`, date et lastmod **2026-09-19**
- categorie: en `Practical Guide`, es `Guía práctica`, ar `دليل عملي`
- fichiers: `content/en/articles/mould-in-the-home-quebec.md`,
  `content/es/articles/moho-vivienda-quebec.md`,
  `content/ar/articles/mould-in-the-home-quebec.md`
- voix: `content/{lang}/articles/hard-to-insure-home-quebec.md`
- a preserver: les articles 1733, 1739, 1910, 1913, 1915 et 2925 du Code civil;
  la norme **BNQ 3009-600** et sa date du 1er mai 2020; les sections **D7,
  D7.1, D7.2, D7.3, D4.1 et D5.2** du formulaire Declarations du vendeur; les
  montants 10 $, 60 $, 8 000 $ et 10 060 $; les dates 25 juin 2019,
  3 novembre 2023 et 21 fevrier 2024; le tableau.
- **la nuance centrale, et elle est fine:** une norme quebecoise sur les
  moisissures **existe**, la BNQ 3009-600, mais elle est d application
  volontaire et **ne fixe aucun seuil de concentration**. Le francais corrige
  ainsi une croyance repandue. Ne le simplifiez pas en « aucune norme
  n existe »: ce serait faux. Ne le simplifiez pas non plus en « une norme
  existe »: ce serait trompeur.
- la case du formulaire qui vise la moisissure est **D7.3**, sous
  « Qualite de l air interieur ». D5.2 et D4.1 n y viennent qu en appui comme
  causes. Ne rattachez pas la moisissure a une autre section.
- trois situations distinctes structurent l article: le proprietaire, l acheteur
  apres la vente, et le locataire face a son locateur. Les recours et les delais
  ne sont pas les memes. Gardez les trois separees.
- **les deux decisions du Tribunal administratif du logement citees ont ete
  verifiees mot a mot.** Elles ont des faits semblables et des issues opposees,
  exprès, pour montrer qu un recours ne se promet pas. Gardez les deux noms et
  les deux dates exacts, et gardez l opposition.
- le texte integral de la BNQ 3009-600 est payant et n a pas ete lu. Le francais
  ne cite donc aucun contenu de la norme. N en inventez aucun.
- aucun seuil de concentration, aucun cout de decontamination.

## F6. vendre-valeur-inferieure-solde-hypothecaire-quebec

- translationKey `article-valeur-inferieure-solde-hypothecaire`, date et lastmod **2026-09-25**
- categorie: en `Seller's Guide`, es `Guía del Vendedor`, ar `دليل البائع`
- fichiers: `content/en/articles/selling-underwater-mortgage-quebec.md`,
  `content/es/articles/vender-casa-vale-menos-hipoteca-quebec.md`,
  `content/ar/articles/selling-underwater-mortgage-quebec.md`
- voix: `content/{lang}/articles/break-mortgage-penalty-quebec.md` si elle
  existe dans votre carte de liens, sinon un autre article de financement.
- a preserver: les articles 1723, 2661, 2757, 2758, 2761, 2762, **2782**,
  **2789** et 3065 du Code civil; les clauses 4.3, 7.1 et 8.4 du formulaire
  OACIQ CCVE 00001; les montants 17 $, 101 $, 145 $, 165 $, 266 $, 3 000 $,
  12 000 $ et 200 000 $; les dates 1er avril 2026, 2 septembre 2026 et
  28 octobre 2026; le preavis de **60 jours**; les deux tableaux.
- **le coeur juridique de l article, a ne surtout pas aplatir:** l article 2782
  dit qu une prise en paiement **eteint** l obligation et ecarte la subrogation,
  alors que l article 2789 laisse au creancier sa creance pour le solde apres
  une vente. Autrement dit, le scenario qui semble le pire peut etre celui qui
  libere le vendeur. Le francais expose les deux regles et **refuse de
  trancher**. Gardez ce refus.
- le francais dit que rien ne permet d affirmer qu une vente de gre a gre
  rapporte plus qu une vente sous controle de justice. N ajoutez pas cette
  affirmation, meme si elle parait de bon sens.
- deux choses ont ete retirees faute de source et ne doivent pas revenir: la
  subrogation de l assureur hypothecaire contre l emprunteur, et la portabilite
  du **pret** lui-meme. La documentation de la SCHL porte sur le transfert de
  l **assurance**, pas du pret. Gardez cette distinction.
- aucun honoraire de notaire pour la quittance: aucun bareme public.
- le ton du francais est factuel et sans dramatisation. Le lecteur est dans une
  situation difficile et a besoin de chiffres, pas de reconfort ni d alarme.
  Gardez ce ton.
