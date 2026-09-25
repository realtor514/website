# Lot 8, consignes de traduction par article

Regles generales: `state/BRIEF_TRADUCTION.md`, a lire en entier d abord.
Cartes de liens: `state/internal_links_en.md`, `_es.md`, `_ar.md`.

**La seule source de verite est le fichier francais.** Les listes « a preserver »
ont ete extraites mecaniquement du texte francais. Si un element listé ne s y
trouve pas, ne l inventez pas: signalez-le et traduisez ce qui est ecrit.

**Contexte particulier de ce lot.** Les huit articles ont ete rediges le
25 septembre 2026, pendant que LegisQuebec, Revenu Quebec, quebec.ca,
justice.gouv.qc.ca et laval.ca etaient inaccessibles. Les redacteurs ont donc
RETIRE des affirmations plutot que de les citer de memoire. **Ces trous sont
voulus. Ne les comblez pas.** Un traducteur qui rajoute un numero d article du
Code civil, un nom de formulaire de Revenu Quebec ou un tarif d Hydro-Quebec
introduit une affirmation non verifiee dans quatre langues a la fois.

**Le drapeau draft.** Ecrivez `draft: true`. Une etape automatisee passera
ensuite les fichiers en `draft: false`. Ne le remettez jamais a true, et ne
retouchez pas `lastmod` apres l avoir ecrit.

**Deux erreurs de cette consigne, corrigees le 25 septembre apres coup.**

1. Les slugs anglais et arabe de D6 pointaient sur `homeowner-tax-deductions-quebec`,
   qui est **deja un article publie**: la traduction de `impot-proprietaire-quebec.md`,
   translationKey `article-impot-proprietaire`. Le slug de D6 est desormais
   `what-homeowners-can-deduct-quebec` en anglais et en arabe. En espagnol il n y
   avait pas de collision, l article existant vivant sous
   `impuestos-propietario-quebec.md`.
2. Les comptes de tableaux annonces etaient faux: ils comptaient les lignes de
   separation, pas les tableaux. Ils sont corriges ci-dessous.

**Regle generale qui en decoule: avant d ecrire un fichier, verifiez qu il
n existe pas deja avec un autre `translationKey`.** S il existe, changez votre
slug et signalez-le. N ecrasez jamais un fichier publie. Et reproduisez toujours
ce qui est reellement dans le fichier francais, jamais le compte de cette
consigne.

**Aucun lien entre les huit articles de ce lot.** Ils sont tous en brouillon,
donc un lien entre eux renvoie 404. Les huit fichiers francais n en contiennent
aucun: ne les rajoutez pas.

**Absolu:** zero tiret long, demi-cadratin ou double tiret. Longueur a 15 % du
francais, sauf l arabe ou 80 % suffit. Chiffres en caracteres latins en arabe.
Section Questions frequentes gardee, titre dans la langue cible. Noms
d organismes, formulaires et termes juridiques gardes en francais, glose a la
premiere occurrence. CTA du formulaire: `/en/form/`, `/es/formulario/`,
`/ar/istimara/`. `needs_expert_review` se recopie du francais: present si le
francais l a, absent s il ne l a pas. Ne l ajoutez jamais de votre propre chef.

---

## D1. particularites-maison-quebecoise

- translationKey `article-particularites-maison-quebecoise`, date et lastmod **2026-09-08**
- categorie: en `Buyer's Guide`, es `Guía del Comprador`, ar `دليل المشتري`
- `needs_expert_review: true` present
- fichiers: `content/en/articles/quebec-house-construction-features.md`,
  `content/es/articles/caracteristicas-casa-quebequense.md`,
  `content/ar/articles/quebec-house-construction-features.md`
- voix: `content/{lang}/articles/home-inspection-checklist-montreal.md`
- a preserver exactement: le renvoi 8.05.01 tel qu ecrit; les montants 167,40 $,
  80 $, 560 $, 1 000 $, 1 500 $ et 9,80 $; les pourcentages 7 %, 36 %, 45 %,
  57 %, 58 % et 80 % avec la source a laquelle le francais les rattache; le
  tableau.
- **le volet Hydro-Quebec a ete ajoute le 25 septembre, apres la redaction.**
  A preserver au chiffre pres: le tarif D avec 46,154 ¢/jour de frais d acces au
  reseau, 7,065 ¢/kWh jusqu a 40 kWh par jour et 11,142 ¢/kWh au-dela; le tarif
  bienergie DT avec la bascule a -12 °C ou -15 °C selon la zone, 5,131 ¢/kWh
  au-dessus du seuil et 30,001 ¢/kWh en dessous; les montants LogisVert de 50 $,
  120 $ et 140 $ par 1 000 BTU/h a -8 °C. Gardez la date de consultation et la
  mention de la revision annuelle au 1er avril: ces tarifs changent.
