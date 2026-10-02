# Audit des 33 points de confiance Google

Date: 2026-10-02
Portee: georgesmatar.ca dans les 4 langues (934 pages construites, 220 URL par
langue) et la fiche Google Business.
Methode: analyse du site construit page par page (titres, descriptions,
canoniques, balisage, nombre de mots, liens internes et externes), requetes
HTTP reelles sur le site en ligne, lecture des gabarits et de hugo.toml.

**Resultat: 18 points conformes, 9 partiels, 4 absents, 2 sans objet.**
Un defaut a ete corrige pendant l audit, il est deja en ligne.

---

## Tableau de bord

| # | Point | Etat |
|---|-------|------|
| 1 | Page "a propos" unique | Partiel |
| 2 | Bing Webmaster Tools | A verifier, probablement absent |
| 3 | Google Search Console | Conforme |
| 4 | Aucune erreur 404 | Corrige aujourd hui |
| 5 | Sitemap XML | Conforme |
| 6 | Sitemap des images | **Absent** |
| 7 | Favicon | Partiel |
| 8 | Aucune erreur 5xx | Conforme |
| 9 | Liens brises repares | Conforme apres correction |
| 10 | Aucune page orpheline | Conforme |
| 11 | Pages choisies en noindex | Conforme |
| 12 | Fil d Ariane | Partiel |
| 13 | Balises canoniques | Conforme |
| 14 | Avis sur les temoins | Conforme |
| 15 | Section auteur sur les articles | Conforme |
| 16 | Page contact | Conforme, mais mince |
| 17 | Politique de confidentialite | Conforme |
| 18 | Liens externes sur la page "a propos" | **Absent** |
| 19 | Fiche Google Business | Partiel |
| 20 | Reseaux sociaux au pied de page | Partiel |
| 21 | Toutes les pages au-dessus de 200 mots | Partiel, 22 pages en dessous |
| 22 | Page "nos services" | **Absent** |
| 23 | Mention de droit d auteur | Conforme |
| 24 | Coordonnees au pied de page | Partiel, adresse manquante |
| 25 | Certificat SSL | Conforme |
| 26 | Compte LinkedIn | **Absent** |
| 27 | Compte Facebook professionnel | A verifier |
| 28 | Conditions d utilisation au pied de page | **Absent** |
| 29 | Politique de retour | Sans objet |
| 30 | Politique de garantie | Sans objet au sens strict |
| 31 | Date de publication sur les articles | Conforme |
| 32 | Controle de lisibilite | Partiel |
| 33 | Contenu duplique retire | Conforme a une exception pres |

---

## Ce qui est deja solide

Le site est nettement au-dessus de la moyenne du metier sur la partie
technique. Ces points n ont rien a corriger.

**3. Google Search Console.** Le fichier de validation
`static/google279547fdbb37f62a.html` est en place et repond en ligne.

**5. Sitemap XML.** Un index de sitemaps a la racine, puis un sitemap par
langue, 220 URL chacun, avec les liens `xhtml:link` entre les 4 versions de
chaque page. Les 5 sitemaps sont declares dans `robots.txt`. C est la bonne
structure pour un site multilingue, bien au-dela du minimum.

**8 et 25. Erreurs serveur et SSL.** Site statique sur GitHub Pages: pas de
serveur applicatif, donc pas de 5xx possible. HTTPS valide, `http://` redirige
en 301 vers `https://`, `www.` redirige en 301 vers le domaine nu. Reponse de
la page d accueil en 0,14 seconde.

**10. Pages orphelines.** Aucune. Les 934 pages construites sont toutes
atteignables par un lien interne. Les seules adresses sans lien entrant sont
les redirections techniques (`/fr/`, `/categories/`, `/tags/`), ce qui est
normal.

**11. Noindex.** Les 4 pages de remerciement (`/merci/`, `/en/thank-you/`,
`/es/gracias/`, `/ar/shukran/`) sont en `noindex, follow`. C est exactement le
bon choix: ces pages n ont aucune valeur de recherche et polluent les
statistiques si elles sont indexees.

