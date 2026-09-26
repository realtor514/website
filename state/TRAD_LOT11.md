# Lot 11, consignes de traduction

**Nouveau, et c est le changement important de ce lot.** Les faits a preserver
ne sont plus listes a la main ici. Ils sont dans **`state/FAITS_LOT11.md`**,
genere par `python tools/trad_spec.py`, qui montre chaque chiffre, article de
loi, numero de reglement, section de formulaire et delai **dans sa phrase**.

Pourquoi. Sur les lots 7 a 10, mes listes plates ont produit une quinzaine
d erreurs, toujours la meme: une liste perd le rattachement. Un article du
reglement de Laval attribue a Montreal, un montant qui passe d une ville a
l autre, un numero venu d un tout autre article, une norme oubliee. Les
traducteurs les ont trouvees a chaque fois. Le fichier de faits supprime cette
classe d erreur.

**Lisez donc `state/FAITS_LOT11.md` pour votre article, puis ce fichier-ci pour
le jugement.** Et la regle ne change pas: **le fichier francais tranche.** Si la
fiche generee et le fichier divergent, suivez le fichier et signalez-le.

## Regles du lot

- Regles generales: `state/BRIEF_TRADUCTION.md` en entier, y compris la section
  sur le **separateur decimal en arabe**, ou le point remplace la virgule.
- Cartes de liens: `state/internal_links_en.md`, `_es.md`, `_ar.md`.
- **Avant d ecrire chaque fichier, verifiez qu il n existe pas deja avec un
  autre `translationKey`.** Les 18 slugs ont ete verifies libres le
  26 septembre, mais verifiez quand meme: c est la derniere barriere.
- `translationKey`, `date`, `lastmod`, `image`: identiques au francais.
- `draft: true`. Une etape automatisee basculera les fichiers ensuite.
- `needs_expert_review`: **present dans cinq, absent du sixieme (H6).**
  Recopiez ce qui est dans le francais, jamais autre chose.
- Aucun lien entre les six articles de ce lot: ils sont tous en brouillon.
- Zero tiret long, demi-cadratin ou double tiret. Longueur a 15 % du francais,
  sauf l arabe ou 80 % suffit.
- CTA: `/en/form/`, `/es/formulario/`, `/ar/istimara/`.

## Les fichiers a produire

| | article francais | en | es | ar | categorie en / es / ar |
|---|---|---|---|---|---|
| H1 | `insectes-rongeurs-infestation-recours-quebec` | `pests-vermin-infestation-recourse-quebec` | `plagas-infestacion-recursos-quebec` | `pests-vermin-infestation-recourse-quebec` | Practical Guide / Guía práctica / دليل عملي |
| H2 | `minimaison-microhabitation-zonage-quebec` | `tiny-house-zoning-financing-quebec` | `casa-minima-zonificacion-quebec` | `tiny-house-zoning-financing-quebec` | Buyer's Guide / Guía del Comprador / دليل المشتري |
| H3 | `vendre-automne-hiver-presentation-quebec` | `selling-in-fall-and-winter-quebec` | `vender-en-otono-e-invierno-quebec` | `selling-in-fall-and-winter-quebec` | Seller's Guide / Guía del Vendedor / دليل البائع |
| H4 | `toit-vert-toit-reflechissant-montreal-reglement` | `green-and-reflective-roofs-montreal` | `techos-verdes-reflectantes-montreal` | `green-and-reflective-roofs-montreal` | Practical Guide / Guía práctica / دليل عملي |
| H5 | `generatrice-panne-courant-assurance-quebec` | `generator-power-outage-insurance-quebec` | `generador-apagon-seguro-quebec` | `generator-power-outage-insurance-quebec` | Practical Guide / Guía práctica / دليل عملي |
| H6 | `marche-haut-de-gamme-montreal-laval-donnees` | `luxury-market-montreal-laval-data` | `mercado-alta-gama-montreal-laval` | `luxury-market-montreal-laval-data` | Market Analysis / Análisis de Mercado / تحليل السوق |