- **en revanche, rien sur Chauffez vert ni sur l interdiction du chauffage au
  mazout.** Ces deux sujets restent absents parce que quebec.ca et LegisQuebec
  etaient inaccessibles. N en ajoutez pas une ligne.
- les chiffres de repartition du chauffage viennent de Statistique Canada, et le
  francais le dit: gardez cette attribution.
- trois precisions de portee geographique sont ecrites dans le texte (cour
  anglaise a Villeray Saint Michel Parc Extension, garde-corps de
  Mercier Hochelaga Maisonneuve, indice de reflectance variable par
  arrondissement). Gardez la portee limitee, ne generalisez pas a Montreal.

## D2. rentabiliser-terrain-zonage-quebec

- translationKey `article-land-potential-zoning`, date et lastmod **2026-09-21**
- categorie: en `Investment`, es `Inversión`, ar `استثمار`
- fichiers: `content/en/articles/accessory-dwelling-unit-quebec.md`,
  `content/es/articles/vivienda-accesoria-quebec.md`,
  `content/ar/articles/accessory-dwelling-unit-quebec.md`
- voix: `content/{lang}/articles/rental-property-management.md`
- a preserver exactement: les montants 90 $, 92 $, 300 $, 450 $, 732 $,
  20 000 $, 500 000 $, 2,50 $, 9,80 $, 167,40 $, 20 $ et 1 000 $; les dates
  1er septembre 1996 et 21 fevrier 2024; le tableau.
- **l article ne donne aucune marge de recul, aucune superficie maximale et
  aucun coefficient d emprise au sol**, parce qu aucun reglement consultable ne
  les publie. Il explique a la place comment obtenir la fiche de zonage.
  N inventez aucun chiffre de zonage.
- le programme federal de prets pour logement accessoire est decrit uniquement
  comme « en cours d elaboration ». N ajoutez ni montant ni taux.
- sur la fixation du loyer d un logement nouvellement ajoute, le francais cite
  la regle du Tribunal administratif du logement puis dit qu il ne peut pas
  trancher le cas et renvoie a un juriste. Gardez les deux mouvements.

## D3. renovations-resilience-climat-quebec

- translationKey `article-climate-resilient-renos`, date et lastmod **2026-09-19**
- categorie: en `Practical Guide`, es `Guía práctica`, ar `دليل عملي`
- fichiers: `content/en/articles/climate-resilient-renovations-quebec.md`,
  `content/es/articles/renovaciones-resiliencia-climatica-quebec.md`,
  `content/ar/articles/climate-resilient-renovations-quebec.md`
- voix: `content/{lang}/articles/renovations-dont-add-value.md`
- a preserver exactement: les renvois 3.03.02, 5.05.01, 5.05.02 et 5.05.03 du
  reglement de Laval, dont l intitule « Exoneration de responsabilite »; les
  dates 6 octobre 2014, 29 aout 2024, 15 juillet 2025, 2 fevrier 2026,
  18 aout 2026 et 25 septembre 2026; les trois tableaux.
- **le point le plus delicat du lot.** L article expose une contradiction reelle
  entre deux pages de la Ville de Montreal sur le programme de clapet
  antiretour: 90 $, 600 $, 1 600 $ et un seuil de 3 860 $/m2 sur la page mise a
  jour le 18 aout 2026, contre 80 $, 560 $, 1 500 $ et 3 476 $/m2 sur celle du
  15 juillet 2025. **Gardez les deux series avec leurs deux dates, et gardez
  l avertissement de faire confirmer au moment de la demande.** Ne choisissez
  pas une des deux series. Ne les fusionnez pas.
- l indice de reflectance solaire n a pas de seuil unique: le francais ne donne
  que deux valeurs d arrondissement (au moins 66 a Ahuntsic Cartierville, au
  moins 78 a Anjou). N en deduisez pas une regle montrealaise.
- le francais dit qu aucune source officielle ne chiffre la duree de vie d un
  drain francais, et qu aucune source ne permet de chiffrer le gain a la
  revente de ces travaux. Gardez les deux aveux.
- **le volet Hydro-Quebec a ete ajoute le 25 septembre, apres la redaction**, dans
  la section sur la surchauffe estivale. A preserver au chiffre pres: les
  montants LogisVert de 50 $, 120 $ et 140 $ par 1 000 BTU/h a -8 °C, le maximum
  de 6 700 $, la majoration de 5 % pour mesures multiples, et la bonification
  Multilogements de 100 $ qui porte le montant a 220 $ pour les installations a
  compter du 15 juin 2026. Gardez la datation « septembre 2026 ».
