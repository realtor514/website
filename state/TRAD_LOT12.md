# Lot 12, consignes de traduction

Meme methode que le lot 11. Les faits a preserver, chacun dans sa phrase, sont
dans **`state/FAITS_LOT12.md`**, genere par `python tools/trad_spec.py
--tous-les-drafts`. Ce fichier-ci ne porte que le jugement. **Le fichier
francais tranche.** Si la fiche generee et le fichier divergent, suivez le
fichier et signalez-le.

## Regles du lot

- Regles generales: `state/BRIEF_TRADUCTION.md` en entier, y compris la section
  sur le **separateur decimal en arabe**.
- Cartes de liens: `state/internal_links_en.md`, `_es.md`, `_ar.md`,
  regenerees le 30 septembre apres le lot 11.
- **Avant d ecrire chaque fichier, verifiez qu il n existe pas deja avec un
  autre `translationKey`.** Les 18 slugs ont ete verifies libres le
  30 septembre.
- `translationKey`, `date`, `lastmod`, `image`: identiques au francais.
- `draft: true`. `tools/release.py` basculera les fichiers ensuite.
- `needs_expert_review: true`: present dans les six, a recopier.
- Aucun lien entre les six articles de ce lot: ils sont tous en brouillon.
- Zero tiret long, demi-cadratin ou double tiret. Longueur a 15 % du francais,
  sauf l arabe ou 80 % suffit.
- Titre: 60 caracteres au plus, comme les titres raccourcis du commit afcc35a.
  Aucun suffixe du genre `[bytes=57]` dans le titre.
- CTA: `/en/form/`, `/es/formulario/`, `/ar/istimara/`.

## Les fichiers a produire

| | article francais | en | es | ar | categorie en / es / ar |
|---|---|---|---|---|---|
| L1 | `acheter-maison-campagne-quebec` | `buying-country-home-quebec` | `comprar-casa-de-campo-quebec` | `buying-country-home-quebec` | Buyer's Guide / Guía del Comprador / دليل المشتري |
| L2 | `entretien-hivernal-maison-quebec` | `winter-home-maintenance-insurance-quebec` | `mantenimiento-invernal-casa-quebec` | `winter-home-maintenance-insurance-quebec` | Practical Guide / Guía práctica / دليل عملي |
| L3 | `hausse-frais-de-condo-quebec` | `condo-fee-increase-quebec` | `aumento-cuotas-condominio-quebec` | `condo-fee-increase-quebec` | Real Estate 101 / Inmobiliaria 101 / عقارات 101 |
| L4 | `maison-passive-novoclimat-quebec` | `passive-house-novoclimat-quebec` | `casa-pasiva-novoclimat-quebec` | `passive-house-novoclimat-quebec` | Real Estate 101 / Inmobiliaria 101 / عقارات 101 |
| L5 | `maisons-abandonnees-ventes-pour-taxes` | `municipal-tax-sale-quebec` | `venta-por-impuestos-municipales-quebec` | `municipal-tax-sale-quebec` | Investment / Inversión / استثمار |
| L6 | `permis-abattage-arbres-quebec` | `tree-cutting-permit-montreal` | `permiso-tala-arbol-montreal` | `tree-cutting-permit-montreal` | Practical Guide / Guía práctica / دليل عملي |

## Ce qu il ne faut pas aplatir, article par article

**L1, maison de campagne.** Le pivot est l ordre des autorites: la zone agricole
et la CPTAQ passent avant la municipalite, et le premier document est
l attestation de zonage, pas le certificat de localisation. Gardez les trois
aveux: aucun pourcentage, aucun delai de revente d un rang hors RMR, aucun ecart
de prix ville contre campagne. N en ajoutez aucun.

**L2, entretien hivernal.** Le coeur est juridique et contre-intuitif:
l article 2464 du Code civil oblige l assureur a reparer le prejudice cause par
la faute de l assure, sauf exclusion expressement et limitativement stipulee.
Une traduction qui dit « la negligence peut reduire l indemnite » inverse
l article. Gardez aussi que les temperatures minimales de chauffage sont
municipales et visent **toutes** les habitations, pas seulement les logements
loues, avec leur rattachement: Montreal 03-096, articles 37 et 38; Laval
L-12519, article 12. Aucun tarif de deneigement de toiture ni de vidange.

**L3, hausse des frais de condo.** Le calendrier du reglement du 14 aout 2025
est la cause des hausses: gardez chaque delai avec sa disposition. L article
1072 dit « sans delai » pour communiquer la quote-part, pas un delai chiffre.
La frontiere entre le conseil d administration (reparation, remplacement,
article 1072) et l assemblee aux trois quarts (amelioration, article 1097) doit
rester nette. Un seul recours de 90 jours. Aucun pourcentage moyen de hausse.

**L4, maison passive.** Trois choses distinctes, jamais fusionnees: la norme
Passive House (0,6 a 50 Pa, 15 kWh/m2), Novoclimat (1,5 CAH a 50 Pa), et les
mots sans organisme. La partie 11 du Code de construction n exige aucun test
d infiltrometrie. L incoherence du document de Quebec, 4 000 $ dans la note 1
contre 2 000 $ dans la ligne du tableau, est **signalee et non tranchee**:
ne choisissez pas un montant. Aucun surcout passif, aucune plus-value chiffree.

**L5, vente pour taxes.** Trois regimes distincts, chacun avec ses articles: ne
melangez pas les numeros de la Loi sur les cites et villes avec ceux du Code
municipal. Le droit de retrait d un an est le centre: l adjudicataire n est
pas proprietaire au jour de l encan. Les dates et lieux d encans 2026 restent
rattaches a leur ville. La TPS et la TVQ viennent de la FAQ de Blainville
seulement: gardez cette attribution.

**L6, permis d abattage.** Corrige le 30 septembre apres le signalement du
traducteur anglais. La page montreal.ca contient un bloc par arrondissement,
chacun avec son identifiant (`<div id="LCH" class="borough-content-unit">`
pour Lachine). L amende de 600 $ a 15 000 $ et l exception du cedre, du
genevrier et du nerprun sont dans le bloc `LCH`: le francais a raison de les
rattacher a Lachine. La conclusion du commit 8b6e5dc, selon laquelle aucune
attribution n etait possible, venait d une lecture par parametre d URL et ne
tient plus. Ne remettez pas l amende dans le tableau. Frais Montreal de 58 $ a 268 $
selon l arrondissement, Laval 84 $ par arbre, formulaire papier par la poste.
Delais: « non publie » la ou le francais le dit, jamais une estimation.