**13. Canoniques.** Chaque page en porte une. Le cas difficile est traite: les
pages de pagination `/articles/page/2/` et suivantes se declarent canoniques
vers elles-memes et non vers la page 1.

**14. Avis sur les temoins.** Banniere conforme a la Loi 25: rien n est charge
avant le choix, refuser est aussi simple qu accepter, le detail par categorie
est consultable, et le pied de page permet de revenir sur son consentement.
Beaucoup de sites d agences echouent precisement la.

**15 et 31. Auteur et date sur les articles.** Signature, date affichee dans
une balise `<time>`, temps de lecture en haut; carte auteur avec photo, titre
professionnel et bouton de contact en bas. Cote balisage: `article:published_time`,
`datePublished`, `dateModified`, et un auteur `Person` relie par identifiant au
`RealEstateAgent`. C est ce que Google attend pour l E-E-A-T.

**17. Confidentialite.** Presente dans les 4 langues, liee au pied de page
partout.

**23. Droit d auteur.** `© 2026 Georges Matar · RE/MAX DU CARTIER INC.` dans
le bas du pied de page, sur toutes les pages.

**33. Contenu duplique.** Zero description meta dupliquee sur 934 pages, ce
qui est rare a cette echelle. Une seule paire de titres identiques, voir plus
bas. Les 38 pages de secteur se ressemblent a 33 % en moyenne, ce qui reste
sous le seuil ou Google parle de pages satellites, mais deux paires montent a
50-60 % et meritent une relecture (voir plus bas).

---

## 4 et 9. Erreurs 404 et liens brises: corrige aujourd hui

**Ce qui n allait pas.** La page 404 proposait cinq boutons de reprise par
langue. En espagnol et en arabe, le bouton "Contactarme" et le bouton
"تواصل معي" pointaient vers `/es/contact/` et `/ar/contact/`. Ces deux
adresses n existent pas: les vraies sont `/es/contacto/` et `/ar/tawasul/`.
Un visiteur hispanophone ou arabophone tombe sur une 404, clique sur le bouton
pour vous joindre, et retombe sur une 404. Verifie en ligne avant correction:
`https://georgesmatar.ca/ar/contact/` renvoyait bien un code 404.

**Correction.** `layouts/404.html` corrige, reconstruit, pousse. Commit
`fix: la page 404 renvoyait vers /es/contact/ et /ar/contact/, deux 404`.

**Etat apres correction.** Zero lien interne brise sur l ensemble des 934
pages. Les 6 liens externes du site (profil RE/MAX, Facebook, Instagram,
YouTube, Cal.com, Google Maps) repondent tous 200.

**Ce qu il reste a verifier et que je ne peux pas voir d ici:** le rapport
"Pages" de Search Console, qui liste les 404 vues par Google, y compris celles
venant de liens externes ou d anciennes adresses. Voir la liste de demandes a
la fin.

---

## Les 4 points absents

### 6. Sitemap des images

Le sitemap ne contient aucune entree image. Hugo ne les ajoute pas seul.

Le site heberge les photos des proprietes, les photos de bureau et les images
d articles. Sans sitemap d images, Google Images les decouvre seulement en
explorant les pages, plus lentement et moins completement. Pour un courtier,
Google Images est un canal reel: les gens cherchent des photos de quartier et
de proprietes.

Correction: un gabarit de sitemap personnalise qui ajoute l espace de noms
`image:image` et liste, pour chaque fiche de propriete et chaque article, les
images de la page. Travail de gabarit, aucune decision de contenu requise.

### 18. Liens externes sur la page "a propos"

La page `/about/` ne contient aucun lien sortant dans son corps. Les seuls
liens externes de la page viennent du pied de page, present partout, ce qui ne
compte pas: Google cherche des liens contextuels qui rattachent la personne a
des entites verifiables.

Ce qui devrait y figurer, et qui existe reellement dans votre cas:
- le registre de l OACIQ, qui confirme un permis de courtier valide,
- votre profil officiel sur remaxducartier.com,
- Centris,
- votre fiche Google Business.