- rien sur Chauffez vert: le programme reste absent, quebec.ca etait
  inaccessible. N en ajoutez pas une ligne.

## D4. acheter-fin-ete-montreal-donnees

- translationKey `article-fall-buying-window`, date et lastmod **2026-09-12**
- categorie: en `Market Analysis`, es `Análisis de Mercado`, ar `تحليل السوق`
- fichiers: `content/en/articles/best-time-to-buy-montreal-data.md`,
  `content/es/articles/mejor-momento-comprar-montreal-datos.md`,
  `content/ar/articles/best-time-to-buy-montreal-data.md`
- voix: `content/{lang}/articles/best-time-sell-home-montreal.md`
- a preserver exactement: tous les montants medians (310 000 $, 437 250 $,
  470 000 $, 530 000 $, 630 000 $, 642 750 $, 650 000 $, 780 000 $, 930 000 $)
  et tous les pourcentages, chacun rattache au meme mois et au meme secteur que
  dans le francais; les dates 6 aout 2025 et 30 juin 2027.
- **trois nuances methodologiques a ne pas ecraser:**
  1. l APCIQ publie une **moyenne** de jours sur le marche, pas une mediane, et
     elle se compte a partir de la signature du contrat de courtage. Le francais
     cite la definition mot a mot: gardez le mot moyenne.
  2. le ratio des ventes sur les nouvelles inscriptions est **le calcul de
     l auteur**, pas une statistique de l APCIQ, et le francais le dit. Gardez
     cette mention. La mesure officielle des conditions de marche est le nombre
     de mois d inventaire.
  3. le plex lavallois d aout 2026 porte la mention « Nombre de transactions
     insuffisant pour produire une statistique fiable ». Gardez-la.
- le francais corrige deux croyances avec la donnee: le stock ne culmine pas en
  aout mais en avril et en mai, et la garantie de taux va de 60 a 130 jours
  selon le preteur, pas de 90 a 120. Ne retablissez pas les versions courantes.
- le francais dit explicitement qu il ne peut pas chiffrer l escompte moyen
  obtenu en aout. Gardez cet aveu.

## D5. prix-demande-prix-vendu-montreal

- translationKey `article-list-vs-sold-price`, date et lastmod **2026-08-26**
- categorie: en `Market Analysis`, es `Análisis de Mercado`, ar `تحليل السوق`
- fichiers: `content/en/articles/list-price-vs-sold-price-montreal.md`,
  `content/es/articles/precio-pedido-vs-precio-vendido-montreal.md`,
  `content/ar/articles/list-price-vs-sold-price-montreal.md`
- voix: `content/{lang}/articles/bidding-wars-truth-montreal.md`
- a preserver exactement: les renvois aux articles 76, 111 et 112 tels qu ecrits;
  le 1,50 $ du Registre foncier depuis le 1er avril 2026; les dates de reference
  des roles (Montreal 2026-2027-2028 au 1er juillet 2024, Laval 2025-2026-2027
  au 1er juillet 2023), les 18 mois et les trois ans; les dates 17 decembre 2025,
  17 juin 2026 et 6 aout 2026; le 17 %; le tableau.
- **la distinction centrale, a ne pas aplatir:** le prix vendu n est pas
  *affiche*, mais il n est pas secret non plus. Il cesse d etre confidentiel des
  la publication de l acte au Registre foncier. Ce qui est encadre par l OACIQ,
  c est la publicite qu un courtier peut en faire. Une traduction qui ecrit que
  les prix de vente « ne sont pas publics au Quebec » est fausse.
- ne laissez jamais entendre que Georges divulguerait un prix confidentiel.
- le francais dit que les communiques de l APCIQ ne publient ni ratio moyen prix
  vendu sur prix demande, ni proportion de ventes au-dessus du prix affiche.
  Gardez cet aveu, n allez pas chercher un chiffre ailleurs.

## D6. impots-proprietaire-quebec-deductions

- translationKey `article-homeowner-tax-quebec`, date et lastmod **2026-09-04**
- categorie: en `Finance`, es `Financiamiento`, ar `تمويل`
- `needs_expert_review: true` present
- fichiers: `content/en/articles/what-homeowners-can-deduct-quebec.md`,
  `content/es/articles/deducciones-fiscales-propietario-quebec.md`,
  `content/ar/articles/what-homeowners-can-deduct-quebec.md`
