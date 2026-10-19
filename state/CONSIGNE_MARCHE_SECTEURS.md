# Serie « Marche immobilier par secteur », consigne commune

Cette consigne s ajoute a `state/CONSIGNE_REDACTEUR.md` et a `state/BRIEF.md`,
qui restent en vigueur en entier: sources primaires, livrables, front matter,
verifications avant de rendre, zero tiret long. Elle ne les remplace que la ou
elle le dit.

## 1. Ce qu est la serie

Pour chaque region (Laval, Montreal, Laurentides, Lanaudiere): un article par
secteur geographique, plus un article synthese qui compare tous les quartiers
de la region. Le trimestre couvert est le **3e trimestre 2026** (juillet a
septembre 2026), le dernier publie par Centris au 19 octobre 2026.

- Le slug est sans annee, et il contient toujours le nom de la ville. C est le
  **titre** qui porte le trimestre.
- Categorie: `Analyse de marché`.
- `date` et `lastmod`: la date donnee dans votre consigne d agent.
- Le front matter suit `state/BRIEF.md` section 9, avec une seule exception:
  le champ `seo_title`, place juste apres `title` (section 1 bis).

## 1 bis. Titres et description, format choisi par Georges le 2026-10-19

Deux titres. Le `title` est le titre visible de la page (H1). Le `seo_title`
remplace le titre dans Google, sans changer le H1: le gabarit
`layouts/_default/baseof.html` le lit deja.

| Champ | Modele | Limite |
|---|---|---|
| `title` | `Marché immobilier à <Quartier>, <Ville>: 3e trimestre 2026` | 75 caracteres |
| `seo_title` | `Prix des maisons et condos à <Quartier>, <Ville> (T3 2026)` | 60 caracteres |
| `description` | quartier, ville et trimestre en ouverture, puis 2 ou 3 chiffres de l article | 155 caracteres |

Regles:

1. **Le nom de la ville est dans les deux titres**, toujours: Laval, Montréal,
   Longueuil, ou la ville elle-meme quand le secteur est une ville (Mirabel,
   Mascouche, Blainville). Exemple: `Marché immobilier à Chomedey, Laval:
   3e trimestre 2026` et `Prix des maisons et condos à Chomedey, Laval
   (T3 2026)`.
2. Plusieurs quartiers: `Marché immobilier à Vimont et Auteuil, Laval:
   3e trimestre 2026`. Si le `title` depasse 75 caracteres, ecrivez `T3 2026`
   au lieu de `3e trimestre 2026`, puis gardez les deux quartiers principaux.
3. `seo_title` au-dela de 60 caracteres: retirez `et condos`; encore trop long,
   gardez le quartier principal seulement. N ecrivez `et condos` que si
   l article donne des chiffres de copropriete.
4. Article synthese: `Marché immobilier à Laval par secteur: 3e trimestre
   2026` et `Prix des maisons à Laval par quartier (T3 2026)`.
5. `description`, exemple: `Chomedey, Laval, au 3e trimestre 2026: 211 ventes,
   unifamiliale à 640 000 $ de prix médian, copropriété à 450 000 $. Chiffres
   Centris.` Chaque chiffre de la description est dans l article.
6. Le nom de la ville apparait dans le premier paragraphe et dans 2 ou 3 H2.
7. Cette consigne prime sur le format de titre de `state/BRIEF.md` pour cette
   serie.

## 2. Les chiffres Centris sont deja recoltes

`state/marche_T3_2026/centris_<region>.json` contient, page par page: l URL
Centris, le nom du territoire, et pour `total_residentiel`, `unifamiliale`,
`copropriete` et `plex` les lignes Ventes, Inscriptions en vigueur, Prix median,
Moyenne de jours sur le marche (plus Nouvelles inscriptions et Volume pour le
total). Chaque ligne donne `trimestre`, `var_trimestre`, `cumul_4t` (cumul des
4 derniers trimestres) et `var_cumul_4t`. Les variations de jours sont en
jours, pas en pourcentage.

Regles:

1. **Ouvrez vous-meme la page Centris de chacun de vos quartiers** au moins une
   fois (curl avec agent de navigateur, voir CONSIGNE_REDACTEUR section 4) et
   lisez ses notes: ce a quoi la variation se compare, ce que couvre le cumul.
   Si la page et le JSON different, la page tranche et vous le signalez.
2. `**` veut dire, selon Centris, « Nombre de transactions insuffisant pour
   produire une statistique fiable ». **Ne comblez jamais un `**`**, ni par un
   calcul ni par une estimation. Dites que Centris ne le publie pas, et utilisez
   le chiffre du cumul des 4 derniers trimestres s il existe, en le nommant
   comme tel.
3. **Ne faites jamais la moyenne ni la somme de prix medians.** Le median d un
   secteur regroupe n existe pas: presentez quartier par quartier.
4. Une variation du prix median n est pas la variation de valeur d une maison
   donnee: la composition des ventes change d un trimestre a l autre. Dites-le
   une fois, en une phrase.
5. Les mois d inventaire officiels sont une mesure de l APCIQ. N en calculez pas
   a partir de Centris. Si vous citez des mois d inventaire, ils viennent d un
   document APCIQ que vous avez ouvert, avec son territoire et sa periode.
