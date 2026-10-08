# Prospection vendeurs

Ce dossier sert a aller chercher des vendeurs hors du site, puis a les ramener
vers le formulaire qui les reconnait. Cree le 2026-10-08.

## Comment un lead vendeur arrive depuis le 2026-10-08

- Tout lien vers `georgesmatar.ca/formulaire/?intention=evaluation` ouvre le
  formulaire sur "Faire evaluer", avec le titre "Evaluation gratuite de votre
  propriete" et deux questions de plus: l'adresse et le delai de vente. Meme
  chose en `/en/form/`, `/es/formulario/` et `/ar/istimara/`.
- L'objet du courriel dit l'urgence des la boite de reception:
  `VENDEUR - moins de 3 mois - evaluation - formulaire (fr) - georgesmatar.ca`.
  Le filtre de `gmail-filtres-leads.xml` le range toujours dans Leads/Vendeur.
- Le champ `campagne` du courriel dit de quelle lettre ou publicite il vient.

**La regle qui compte le plus:** un "VENDEUR - moins de 3 mois" se rappelle
dans l'heure. C'est celui que Rovena recoit, et c'est le seul qui ne t'attend
pas.

## La routine

**1. Une lettre "vendu" autour de chaque vente.** Les voisins d'une maison
vendue sont les proprietaires les plus curieux de leur propre valeur ce
mois-la. Viser 150 a 200 portes autour de la maison. Respecter les
autocollants "pas de circulaires".
Premiere campagne prete: `lettre-vendu-28-st-hilaire.md`, avec ses codes QR.
Pour une nouvelle vente: `python prospection-vendeurs/qr.py vendu-<adresse>`,
copier la lettre, changer l'adresse. La vente de Mirabel est a Saint-Hermas,
en rang: trop peu de voisins pour une campagne.

**2. Les successions.** Un heritier qui ne garde pas la maison est un vendeur
presque certain. Le site sort deja en 14e position sur "vente de succession
saint-bruno-de-montarville" (136 affichages en 3 mois, Search Console du
2026-10-07). Se presenter a cinq notaires de tes secteurs avec l'article
[Heriter d'une propriete au Quebec](https://georgesmatar.ca/articles/inheritance-property-quebec/).
Ne propose aucune commission de reference: un courtier ne partage sa
retribution qu'avec un autre titulaire de permis.

**3. Les inscriptions expirees.** Un proprietaire dont l'inscription Centris a
expire voulait vendre et n'a pas vendu. Lettre ou porte a porte. Avant
d'appeler, verifier le numero sur la Liste nationale de numeros de
telecommunication exclus (LNNTE): le courtage immobilier n'en est pas
exempte. Et verifier que l'inscription n'a pas ete renouvelee avec un autre
courtier: la mention en bas de la lettre est la pour ca.

**4. Les avis Google.** Chaque avis rend la lettre plus credible au moment ou
le voisin te cherche sur Google. Messages prets: `SEO-PLAN.md`, partie 2.

**5. Le marche arabophone.** `TODO.md`, point 9.

## Mesurer

Une fois par mois, compter dans Leads/Vendeur les courriels par `campagne`.
Une campagne qui ne rapporte rien apres deux envois s'arrete; celle qui
rapporte se repete dans la rue voisine.
