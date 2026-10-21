# Lot « questions des consommateurs », consignes de traduction

Serie t284 a t297, ecrite le 2026-10-21. Meme methode que les lots 11 et 12.
Les faits a preserver, chacun dans sa phrase, sont dans
**`state/FAITS_LOT_CONSOMMATEURS.md`**, genere par `tools/trad_spec.py`. Ce
fichier-ci ne porte que le jugement. **Le fichier francais tranche.** Si la
fiche generee et le fichier divergent, suivez le fichier et signalez-le.

## Regles du lot

- Regles generales: `state/BRIEF_TRADUCTION.md` en entier, y compris la section
  sur le **separateur decimal en arabe** (le point, jamais la virgule) et sur
  les nombres negatifs en arabe (le mot, pas le signe).
- Cartes de liens: `state/internal_links_en.md`, `_es.md`, `_ar.md`. Chaque lien
  interne du francais pointe vers la version de la MEME langue du meme article;
  trouvez-la par son titre ou par son `translationKey` dans `content/<lang>/articles/`.
  Si elle n existe pas, retirez le lien. Jamais de lien mort.
- **Aucun lien vers un autre article de ce lot**: ils sont tous en brouillon.
- `translationKey`, `date`, `lastmod`, `image`: identiques au francais.
- `draft: true`. `tools/release.py --only` basculera les fichiers ensuite.
- `needs_expert_review: true`: a recopier seulement la ou le francais le porte
  (L4, L6, L11, L12). Ne l ajoutez nulle part ailleurs.
- Zero tiret long, demi-cadratin ou double tiret. Longueur a 15 % du francais,
  sauf l arabe ou 80 % suffit.
- Titre: 60 caracteres au plus, en forme de question comme le francais, avec la
  formulation que le lecteur taperait vraiment dans sa langue.
- CTA final: `/en/form/`, `/es/formulario/`, `/ar/istimara/`. Outils:
  `/en/tools/...`, `/es/tools/...`, `/ar/tools/...`. Pages de ville:
  `/en/courtier-immobilier/laval/` etc. seulement si la carte de liens de la
  langue les liste; sinon retirez le lien et gardez le texte.
- La phrase de service du bloc final reste « francais, anglais et arabe » dans
  les 4 langues, **y compris en espagnol**. Georges ne sert pas en espagnol.
- Les citations d organismes (APCIQ, SCHL, Banque du Canada, OACIQ, RBQ, TAL)
  se traduisent, mais restent entre guillemets et attribuees a la meme source.
- Une prevision reste une prevision, une illustration reste une illustration,
  une estimation reste une estimation. Ne durcissez aucun conditionnel.

## Les fichiers a produire

| | article francais | en | es | ar | categorie en / es / ar |
|---|---|---|---|---|---|
| L1 | `prix-maisons-baisser-quebec` | `will-house-prices-drop-quebec` | `bajaran-precios-casas-quebec` | `will-house-prices-drop-quebec` | Market Analysis / Análisis de Mercado / تحليل السوق |
| L2 | `taux-hypothecaires-baisser-quebec` | `will-mortgage-rates-go-down-quebec` | `bajaran-tasas-hipotecarias-quebec` | `will-mortgage-rates-go-down-quebec` | Finance / Financiamiento / تمويل |
| L3 | `bulle-immobiliere-quebec` | `housing-bubble-quebec` | `burbuja-inmobiliaria-quebec` | `housing-bubble-quebec` | Market Analysis / Análisis de Mercado / تحليل السوق |
| L4 | `pouvoir-achat-premiers-acheteurs-quebec` | `first-time-buyer-purchasing-power-quebec` | `poder-adquisitivo-primeros-compradores-quebec` | `first-time-buyer-purchasing-power-quebec` | Finance / Financiamiento / تمويل |
| L5 | `risques-transaction-immobiliere-quebec` | `real-estate-transaction-risks-quebec` | `riesgos-transaccion-inmobiliaria-quebec` | `real-estate-transaction-risks-quebec` | Real Estate 101 / Inmobiliaria 101 / عقارات 101 |
| L6 | `faut-il-inspecter-maison-avant-achat-quebec` | `home-inspection-before-buying-quebec` | `inspeccion-antes-de-comprar-quebec` | `home-inspection-before-buying-quebec` | Buyer's Guide / Guía del Comprador / دليل المشتري |
| L7 | `facteurs-marche-immobilier-quebec` | `factors-quebec-real-estate-market` | `factores-mercado-inmobiliario-quebec` | `factors-quebec-real-estate-market` | Market Analysis / Análisis de Mercado / تحليل السوق |
| L8 | `investir-immobilier-locatif-quebec` | `invest-rental-property-quebec` | `invertir-inmueble-alquiler-quebec` | `invest-rental-property-quebec` | Investment / Inversión / استثمار |
| L9 | `preparer-achat-premiere-propriete-quebec` | `prepare-first-home-purchase-quebec` | `prepararse-compra-primera-vivienda-quebec` | `prepare-first-home-purchase-quebec` | Buyer's Guide / Guía del Comprador / دليل المشتري |
| L10 | `inflation-quebec-immobilier` | `inflation-quebec-homeowners` | `inflacion-quebec-propietarios` | `inflation-quebec-homeowners` | Finance / Financiamiento / تمويل |
| L11 | `maisons-2030-quebec` | `quebec-homes-2030` | `casas-2030-quebec` | `quebec-homes-2030` | Real Estate 101 / Inmobiliaria 101 / عقارات 101 |
| L12 | `changements-proprietaires-quebec` | `changes-homeowners-quebec` | `cambios-propietarios-quebec` | `changes-homeowners-quebec` | Real Estate 101 / Inmobiliaria 101 / عقارات 101 |
| L13 | `fin-crise-logement-quebec` | `when-will-housing-crisis-end-quebec` | `fin-crisis-vivienda-quebec` | `when-will-housing-crisis-end-quebec` | Market Analysis / Análisis de Mercado / تحليل السوق |
| L14 | `maisons-abordables-quebec` | `home-affordability-quebec` | `asequibilidad-vivienda-quebec` | `home-affordability-quebec` | Market Analysis / Análisis de Mercado / تحليل السوق |