C est le point le plus rentable de cette liste par rapport a l effort: il
transforme une page de presentation en page verifiable.

### 22. Page "nos services"

Il n y a pas de page qui dise, en un endroit, ce que vous faites. L offre est
eclatee entre `/buyer/`, `/seller/`, `/advantages/` et `/tools/`, et le
visiteur doit la reconstituer lui-meme.

Deux consequences: Google n a pas de page unique a faire correspondre a une
recherche du type "services courtier immobilier Laval", et la section
"Services" de la fiche Google Business, qui est a remplir de toute facon
(etape 11 du fichier `TODO-GOOGLE-BUSINESS.md`), n a pas de page du site vers
laquelle pointer.

### 28. Conditions d utilisation

Aucune page de conditions, dans aucune langue. Seule la confidentialite
existe. Pour un site qui recueille des demandes par formulaire, offre six
calculateurs produisant des chiffres, et publie 159 articles traitant de
fiscalite et de droit, c est la page qui dit la portee et les limites de tout
ca. Elle protege autant qu elle rassure.

A couvrir: la valeur indicative des calculateurs, le fait que les articles ne
sont pas un avis juridique ou fiscal, l absence de relation de courtage avant
contrat signe, la propriete du contenu, le droit applicable au Quebec.

---

## Les points partiels

### 1 et 21. Pages minces, dont la page "a propos"

22 pages indexables passent sous les 200 mots. Comptage sur le texte visible
de la zone principale, hors en-tete et pied de page.

| Page | Mots | Langues |
|------|------|---------|
| `/tools/` le carrefour des calculateurs | 38 a 52 | les 4 |
| `/listings/` la liste des proprietes | 60 a 70 | les 4 |
| `/contact/` | 127 a 136 | les 4 |
| `/formulaire/` | 141 a 166 | les 4 |
| `/about/` | 154 a 195 | les 4 |
| `/tools/closing-costs/` | 172 et 199 | ar, en |

Le cas le plus genant est `/tools/`. Le pied de page y envoie depuis les 4
langues sous le nom "Outils et calculateurs", et la page n est qu une liste de
six liens nus, sans une phrase pour chacun. C est le gabarit par defaut de Hugo
qui la rend, faute d un gabarit dedie.

La page "a propos" merite son propre traitement, parce que c est le point 1 de
la liste et une des trois pages que Google regarde pour decider s il a affaire
a une vraie entreprise. Ce qui lui manque: le numero de permis OACIQ, la date
de debut de pratique, les langues parlees, les liens externes du point 18, et
assez de texte pour depasser nettement les 200 mots.

### 2. Bing Webmaster Tools

Aucune trace de validation: ni `BingSiteAuth.xml` dans `static/`, ni balise
`msvalidate.01` dans les gabarits. Si le compte existe, il a ete valide
autrement, par import depuis Search Console par exemple. A confirmer.

Cela compte plus qu avant: Bing alimente les reponses de ChatGPT et de Copilot.

### 7. Favicon

Une icone est bien declaree, mais mal: `images/remax-logo.png` fait 1996 x 2008
pixels pour 134 ko, et n est donc pas carree. Google demande une icone carree
dont le cote est un multiple de 48. Et `https://georgesmatar.ca/favicon.ico`
repond 404, alors que beaucoup de robots et de navigateurs la demandent a cette
adresse en premier.

Correction: produire un jeu propre (`favicon.ico` 48 x 48, PNG en 48, 96, 192 et
512, icone Apple en 180) a partir du logo, et declarer les tailles.

### 12. Fil d Ariane

Le balisage `BreadcrumbList` est present sur toutes les pages, c est ce que
Google lit pour le fil d Ariane des resultats. Le fil visible, lui, manque sur
52 pages: `/about/`, `/buyer/`, `/seller/`, `/tools/` et les 6 calculateurs,
`/confidentialite/`, `/formulaire/`, `/merci/`, dans les 4 langues. Il est en
place sur les articles, les proprietes, les secteurs, les avantages et le
contact.