- voix: `content/{lang}/articles/first-time-buyer-tax-credits.md`
- a preserver exactement: les renvois 271, 210.7 et 1029.8.61.5 tels qu ecrits;
  les montants 500 $, 8 000 $, 19 500 $, 25 500 $, 64 200 $, 72 465 $,
  117 395 $ et 622 300 $; les pourcentages, dont le 7,5 % du test de la
  subvention aux aines et le 37 % de la hausse du role de Laval; les dates
  2 octobre 2016, 1er juillet 2023 et 1er janvier 2025; le tableau. Le francais
  ajoute une penalite de 100 $ par mois que cette consigne ne listait pas:
  gardez-la, le francais fait foi.
- **les noms de formulaires de Revenu Quebec ont ete retires** parce que le site
  etait inaccessible. Le francais dit seulement que Revenu Quebec a son propre
  formulaire de revenus de location. N ajoutez aucun numero de formulaire, ni
  TP-128, ni TP-274, ni autre.
- gardez la ligne canadienne fondamentale: les interets hypothecaires d une
  residence principale ne sont pas deductibles, et la vente d une residence
  principale se declare quand meme pour que l exemption s applique.
- aucun conseil fiscal definitif: le francais renvoie au comptable, gardez ce
  renvoi partout ou il apparait.

## D7. duree-de-vie-composantes-maison-quebec

- translationKey `article-component-lifespan`, date et lastmod **2026-08-30**
- categorie: en `Buyer's Guide`, es `Guía del Comprador`, ar `دليل المشتري`
- fichiers: `content/en/articles/roof-and-window-lifespan-quebec.md`,
  `content/es/articles/vida-util-techo-ventanas-quebec.md`,
  `content/ar/articles/roof-and-window-lifespan-quebec.md`
- voix: `content/{lang}/articles/home-inspection-checklist-montreal.md`
- a preserver exactement: les durees de vie telles qu ecrites, chacune avec la
  source a laquelle le francais la rattache; le decret du 30 juillet 2025 et son
  exigence de vie utile residuelle par ecrit; les montants 92 $, 1 000 $,
  2,50 $ et 20 000 $; le tableau.
- **le coeur du texte est un aveu, et c est le passage le plus facile a trahir:**
  les durees publiees sont des **moyennes canadiennes**, pas des durees
  quebecoises, et **aucun organisme officiel ne chiffre l effet du gel et du
  degel**. Le francais le dit franchement dans une section entiere. Une
  traduction qui laisse entendre que ces durees valent pour le Quebec, ou qui
  suggere un pourcentage a retrancher, est fausse.
- le francais ne cite aucun numero de section du formulaire Declarations du
  vendeur, parce que la page de l OACIQ repondait 404. N en ajoutez pas.
- aucune duree de vie n est donnee pour le drain francais ni pour la fondation.
  N en inventez pas.

## D8. vice-cache-pendant-renovation-quebec

- translationKey `article-hidden-defect-renovation`, date et lastmod **2026-09-25**
- categorie: en `Practical Guide`, es `Guía práctica`, ar `دليل عملي`
- `needs_expert_review: true` present
- fichiers: `content/en/articles/hidden-defect-found-during-renovation-quebec.md`,
  `content/es/articles/vicio-oculto-durante-renovacion-quebec.md`,
  `content/ar/articles/hidden-defect-found-during-renovation-quebec.md`
- voix: `content/{lang}/articles/vice-cache-conditions-recours-quebec.md`
- a preserver exactement: les paliers de competence des tribunaux avec leurs
  bornes au cent pres (15 000 $, 15 000,01 $, 74 999,99 $, 75 000 $,
  99 999,99 $, 100 000 $), les montants 21 000 $, 40 000 $, 20 000 $, 1 500 $,
  1 000 $, 92 $ et 2,50 $, et le tableau.
- **interdiction absolue, la plus importante de ce lot: n ajoutez aucun numero
  d article du Code civil du Quebec.** LegisQuebec a repondu 502 pendant les
  25 tentatives du redacteur, donc aucun numero n a pu etre verifie et aucun
  n apparait dans le francais. Les regles y sont attribuees a Educaloi et a
  l OACIQ. Si vous ecrivez 1726, 1728, 1739, 2925 ou 2926, vous introduisez une
  citation non verifiee dans trois langues. Ces numeros seront ajoutes plus tard,
  dans les quatre langues en meme temps, quand LegisQuebec repondra.
- gardez la sequence procedurale dans son ordre exact: ne pas refermer le mur,
  documenter, identifier lequel des trois responsables est vise, denoncer par
  ecrit, et seulement ensuite reparer. C est tout l article.
- gardez les trois horloges distinctes et le renvoi a l avocat ou au notaire.
  Ne promettez jamais qu un recours reussira.
