# Plan SEO - georgesmatar.ca + Google Business Profile

Date: 2026-08-05

---

## PARTIE 1 - Ce qui est deja fait (site web)

Tout ceci est en ligne. Le deploiement GitHub Pages prend 2 a 3 minutes.

| Element | Avant | Apres |
|---|---|---|
| Pages indexables (FR) | 28 | 113 |
| Pages indexables (EN) | 28 | 111 |
| Pages indexables (AR) | 28 | 111 |
| Pages indexables (ES) | 28 | 62 |
| Donnees structurees | aucune | 8 types de schema |
| Balises hreflang | aucune | 4 langues + x-default |
| robots.txt | vide | sitemaps + bots IA autorises |
| Pages ciblant une ville | 0 | 120 (30 villes x 4 langues, 2026-09-19) |
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

Rive-Nord, Laurentides et Lanaudiere (11): Laval, Terrebonne, Blainville,
Repentigny, Saint-Jerome, Boisbriand, Sainte-Therese, Rosemere, Mascouche,
Saint-Eustache, Mirabel

Ile de Montreal (1): les 19 arrondissements

Rive-Sud et Monteregie (12): Longueuil, Brossard, Boucherville,
Saint-Bruno-de-Montarville, Chambly, La Prairie, Candiac, Delson,
Sainte-Julie, Varennes, Chateauguay, Saint-Constant

Format des URL: `/courtier-immobilier/<ville>/`

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

### Par ou commencer, d'apres Search Console (mis a jour le 2026-10-07)

**Pourquoi c'est maintenant la priorite.** Sur 3 mois, Google a montre tes
pages de secteurs 5 500 fois, sur 4 200 recherches du type "courtier immobilier
+ ville". Elles sont donc jugees pertinentes. Mais leur position moyenne est 38,
soit la page 4: personne ne clique. Ce qui manque n'est pas dans le code, c'est
la confiance que Google accorde au site et a la fiche, et elle vient de trois
choses: les avis, les mentions dans les annuaires, les liens d'autres sites.

**Ce mois-ci, dans cet ordre:**

