# Correction: effet de la gare sur les prix et Mirabel, pages de quartier (2026-10-21)

Dix pages de quartier affirment, sans source, que la gare, le REM ou le metro
font monter les prix autour d eux. Aucune statistique publique ne le mesure:
Centris publie un seul chiffre par ville, sans decoupage par distance a une
gare. L article 112 du Reglement sur les conditions d exercice et les regles
de l OACIQ exigent qu une affirmation publicitaire soit verifiable. Ces
phrases doivent donc devenir verifiables, sans perdre l information utile sur
le transport.

Le modele est la correction deja faite a Mascouche le 2026-10-21:
- question FAQ: « La gare de Mascouche change-t-elle le calcul pour un acheteur? »
- reponse: le fait de transport reste (ligne exo, ce qu elle evite), puis
  « Aucune statistique publique ne mesure l effet de la gare sur les prix:
  Centris publie un seul chiffre pour Mascouche, et pour une propriete donnee,
  ce sont les ventes recentes autour de la gare qui le montrent. »
- corps: « Aucune statistique publique ne mesure son effet sur les prix. »

## Passages a corriger (texte francais de reference)

1. candiac.md
   - FAQ « La gare exo change-t-elle la valeur des proprietes? »: la question
     devient « La gare exo change-t-elle le calcul pour un acheteur? ». Dans la
     reponse, garder la ligne Candiac et la gare Lucien-L Allier, remplacer
     « L effet est reel mais localise » et « un segment d acheteurs qui
     n existerait pas autrement » par la phrase modele.
   - Corps: « Le secteur de la gare beneficie d une prime liee au transport
     collectif, concentree sur un rayon reduit. » devient « Le secteur de la
     gare donne acces a la ligne Candiac. Aucune statistique publique ne mesure
     son effet sur les prix. »
2. delson.md, FAQ « La gare exo est-elle un avantage reel? »: remplacer la
   derniere phrase, « L effet sur les prix est concentre... », par la phrase
   modele (Centris publie un seul chiffre pour Delson).
3. saint-constant.md
   - FAQ: remplacer « L effet sur les prix est reel mais concentre. » par la
     phrase modele.
   - Corps: « avec une prime de prix localisee autour de la gare » est retire;
     la phrase finit apres « un segment precis d acheteurs ».
4. brossard.md, FAQ « Le REM a-t-il vraiment fait monter les prix a Brossard? »:
   la question devient « Le REM change-t-il le calcul pour un acheteur a
   Brossard? ». La reponse garde les stations Panama, Du Quartier et Brossard
   et l acces sans voiture, puis la phrase modele adaptee au REM. Retirer
   « Oui, mais pas partout », « surtout sur les condos » et « sans prime
   particuliere ».
5. saint-jerome.md, FAQ « Le train de banlieue change-t-il la valeur des
   proprietes? »: la question devient « Le train de banlieue change-t-il le
   calcul pour un acheteur? ». La reponse garde la ligne Saint-Jerome vers le
   centre-ville, et remplace « un segment d acheteurs qui n existerait pas
   autrement » et « L effet sur le prix est reel mais localise: il ne se
   propage pas a toute la ville » par la phrase modele.
6. sainte-therese.md, FAQ « La gare influence-t-elle les prix? »: la question
   devient « La gare change-t-elle le calcul pour un acheteur? ». La reponse
   dit que la gare de Sainte-Therese est sur la ligne exo Saint-Jerome, puis la
   phrase modele.
7. saint-basile-le-grand.md: « A l interieur de la ville, la proximite de la
   gare et l age de la maison comptent parmi les premiers facteurs d ecart de
   prix. » devient « A l interieur de la ville, comparez des proprietes d age
   semblable et a distance semblable de la gare. »
8. mont-saint-hilaire.md: « la vue sur la montagne, la distance a la gare et
   les contraintes du terrain expliquent une bonne partie des ecarts de prix »
   devient « comparez des proprietes semblables pour la vue sur la montagne,
   la distance a la gare et les contraintes du terrain ».
9. longueuil.md: « Les rues situees a distance de marche de la station
   Longueuil-Universite-de-Sherbrooke se negocient a des prix qui n ont plus
   grand-chose a voir avec le reste de la ville: c est le seul endroit de la
   Rive-Sud ou un acheteur peut se passer d une voiture. » devient « Les rues
   a distance de marche de la station Longueuil-Universite-de-Sherbrooke
   donnent acces au metro de Montreal sans voiture. »
10. mirabel.md
   - H2 « Une ville, dix marches » devient « Une ville, 13 secteurs ».
   - « Mirabel est le territoire le plus vaste et le plus fragmente de la
     region. C est aussi l une des villes ou une estimation automatisee a le
     plus de chances d etre fausse. » devient « Avec 486 km2, Mirabel a l un
     des plus grands territoires municipaux du Quebec, selon la Ville. »
   - « Comparer une vente de Saint-Janvier a une propriete de Saint-Benoit n a
     aucun sens. C est pourtant exactement ce que font les outils en ligne. »
     devient « Une vente de Saint-Janvier ne se compare pas a une propriete de
     Saint-Benoit: un prix se compare aux ventes recentes du meme secteur. »

Les versions anglaise, espagnole et arabe sont des traductions: trouvez le
passage equivalent et ecrivez la correction dans la langue de la page. Si une
de ces 10 pages contient, dans votre langue, une autre phrase qui attribue a
la gare, au REM ou au metro un effet sur les prix, corrigez-la de la meme
facon et signalez-la.

## Regles

- Ne touchez a rien d autre: ni aux autres facts, ni aux autres questions, ni
  au reste du texte.
- `lastmod: 2026-10-21` sur chaque page modifiee. Si la page n a pas de
  `date:`, ajoutez-la juste avant lastmod, a la date du premier commit du
  fichier: `git log --diff-filter=A --follow --format=%as -- <fichier> | tail -1`.
- Zero tiret long, em dash, en dash ou double tiret.
- Pas de commit, pas de push.

## Rapport

Pour chaque fichier: l ancien texte et le nouveau, passage par passage.
