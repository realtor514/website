# Audit des 33 points de confiance Google

Date: 2026-10-02
Portee: georgesmatar.ca dans les 4 langues (934 pages construites, 220 URL par
langue) et la fiche Google Business.
Methode: analyse du site construit page par page (titres, descriptions,
canoniques, balisage, nombre de mots, liens internes et externes), requetes
HTTP reelles sur le site en ligne, lecture des gabarits et de hugo.toml.

**Resultat de l audit initial: 18 points conformes, 9 partiels, 4 absents, 2
sans objet.**

**Etat apres les corrections du 2026-10-02: 28 conformes, 3 partiels, 0 absent,
2 sans objet.** Les points 1 a 8 de l ordre de travail ont ete executes et
pousses en ligne. Ce qui reste depend de vous: Bing, LinkedIn, la fiche Google
Business et la campagne de lisibilite. Le detail est a la fin, section
**Ce qui a ete fait**.

---

## Tableau de bord

| # | Point | Etat initial | Etat au 2026-10-02 |
|---|-------|--------------|--------------------|
| 1 | Page "a propos" unique | Partiel | **Conforme** |
| 2 | Bing Webmaster Tools | A verifier, probablement absent | A verifier avec vous |
| 3 | Google Search Console | Conforme | Conforme |
| 4 | Aucune erreur 404 | Corrige aujourd hui | **Conforme** |
| 5 | Sitemap XML | Conforme | Conforme |
| 6 | Sitemap des images | **Absent** | **Conforme** |
| 7 | Favicon | Partiel | **Conforme** |
| 8 | Aucune erreur 5xx | Conforme | Conforme |
| 9 | Liens brises repares | Conforme apres correction | **Conforme** |
| 10 | Aucune page orpheline | Conforme | Conforme |
| 11 | Pages choisies en noindex | Conforme | **Conforme** |
| 12 | Fil d Ariane | Partiel | **Conforme** |
| 13 | Balises canoniques | Conforme | Conforme |
| 14 | Avis sur les temoins | Conforme | Conforme |
| 15 | Section auteur sur les articles | Conforme | Conforme |
| 16 | Page contact | Conforme, mais mince | **Conforme** |
| 17 | Politique de confidentialite | Conforme | Conforme |
| 18 | Liens externes sur la page "a propos" | **Absent** | **Conforme** |
| 19 | Fiche Google Business | Partiel | Partiel, action de votre cote |
| 20 | Reseaux sociaux au pied de page | Partiel | Partiel, LinkedIn a creer |
| 21 | Toutes les pages au-dessus de 200 mots | Partiel, 22 pages en dessous | **Conforme** |
| 22 | Page "nos services" | **Absent** | **Conforme** |
| 23 | Mention de droit d auteur | Conforme | Conforme |
| 24 | Coordonnees au pied de page | Partiel, adresse manquante | **Conforme** |
| 25 | Certificat SSL | Conforme | Conforme |
| 26 | Compte LinkedIn | **Absent** | **Absent, a creer** |
| 27 | Compte Facebook professionnel | A verifier | **Conforme** |
| 28 | Conditions d utilisation au pied de page | **Absent** | **Conforme** |
| 29 | Politique de retour | Sans objet | Sans objet |
| 30 | Politique de garantie | Sans objet au sens strict | **Conforme** |
| 31 | Date de publication sur les articles | Conforme | Conforme |
| 32 | Controle de lisibilite | Partiel | Partiel, reecriture a faire |
| 33 | Contenu duplique retire | Conforme a une exception pres | **Conforme** |

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

## Ce qui a ete fait, le 2026-10-02

Les points 1 a 8 de l ordre de travail sont executes, construits, verifies et
pousses en ligne. Tout a ete fait dans les 4 langues.

