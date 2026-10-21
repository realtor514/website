# Serie « Les 10 questions des vendeurs », consigne commune

Cette consigne s ajoute a `state/CONSIGNE_REDACTEUR.md` et a `state/BRIEF.md`,
qui restent en vigueur en entier. Elle ne les remplace que la ou elle le dit.

## 1. Le but

Georges a donne, le 2026-10-19, les dix questions que ses clients vendeurs
posent le plus. Chaque article repond a une de ces questions mieux que toute
autre page, pour un proprietaire de Laval, de Montreal ou des couronnes. Le
lecteur repart avec la reponse, chiffree pour sa ville, et une raison concrete
d ecrire a Georges. Pas une seule affirmation que Georges ne pourrait pas
demontrer a l OACIQ.

Votre ligne de plan (`state/content_plan.json`) donne la question, la requete
principale et, dans `requetes`, des recherches reelles relevees dans les
suggestions de Google le 2026-10-19. Ce sont les formulations a reprendre.

## 2. Un format pense pour Google et ses reponses generees

1. **L accroche est la reponse.** Les 2 ou 3 premieres phrases, 40 a 60 mots,
   repondent directement a la question, avant tout contexte, et nomment Laval.
   Un lecteur qui s arrete la a sa reponse.
2. **2 ou 3 H2 sont formules comme les questions tapees**, reprises de
   `requetes`, avec leurs mots.
3. **Une liste numerotee** quand la question est un « comment ». **Un tableau**
   quand on compare.
4. **Questions frequentes**: 4 a 6 questions qui reprennent mot pour mot des
   formulations de `requetes`, dont au moins une avec le nom d une ville. La
   premiere phrase de chaque reponse est la reponse.

## 3. Les villes, mots-cles de chaque article

Georges veut le nom des villes en mots-cles. Le territoire: Laval, Montreal,
Longueuil, Brossard, Terrebonne, Mascouche, Repentigny, Blainville, Mirabel,
Saint-Jerome, Saint-Eustache.

- **Laval** est dans le `title`, le `seo_title`, la `description`, l accroche et
  un ou deux H2. **Montreal** apparait dans l accroche ou le premier H2.
- **Une section « Dans votre ville »** (formulation libre) avec un tableau: une
  ligne par ville du territoire, et la mesure Centris du 3e trimestre 2026 qui
  repond a la question de l article (prix median pour la valeur, jours sur le
  marche pour le delai, ventes et inscriptions en vigueur pour les conditions,
  etc.). Les donnees sont deja recoltees:
  - Laval et ses 13 quartiers: `state/marche_T3_2026/centris_laval.json`
  - Ile de Montreal: `state/marche_T3_2026/centris_montreal-ile.json` (page
    de region `montreal-ile`)
  - Longueuil (trois arrondissements, Centris ne publie pas de total pour la
    ville: dites-le) et Brossard: `centris_montreal-rive-sud.json`
  - Terrebonne (trois secteurs), Mascouche, Repentigny (deux secteurs):
    `centris_lanaudiere.json`
  - Blainville, Mirabel, Saint-Jerome, Saint-Eustache: `centris_laurentides.json`
  Les regles de `state/CONSIGNE_MARCHE_SECTEURS.md` section 2 s appliquent:
  ouvrez les pages Centris que vous citez, ne comblez jamais un `**`, ne faites
  jamais la moyenne de medianes, une ligne de source sous le tableau.
- Pas de bourrage: chaque mention d une ville porte un chiffre ou un fait.

## 4. Titres et description

Meme systeme que la serie de marche, choisi par Georges:

- `title` (H1, 75 caracteres au plus): la question, avec « à Laval ». Exemple:
  `Combien vaut ma maison aujourd'hui à Laval?`
- `seo_title`, place juste apres `title`, 60 caracteres au plus: commence par
  les mots de la requete principale et contient Laval. Exemple: `Combien vaut
  ma maison à Laval? Chiffres du T3 2026`.
- `description`, 155 caracteres au plus: la reponse en une phrase, avec Laval
  et un chiffre.

## 5. Les deux appels a l action

- Au milieu: l outil ou la page de service qui sert vraiment le paragraphe
  (`/tools/home-estimate/`, `/tools/closing-costs/`, `/tools/welcome-tax/`,
  `/seller/`...).
- A la fin: le bloc `/formulaire/` de `state/BRIEF.md`, avec une offre liee a
  la question. Exemple: « Vous voulez le chiffre pour votre adresse? Je
  prépare une analyse comparative de marché sans frais, avec les ventes de
  votre rue. [Écrivez-moi](/formulaire/). Service en français, en anglais et
  en arabe. »

## 6. Conformite OACIQ, plus stricte encore que d habitude

- **Aucune affirmation de rang ou de competence sur Georges**: ni « meilleur »,
  ni « expert », ni « specialiste », ni volume de ventes, ni annees
  d experience. Georges a obtenu son permis en mai 2026.
- **Aucune prediction ni verdict**: on ne dit jamais « c est le bon moment »,
  « les prix vont monter », « vous vendrez en X jours ». On donne les mesures
  datees et ce qu elles signifient, et la decision reste au lecteur.
- **L opinion de prix d un courtier** est une « valeur marchande estimee » ou
  une « analyse comparative de marche ». Jamais une « evaluation » de la
  « valeur reelle »: seul un evaluateur agree de l OEAQ produit une
  evaluation reconnue. Le role foncier n est pas la valeur marchande.
- **La retribution se negocie**: aucun « taux habituel » sans source.
- **Aucun denigrement** de DuProprio, d un autre courtier ou d une autre
  formule. L offre de DuProprio se decrit avec sa propre page, citee et datee.
- **Aucun rendement de renovation** sans source quebecoise: si aucune source
  ne chiffre ce qu une renovation rapporte a la revente, l article le dit.
- **Prix demande gonfle**: on expose ce que les donnees montrent, sans
  recommander une tactique que rien ne mesure.
- **Financement** (pret-relais, double hypotheque): on explique le mecanisme
  et on renvoie au preteur ou au courtier hypothecaire pour la decision.
- Aucun temoignage, aucune anecdote, aucun « mes clients ». Georges sert en
  francais, en anglais et en arabe, jamais en espagnol.

## 7. Liens, les « backlinks » internes

- **Vers les articles existants qui approfondissent**: ceux de `distinct_de`
  en priorite. Vous renvoyez au lieu de repeter. 3 a 6 liens au total.
- **Vers la serie de marche de Laval deja publiee** quand un quartier est
  cite: les chemins sont dans `state/internal_links_fr.md` (articles
  `marche-immobilier-...-laval...`).
- **Vers les pages de ville** `/courtier-immobilier/...` des villes du tableau
  qui en ont une.
- **Liens externes vers les sources officielles**: les pages Centris citees,
  l OACIQ, l APCIQ.
- **Aucun lien vers un autre article de cette serie**: ils sont en brouillon.
  Le coordinateur les relie apres publication.

## 8. Dedupe

`distinct_de` nomme les articles du site les plus proches. Lisez-les avant
d ecrire: votre article est la version locale et chiffree, eux restent la
reference generale. `python tools/dedupe.py check` doit passer sans FAIL
`topic` ni `content`. Si un FAIL tombe, recentrez sur Laval, les chiffres des
villes et la question exacte.