6. Chaque page Centris utilisee est une entree de `sources` dans le JSON.
7. Dans le texte, sous chaque tableau, une ligne de source sur le modele de la
   page La Plaine: `Source: [statistiques immobilières de Centris pour
   Laval (Chomedey)](URL), 3e trimestre 2026, soit de juillet à septembre.`

## 3. L actualite du secteur: ce qu il faut chercher

Un article qui ne contient que le tableau Centris n est pas un article
d actualite. Cherchez, pour VOTRE secteur, ce qui a change ou va changer et qui
touche un acheteur ou un vendeur:

- **La ville**: projets d urbanisme et programmes particuliers d urbanisme,
  modifications recentes du zonage, grands chantiers, nouveaux parcs ou
  equipements, programmes de subvention en vigueur, role d evaluation et
  variation moyenne publiee pour le secteur s il y en a une.
- **Le transport**: exo, STM, STL, ARTM, REM (CDPQ Infra), ministere des
  Transports. Seulement un statut confirme par la source officielle, avec sa
  date.
- **Le logement**: SCHL (mises en chantier, taux d inoccupation par zone de
  l Enquete sur les logements locatifs, avec l annee de l enquete), CMM,
  Institut de la statistique du Quebec.
- **L eau**: zones inondables et cartes applicables, pour les quartiers
  riverains.

Chaque nouvelle est datee, sourcee a une page officielle, et rattachee a une
consequence pratique pour le lecteur. Un article de presse locale peut vous
indiquer quel document officiel chercher, il n est jamais une source.

**Interdit**: annoncer l effet d un projet sur les prix (« le REM fera monter
les prix ») sans source qui le mesure. Si rien de verifiable n existe pour un
theme, omettez le theme. Ne remplissez pas.

## 4. Le contexte regional est deja verifie

`state/marche_T3_2026/contexte_<region>.md` contient les faits communs a toute
la region (taux directeur, communique APCIQ, droits de mutation, role
d evaluation, cadre des zones inondables, transport), chacun avec sa source.
Vous pouvez les reprendre en citant la meme source dans votre JSON, apres
l avoir rouverte.

Dans un article de secteur, **le contexte regional tient en trois phrases au
plus**: l article synthese le couvre. Ecrivez ces phrases vous-meme. Les
articles de la serie ne doivent pas partager de paragraphes identiques, sinon
la porte de contenu de `dedupe.py` les rejette.

## 5. Structure

**Article de secteur**, 1 200 a 1 800 mots:

1. Accroche de 2 a 4 phrases avec le chiffre qui compte.
2. Les chiffres du secteur: un tableau par categorie qui a des donnees
   (unifamiliale, copropriete, plex), une ligne par quartier, colonnes courtes.
3. La comparaison entre les quartiers du secteur et avec l ensemble de la
   region, chiffres a l appui.
4. Ce qui a change en un an, limite a ce que les donnees montrent.
5. Une ou deux sections d actualite du secteur (section 3 ci-dessus).
6. Ce que ces chiffres changent pour un vendeur, puis pour un acheteur:
   concret, sans promesse, sans verdict sur le « bon moment ».
7. `## Questions fréquentes`, 3 a 5 questions.
8. Le bloc de fin de `state/BRIEF.md` section 6.

**Article synthese**, 1 300 a 1 900 mots: le tableau de tous les quartiers de
la region (ventes du trimestre et variation, prix median de l unifamiliale au
trimestre ou, a defaut, sur 4 trimestres, jours sur le marche), la copropriete
et le plex a l echelle de la region, le contexte regional, et une section qui
presente les secteurs de la serie par leur nom, **sans lien**.

## 6. Liens

- **Aucun lien vers un autre article de cette serie**: ils sont tous en
  brouillon, et le validateur refuse un lien vers un brouillon. Le
  coordinateur ajoute ce maillage apres publication.
- Les pages de ville et de quartier qui existent, par exemple
  `/courtier-immobilier/chomedey-laval/`, se prennent dans
  `state/internal_links_fr.md`, comme les 3 a 5 articles existants.
- Les pages Centris sont des liens externes, dans la ligne de source.

## 7. Conformite: ce qui fait rejeter un texte de cette serie

- Une prediction de prix, de delai ou de rendement.
- Un verdict « marche vendeur » ou « marche acheteur » qui ne vient pas d un
  document APCIQ pour ce territoire et cette periode.
- Le prix d une propriete vendue en particulier, ou ce qui permet de le
  deduire.
- « Expert », « specialiste », « le meilleur », toute affirmation sur
  l activite de Georges dans le secteur, toute anecdote. Le « je » apparait
  au plus deux fois, jamais en ouverture.
- Une promesse de service en espagnol.

## 8. Dedupe dans une serie

`python tools/dedupe.py check drafts/fr/<SLUG>.md`. Contre un autre article de
**cette serie**, un REVIEW ou un FAIL sur le titre, le slug ou le mot-cle est
attendu, a cause du gabarit commun: il est tolere si les portes `topic` et
`content` passent contre lui. Tout FAIL `content` ou `topic`, et tout FAIL
contre un article hors serie, se corrige.
