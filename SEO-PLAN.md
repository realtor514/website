# Plan SEO - georgesmatar.ca + Google Business Profile

Date: 2026-08-05

---

## PARTIE 1 - Ce qui est deja fait (site web)

Tout ceci est en ligne. Le deploiement GitHub Pages prend 2 a 3 minutes.

| Element | Avant | Apres |
|---|---|---|
| Pages indexables (FR) | 28 | 103 |
| Pages indexables (EN) | 28 | 101 |
| Pages indexables (AR) | 28 | 101 |
| Pages indexables (ES) | 28 | 52 |
| Donnees structurees | aucune | 8 types de schema |
| Balises hreflang | aucune | 4 langues + x-default |
| robots.txt | vide | sitemaps + bots IA autorises |
| Pages ciblant une ville | 0 | 56 (14 villes x 4 langues) |
| FAQ structuree | aucune | 8 questions x 4 langues |

### Detail

**1. Donnees structurees JSON-LD**
Google sait maintenant que tu es un courtier immobilier local, ou tu es situe,
quelles villes tu couvres, quelles langues tu parles et quels sont tes horaires.
C'est ce qui permet d'apparaitre dans le pack local (la carte avec 3 resultats).

**2. Balises hreflang**
Avant, tes 4 langues se faisaient concurrence dans Google. Maintenant Google
sait que ce sont des traductions et sert la bonne version selon l'utilisateur.

**3. 147 articles publies**
49 articles etaient marques `draft: true` en FR, EN et AR. Ils avaient leurs
images, leurs descriptions, tout etait pret. Ils etaient invisibles pour Google.
Ils sont maintenant en ligne.

**4. Pages par ville** (le plus gros levier pour les leads)

Rive-Nord et Laurentides: `/courtier-immobilier/laval/`, `/terrebonne/`,
`/blainville/`, `/repentigny/`, `/saint-jerome/`

Île de Montréal: `/courtier-immobilier/montreal/`

Rive-Sud et Montérégie: `/courtier-immobilier/longueuil/`, `/brossard/`,
`/boucherville/`, `/saint-bruno-de-montarville/`, `/chambly/`, `/la-prairie/`,
`/candiac/`, `/delson/`

Et les equivalents en EN (`/en/real-estate-broker/...`), ES
(`/es/corredor-inmobiliario/...`) et AR (`/ar/wasit-aqari/...`).

Ces pages ciblent exactement les requetes qui generent des leads:
"courtier immobilier Laval", "real estate broker Laval", etc.

**5. FAQ sur l'accueil**
8 questions dans chaque langue, avec le schema FAQPage. Ces reponses peuvent
apparaitre directement dans les resultats Google.

---

## PARTIE 2 - Ce que tu dois faire toi (30 a 60 min, une seule fois)

Ces etapes demandent tes identifiants. Je ne peux pas les faire a ta place.

### A. Google Search Console (10 min) - PRIORITE 1

Sans ca, Google decouvre tes 300 nouvelles pages en quelques semaines au lieu
de quelques jours.