Google demande que le balisage corresponde a ce que le visiteur voit. L ecart
n est pas sanctionne ici, mais il est facile a fermer: un partiel commun,
insere dans les cinq gabarits concernes.

### 16 et 24. Contact et coordonnees au pied de page

Le pied de page porte le telephone, le courriel, le profil RE/MAX et un bouton
de rendez-vous. **Il n y a pas d adresse postale.**

C est le point le plus important de tout cet audit pour le referencement
local. L adresse du bureau est dans `hugo.toml` et dans le balisage JSON-LD,
mais pas dans le texte visible de la moindre page. Google verifie la coherence
NAP, nom, adresse, telephone, entre la fiche Google Business, le site et les
annuaires, et il lit le texte visible. Une adresse presente seulement dans le
balisage ne vaut pas une adresse ecrite.

La page `/contact/` elle-meme reste mince, 127 a 136 mots.

### 19. Fiche Google Business

La fiche existe, elle est reliee au site comme il faut: elle alimente le
`sameAs` et le `hasMap` du balisage, et son identifiant est dans
`hugo.toml`.

En revanche, le fichier `TODO-GOOGLE-BUSINESS.md` recense 16 etapes et 14
restent marquees "pending", dont les plus lourdes:

- le nom de la fiche contient des mots-cles descriptifs, ce que les regles de
  Google interdisent, avec un risque de modification d office ou de suspension
  sur signalement d un concurrent (decision en attente),
- les profils sociaux ne sont pas renseignes dans l onglet Coordonnees,
- le bouton de rendez-vous Cal.com n est pas pose,
- la section Services est vide, c est celle qui fait correspondre la fiche aux
  recherches,
- moins de 20 photos,
- aucune publication hebdomadaire,
- les avis, qui sont le levier le plus fort d une fiche locale.

Le detail et l ordre sont deja ecrits dans ce fichier. Je ne les reprends pas
ici.

### 20, 26 et 27. Reseaux sociaux

Au pied de page: Instagram, Facebook, YouTube. Les trois liens repondent.

**LinkedIn est vide** dans `hugo.toml`. Pour un courtier qui travaille avec des
acheteurs professionnels et des investisseurs, c est le reseau qui manque le
plus, et c est un des rares profils que Google traite comme une confirmation
d identite professionnelle.

**Facebook est a verifier.** Le lien de partage enregistre redirige vers
`facebook.com/people/Georges-Matar-Courtier-immobilier-residentiel/61593154731365/`.
Cette forme d adresse est celle d un profil, pas d une page professionnelle.
Si c est un profil personnel, il faut une page professionnelle: elle seule
permet les avis, les statistiques, la publicite, et elle seule est traitee
comme une entite d entreprise. Si c est deja une page, il faut lui donner un
nom d utilisateur pour obtenir une adresse courte, plus propre dans le
`sameAs` que le lien de partage actuel.

### 32. Lisibilite

Mesure sur les 158 articles francais et les 158 anglais.

| Mesure | Francais | Anglais |
|--------|----------|---------|
| Longueur mediane | 1854 mots | 1847 mots |
| Phrase moyenne | 19,6 mots | 19,2 mots |
| Score Flesch | 55,5 | 52,7 |
| Phrases de plus de 30 mots | 19,7 % | 15,9 % |

Un score Flesch de 52 correspond a un niveau de fin de secondaire. Pour un
public general, la cible est 60 et plus. Une phrase sur cinq depasse 30 mots en
francais: c est la ou se perd le lecteur sur telephone, qui est la majorite du
trafic.

Ce n est pas un defaut technique, c est un travail de reecriture. Les articles
les plus durs, a traiter en premier:
`maison-ecoenergetique-novoclimat-quebec`, `insectes-rongeurs-infestation-recours-quebec`,
`solarium-veranda-permis-evaluation-quebec`, `guide-nouveaux-arrivants-quebec`,
`heritage-property-montreal`, `listing-exposure-centris-advertising-quebec`.

### 33. Les deux reserves sur le contenu duplique

