# Lot 6, consignes de traduction par article

Regles generales: `state/BRIEF_TRADUCTION.md`, a lire en entier d abord.
Cartes de liens: `state/internal_links_en.md`, `_es.md`, `_ar.md`.

**Le drapeau draft.** Ecrivez `draft: true`. Une etape automatisee passera
ensuite les fichiers en `draft: false`. C est la publication qui fonctionne
normalement, ce n est pas une corruption. Ne le remettez jamais a true, et ne
retouchez pas `lastmod` apres l avoir ecrit.

**Ne liez jamais un article marque (brouillon) dans la carte de liens.** Hugo
ne rend pas les brouillons, donc le lien renvoie 404 en production. Le
validateur refuse maintenant ce cas.

**Absolu:** zero tiret long, demi-cadratin ou double tiret. Longueur a 15 % du
francais, sauf l arabe ou 80 % suffit. Chiffres en caracteres latins en arabe.
Section Questions frequentes gardee, titre dans la langue cible. Noms
d organismes, formulaires et termes juridiques gardes en francais, glose a la
premiere occurrence. CTA du formulaire: `/en/form/`, `/es/formulario/`,
`/ar/istimara/`. Chaque article garde `needs_expert_review: true`.

---

## B1. contrat-courtage-achat-quebec

- translationKey `article-contrat-courtage-achat`, date et lastmod **2026-08-28**
- categorie: en `Real Estate 101`, es `Inmobiliaria 101`, ar `عقارات 101`
- fichiers: `content/en/articles/buyer-brokerage-contract-quebec.md`,
  `content/es/articles/contrato-corretaje-compra-quebec.md`,
  `content/ar/articles/buyer-brokerage-contract-quebec.md`
- voix: `content/{lang}/articles/commission-explained-quebec.md`
- a preserver exactement: le nom et le numero du formulaire CCA 00001, le
  formulaire distinct CCADI pour la copropriete depuis le 29 novembre 2023, la
  clause 6 et surtout la clause 6.2, la clause 3.1, la clause R2.5 de l annexe R,
  l article 29.1 et l article 27 alinea 2, les 180 jours, et le tableau a quatre
  lignes. Ne renumerotez aucune clause.
- l article souleve une question ouverte entre le libelle de la clause 6.1 et
  celui de la loi: gardez-la comme une question, ne la tranchez pas.

## B2. deces-conjoint-proteger-propriete-quebec

- translationKey `article-deces-conjoint`, date et lastmod **2026-09-03**
- categorie: en `Real Estate 101`, es `Inmobiliaria 101`, ar `عقارات 101`
- fichiers: `content/en/articles/protecting-home-after-death-quebec.md`,
  `content/es/articles/proteger-vivienda-fallecimiento-quebec.md`,
  `content/ar/articles/protecting-home-after-death-quebec.md`
- voix: `content/{lang}/articles/inheritance-property-quebec.md`
- a preserver exactement: les articles 2457, 2459, 2462 et 2999, les trois
  formes de testament, la distinction entre une assurance vendue par le preteur
  et une police personnelle, et le fait que l insaisissabilite et la caducite ne
  visent que l epoux et le conjoint uni civilement, jamais le conjoint de fait.
- ne rajoutez pas de lien vers l article sur les conjoints de fait: il est
  encore en brouillon.

## B3. loi-16-copropriete-acheteur-quebec

- translationKey `article-loi-16-copropriete`, date et lastmod **2026-09-10**
- categorie: en `Buyer's Guide`, es `Guía del Comprador`, ar `دليل المشتري`
- fichiers: `content/en/articles/condo-buyer-disclosure-quebec.md`,
  `content/es/articles/documentos-condominio-comprador-quebec.md`,
  `content/ar/articles/condo-buyer-disclosure-quebec.md`
- voix: `content/{lang}/articles/condo-fees-investment-killer.md`
- a preserver exactement, c est le coeur de l article: ce qui s applique
  aujourd hui contre ce qui est encore a venir. L attestation du syndicat de
  l article 1068.1 sans transition depuis le 14 aout 2025, mais le premier
  carnet d entretien et la premiere etude du fonds de prevoyance seulement le
  15 aout 2028. Un syndicat sans carnet en 2026 n est donc pas en faute.
  Gardez aussi le 100 000 $, les minimums de 1 000 000 $ et 2 000 000 $, les
  30 jours, les 10 ans, la clause 9.1 et les fenetres de 15 jours, et la
  mention que le certificat RBQ d inspecteur n est exige qu au 1er octobre 2027.

## B4. proprietaire-occupant-plex-reprise

- translationKey `article-occupant-plex`, date et lastmod **2026-09-18**
- categorie: en `Investment`, es `Inversión`, ar `استثمار`
- fichiers: `content/en/articles/owner-occupied-plex-repossession-quebec.md`,
  `content/es/articles/plex-ocupado-propietario-quebec.md`,
  `content/ar/articles/owner-occupied-plex-repossession-quebec.md`
- voix: `content/{lang}/articles/rental-property-management.md`
- a preserver exactement: les articles 1958, 1959.1, 1960, 1963, 1964 et 1968,
  le seuil de 65 ans avec 10 ans d occupation et un revenu a 125 % du plafond
  d admissibilite HLM, la loi sanctionnee le 6 juin 2024, le gel de trois ans
  sur l eviction, et l arithmetique de calendrier: six mois d avis avant un bail
  qui finit le 30 juin, donc une prise de possession au printemps repousse
  l entree au 30 juin de l annee suivante.
- ne promettez jamais qu une reprise reussira.

## B5. reglement-piscine-securite-quebec

- translationKey `article-piscine-reglement`, date et lastmod **2026-09-24**
- categorie: en `Practical Guide`, es `Guía práctica`, ar `دليل عملي`
- fichiers: `content/en/articles/pool-safety-rules-quebec.md`,
  `content/es/articles/reglamento-piscinas-quebec.md`,
  `content/ar/articles/pool-safety-rules-quebec.md`
- voix: `content/{lang}/articles/renovations-dont-add-value.md`
- a preserver exactement: l echeance du **30 septembre 2027** pour les
  installations anterieures au 1er novembre 2010, le decret 120-2026, la
  cloture de 1,2 m, la porte a fermeture et loquet automatiques, la regle du
  metre pour tout ce qui est escaladable, les trois modes d acces permis pour
  une piscine hors terre ou demontable, l amende de 500 $ a 700 $ et
  l article 1457 du Code civil.
- **l echeance n est pas passee.** Si votre traduction laisse entendre le
  contraire, elle est fausse. C est le point le plus important du texte.
- le lien du milieu pointe vers la page de ville: `/en/real-estate-broker/laval/`,
  `/es/corredor-inmobiliario/laval/`, `/ar/wasit-aqari/laval/`.
