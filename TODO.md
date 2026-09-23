# Todo List

## Instructions pour Claude
Quand l'utilisateur ecrit "fais todo":
1. Identifier le prochain point avec Status: pending
2. Executer CE POINT SEULEMENT
3. Marquer le point comme done dans ce fichier
4. Confirmer si ca a bien fonctionne
5. S'ARRETER et demander: "Veux-tu passer au point suivant?"
Ne jamais executer plusieurs points d'un coup sans confirmation.

## Point 7 - Outil Alerte immobiliere
Ajouter une page ou section "Alerte immobiliere" avec un formulaire permettant aux acheteurs d'etre avises par courriel des nouvelles inscriptions selon leurs criteres. Service gratuit et confidentiel. Inspirer du texte suivant: "Soyez informes des nouvelles inscriptions de residences a vendre. Notre alerte immobiliere offre la possibilite aux acheteurs d'etre avises rapidement des nouvelles inscriptions sur le marche selon vos criteres prealablement etablis. Les resultats vous seront achemines par courriel."
**Status:** pending

## Point 8 - Rappel immediat des leads vendeurs
Faire en sorte qu'un lead vendeur declenche une alerte sur le telephone de Georges en moins de cinq minutes, pas seulement un courriel. Un vendeur rappele dans les minutes qui suivent sa demande se convertit plusieurs fois mieux qu'un vendeur rappele une heure plus tard. C'est le levier le plus rentable du site et il ne coute presque rien.
Le tri est deja fait: depuis la separation des leads, le courriel Formspree d'une estimation arrive avec l'objet "VENDEUR - estimation de propriete", et les champs `outil` et `intention` accompagnent chaque envoi.
Ce qui reste a faire:
- Creer une regle dans Gmail qui repere l'objet commencant par "VENDEUR" et lui met une etiquette dediee
- Activer la notification push du telephone pour cette etiquette seulement, pour que seuls les vendeurs sonnent
- Verifier le delai reel avec un envoi de test depuis le site
- Option a evaluer plus tard: un envoi SMS automatique via un connecteur, si le courriel s'avere trop lent
**Status:** pending

## Point 9 - Occuper le marche arabophone
Devenir le courtier de reference des communautes arabophones de Laval et de Montreal. C'est le seul territoire ou Georges part avec un avantage que personne d'autre a l'agence ne possede, et le bouche a oreille dans une communaute soudee produit des vendeurs motives et reels, ceux qui appellent parce qu'on leur a dit d'appeler.
L'actif existe deja: 64 articles en arabe sont en ligne, soit plus que ce que la majorite des courtiers publient dans leur langue principale. Ce qui manque, c'est la visibilite hors du site.
Ce qui reste a faire:
- Ajouter l'arabe dans la fiche Google Business: description, services et publications
- Creer une page d'entree dediee "courtier immobilier arabophone a Laval et Montreal", dans les 4 langues
- Se rendre visible dans les groupes Facebook des communautes libanaise, syrienne, egyptienne et maghrebine de Montreal, sans vendre, en repondant aux questions immobilieres
- Verifier que les articles arabes sont bien indexes dans Search Console
- Viser les quartiers ou la communaute est dense: Saint-Laurent, Saint-Leonard, Laval Chomedey
**Status:** pending

## Point 10 - Avis Google
Systematiser la collecte d'avis Google. Les avis sont ce qui transforme une recherche anonyme en appel telephonique, et ils comptent aussi pour le classement dans le pack local.
Attention: ce chantier est deja decrit en detail dans `TODO-GOOGLE-BUSINESS.md`, etape 15, de 15.1 a 15.4, avec le lien de demande d'avis, la relance des anciens clients, la demande systematique aux nouveaux et la reponse a chaque avis. Ne pas refaire le travail ici, suivre ce fichier.
**Status:** pending