Les 42 slugs ont ete verifies libres le 2026-10-21.

## Ce qu il ne faut pas aplatir, article par article

**L1, prix.** Aucune prediction. Les quatre editions de prevision gardent leur
organisme, leur date et leur mesure: l APCIQ prevoit des medianes, la SCHL un
prix MOYEN toutes categories. Gardez la section qui explique pourquoi mediane,
moyenne et indice divergent, et l aveu: aucune prevision de l APCIQ pour 2027
au 21 octobre 2026.

**L2, taux.** Le calcul du quart de point repose sur le taux moyen EXIGE de
4,49 %, pas sur le taux affiche: ne les confondez pas. Le calendrier des
annonces est date; la prochaine est le 28 octobre 2026. Les donnees de
renouvellement sont nationales, l article le dit.

**L3, bulle.** L ecart de dates entre les revenus (2020) et les prix (2026)
gonfle les ratios, et l article le dit: gardez cet aveu. Plusieurs series ne
sont que nationales: gardez le mot « Canada » partout ou le francais le met.
L Evaluation du marche de l habitation de la SCHL est abandonnee.

**L4, pouvoir d achat.** Le revenu de 2026 est une ESTIMATION indexee, pas une
mesure. Le territoire de la RMR change entre 2016 et 2021; c est pour cela que
Laval est montree a cote. Les versements utilisent le taux affiche.

**L5, risques.** Les plafonds sont exacts et rattaches a leur fonds: 100 000 $
pour le fonds de l OACIQ (FICI), 200 000 $ par reclamation pour celui des
notaires. Le paragraphe Integri-T decrit le programme exactement comme la page
du site, exclusion de la vente sans garantie legale comprise: ne le resumez pas.
Gardez « non publiee » pour le montant d assurance du courtier.

**L6, inspection.** Le coeur est l article 1726: le vice apparent est celui
qu un acheteur prudent et diligent peut constater SANS recourir a un expert.
Le certificat de la RBQ devient obligatoire le 1er octobre 2027; d ici la, un
inspecteur peut exercer sans certificat. Pour la GCR, le delai de 3 jours court
a partir de la RECEPTION du batiment, pas de l inspection.

**L7, facteurs.** Aucun facteur n est dit plus important qu un autre. La
detente locative de 2025 a DEUX causes selon la SCHL (offre en forte hausse,
demande ralentie surtout par la baisse des residents non permanents): gardez
les deux.

**L8, locatif.** L exemple de plex est un exemple, ses hypotheses sont nommees
comme telles (assurance, entretien). Ne transformez pas le resultat en verdict
general. Pourcentage de base du TAL 2026: 3,1 %.

**L9, premier achat.** Le lecteur qui commence un plan de 12 mois achetera en
2027: les seuils des droits de mutation de 2027 (64 400 $ et 322 600 $) sont
voulus. Le calendrier a rebours garde son ordre.

**L10, inflation.** Le 2,6 % pour le TAL 2027 est une ILLUSTRATION qui applique
la formule a une projection du ministere: gardez la phrase qui dit que seul le
chiffre publie par le TAL fera foi. Les chiffres canadiens restent dits
canadiens. Les projections citees datent de juillet et d aout 2026.

**L11, maisons 2030.** La distinction adopte, en vigueur, projet est le coeur
de l article: chaque regle garde son statut exact. Nom exact du reglement de
Montreal: Reglement sur les emissions de GES des nouveaux batiments (23-046).
Le reglement 2024-111 de la CMM est adopte mais NON en vigueur.

**L12, changements.** Les echeances marquees « passee » le restent. La section
« annonce, mais pas adopte » garde ce statut. Fin de la taxe sur les logements
sous-utilises pour 2025 et suivantes. Prochaine echeance de la loi 16: 15 aout
2028, pas 2027.

**L13, crise du logement.** Aucune source officielle ne fixe le seuil
d equilibre a 3 %: la SCHL propose une fourchette par ville, de 2,5 % a 4,0 %
pour Montreal. Aucune date de fin de crise. Les mises en chantier
« Quebec » portent la precision des centres de 10 000 habitants et plus.

**L14, abordabilite.** Le seuil de 30 % de la SCHL couvre TOUS les frais de
logement, pas seulement le versement: gardez la phrase qui dit que le ratio de
l article sous-estime donc l effort reel. Deux ratios seulement sont publies
(Laval, revenu 2020; ile de Montreal, revenu 2021 de l agglomeration); pour les
autres villes, le tableau donne le revenu necessaire sans ratio, et le texte dit
pourquoi. Les trois scenarios A, B, C sont des calculs, pas des previsions; la
hausse de revenu de 2,1 % est une hypothese.

## Livrable de chaque traducteur

Trois fichiers: `content/en/articles/<slug-en>.md`,
`content/es/articles/<slug-es>.md`, `content/ar/articles/<slug-en>.md`.
Puis:

```
python tools/validate.py content/en/articles/<slug-en>.md content/es/articles/<slug-es>.md content/ar/articles/<slug-en>.md
```

Zero erreur. Rapport court: les trois chemins, la longueur de chacun en
proportion du francais, tout lien retire, toute divergence entre la fiche de
faits et le fichier francais.