**Titres identiques.** `/contact/` et `/en/contact/` portent tous deux
`Contact | Georges Matar`. Les deux pages sont dans des langues differentes et
le `hreflang` les relie, donc le risque est faible, mais le titre francais
gagnerait a dire "Me joindre" ou "Contacter Georges Matar".

**Pages de secteur.** 38 pages de ville, ressemblance moyenne de 33 %, ce qui
est sain. Deux paires montent plus haut: Mascouche et Saint-Constant a 60 %,
Blainville et Boucherville a 53 %. Ce sont celles a relire en premier si vous
voulez vous eloigner du modele de la page satellite: un prix median local, un
quartier nomme, une ecole, une station, bref quelque chose qui ne pourrait pas
etre dit d une autre ville.

---

## Les deux points sans objet

**29. Politique de retour.** Elle n a pas de sens pour un service de courtage.
L equivalent utile, et qui rassure vraiment un vendeur, est l explication des
conditions de resiliation du contrat de courtage. Cela a sa place dans les
conditions d utilisation du point 28.

**30. Politique de garantie.** Pas de garantie produit non plus. L equivalent
existe chez vous: Tranquilli-T, deja documente dans `/advantages/tranquilli-t/`.
Il n est pas lie depuis le pied de page. Un lien "Garanties RE/MAX" dans le
pied de page coche ce point dans son esprit.

---

## Ordre de travail propose

Du plus rentable au moins rentable, par rapport a l effort.

1. **Adresse du bureau dans le pied de page**, 4 langues. Le plus court chemin
   vers un gain de referencement local reel. Points 24 et 19.
2. **Page "a propos" refaite**, 4 langues: permis OACIQ, parcours, langues,
   liens externes vers OACIQ, RE/MAX, Centris, Google Business. Points 1, 18, 21.
3. **Conditions d utilisation**, 4 langues, liees au pied de page. Point 28.
4. **Page "Mes services"**, 4 langues, qui alimente aussi la section Services
   de la fiche Google Business. Point 22.
5. **Carrefour `/tools/` refait** avec un gabarit dedie et une description par
   calculateur. Point 21.
6. **Jeu de favicons propre**. Point 7.
7. **Fil d Ariane visible** sur les 52 pages qui en manquent. Point 12.
8. **Sitemap des images**. Point 6.
9. **Fiche Google Business**: reprendre `TODO-GOOGLE-BUSINESS.md` dans l ordre,
   en commencant par la decision sur le nom. Point 19.
10. **LinkedIn**, puis verification du statut de la page Facebook. Points 26, 27.
11. **Lisibilite**: campagne de reecriture, les 6 articles les plus durs
    d abord. Point 32.
12. **Relecture des pages de secteur** les plus semblables. Point 33.

Les points 1 a 8 sont du travail que je fais seul. Les points 9 a 12 demandent
soit vos identifiants, soit vos decisions, soit les deux.

---

## Ce dont j ai besoin de vous

1. **Bing Webmaster Tools**: le compte existe-t-il? Si non, je prepare le
   fichier de validation et vous n avez qu a creer le compte.
2. **Search Console**: une capture ou une exportation du rapport "Pages"
   (Indexation). C est le seul endroit ou apparaissent les 404 vues par Google
   depuis l exterieur, que mon analyse du site ne peut pas voir.
3. **Numero de permis OACIQ** et **date de debut de pratique**, pour la page "a
   propos" et le pied de page.
4. **Facebook**: est-ce une page professionnelle ou un profil personnel? Si
   c est une page, son adresse courte.
5. **LinkedIn**: voulez-vous que je prepare le texte du profil, ou le compte
   existe-t-il deja quelque part?
6. **Conditions d utilisation**: je rediges un texte standard pour un courtier
   au Quebec, que vous faites relire. Confirmez que cela vous va, ou donnez-moi
   un modele de RE/MAX DU CARTIER s il en existe un.
7. **Adresse exacte a afficher au pied de page**: je reprends celle de
   `hugo.toml`, `2820, boul. Saint-Martin Est, bureau 201, Laval (Duvernay),
   Quebec H7E 5A1`, sauf avis contraire. Elle doit etre ecrite exactement comme
   sur la fiche Google Business.