1. Va sur https://search.google.com/search-console
2. Ajoute la propriete `georgesmatar.ca` (choisis "Prefixe d'URL",
   pas "Domaine", c'est plus simple avec GitHub Pages)
3. Methode de verification: choisis "Balise HTML". Google te donne un code
   du type `<meta name="google-site-verification" content="ABC123...">`.
   **Envoie-moi ce code, je l'installe dans le site en 2 minutes.**
4. Une fois verifie, va dans "Sitemaps" et soumets:
   - `sitemap.xml`
   - `fr/sitemap.xml`
   - `en/sitemap.xml`
   - `es/sitemap.xml`
   - `ar/sitemap.xml`

### B. Google Business Profile (30 min) - PRIORITE 1

C'est ce qui genere le plus de leads pour un courtier. La majorite des gens qui
cherchent "courtier immobilier Laval" cliquent sur le pack local, pas sur les
resultats bleus.

Va sur https://business.google.com

**1. Categorie principale**
Mets exactement: **Agence immobiliere** ou **Courtier immobilier**
(pas "Service immobilier", pas "Consultant"). La categorie principale est
le facteur numero 1 du classement local.

Categories secondaires a ajouter:
- Agent immobilier
- Service d'evaluation immobiliere
- Immobilier commercial (si applicable)

**2. Nom de l'etablissement**
`Georges Matar - Courtier immobilier | RE/MAX Du Cartier`

Ne mets pas de mots-cles supplementaires (Google peut suspendre la fiche).

**3. Adresse et zone de service**
- Adresse: 2820, boul. St-Martin Est, Bureau 201, Laval (Duvernay), QC H7E 5A1
- Active "Je sers aussi mes clients en dehors de cette adresse"
- Zones de service a ajouter: Laval, Montreal, Longueuil, Brossard, Terrebonne,
  Boucherville, Blainville, Repentigny, Saint-Bruno-de-Montarville, Chambly,
  La Prairie, Candiac, Delson, Saint-Jerome, Boisbriand, Sainte-Therese,
  Rosemere, Mascouche, Mirabel, Saint-Eustache, Sainte-Julie, Varennes

**4. Horaires**
Mets des horaires reels et larges (ex. lundi-dimanche 8h-20h). Une fiche sans
horaires perd des positions.

**5. Description (750 caracteres max)**
Copie-colle ceci:

> Georges Matar, courtier immobilier residentiel chez RE/MAX Du Cartier, dessert
> Laval, Montreal, Longueuil, Brossard, Terrebonne, Boucherville, Repentigny et
> l'ensemble de la Rive-Nord, de la Rive-Sud, des Laurentides, de Lanaudiere et
> de la Monteregie. Achat, vente et
> investissement immobilier: analyse comparative de marche gratuite, strategie de
> prix basee sur les donnees reelles du secteur, negociation et accompagnement
> jusqu'a la signature chez le notaire. Services offerts en francais, anglais,
> espagnol et arabe. Les programmes exclusifs RE/MAX Quebec sont inclus sans
> frais: Tranquilli-T (assistance juridique), Integri-T (jusqu'a 50 000 $ de
> protection contre les vices caches pendant 3 ans) et Coproprie-T (expertise en
> copropriete). Premiere consultation gratuite et sans engagement.

**6. Photos - minimum 20** (c'est le point le plus neglige)
- 1 logo (RE/MAX Du Cartier)
- 1 photo de couverture (toi, professionnelle)
- 3 a 5 photos de l'exterieur du bureau (dont une avec l'enseigne visible)
- 3 a 5 photos de l'interieur du bureau
- 5 a 10 photos de proprietes vendues ou d'inscriptions
- 2 a 3 photos de toi en action (visite, signature, remise de cles)

Les fiches avec 20+ photos recoivent nettement plus d'appels que celles avec 5.

**7. Lien du site web**
Mets: `https://georgesmatar.ca/?utm_source=google&utm_medium=organic&utm_campaign=gbp`

Ca te permettra de savoir combien de visites viennent de ta fiche Google.

**8. Bouton de rendez-vous**
Ajoute ton lien cal.com dans "Reservations".

**9. Messagerie**
Active la messagerie. Google favorise les fiches qui repondent vite.

**10. Questions/Reponses**
Publie toi-meme 5 questions et reponds-y (c'est permis et recommande):
- "Est-ce que l'evaluation de ma propriete est gratuite?"
- "Quelles villes desservez-vous sur la Rive-Sud?"
- "Parlez-vous arabe et espagnol?"
- "Combien coute un courtier pour un acheteur?"
- "Offrez-vous une protection contre les vices caches?"

### C. Les avis - PRIORITE 1 (c'est ce qui fait la difference)

Le nombre et la fraicheur des avis sont le 2e facteur de classement local apres
la categorie. Un courtier avec 30 avis bat presque toujours un courtier avec 3.

**Objectif: 20 avis dans les 90 prochains jours.**

1. Dans Google Business Profile, recupere ton lien direct d'avis
   ("Demander des avis" -> copie le lien court `g.page/r/...`)
2. Envoie-le a **tous** tes anciens clients, pas seulement les recents. Message
   type:

> Bonjour [Prenom], j'espere que vous etes bien installes. Je construis ma
> presence en ligne et un avis Google de votre part m'aiderait beaucoup. Ca
> prend 30 secondes: [lien]. Merci!

3. Ensuite, demande systematiquement un avis **le jour de la signature chez le
   notaire**, pas trois semaines apres. Le taux de reponse est 5 fois plus eleve.
4. Reponds a **chaque** avis, positif comme negatif, dans les 48 heures. Google
   mesure ton taux de reponse.

### D. Publications Google (10 min par semaine)

Chaque semaine, publie un post dans ta fiche Google. Le plus simple: reprends
un de tes articles.

Tu as 147 articles publies. Ca te fait presque 3 ans de contenu hebdomadaire.

Format: 1 photo + 2 phrases + bouton "En savoir plus" vers l'article.

### E. Coherence NAP (nom, adresse, telephone) - 20 min

Google verifie que tes coordonnees sont identiques partout. La moindre
difference (bureau 201 vs suite 201, 438-372-0102 vs (438) 372-0102) dilue ton
autorite locale.

Verifie et corrige sur:
- Ta fiche RE/MAX Quebec
- Ton profil Centris
- Facebook (page professionnelle)
- LinkedIn
- Pages Jaunes / YellowPages
- Yelp

Format de reference a utiliser partout:
```
Georges Matar - Courtier immobilier | RE/MAX Du Cartier
2820, boul. St-Martin Est, Bureau 201
Laval (Duvernay), QC H7E 5A1
(438) 372-0102
https://georgesmatar.ca
```

---

## PARTIE 3 - Ce que je fais des que tu me donnes l'information

| Ce dont j'ai besoin | Ce que je fais |
|---|---|
| Le code de verification Search Console | Je l'installe dans le site |
| L'URL Google Maps de ta fiche (format `https://maps.app.goo.gl/...`) | Je la lie au site dans les donnees structurees, ce qui connecte ta fiche et ton site aux yeux de Google |
| Tes liens Facebook / Instagram / LinkedIn | Je les ajoute au schema (champ `sameAs`), ce qui renforce ton entite dans le Knowledge Graph |
| Ta note et ton nombre d'avis Google | J'ajoute le schema AggregateRating (les etoiles peuvent apparaitre dans les resultats de recherche) |

---

## PARTIE 4 - Prochaines ameliorations du site (par ordre d'impact)

1. **Completer l'espagnol.** L'ES a 44 pages contre 93 pour EN et AR. Il manque
   environ 32 articles. C'est la seule langue incomplete.
2. **Etoffer les articles courts.** Environ 49 articles font 250 a 350 mots.
   Google favorise nettement les contenus de 800 a 1500 mots sur les sujets
   concurrentiels. Priorite aux 10 articles qui ciblent les requetes les plus
   commerciales (commission, evaluation, premier acheteur, taxe de bienvenue).
3. **Ajouter des pages villes secondaires**: Boisbriand, Sainte-Therese,
   Rosemere, Mascouche, Mirabel, Saint-Eustache, Sainte-Julie, Varennes,
   Chateauguay, Saint-Constant, Sainte-Catherine.
4. **Ajouter des inscriptions reelles** dans `/listings/`. Une page par
   propriete avec le schema `RealEstateListing` genere des leads directs.
5. **Optimiser la vitesse.** Les polices Google Fonts sont chargees depuis un
   domaine externe, ce qui coute environ 300 ms. Les heberger localement
   ameliore le Core Web Vital LCP.

---

## Calendrier realiste des resultats

| Delai | Ce qui se passe |
|---|---|
| 2 a 3 jours | Google indexe les nouvelles pages (si Search Console est configure) |
| 2 a 4 semaines | Les pages villes commencent a apparaitre sur les requetes longue traine |
| 4 a 8 semaines | La fiche Google gagne des positions dans le pack local (si les avis suivent) |
| 3 a 6 mois | Positionnement sur "courtier immobilier Laval" et equivalents |

Le SEO local n'est pas instantane. Mais l'element qui accelere le plus tout le
reste, ce sont les avis Google. C'est la seule chose que je ne peux pas faire a
ta place, et c'est celle qui compte le plus.