**1. Adresse et permis au pied de page.** L adresse du bureau est maintenant
ecrite en texte visible sur chaque page, composee a partir des memes champs que
le JSON-LD pour que les deux ne puissent pas diverger, et liee a la fiche
Google Business. Une bande legale a ete ajoutee au-dessus du droit d auteur:
numero de permis **J7941**, lien vers le [registre public de l OACIQ](https://registre.oaciq.com/),
puis confidentialite, conditions d utilisation et garanties RE/MAX.
Points 24, 30 et une partie de 19.

**2. Page "a propos" refaite.** Permis, parcours d ingenieur, domaines,
territoire, langues, coordonnees, et surtout quatre liens externes
verifiables: registre de l OACIQ, profil RE/MAX DU CARTIER, Centris, fiche
Google Business. Elle est passee de 154-195 mots a plus de 400.
Points 1, 18 et 21.

**3. Conditions d utilisation.** Page creee dans les 4 langues et liee au pied
de page: portee des calculateurs, absence de relation de courtage avant contrat
signe, limites des articles, fiches de proprietes, propriete du contenu,
plainte et encadrement OACIQ, droit applicable au Quebec. Point 28, et le
point 29 y est traite sous sa forme utile pour un courtier.

**4. Page "Mes services".** Creee dans les 4 langues, avec une FAQ balisee en
`FAQPage` qui peut sortir en resultat enrichi. Elle sert aussi de cible a la
section Services de la fiche Google Business, qui reste a remplir. Point 22.

**5. Carrefour des calculateurs.** Gabarit dedie, texte d introduction, une
carte par calculateur avec sa description. La page est passee de 38-52 mots a
plus de 450. Un bloc explicatif commun a aussi ete ajoute sous chaque
calculateur: d ou viennent les chiffres, et ou s arrete leur portee.
Point 21.

**6. Favicons.** Jeu complet genere depuis le logo, cadre et detoure: ico
multi-taille 16, 32 et 48, PNG en 48, 96, 192 et 512, icone Apple 180 sur fond
creme de la charte. `/favicon.ico` ne repond plus 404. Point 7.

**7. Fil d Ariane visible.** Ajoute sur les 52 pages qui en manquaient, par un
partiel commun reutilisable. Il reste volontairement absent des pages d accueil
et des 4 pages de formulaire, qui sont des pages de conversion sans
navigation. Point 12.

**8. Sitemap des images.** Gabarit de sitemap personnalise: 212 images
declarees par langue, plus `lastmod` sur chaque page et exclusion des pages en
noindex. Les 5 sitemaps ont ete valides au parseur XML. Point 6.

**Travaux complementaires.**

- Pages minces traitees: listes de proprietes, pages de contact et pages de
  calculateurs. Les 4 pages de formulaire passent en noindex, ce sont des pages
  de conversion qui doublaient la page de contact. Deux lignes a retirer de
  leur frontmatter suffisent a revenir en arriere.
- Lien Facebook remplace par l adresse stable de la page, au lieu du lien de
  partage qui redirigeait. Point 27.
- Titre de la page de contact francaise differencie de l anglaise. Point 33.
- Page 404: les boutons espagnol et arabe menaient a une 404. Points 4 et 9.

**Verification apres coup, sur les 942 pages construites:** zero lien interne
brise, zero page orpheline, zero page indexable sous 200 mots, zero description
meta dupliquee, zero image sans attribut `alt`, 5 sitemaps valides.

---

## Ce qui reste

Trois points, tous dependants de vous.

**19. Fiche Google Business.** Le fichier `TODO-GOOGLE-BUSINESS.md` reste la
reference. Dans l ordre: trancher sur le nom de la fiche, qui contient des
mots-cles descriptifs interdits par Google; remplir la section Services, qui a
maintenant une page du site vers laquelle pointer; poser le bouton Cal.com;
monter a 20 photos; lancer les demandes d avis. L adresse du site est
maintenant coherente avec la fiche, ce qui etait le prerequis.

**20 et 26. LinkedIn.** Le parametre est vide dans `hugo.toml`. Des que le
compte existe, une seule ligne a changer et l icone apparait au pied de page
dans les 4 langues, et le profil entre dans le `sameAs` du balisage.

**32. Lisibilite.** Flesch median de 52,7 en anglais pour une cible de 60, et
une phrase sur cinq au-dessus de 30 mots en francais. C est une campagne de
reecriture, pas une correction technique. Les six articles les plus durs sont
nommes plus haut.

**2. Bing Webmaster Tools.** Des que vous confirmez si le compte existe. S il
n existe pas, l import depuis Search Console prend deux clics et ne demande
aucun fichier.

---

## Ce dont j ai encore besoin de vous

1. **Bing Webmaster Tools**: le compte existe-t-il?
2. **Search Console**: le rapport "Pages", a
   `https://search.google.com/search-console/index?resource_id=sc-domain:georgesmatar.ca`
   ou, si la propriete est de l autre type,
   `https://search.google.com/search-console/index?resource_id=https://georgesmatar.ca/`.
   C est le seul endroit ou apparaissent les 404 vues par Google depuis
   l exterieur.
3. **Adresse du pied de page**: elle doit etre identique, mot pour mot, a celle
   de la fiche Google Business. Elle affiche aujourd hui
   `2820, boul. Saint-Martin Est, bureau 201 / Laval, QC H7E 5A1`. Si la fiche
   ecrit autre chose, par exemple avec la mention Duvernay, dites-le moi.
4. **Conditions d utilisation**: le texte est complet et prudent, mais il n a
   pas ete relu par un juriste. A faire relire avant de vous y fier.
5. **LinkedIn**: le compte existe-t-il quelque part, ou faut-il le creer?
6. **Date de debut de pratique**, si vous voulez l afficher sur la page "a
   propos". Elle n y figure pas pour l instant.