1. **Le bouton "source preferee" de Google** (ajoute le 2026-10-08). Depuis
   aout 2026, un visiteur peut ajouter ton site a ses sources preferees Google
   depuis un bouton place sur ton propre site, sans quitter la page. Ensuite,
   il voit tes pages avec un badge "preferee" dans A la une (Top Stories), les
   apercus IA et le mode IA, la ou les clics disparaissent aujourd'hui. Selon
   la video, Google annonce deux fois plus de clics sur une source preferee
   (chiffre non verifie). Ce n'est pas un truc de classement: ce sont tes
   lecteurs fideles qui te choisissent, a chaque recherche.
   - **A verifier d'abord, par toi.** Ouvre, connecte a ton compte Google,
     `https://www.google.com/preferences/source?q=georgesmatar.ca`. Si le site
     n'apparait pas dans l'outil, le bouton ne fera rien. Seul un domaine entier
     est admissible, pas un sous-dossier: georgesmatar.ca l'est. Il faut aussi
     publier du contenu frais, ce que font les 3 articles par semaine. Pour les
     apercus IA et le mode IA, le site doit en plus etre admissible aux
     fonctions d'IA de la recherche, a verifier dans Search Console.
   - **Version code, je m'en occupe.** Deux lignes. Dans le `<head>`:
     `<script async src="https://news.google.com/swg/js/v1/publisher.js"></script>`.
     La ou le bouton doit apparaitre: `<div google-add-preferred-source-btn></div>`,
     avec `data-theme="dark"` sur fond navy et `data-lang` pour forcer fr, en,
     es ou ar. Google dessine le bouton, le traduit et gere le mode sombre.
     **Ta decision, c'est un choix de design:** ou le placer (fin de chaque
     article, pied de page, ou les deux).
   - **Version sans code, pour toi.** Le meme lien, a coller dans la bio
     Instagram et Facebook, la signature courriel, l'infolettre et les messages
     aux clients.
   - Source: [Google Search Central, Preferred Sources](https://developers.google.com/search/docs/appearance/preferred-sources)
2. **10 avis Google en 30 jours.** Messages prets ci-dessous, dans les 4 langues.
3. **Les 8 annuaires de l'etape 1**, plus bas. Descriptions pretes ci-dessous.
4. **Centris**: verifier que ta fiche courtier pointe vers `https://georgesmatar.ca`.
5. **Une chambre de commerce locale.** L'adhesion est payante, mais la fiche
   membre donne un lien local que Google respecte, dans les villes ou tes pages
   sont les plus vues. Par ordre d'impressions: Terrebonne et Mascouche
   (Chambre de commerce et d'industrie Les Moulins), Blainville, Rosemere,
   Boisbriand, Sainte-Therese et Lorraine (Chambre de commerce et d'industrie
   Therese-De Blainville), puis Laval (Chambre de commerce et d'industrie de
   Laval). Verifie le cout et ce que comprend la fiche avant de payer.

#### Demander un avis: messages a copier

Le lien: dans Google Business Profile, "Demander des avis", copie le lien court
`g.page/r/...` et remplace `[lien]`. Envoie a tous tes anciens clients, puis
systematiquement le jour de la signature chez le notaire.

Demander au client de mentionner la ville et le type de transaction est permis:
c'est une suggestion, pas un texte impose. Ne jamais offrir de contrepartie,
Google retire les avis obtenus contre un avantage.

**Francais, courriel**
> Bonjour [Prénom], j'espère que tout va bien dans la maison. J'ai une petite
> demande: un avis Google de votre part aiderait d'autres familles à me trouver.
> Ça prend 30 secondes: [lien]. Si vous le souhaitez, mentionnez la ville et ce
> que nous avons fait ensemble, achat ou vente. Merci beaucoup! Georges

**Francais, texto**
> Bonjour [Prénom], c'est Georges. Un avis Google de votre part m'aiderait
> beaucoup, 30 secondes: [lien]. Merci!

**English, email**
> Hi [First name], I hope you are enjoying the house. A small favour: a Google
> review from you would help other families find me. It takes 30 seconds:
> [lien]. If you like, mention the city and what we did together, buying or
> selling. Thank you so much! Georges

**English, text**
> Hi [First name], it's Georges. A Google review would help me a lot, it takes
> 30 seconds: [lien]. Thank you!

**Español, correo**
> Hola [Nombre], espero que estén disfrutando de la casa. Un pequeño favor: una
> reseña en Google ayudaría a otras familias a encontrarme. Toma 30 segundos:
> [lien]. Si lo desea, mencione la ciudad y lo que hicimos juntos, compra o
> venta. ¡Muchas gracias! Georges

**العربية، رسالة**
> مرحباً [الاسم]، أتمنى أن تكونوا مرتاحين في منزلكم الجديد. لدي طلب صغير: تقييمكم
> على Google يساعد عائلات أخرى على إيجادي. يستغرق 30 ثانية فقط: [lien]. وإن
> رغبتم، اذكروا المدينة ونوع المعاملة، شراء أو بيع. شكراً جزيلاً! جورج

#### Descriptions pretes pour les annuaires

Coordonnees: toujours le bloc de la section E, au caractere pres.

**Courte, francais (moins de 250 caracteres)**
> Georges Matar, courtier immobilier résidentiel chez RE/MAX Du Cartier à
> Laval. Achat, vente et évaluation gratuite à Laval, Montréal, sur la
> Rive-Nord et la Rive-Sud. Services en français, anglais, espagnol et arabe.

**Short, English (under 250 characters)**
> Georges Matar, residential real estate broker with RE/MAX Du Cartier in
> Laval. Buying, selling and free home evaluations in Laval, Montreal, the
> North Shore and the South Shore. Service in French, English, Spanish and
> Arabic.

**Longue, francais:** la description Google de la section B, telle quelle.

**Long, English**
> Georges Matar, residential real estate broker with RE/MAX Du Cartier. I
> serve Laval, Montreal, Longueuil, Brossard, Terrebonne, Boucherville and
> Repentigny, as well as the North Shore, the South Shore, the Laurentians,
> Lanaudière and Montérégie. Buying, selling and investing: a comparative
> market analysis, pricing based on real data for your area, negotiation and
> guidance through to the notary signing. Service in French, English, Spanish
> and Arabic. Included at no cost: Tranquilli-T, RE/MAX Québec's exclusive
> legal assistance. Optional, paid: the Intégri-T guarantee, up to $50,000
> against latent defects for 3 years. Coproprié-T certified (condominiums).
> Contact me for a free consultation.

### 0. Citations et annuaires d'entreprises - PRIORITE 1

Objectif: que `georgesmatar.ca`, le nom de courtage et la fiche Google Business
soient cites le plus souvent possible sur des annuaires d'entreprises, a Laval,
a Montreal, au Quebec, et sur les plateformes que consultent les acheteurs
etrangers.

Une citation, c'est une mention de ton nom, ton adresse et ton telephone sur un
site tiers. Google compte ces mentions pour decider quelles fiches il montre
dans le pack local. Trois annuaires bien remplis valent mieux que trente
remplis a moitie.

**Regle absolue avant de commencer.** Tes coordonnees doivent etre ecrites
exactement de la meme facon sur chaque annuaire. Meme nom, meme adresse, meme
numero, au caractere pres.

Google compare ces mentions entre elles pour confirmer que l'entreprise existe
vraiment. Si un annuaire dit "suite 201" et un autre "bureau 201", ou si l'un
ecrit "438-372-0102" et l'autre "(438) 372-0102", Google n'est plus certain
qu'il s'agit de la meme entreprise. Il partage alors la confiance entre deux
fiches au lieu d'en renforcer une seule.

C'est ce qui fait le plus de difference, plus que le nombre d'annuaires. Cinq
fiches ecrites a l'identique valent mieux que trente fiches qui se
contredisent.

Le bloc exact a copier-coller est plus bas, section E, sous le titre "Format de
reference a utiliser partout". Garde-le ouvert pendant que tu remplis les
formulaires et copie-colle plutot que de retaper.

Ajouter systematiquement, dans chaque fiche:
- Le site: `https://georgesmatar.ca`
- Le lien de la fiche Google: `https://maps.google.com/?cid=7533992484077488450`
- La categorie: Courtier immobilier / Real Estate Agent
- Les langues: francais, anglais, espagnol, arabe

---

**Etape 1 - Le socle canadien.** Ce sont les huit qui pesent le plus lourd. Si
tu n'en fais que huit, fais celles-la.

- [ ] Google Business Profile (voir section B) - PRIORITE ABSOLUE
- [ ] Apple Maps Connect, `mapsconnect.apple.com` (visible dans Siri et Plans)
- [ ] Bing Places, `bingplaces.com` (alimente aussi Copilot et ChatGPT Search)
- [ ] Facebook, page professionnelle avec adresse et telephone
- [ ] Pages Jaunes, `pagesjaunes.ca` (la plus forte autorite francophone)
- [ ] Yelp.ca (celui de ta liste, il est legitime et bien classe au Canada)
- [x] Foursquare, `foursquare.com` (alimente Uber, Apple, Samsung). Fait le
      2026-10-08: `app.foursquare.com/v/georges-matar-remax-du-cartier/6ac7b5dc2f76fc6486731565`.
      Compte ouvert avec l'adresse remax-quebec.com. La page de la fiche exige
      une connexion: elle n'est pas ajoutee au sameAs du site, Google ne la
      verrait pas.
- [ ] MapQuest, `mapquest.ca`. Verifie le 2026-10-08: pas de formulaire
      gratuit. "Claim it" renvoie vers Yext, un service payant. Trafic tres
      faible au Quebec: a faire en dernier, seulement si c'est gratuit.

**Etape 2 - Annuaires canadiens generiques.** Gratuits, 5 a 10 minutes chacun.
Fais-en 3 ou 4 par semaine, pas tout d'un coup: une salve de vingt inscriptions
en une journee ressemble a du spam.

- [ ] n49.com
- [ ] OurBis.ca (quebecois)
- [ ] Cylex-usa.ca
- [ ] HotFrog.ca
- [ ] Brownbook.net
- [ ] Opendi.ca
- [ ] Infobel.com/fr/canada
- [ ] ProfileCanada.com
- [ ] CanadaOne.com
- [ ] Lacartes.com
- [ ] GoldBook.ca
- [ ] Fyple.ca
- [ ] 2FindLocal.com
- [ ] Websites.ca
- [ ] BBB.org (Better Business Bureau, payant mais forte confiance)

**Etape 3 - Immobilier et Quebec.** C'est ici que se trouvent les vrais leads,
pas seulement du signal SEO. Les gens qui consultent ces sites cherchent deja
un courtier.

- [x] Centris, fiche courtier - FAIT. Trouvee et verifiee le 2026-10-09:
      `www.centris.ca/en/real-estate-broker~georges-matar~re-max-du-cartier-inc.-duvernay/j7941`.
      Le lien vers georgesmatar.ca y est deja, c'etait la seule chose a
      confirmer. Adresse affichee: 2820, boul. Saint-Martin E. #201, Laval QC
      H7E 5A1, ville Laval. Deux numeros, le tien 438-372-0102 et celui de
      l'agence 450-661-6810. Seule reserve, l'adresse se lit #201 et non
      Bureau 201. Ajoutee au sameAs du site le meme jour, commit 26ce52f.
- [ ] RE/MAX Quebec, `remax-quebec.com` - FAIT
- [ ] RE/MAX du Cartier, `remaxducartier.com` - FAIT
- [ ] Trouvetoncourtier.net (celui de ta liste)
- [ ] Reseauagentsimmobilier.com (celui de ta liste)
- [ ] Courtiers.immo
- [ ] Mon-Proprio.ca
- [ ] ImmoAction.ca, repertoire des courtiers
- [ ] Soumissions Quebec, `soumissionsquebec.ca` (service de referencement)
- [ ] MeilleurCourtier.ca (celui de ta liste). Attention: ils n'acceptent que
      les courtiers notes 5 etoiles sur Google. A faire APRES avoir obtenu tes
      premiers avis, sinon la candidature est refusee. Voir section C.
- [ ] Vendre.ca, profil de courtier, `user.vendre.ca/broker-profile`.
      Commence le 2026-10-08. Une fois enregistre, m'envoyer l'adresse
      publique du profil: je l'ajoute a la fiche d'identite du site.

**Etape 4 - Acheteurs etrangers.** Pour les gens qui achetent au Quebec depuis
l'exterieur. Ton avantage a quatre langues joue a plein ici.

- [ ] Point2Homes.com, profil de courtier (portail canadien tres consulte a
      l'international)
- [ ] Properstar.ca, profil de courtier (diffusion vers plus de 60 pays)
- [ ] Realtor.ca (via Centris, verifier que ta fiche courtier est complete)
- [ ] LinkedIn, profil professionnel avec l'adresse du bureau
- [ ] Realestateagents.com (celui de ta liste, surtout americain, valeur
      moyenne pour le Quebec mais gratuit)

---

**Ce qui ne vaut pas l'effort, dans la liste que tu m'as envoyee.** Je les ai
verifies un par un pour ne pas te faire perdre de temps:

| Site | Verdict |
|---|---|
| `am.maptons.com`, `ht.maptons.com` | Sous-domaines Armenie et Haiti d'un agregateur de cartes. Les fiches sont generees automatiquement a partir de donnees copiees, on ne s'y inscrit pas vraiment. Aucun acheteur lavallois n'ira sur la version armenienne. |
| `wheree.com` | Meme principe: agregateur qui aspire les donnees publiques. Ta fiche peut y apparaitre toute seule, mais il n'y a rien a soumettre. |
| `splandidebiz.com` | Annuaire sans trafic ni autorite. Le genre de lien que Google ignore. |
| `magicpin.com` | Plateforme indienne de commerces locaux. Aucune pertinence pour le Quebec. |
| `renogiants.com` | Annuaire d'entrepreneurs en renovation. Mauvaise categorie, tu n'es pas renovateur. |
| `birdeye.com` | C'est un logiciel de gestion d'avis, pas un annuaire. Les pages publiques n'apportent rien sans l'abonnement, qui coute plusieurs centaines de dollars par mois. A considerer seulement quand tu auras 50 avis a gerer. |

---

**Suivi.** Cree un fichier ou un tableau avec: nom de l'annuaire, date
d'inscription, courriel utilise, mot de passe, URL de la fiche publique. Sans
ca, dans six mois tu ne sauras plus ou tu es inscrit ni comment corriger une
coordonnee.

**Envoie-moi ensuite la liste des adresses de tes fiches.** Exemple: une fois
inscrit sur Yelp, ta fiche a une adresse du genre
`https://www.yelp.ca/biz/georges-matar-laval`. Copie-la et envoie-la moi.

Ce que j'en fais: le site contient une fiche d'identite invisible, lue par
Google, qui enumere tous les endroits ou tu es present sur le web. J'y ajoute
chaque adresse que tu m'envoies. Google cesse alors de deviner que ces fiches
parlent de la meme personne, il en a la confirmation directe depuis ton site.
Ca renforce l'ensemble des mentions d'un coup.

**Ordre recommande.** Etape 1 en entier la premiere semaine. Puis 3 ou 4
inscriptions par semaine, en alternant etape 2 et etape 3. L'etape 4 quand les
etapes 1 a 3 sont faites.

---

### 0 bis. 100 liens de plus pour l'autorite (recherche du 2026-10-08)

Cent endroits de plus ou georgesmatar.ca peut etre cite ou lie, aucun deja
dans la section 0. Chaque site a ete ouvert le 2026-10-08 pour verifier qu'il
est actif et qu'il accepte un courtier residentiel du Quebec: 121 candidats
trouves, 21 ecartes (liste en bas).

**Tous ces liens ne pesent pas pareil.**
- **Groupes 1 a 4, medias, experts, journalistes, balados:** ce sont eux qui
  font monter l'autorite. Un texte publie dans un journal local vaut plus que
  vingt annuaires. Il faut un texte a proposer: dis-moi quel media, j'ecris la
  proposition et l'article a partir de tes articles existants.
- **Groupes 5 et 6, communautes et chambres de commerce:** liens locaux, et
  des clients en prime.
- **Groupes 7 a 11, immobilier, avis, profils, annuaires, cartes:** souvent
  sans lien suivi, mais chaque mention identique de ton nom, ton adresse et
  ton telephone renforce la fiche Google.
- **Groupe 12, payant:** de la visibilite et des clients, pas d'autorite.
  Google exige qu'un lien paye porte rel="sponsored", et acheter un lien pour
  le classement va contre ses regles. Paie pour etre vu, jamais pour le lien.

**Deux regles.**
1. Sur chaque fiche, copier exactement le bloc de la section E, tel quel,
   avec le Bureau 201 et Laval comme ville, jamais Duvernay.
2. Aucun site qui preleve une commission de reference: un courtier ne partage
   sa retribution qu'avec un autre titulaire de permis.

#### 1. Medias locaux qui publient des textes d'experts, gratuits

- [ ] **1. Media Laval (MCL)**, `mclmedialaval.com`. Envoyer un texte a
      `redaction@mclmedia.ca`.
- [ ] **2. Laval Weekly**, `lavalweekly.com`. Meme editeur: la version
      anglaise du meme texte, a la meme adresse.
- [ ] **3. Courrier Laval**, `courrierlaval.com/contactez-nous/`. Devenir la
      source locale sur le marche lavallois: `lavalredaction@2m.media`.
- [ ] **4. The Laval News**, `lavalnews.ca/contact-us/`. Chronique ou
      commentaires sur l'immobilier a Laval: `info@newsfirst.ca`.
- [ ] **5. La Revue, Terrebonne et Mascouche**,
      `larevue.qc.ca/contact/collaboration-speciale/`. Collaboration
      speciale: `redaction@medialo.ca`. Terrebonne est ta page de secteur la
      plus vue sur Google.
- [ ] **6. Hebdo Rive Nord, Repentigny**,
      `hebdorivenord.com/contact/collaboration-speciale/`. Meme editeur et
      meme adresse que La Revue.
- [ ] **7. L'Oeil Regional, Beloeil**, `oeilregional.com/nous-joindre/`.
      Chronique: `redaction@oeilregional.com`.

#### 2. Sites et grands medias qui publient des experts

- [ ] **8. REM, Real Estate Magazine**,
      `realestatemagazine.ca/frequestly-asked-questions/`. Texte inedit pour
      courtiers, par exemple la declaration du vendeur au Quebec. Eviter
      "Voices by REM", qui est payant.
- [ ] **9. Moving2Canada**,
      `moving2canada.com/about-us/become-our-partner/share-your-experience/`.
      Resume de 2 phrases sur l'achat au Quebec par un nouvel arrivant; 1 ou 2
      liens dans la bio.
- [ ] **10. New Canadian Media**, `newcanadianmedia.ca/ecrire-pour-ncm/`.
      Chronique pour nouveaux arrivants, par exemple acheter sans historique
      de credit.
- [ ] **11. Canadian Immigrant**, `canadianimmigrant.ca/contact-us`. Une
      "Guest column" sur l'achat au Quebec.
- [ ] **12. Immigrant Quebec, Conseils d'experts et balado "Ca jase"**,
      `immigrantquebec.com/fr/conseils-d-experts/`. Proposer par
      `immigrantquebec.com/fr/contact/`. Partenariats payants possibles:
      demander.
- [ ] **13. Immigrant Quebec, page "Acheter une maison"**,
      `immigrantquebec.com/fr/reussir-votre-installation/logement/acheter-maison-appartement/`.
      La page lie deja des sites commerciaux: y suggerer ton article sur la
      taxe de bienvenue.
- [ ] **14. Condoliaison, magazine du RGCQ**,
      `rgcq.org/decouvrez-le-condoliaison`. Article d'expert sur l'achat ou
      la vente d'un condo: `info@rgcq.org`. Tu es certifie Coproprie-T.
- [ ] **15. Universite McGill, page Housing du personnel**,
      `mcgill.ca/apo/staff-guides/life-quebec/housing`. Proposer ton guide
      anglais d'achat au Quebec au conseiller en relocalisation. Un lien
      universitaire est parmi les plus forts.
- [ ] **16. Montreal Gazette, Op-Ed**,
      `montrealgazette.com/opinion/sending-an-opinion-column-or-letter-to-the-montreal-gazette/`.
      650 a 800 mots inedits, lies a l'actualite, a
      `opinion@montrealgazette.com`. Souvent une mention sans lien, mais une
      autorite enorme.
- [ ] **17. La Presse, Dialogue**, `lapresse.ca/dialogue/`. Texte d'opinion
      lie a l'actualite immobiliere. Adresse d'envoi a confirmer sur la page.

#### 3. Plateformes de sources pour journalistes

Un journaliste pose une question, tu reponds, il te cite avec un lien.
Repondre seulement sur l'immobilier canadien, sinon on se fait exclure.

- [ ] **18. Qwoted**, `app.qwoted.com/users/sign_up`. Gratuit, 2 propositions
      par mois.
- [ ] **19. HARO**, `helpareporter.com`. Gratuit, 3 courriels de demandes par
      jour.
- [ ] **20. Connectively**, `connectively.us`. Filtrer sur l'immobilier, le
      Canada et l'immigration.
- [ ] **21. Featured.com**, `featured.com`. Les reponses retenues sont
      publiees avec ton nom. Gratuit limite.
- [ ] **22. Source of Sources**, `sourceofsources.com`. Gratuit.
- [ ] **23. SourceExpert, de Laval**, `sourceexpert.com`. Francais et
      anglais, credits a quelques sous. Activite en 2026 a confirmer.

#### 4. Balados qui recoivent des invites

- [ ] **24. L'immobilier en mouvement, de l'APCIQ**,
      `apciq.ca/balado-limmobilier-en-mouvement/`. Proposer un sujet, ventes
      sans garantie legale ou successions, par `apciq.ca/nous-joindre/`.
- [ ] **25. REAL TIME, de l'ACI**, `crea.ca/media-hub/real-time-podcast/`.
      Formulaire "Apply now". Il demande si tu es REALTOR, ce qui depend de
      ton adhesion a l'APCIQ.
- [ ] **26. The Canadian Real Estate Investor**, `realist.ca`. Un angle
      quebecois qu'ils couvrent peu: plex, notaire, taxe de bienvenue.
      `tcreipodcast@gmail.com`.
- [ ] **27. Bienvenue au Canada**, `bienvenueaucanada.ca/en/welcome`.
      Episode sur l'achat au Quebec apres l'arrivee:
      `contact@bienvenueaucanada.ca`.
- [ ] **28. More Money Podcast**, `jessicamoorhouse.com/podcast-submissions`.
      Seulement par ce formulaire, pas par courriel.

#### 5. Communautes arabophone, maghrebine et latino

Le terrain ou tu pars avec un avantage, voir `TODO.md`, point 9.

- [ ] **29. Arabz**, `arabz.ca/arabz-for-business/ads/`. Gratuit, categorie
      agent immobilier en arabe, champ site web.
- [ ] **30. Maghrebins du Canada**, `maghrebins.ca/ajouter/`. Gratuit, champ
      site web, categorie immobilier.
- [ ] **31. Hala Canada**, `halacanada.ca/contact`. Article ou entrevue en
      arabe sur l'achat au Quebec.
- [ ] **32. Arab Canada News**, `arabcanadanews.ca`, page de contact.
      Devenir leur commentateur des nouvelles immobilieres:
      `info@arabcanadanews.ca`.
- [ ] **33. Maghreb Canada Express**, `maghreb-canada.ca`. Chronique
      "acheter au Quebec": `info@maghreb-canada.ca`.
- [ ] **34. Atlas.Mtl**, `atlasmedias.com/contactez-nous/`. Article ou
      publicite, par le formulaire.
- [ ] **35. CCICL, Chambre de commerce Canada-Liban**,
      `ccicl.com/devenir-membre/`. 100 $ par an, fiche au repertoire.
- [ ] **36. Montreal Hispano, annuaire**,
      `montrealhispano.com/negocios-directorio/registra-tu-negocio-gratis`.
      Gratuit, fiche en espagnol, categorie "Agentes de Bienes Raices".
- [ ] **37. Latinos Quebec**, `latinosquebec.com/en/registration`. Gratuit,
      categorie "Real estate services".
- [ ] **38. Latinos en Montreal, annuaire**, `latinosenmontreal.ca/directorio/`.
      Bouton "Agregar negocio", categorie "Inmobiliaria".
- [ ] **39. Latinos en Montreal, collaboration**,
      `latinosenmontreal.ca/contacto/`. Guide ou entrevue pour la rubrique
      "Recien llegados".
- [ ] **40. Pulso**, `pulso.ca/impliquez-vous/`. Gratuit, article en espagnol.
- [ ] **41. QUEtAL, chambre de commerce latino-americaine**,
      `quetal.cc/fr/devenir-membre/adhesion/`. 79 $. Pas de repertoire
      public: demander une mention avec lien.

#### 6. Chambres de commerce et reseaux d'affaires

Payants, mais une fiche de membre donne un lien local que Google respecte.
S'ajoutent aux trois chambres de la partie 2. Avant de payer, verifier sur une
fiche existante que le lien vers le site y apparait.

- [ ] **42. CCIRS, Rive-Sud**, `ccirs.qc.ca/devenir-membre/`. 225 $ par an.
      Longueuil, Brossard, Boucherville, Saint-Bruno, Sainte-Julie. Cocher
      "Afficher la page web dans le repertoire".
- [ ] **43. CCEM, Est de Montreal**, `ccemontreal.ca/devenir-membre-de-la-ccem/`.
      Prix sur demande. Saint-Leonard, Riviere-des-Prairies.
- [ ] **44. CCI de Mirabel**, `ccimirabel.com/reseau/devenir-membre/`. 176 $
      plus taxes.
- [ ] **45. CCIVRR, Vallee-du-Richelieu**, `ccivrr.com/etre-membre/devenir-membre/`.
      150 $ plus taxes. Beloeil, Mont-Saint-Hilaire, Chambly.
- [ ] **46. CCMLA, MRC de L'Assomption**, `ccmla.ca/devenir-membre/`. 185 $.
      Repentigny.
- [ ] **47. CCI2M, Deux-Montagnes**,
      `acces.chambrecommerce.com/fr/devenir-membre/adhesion/`. 195 $.
      Saint-Eustache.
- [ ] **48. CCIGR, Grand Roussillon**, `ccigr.ca/devenir-membre-ccigr/`.
      194,75 $. Saint-Constant, Delson, Sainte-Catherine; Candiac et
      La Prairie a confirmer.
- [ ] **49. CCMM, Montreal metropolitain**, `ccmm.ca/fr/devenir-membre/`.
      Prix sur demande.
- [ ] **50. Bizzz.ca**, `bizzz.ca`. Annuaire national des membres des
      chambres: une fiche gratuite de plus des que tu adheres a une chambre
      du reseau.
- [ ] **51. BNI Laval Laurentides Lanaudiere**, `bnilll.com/fr-CA/findachapter`.
      Un seul courtier par chapitre. Y aller en invite d'abord. Apporte
      surtout des references.

#### 7. Proprietaires, copropriete et immobilier

- [ ] **52. CORPIQ, repertoire des partenaires**,
      `corpiq.com/en/partners/become-a-partner`. Prix sur demande, 2 ans
      d'activite exiges. Categorie "Courtier immobilier", public de
      proprietaires de plex.
- [ ] **53. APQ, Bottin**,
      `apq.org/services-apq/rabais-et-economies/visibilite-apq/`. Categorie
      "Courtiers immobiliers".
- [ ] **54. RPHL, bottin des fournisseurs**,
      `rphl.org/services-rphl/rabais-et-economies/bottin-des-fournisseurs/`.
      Meme modele que l'APQ.
- [ ] **55. RGCQ, membre corporatif**, `rgcq.org/devenir-membre-corporatif`.
      650 $ plus taxes. Les syndicats de copropriete y choisissent leurs
      fournisseurs, et Coproprie-T y parle.
- [ ] **56. RankMyAgent**, `rankmyagent.com/register`. Gratuit, avis
      verifies par transaction. La page Laval compte tres peu de courtiers.
      Pas de lien en version gratuite.
- [ ] **57. Nobul**, `nobul.com/agent-profile/`. Plateforme canadienne.
      Frais et presence au Quebec non confirmes: verifier l'absence de
      commission de reference avant de t'inscrire.
- [ ] **58. ActiveRain**, `activerain.com`. Profil et blogue de courtiers,
      base gratuite.
- [ ] **59. BiggerPockets**, `biggerpockets.com`. Profil gratuit, lu par des
      investisseurs canadiens qui cherchent des plex.

#### 8. Avis

- [ ] **60. Trustpilot**, `signup.business.trustpilot.com/create-account`.
      Gratuit. Seulement 54 entreprises dans "Real Estate Agents" au Canada.
- [ ] **61. ThreeBestRated.ca**, `threebestrated.ca/submit-business?reason=new`.
      Gratuit, selection sur les avis. A faire apres les 10 premiers avis
      Google. Lien non suivi, mais la page Laval est consultee.
- [ ] **62. ProvenExpert**, `provenexpert.com/fr-fr/`. Plan gratuit apres
      l'essai.

#### 9. Profils et plateformes

Rapides et gratuits, souvent sans lien suivi, mais ils confirment a Google
qui tu es. Envoie-moi chaque adresse de profil: je l'ajoute a la fiche
d'identite du site (section 0, "Suivi").

- [ ] **63. YouTube**, `youtube.com/create_channel`. Le site dans "A propos"
      et dans chaque description. Tes reels y vont tels quels en Shorts.
- [ ] **64. Pinterest Business**, `pinterest.com/business/create/`.
      Revendiquer georgesmatar.ca, epingler articles et fiches.
- [ ] **65. Medium**, `medium.com`. Republier avec l'outil d'importation, qui
      pointe la version originale vers ton site.
- [ ] **66. Substack**, `substack.com/signup`. Infolettre mensuelle sur le
      marche, avec liens vers les articles.
- [ ] **67. Gravatar**, `gravatar.com`.
- [ ] **68. About.me**, `about.me/signup`.
- [ ] **69. Flipboard**, `flipboard.com/signup`. Un magazine "Immobilier
      Quebec" de tes articles.
- [ ] **70. Quora**, `quora.com`. Repondre aux questions sur l'achat au
      Quebec.
- [ ] **71. Reddit**, `reddit.com/register/`. r/montreal et
      r/PersonalFinanceCanada, en respectant leurs regles contre
      l'autopromotion.
- [ ] **72. Crunchbase, profil de personne**, `crunchbase.com/register`.
- [ ] **73. Bluesky**, `bsky.app`. Ton domaine comme identifiant,
      @georgesmatar.ca: je prepare la verification sur le site.
- [ ] **74. Mastodon**, `joinmastodon.org/servers`. Lien verifie par un
      rel="me" sur le site, que j'ajoute.
- [ ] **75. Issuu**, `issuu.com/signup`. Guides PDF avec l'adresse du site
      en derniere page.
- [ ] **76. Linktree**, `linktr.ee/register`. Lien de bio Instagram, le site
      en premier, puis le lien "source preferee" de la tache 1.
- [ ] **77. Nextdoor**, `nextdoor.com/create-business/`. Page gratuite prevue
      pour les courtiers, en francais au Canada.
- [ ] **78. Alignable**, `alignable.com/biz_users/sign_up`. Plus de 5 000
      membres a Laval.

#### 10. Annuaires gratuits

- [ ] **79. MaCommunaute.ca**, `macommunaute.ca/inscription/`. Lien inclus
      meme au forfait gratuit. Le meilleur de ce groupe.
- [ ] **80. Expat.com**, `expat.com/fr/business/add`. Fiche gratuite, mais le
      lien est reserve au Premium.
- [ ] **81. Le Petit Journal Montreal**, `lepetitjournal.com/ajout-adresse`.
      Le media des Francais a l'etranger.
- [ ] **82. ZipLeaf.ca**, `zipleaf.ca/Add-Your-Business`.
- [ ] **83. MisterWhat**, `ca.misterwhat.com`. Valeur faible.
- [ ] **84. Infoisinfo**, `infoisinfo-ca.com/account/register-business`.
      Valeur faible.

#### 11. Cartes et donnees d'entreprises

Aucun lien, mais ces bases alimentent les GPS, les voitures et d'autres
annuaires.

- [ ] **85. OpenStreetMap**, `openstreetmap.org/user/new`.
- [ ] **86. Waze**, `waze.com/editor`.
- [ ] **87. TomTom MapShare**, `tomtom.com/mapshare/tools/`.
- [ ] **88. Dun & Bradstreet, numero D-U-N-S**, `dnb.com/en-ca/smb/duns.html`.
      Gratuit.
- [ ] **89. Data Axle, Local Listings**, `local-listings.data-axle.com/search`.
      Gratuit; adresse canadienne a confirmer.

#### 12. Payant: visibilite et clients, pas autorite

Le lien d'un contenu commandite porte presque toujours rel="sponsored" et
n'aide pas le classement. Demander l'attribut avant de payer.

- [ ] **90. Le Courrier du Sud, Longueuil**, `lecourrierdusud.ca/nous-joindre/`.
      Contenu partenaire.
- [ ] **91. Le Reflet, Candiac et La Prairie**, `lereflet.qc.ca/nous-joindre/`.
- [ ] **92. La Releve, Boucherville et Sainte-Julie**,
      `lareleve.qc.ca/nous-joindre/`.
- [ ] **93. Le Journal de Chambly**, `journaldechambly.com/nous-joindre/`.
      Publireportage.
- [ ] **94. Les Versants, Saint-Bruno**, `versants.com/nous-joindre/`.
      Publireportage, dans la ville ou le site ressort deja sur "vente de
      succession".
- [ ] **95. Nord Info, Blainville, Sainte-Therese, Boisbriand, Rosemere**,
      `nordinfo.com/nous-joindre`. Les communiques sont gratuits:
      `infojournaux@groupejcl.com`.
- [ ] **96. Journal Metro, Saint-Leonard et RDP**,
      `journalmetro.com/annoncez-avec-nous/`.
- [ ] **97. Festival libanais de Laval**, `festivallibanais.org/commandite`.
      Demander un lien texte: la page actuelle des commanditaires est une
      image.
- [ ] **98. Festival du Monde Arabe de Montreal**, `festivalarabe.com`.
- [ ] **99. Festival LatinArte**, `latinarte.ca/contactez-nous/`. La page
      partenaires affiche les logos avec liens.
- [ ] **100. Soccer Laval**, `soccer-laval.qc.ca/commanditaires-et-partenaires/`.
      Les logos des partenaires renvoient vers leurs sites.

**Ecartes apres verification, pour ne pas les reverifier.** Agent Pronto
(commission de reference sur la vente). LuxuryEstate, JamesEdition, CLHMS et
FIABCI (luxe ou international, passent par l'agence). Expatica (299 euros par
an), RealSatisfied et Testimonial Tree (payants, peu utiles au Quebec).
ProfNet (tarif d'agence). Zhaboom (Toronto). ChamberofCommerce.com (prive,
pousse des forfaits). iGlobal (vend du "backlinking"). Journal Le Nord et
L'Eveil (payants, villes peu vues). Montreal Hispano, blogue (payant;
l'annuaire gratuit est garde). PodcastGuests (profil payant). Snapchat,
Tupalo, Cybo, iBegin, Nexdu et HERE (valeur faible ou non verifiable). Morts
ou hors sujet: Media Spot Me, Laval Families Magazine, Help a B2B Writer,
SourceBottle. Muck Rack (journalistes seulement). Wikidata: pas avant d'avoir
ete cite par des medias independants, sinon la fiche est supprimee.

---

### A. Google Search Console - FAIT

1. Propriete `georgesmatar.ca` ajoutee en "Prefixe d'URL"
2. Validee par fichier HTML (`/google279547fdbb37f62a.html`, ne pas supprimer)
3. Les 5 sitemaps sont soumis et acceptes:
   `sitemap.xml`, `fr/sitemap.xml`, `en/sitemap.xml`, `es/sitemap.xml`,
   `ar/sitemap.xml`
   URLs declarees: 102 en FR, 102 en EN, 102 en AR, 53 en ES

---

### A-bis. Demandes d'indexation, jour par jour

Google explore tout seul, mais lentement. L'outil "Inspection de l'URL"
permet de passer devant la file. La limite pratique est d'environ 10 a 12
demandes par jour et par propriete.

**Comment faire, pour chaque URL:**
1. Colle l'URL dans la barre de recherche tout en haut de Search Console
2. Attends l'analyse (10 a 30 secondes)
3. Clique sur "Demander une indexation"
4. Attends la confirmation, puis passe a la suivante

Un message du type "URL disponible pour Google" ou "Detectee, actuellement
non indexee" est normal a ce stade. La demande est prise en compte quand
meme.

Toutes les URLs commencent par `https://georgesmatar.ca`.

---

#### JOUR 1 - FAIT

```
/
/courtier-immobilier/
/courtier-immobilier/laval/
/courtier-immobilier/montreal/
/courtier-immobilier/longueuil/
/courtier-immobilier/brossard/
/courtier-immobilier/terrebonne/
/courtier-immobilier/repentigny/
/courtier-immobilier/blainville/
/courtier-immobilier/boucherville/
/courtier-immobilier/saint-bruno-de-montarville/
```

#### JOUR 2 - Les 10 villes suivantes

```
https://georgesmatar.ca/courtier-immobilier/saint-jerome/
https://georgesmatar.ca/courtier-immobilier/mascouche/
https://georgesmatar.ca/courtier-immobilier/saint-eustache/
https://georgesmatar.ca/courtier-immobilier/chateauguay/
https://georgesmatar.ca/courtier-immobilier/sainte-therese/
https://georgesmatar.ca/courtier-immobilier/boisbriand/
https://georgesmatar.ca/courtier-immobilier/mirabel/
https://georgesmatar.ca/courtier-immobilier/sainte-julie/
https://georgesmatar.ca/courtier-immobilier/la-prairie/
https://georgesmatar.ca/courtier-immobilier/chambly/
```

#### JOUR 3 - Les 5 dernieres villes + les pages de service

```
https://georgesmatar.ca/courtier-immobilier/rosemere/
https://georgesmatar.ca/courtier-immobilier/varennes/
https://georgesmatar.ca/courtier-immobilier/candiac/
https://georgesmatar.ca/courtier-immobilier/saint-constant/
https://georgesmatar.ca/courtier-immobilier/delson/
https://georgesmatar.ca/buyer/
https://georgesmatar.ca/seller/
https://georgesmatar.ca/about/
https://georgesmatar.ca/tools/
https://georgesmatar.ca/advantages/
```

A la fin du jour 3, les 24 villes sont soumises.

#### JOUR 4 - Outils et avantages (pages a forte intention commerciale)

```
https://georgesmatar.ca/tools/home-estimate/
https://georgesmatar.ca/tools/mortgage/
https://georgesmatar.ca/tools/affordability/
https://georgesmatar.ca/tools/closing-costs/
https://georgesmatar.ca/tools/welcome-tax/
https://georgesmatar.ca/tools/rent-vs-buy/
https://georgesmatar.ca/advantages/integri-t/
https://georgesmatar.ca/advantages/tranquilli-t/
https://georgesmatar.ca/advantages/coproprie-t/
https://georgesmatar.ca/advantages/mes-rabais-remax/
```

#### JOUR 5 - Les 10 articles les plus commerciaux

Ce sont ceux qui repondent a une question que les gens tapent avant de
contacter un courtier.

```
https://georgesmatar.ca/articles/commission-explained-quebec/
https://georgesmatar.ca/articles/guide-hypotheque-premier-acheteur/
https://georgesmatar.ca/articles/vrai-cout-achat-premiere-maison/
https://georgesmatar.ca/articles/guide-nouveaux-arrivants-quebec/
https://georgesmatar.ca/articles/down-payment-myth-debunked/
https://georgesmatar.ca/articles/property-tax-explained/
https://georgesmatar.ca/articles/credit-score-home-buying-quebec/
https://georgesmatar.ca/articles/questions-hire-broker/
https://georgesmatar.ca/articles/broker-agent-difference-quebec/
https://georgesmatar.ca/articles/preparer-maison-vente/
```

#### JOUR 6 - Suite des articles FR + l'index du blogue

```
https://georgesmatar.ca/articles/
https://georgesmatar.ca/articles/marche-immobilier-montreal/
https://georgesmatar.ca/articles/best-time-sell-home-montreal/
https://georgesmatar.ca/articles/condo-vs-house-montreal/
https://georgesmatar.ca/articles/acheter-laval-2025/
https://georgesmatar.ca/articles/renovations-dont-add-value/
https://georgesmatar.ca/articles/home-inspection-checklist-montreal/
https://georgesmatar.ca/articles/red-flags-walk-away-property/
https://georgesmatar.ca/articles/investir-triplex-laval/
https://georgesmatar.ca/articles/rive-nord-guide-laval/
```

#### JOUR 9 - Les 6 nouvelles villes (ajoutees le 2026-09-19)

```
https://georgesmatar.ca/courtier-immobilier/beloeil/
https://georgesmatar.ca/courtier-immobilier/sainte-catherine/
https://georgesmatar.ca/courtier-immobilier/mont-saint-hilaire/
https://georgesmatar.ca/courtier-immobilier/saint-basile-le-grand/
https://georgesmatar.ca/courtier-immobilier/carignan/
https://georgesmatar.ca/courtier-immobilier/lorraine/
```

Ce jour peut passer avant les jours 7 et 8: ce sont des pages neuves que
Google n a jamais vues, alors que les versions anglaises et arabes des autres
villes sont deja dans les sitemaps depuis aout.

#### JOUR 7 - Anglais: accueil, hub et villes principales

```
https://georgesmatar.ca/en/
https://georgesmatar.ca/en/real-estate-broker/
https://georgesmatar.ca/en/real-estate-broker/laval/
https://georgesmatar.ca/en/real-estate-broker/montreal/
https://georgesmatar.ca/en/real-estate-broker/longueuil/
https://georgesmatar.ca/en/real-estate-broker/brossard/
https://georgesmatar.ca/en/real-estate-broker/terrebonne/
https://georgesmatar.ca/en/real-estate-broker/boucherville/
https://georgesmatar.ca/en/buyer/
https://georgesmatar.ca/en/seller/
```

#### JOUR 8 - Arabe et espagnol: accueil, hub et villes principales

Ce sont tes deux avantages concurrentiels les plus rares. Presque aucun
courtier de la region ne se positionne sur ces requetes.

```
https://georgesmatar.ca/ar/
https://georgesmatar.ca/ar/wasit-aqari/
https://georgesmatar.ca/ar/wasit-aqari/laval/
https://georgesmatar.ca/ar/wasit-aqari/montreal/
https://georgesmatar.ca/ar/wasit-aqari/brossard/
https://georgesmatar.ca/es/
https://georgesmatar.ca/es/corredor-inmobiliario/
https://georgesmatar.ca/es/corredor-inmobiliario/laval/
https://georgesmatar.ca/es/corredor-inmobiliario/montreal/
https://georgesmatar.ca/es/corredor-inmobiliario/brossard/
```

---

**Apres le jour 8, arrete.** Le rendement des demandes manuelles chute
fortement une fois que les pages principales sont indexees. Google suivra
les liens internes depuis ces pages pour trouver le reste, et les sitemaps
couvrent l'ensemble. Continuer a soumettre manuellement n'accelere plus rien.

**Ce qu'il faut surveiller a la place**, une fois par semaine:
- `Indexation > Pages`: le nombre de pages indexees doit monter
- `Performances`: les premieres impressions apparaissent generalement
  entre la 3e et la 5e semaine
- Toute erreur signalee dans `Indexation > Pages > Pourquoi des pages ne
  sont pas indexees`: envoie-moi une capture, je corrige

#### VAGUE DU 2026-10-07 - Pages modifiees ce jour et pages en attente

Deux sources: les pages changees le 2026-10-07 (nouvelle page La Plaine, chiffres
Centris sur 4 villes, titre de l'article commission, dans les 4 langues), et
les 30 adresses que Search Console montrait en "Detectee, actuellement non
indexee". Toutes verifiees en ligne le 2026-10-07: elles repondent.

#### Vague 2026-10-07, jour 1 - Francais: La Plaine, les 4 villes avec chiffres, la commission, et les pages en attente les plus utiles

```
https://georgesmatar.ca/courtier-immobilier/la-plaine-terrebonne/
https://georgesmatar.ca/courtier-immobilier/terrebonne/
https://georgesmatar.ca/courtier-immobilier/blainville/
https://georgesmatar.ca/courtier-immobilier/saint-bruno-de-montarville/
https://georgesmatar.ca/courtier-immobilier/rosemere/
https://georgesmatar.ca/articles/commission-explained-quebec/
https://georgesmatar.ca/listings/
https://georgesmatar.ca/courtier-immobilier/sainte-therese/
https://georgesmatar.ca/articles/banlieue-ou-ville-cout-reel-montreal/
https://georgesmatar.ca/articles/vendre-avant-acheter-clauses-quebec/
```

#### Vague 2026-10-07, jour 2 - Francais, suite, puis anglais: pages modifiees

```
https://georgesmatar.ca/articles/vendre-automne-hiver-presentation-quebec/
https://georgesmatar.ca/articles/toit-vert-toit-reflechissant-montreal-reglement/
https://georgesmatar.ca/articles/home-inspection-checklist-montreal/
https://georgesmatar.ca/en/real-estate-broker/la-plaine-terrebonne/
https://georgesmatar.ca/en/real-estate-broker/terrebonne/
https://georgesmatar.ca/en/real-estate-broker/blainville/
https://georgesmatar.ca/en/real-estate-broker/saint-bruno-de-montarville/
https://georgesmatar.ca/en/real-estate-broker/rosemere/
https://georgesmatar.ca/en/articles/commission-explained-quebec/
https://georgesmatar.ca/en/listings/
```

#### Vague 2026-10-07, jour 3 - Anglais, articles en attente, puis espagnol: pages modifiees

```
https://georgesmatar.ca/en/articles/breaking-mortgage-penalty-quebec/
https://georgesmatar.ca/en/articles/buying-in-flood-zone-quebec/
https://georgesmatar.ca/en/articles/down-payment-myth-debunked/
https://georgesmatar.ca/es/corredor-inmobiliario/la-plaine-terrebonne/
https://georgesmatar.ca/es/corredor-inmobiliario/terrebonne/
https://georgesmatar.ca/es/corredor-inmobiliario/blainville/
https://georgesmatar.ca/es/corredor-inmobiliario/saint-bruno-de-montarville/
https://georgesmatar.ca/es/corredor-inmobiliario/rosemere/
https://georgesmatar.ca/es/articles/commission-explained-quebec/
https://georgesmatar.ca/es/listings/
```

#### Vague 2026-10-07, jour 4 - Espagnol: articles en attente

```
https://georgesmatar.ca/es/articles/arboles-propiedad-reglamentos-quebec/
https://georgesmatar.ca/es/articles/best-time-sell-home-montreal/
https://georgesmatar.ca/es/articles/home-staging-client-story/
https://georgesmatar.ca/es/articles/jornada-puertas-abiertas-vendedor-quebec/
https://georgesmatar.ca/es/articles/radon-vivienda-quebec/
https://georgesmatar.ca/es/articles/suburbio-o-ciudad-costo-real-montreal/
https://georgesmatar.ca/es/articles/when-not-to-buy-real-estate/
https://georgesmatar.ca/es/articles/worst-real-estate-deal-lessons/
```

#### Vague 2026-10-07, jour 5 - Arabe: pages modifiees et pages en attente

```
https://georgesmatar.ca/ar/wasit-aqari/la-plaine-terrebonne/
https://georgesmatar.ca/ar/wasit-aqari/terrebonne/
https://georgesmatar.ca/ar/wasit-aqari/blainville/
https://georgesmatar.ca/ar/wasit-aqari/saint-bruno-de-montarville/
https://georgesmatar.ca/ar/wasit-aqari/rosemere/
https://georgesmatar.ca/ar/articles/commission-explained-quebec/
https://georgesmatar.ca/ar/listings/
https://georgesmatar.ca/ar/listings/4071-rang-saint-hyacinthe-mirabel/
https://georgesmatar.ca/ar/wasit-aqari/chomedey-laval/
```

#### Vague 2026-10-07, jour 6 - Arabe: articles en attente

```
https://georgesmatar.ca/ar/articles/buying-century-old-home-quebec/
https://georgesmatar.ca/ar/articles/documents-before-meeting-broker-quebec/
https://georgesmatar.ca/ar/articles/hard-to-insure-home-quebec/
https://georgesmatar.ca/ar/articles/house-flipping-montreal/
https://georgesmatar.ca/ar/articles/increasing-plex-value-montreal/
https://georgesmatar.ca/ar/articles/neighbour-disputes-quebec/
https://georgesmatar.ca/ar/articles/spring-melt-water-infiltration-montreal/
```

Quand les 6 jours sont faits, retourne sur la ligne "Detectee, actuellement
non indexee" et clique "Valider la correction".

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
- Courtier immobilier residentiel
- Conseiller immobilier
- Copropriete

Corrige le 2026-10-09. L'ancienne liste proposait trois categories a retirer:

- **Immobilier commercial.** Hors permis. Le permis J7941 est un permis de
  courtier immobilier **residentiel**, limite aux immeubles principalement
  residentiels de moins de 5 logements, aux terrains vacants a usage
  residentiel et aux fractions de copropriete. L'immeuble commercial en est
  explicitement exclu. Annoncer cette categorie, c'est offrir un service que
  le permis ne couvre pas. Meme regle pour le contenu du site: duplex,
  triplex et quadruplex sont dans le permis, un 5-plex ne l'est pas.
- **Service d'evaluation immobiliere.** Seul un evaluateur agree de l'OEAQ
  produit une evaluation reconnue. Un courtier produit une valeur marchande
  estimee, une ACM, sans valeur legale. L'offre d'estimation gratuite reste
  dans la description, ou elle est formulee correctement.
- **Agent immobilier.** Le titre d'agent immobilier est aboli au Quebec
  depuis 2010. Prendre "Courtier immobilier" partout ou il est offert.

**2. Nom de l'etablissement**
`Georges Matar - RE/MAX Du Cartier`

Ne mets pas de mots-cles supplementaires (Google peut suspendre la fiche).

Corrige le 2026-10-09. L'ancienne version, `Georges Matar - Courtier
immobilier | RE/MAX Du Cartier`, contredisait la phrase ci-dessus et
tronquait le titre du permis, qui est residentiel. Le titre n'a pas besoin
d'etre dans le champ Nom: l'article 114 exige que **la publicite**, prise
dans son ensemble, indique le nom du courtier, le permis qu'il detient et le
nom de l'agence, pas qu'ils tiennent tous dans une seule case. Le titre vit
donc dans la categorie et dans la description, et le champ Nom reste la
chaine courte et identique que Google compare d'un annuaire a l'autre.

**Condition:** remplir la description sur chaque fiche. Une fiche qui ne
porterait que le nom, l'adresse et le telephone, sans le titre de courtier
immobilier residentiel, ne respecterait pas l'article 114. Si un annuaire
n'offre aucun champ de description, et seulement dans ce cas, utiliser le nom
long: `Georges Matar, courtier immobilier residentiel - RE/MAX Du Cartier`.

**3. Adresse et zone de service**
- Adresse: celle du bloc de la section E. Dans la fiche: ligne 1
  `2820, boul. St-Martin Est`, ligne 2 `Bureau 201`, ville `Laval`, code
  postal `H7E 5A1`. Corrige le 2026-10-08: la fiche n'avait pas le bureau
  201. Une seule ecriture partout, sinon Google divise sa confiance entre
  deux adresses.
- Active "Je sers aussi mes clients en dehors de cette adresse"
- Zones de service: Google en accepte 20 au maximum. Le site couvre 30
  villes, il faut donc choisir. Proposition, les plus grands marches autour
  du bureau et les deux villes ou tu as deja vendu (Longueuil, Mirabel):
  Laval, Montreal, Longueuil, Brossard, Terrebonne, Boucherville, Blainville,
  Repentigny, Saint-Bruno-de-Montarville, Mascouche, Sainte-Therese,
  Boisbriand, Rosemere, Saint-Eustache, Mirabel, Saint-Jerome, Sainte-Julie,
  Chambly, Chateauguay, La Prairie
  Les zones de service ne font pas monter la fiche dans le pack local, c est
  surtout l adresse du bureau qui compte. Les 10 autres villes restent
  couvertes par leurs pages sur le site.

**4. Horaires**
Mets des horaires reels et larges (ex. lundi-dimanche 8h-20h). Une fiche sans
horaires perd des positions.

**5. Description (750 caracteres max)**
Copie-colle ceci:

> Georges Matar, courtier immobilier résidentiel chez RE/MAX Du Cartier. Je
> dessers Laval, Montréal, Longueuil, Brossard, Terrebonne, Boucherville,
> Repentigny, ainsi que la Rive-Nord, la Rive-Sud, les Laurentides, Lanaudière
> et la Montérégie. Achat, vente et investissement: analyse comparative de
> marché, stratégie de prix basée sur les données réelles du secteur,
> négociation et accompagnement jusqu'à la signature chez le notaire. Services
> en français, anglais, espagnol et arabe. Inclus sans frais: Tranquilli-T,
> l'assistance juridique exclusive de RE/MAX Québec. En option, payante: la
> garantie Intégri-T, jusqu'à 50 000 $ contre les vices cachés pendant 3 ans.
> Certifié Coproprié-T (copropriété). Contactez-moi pour une consultation
> gratuite.

(746 caractères, la limite de Google est 750. Colle le texte d'un seul bloc,
sans les chevrons.)

Corrige le 2026-10-07: l'ancienne version disait Intégri-T "inclus sans
frais". C'est faux: la garantie coute a partir de 975 $ plus taxes payee par le
vendeur, 675 $ plus taxes payee par l'acheteur (page Intégri-T du site). Seul
Tranquilli-T est gratuit. Coproprié-T est une formation du courtier, pas une
protection du client.

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

Format de reference a utiliser partout (mis a jour le 2026-10-08: adresse
confirmee par Georges, avec le bureau 201 et Laval comme ville, jamais
Duvernay. Voir TODO-GOOGLE-BUSINESS.md, etape 16. Mis a jour le 2026-10-09:
le nom prend un tiret, plus une virgule. Les fiches Google et Yelp affichent
deja `Georges Matar - RE/MAX Du Cartier`, donc le tiret ne demande aucune
correction, alors que la virgule aurait oblige a modifier les deux):
```
Georges Matar - RE/MAX Du Cartier
2820, boul. St-Martin Est, Bureau 201
Laval, QC H7E 5A1
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
3. **Ajouter les dernieres villes manquantes** - FAIT le 2026-09-19:
   Sainte-Catherine, Lorraine, Carignan, Saint-Basile-le-Grand, Beloeil,
   Mont-Saint-Hilaire, dans les 4 langues.
4. **Ajouter des inscriptions reelles** dans `/listings/`. Une page par
   propriete avec le schema `RealEstateListing` genere des leads directs.
5. **Optimiser la vitesse.** Les polices Google Fonts sont chargees depuis un
   domaine externe, ce qui coute environ 300 ms. Les heberger localement
   ameliore le Core Web Vital LCP.

---

## PARTIE 5 - Audit marketing recu le 2026-09-20

Points souleves par un audit externe, tries et verifies dans le depot. Trois
corrections a l audit avant de commencer: le site a QUATRE langues, pas deux,
l espagnol existe aussi; il n est pas sur WordPress ni sur un gabarit RE/MAX,
c est un site Hugo sur mesure; et il n a pas de pages de quartier, il a 30
pages de ville, ce qui n est pas la meme chose.

### 5.1 - Mesure: rien n est mesure aujourd hui - PRIORITE 1

Verifie le 2026-09-20: aucun outil de mesure n est installe, ni Google
Analytics, ni Tag Manager, ni aucun autre. On ne sait donc pas combien de
visiteurs arrivent, d ou ils viennent, quelles pages ils lisent, ni a quel
endroit ils abandonnent le formulaire. Toute discussion sur "ameliorer la
conversion" est aveugle tant que ca n est pas regle.

- [ ] DECISION: installer Google Analytics 4, ou une solution respectueuse de
      la vie privee (Plausible, Umami) qui evite la banniere de consentement.
      A trancher avant l installation.
- [ ] Marquer les conversions: envoi du formulaire, clic sur le telephone,
      reservation d un rendez-vous, telechargement d un outil.
- [ ] Relier Search Console a l outil choisi.

### 5.2 - Conversion mobile - PRIORITE 1

Verifie: il n y a aucune barre d action collante en bas d ecran sur mobile.
Un visiteur qui lit un article doit remonter jusqu au menu pour te joindre.

- [ ] Barre collante mobile avec deux actions: appeler, et reserver. Elle doit
      respecter la charte (voir `CHARTE-COULEURS.md`) et ne pas masquer le
      contenu.
- [ ] Mesurer avec PageSpeed Insights avant et apres, sur mobile, pour trois
      types de pages: accueil, page de ville, article.

### 5.3 - Page de contact et fiche Google

- [ ] Aucune carte Google n est integree a la page de contact. En ajouter une,
      avec l adresse exacte du bureau, la meme que celle de la fiche Google
      Business, au caractere pres.
- [ ] Verifier que l adresse du site, de la fiche Google et des annuaires est
      identique partout (voir PARTIE 2, section E, coherence NAP).

### 5.4 - Titre de l accueil - DECISION EN ATTENTE

Le H1 de l accueil est "Georges Matar", suivi de "Courtier Immobilier
Residentiel" dans un paragraphe. Le titre le plus important du site ne
contient donc ni ville, ni proposition de valeur. L audit propose d y mettre
l avantage analytique et les protections.

Cette page ne se touche pas sans ton accord (regle du projet). Deux options a
trancher:
- garder le nom en H1, et ajouter les villes et l avantage dans le
  sous-titre, qui est deja un paragraphe;
- passer a un H1 qui porte le positionnement, avec le nom juste au-dessus.

- [ ] DECISION a prendre avant toute modification de l accueil.
- [ ] Mettre en avant les protections (Tranquilli-T, Integri-T, Coproprie-T)
      des l accueil. Elles existent en pages dediees mais ne sont pas un
      argument visible en haut de l accueil.

### 5.5 - Pages de quartier, apres les pages de ville

Les 30 pages de ville couvrent la geographie large. L etage en dessous n est
pas couvert: les quartiers de Laval (Chomedey, Duvernay, Sainte-Dorothee,
Vimont, Fabreville, Sainte-Rose, Laval-des-Rapides, Pont-Viau, Auteuil,
Saint-Francois, Saint-Vincent-de-Paul, Laval-Ouest) et les arrondissements de
Montreal (Ahuntsic-Cartierville, Villeray, Rosemont, Saint-Leonard, Riviere
des Prairies et d autres).

- [x] FAIT le 2026-09-23, commits 95e855d et 688358c. Huit quartiers dans les
      4 langues, 32 fichiers, environ 1 000 mots en fr, en et es et 800 en ar:
      Chomedey, Duvernay et Sainte-Dorothee a Laval, Riviere-des-Prairies et
      Saint-Leonard a Montreal, Vieux-Longueuil et Saint-Hubert, et
      Vieux-Terrebonne.
      Modele retenu, a reprendre pour les prochains: meme section `secteurs`
      et meme gabarit que les pages de ville, `weight` a partir de 101 pour
      qu ils se classent apres les villes, `translationKey: quartier-<nom>`,
      et une URL par langue, `/courtier-immobilier/<slug>/`,
      `/en/real-estate-broker/`, `/es/corredor-inmobiliario/`,
      `/ar/wasit-aqari/`. Le slug porte la ville quand le nom seul est
      ambigu: `chomedey-laval`, mais `vieux-longueuil`.
      Regle non negociable verifiee par script sur les 32 fichiers: jamais
      decrire un secteur par l origine, la religion, la langue ou la classe
      sociale de ses residents. Seulement le bati, le transport, les ecoles,
      les services et les prix avec leur source.
      Prochains candidats si tu veux continuer: Vimont, Sainte-Rose,
      Laval-des-Rapides et Pont-Viau a Laval, Anjou et Montreal-Nord a
      Montreal, Greenfield Park a Longueuil, Lachenaie a Terrebonne. A ne
      faire que la ou tu transiges vraiment.

### 5.6 - Contenu arabe et espagnol propre a la communaute

L audit a raison sur un point: la concurrence est plus faible en arabe et en
espagnol. Mais les articles y sont aujourd hui des traductions des sujets
francais, pas des sujets propres a ces publics.

- [ ] Ecrire en arabe et en espagnol des sujets que personne ne traite:
      l achat par un non resident et l impot supplementaire applicable,
      l historique de credit quand on vient d arriver au pays, le financement
      sans historique canadien, les vices caches expliques a quelqu un qui
      vient d un autre systeme juridique, le role du notaire au Quebec compare
      a celui d un avocat ailleurs.

### 5.7 - Aimants a prospects

Le site a deja 6 outils de calcul, ce qui est mieux qu un simple formulaire.
Ce qui manque, c est la capture: les outils donnent un resultat sans jamais
demander de courriel.

- [ ] DECISION: ajouter une etape facultative "recevoir ce calcul par
      courriel" a la fin des calculateurs, sans bloquer le resultat. Bloquer
      le resultat ferait fuir plus de monde que ca n en capturerait.
- [ ] Guide telechargeable pour les investisseurs, en PDF, avec les vraies
      regles de financement d un immeuble a revenus. A ne faire qu apres les
      articles, parce que le contenu sera le meme.

### 5.8 - Autorite du domaine et liens entrants

C est la vraie faiblesse, et l audit a raison. Le site est jeune et se bat
contre Centris et REMAX Quebec. Rien ne se regle ici en une semaine.

- [ ] Executer la PARTIE 2, section 0: les annuaires et citations. C est
      deja planifie, ce n est pas fait.
- [ ] Demander a ton bureau RE/MAX Du Cartier un lien vers ton site depuis la
      page de l equipe.
- [ ] Les avis Google, avec des mots precis (ville, type de transaction). Voir
      PARTIE 2, section C. C est le levier le plus fort et il ne depend que de
      toi.

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