Voix: `hard-to-insure-home-quebec` pour H1 et H5,
`home-inspection-checklist-montreal` pour H2, `best-time-sell-home-montreal`
pour H3, `renovations-dont-add-value` pour H4, et pour H6 un article d analyse
de marche de votre carte de liens.

## Ce qu il ne faut pas aplatir, article par article

**H1, insectes et vermine.** Trois situations distinctes, avec des recours et
des delais differents: le proprietaire, l acheteur apres la vente, le locataire
face a son locateur. Gardez-les separees. Deux aveux d ignorance sont explicites
et volontaires: aucun jugement n est cite parce que les bases de jurisprudence
ont refuse l acces pendant la redaction, et aucune source ouverte ne nomme la
vermine dans une exclusion type d assurance au Quebec. La liste des huit
exclusions du Bureau d assurance du Canada est la **preuve** de cette
affirmation negative: gardez-la entiere.

**H2, minimaison.** Le pivot est juridique, pas esthetique: sur fondation c est
un immeuble publie au registre foncier, donc hypothecable; sur roues c est un
meuble publie au RDPRM. Une traduction qui presente la minimaison comme un
« type de propriete » rate tout l article. Gardez aussi le point
contre-intuitif: une minimaison unifamiliale est **exemptee** du chapitre I du
Code de construction, donc « conforme au Code » ne veut rien dire seul. Aucune
liste de municipalites qui les acceptent: seules deux villes sont nommees, avec
leur numero de reglement.

**H3, vendre en saison froide.** Son centre est la regle d exactitude appliquee
a une photo d ete diffusee en janvier, avec une frontiere nette: rien n oblige a
dater une image authentique, et le francais le dit, mais une image dont
l intelligence artificielle a transforme la saison exige une mention. Ne
brouillez pas cette frontiere. Gardez aussi les deux **absences** du formulaire
de declaration, aucune question sur le revetement exterieur et aucune sur le
montant des factures, qui expliquent pourquoi l acheteur d hiver reclame
l historique Hydro-Quebec.

**H4, toit vert et toit reflechissant.** Le tableau des 19 arrondissements est
le coeur de l article: **chaque indice appartient a son arrondissement**, et
trois exceptions changent la reponse selon l adresse. Ne generalisez jamais a
Montreal. Gardez la distinction du guide du ministere: le toit vert **retire**
du volume d eau, le toit bleu ne fait que l **etaler dans le temps**. Et gardez
la consequence que le francais assume: la condition de construction
incombustible du guide de la Regie du batiment ecarte de fait le plex a
ossature de bois.

**H5, generatrice.** Deux points a ne pas perdre. D abord, la regle
d Hydro-Quebec exige une autorisation **ecrite et prealable** et un
interverrouillage **mecanique**, et le francais donne les deux raisons
techniques: le groupe en aval de l appareillage de mesure, et le compteur qui ne
doit pas pouvoir etre mis sous tension par le groupe. Ensuite, la croyance
corrigee: **aucune distance chiffree** n existe pour le monoxyde de carbone. Les
3, 6 et 7 metres qui circulent viennent de communiques regionaux, pas d une
regle provinciale. N en ajoutez aucune.

**H6, marche haut de gamme.** C est le seul article du lot **sans**
`needs_expert_review`, parce que son finisseur a rouvert chaque source et retire
tout ce qui ne tenait pas. Ne reintroduisez rien. En particulier: le francais ne
donne **aucune methode** de calcul de la borne du segment, parce que l APCIQ
n en publie pas et que le ratio qui circule ne tient pas. Le ton est sobre
exprès: **aucun superlatif, aucune promesse de service haut de gamme, aucune
clientele exclusive.** Georges est courtier residentiel. Si une tournure de
votre langue rend le texte plus vendeur que le francais, choisissez la tournure
plus plate.
