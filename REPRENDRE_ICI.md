# Reprendre ici

Etat au **2026-09-26**. Ce fichier existe pour qu une session puisse continuer le
moteur de contenu du blogue sans rien redecouvrir. Il remplace la version du
2026-09-25, ecrite quand le site comptait 121 articles par langue.

Repertoire du projet:
`C:\Users\georg\OneDrive\A_personal\career\ciq25\ciqq\remax du cartier\website`

`hugo` n est PAS installe sur ce poste. `tools/validate.py` remplace le build.

---

## 1. Ou en est le site

```
En ligne dans les 4 langues    146 par langue    584 fichiers
Brouillon francais en attente    1  (minimaison, a traduire)
Articles marques a revoir       72 sur 147
```

Branche de travail: `main`. Le deploiement part de `main` par GitHub Actions
(Hugo 0.155.0), environ 30 secondes. Depot `realtor514/website`.

Etat chiffre a tout moment: `python tools/status.py`

Le plan de contenu, `state/content_plan.json`, compte 211 lignes:

```
clear            93   a ecrire
written_draft    84   ecrits et publies
already_covered  24   refuses par la porte 1, avec covered_by
parked            5   a trancher par Georges
in_progress       5   reclames dans le registre, en cours
```

## 2. La boucle de production, en huit etapes

1. `python tools/plan_gate.py gate1` reannote le plan contre le contenu reel.
   A refaire apres chaque vague: un sujet `clear` peut devenir `already_covered`
   parce qu on vient d ecrire son voisin.
2. `python tools/plan_gate.py claim t01 t02 ...` reclame les sujets de la vague.
3. Lancer un agent redacteur par sujet. Le prompt tient en dix lignes: il pointe
   vers `state/CONSIGNE_REDACTEUR.md`, donne l `id`, le slug et la date, puis
   ajoute les notes propres au sujet. **Ne repetez pas la consigne commune dans
   le prompt**, elle est dans le fichier.
4. Quand un redacteur a rendu son rapport, et seulement alors,
   `python tools/publish.py run --slugs <slug> ...` copie de `drafts/fr/` vers
   `content/fr/articles/`, en `draft: true`.
5. `python tools/trad_spec.py <slug> ...` genere la fiche de faits. La coller
   dans `state/TRAD_LOT<n>.md`, puis **ajouter a la main ce que le script ne sait
   pas**: le coeur de l article, ce qu il ne faut pas aplatir, les slugs cibles
   par langue, et les references de voix.
6. Verifier que chaque slug cible est libre, avec un script, avant de lancer:
   `os.path.exists('content/<lang>/articles/<slug>.md')`. Voir le piege 3.
7. Lancer trois traducteurs, un par langue.
8. `python tools/release.py --check` puis sans `--check`. Il ne publie qu un
   groupe complet dans les 4 langues et valide les 4 fichiers avant de basculer
   `draft: false`. Puis `python tools/fetch_images.py`, `git commit`, `git push`.

## 3. Les outils, et ce que chacun resout

| Outil | Role |
|---|---|
| `tools/dedupe.py check <fichier>` | six portes anti-doublon. **Sous-commande `check`, pas `--check`**: avec `--check` il affiche l aide et sort en 0, ce qui ressemble a un succes |
| `tools/validate.py <fichiers>` | remplace `hugo build`, qui n est pas installe ici |
| `tools/publish.py run --slugs ...` | copie vers `content/`, repartit les dates |
| `tools/release.py` | publie tout groupe complet dans les 4 langues |
| `tools/linkmap.py` | refait les 4 cartes de liens depuis le contenu reel |
| `tools/trad_spec.py <slug>` | fiche de faits, chaque fait dans sa phrase |
| `tools/ccq.py <numeros>` | lit le Code civil quand LegisQuebec est hors service |
| `tools/fetch_images.py` | telecharge les images a la une manquantes |
| `tools/status.py` | etat du corpus |
| `tools/approve.py` | **pour Georges seulement**, bascule draft a false a la main |

## 4. Les pieges, tous rencontres pour de vrai

**1. Ne publiez jamais depuis un instantane en vol.** Attendez le rapport de
l agent. Sept articles ont ete publies un jour depuis des fichiers que les
redacteurs etaient encore en train de resserrer.

**2. Un lien vers un article encore en draft est un 404 en production.** Hugo ne
rend pas les brouillons. Le validateur refuse ce cas depuis.

**3. Un slug cible peut deja etre pris par un AUTRE article.** Au lot 8, le slug
que j avais donne pour l article sur les deductions pointait sur la traduction
anglaise et arabe d un article publie. Les trois traducteurs l ont vu et ont
change de slug d eux-memes. Verifiez avant, et dites aux traducteurs de verifier
aussi: c est la derniere barriere.

**4. Mes listes de faits a preserver se trompent, systematiquement.** Sur les
lots 7 a 10, les traducteurs ont trouve une quinzaine d erreurs, toujours la meme
classe: **une liste plate perd le rattachement.** Un article du reglement de
Laval attribue a Montreal, un montant qui passe d une ville a l autre, un numero
venu d un autre article. C est pour ca que `tools/trad_spec.py` existe: il montre
chaque fait dans sa phrase. **Utilisez-le, n ecrivez plus de listes plates.**

**5. Dites aux traducteurs que le fichier francais tranche.** A chaque lot, au
moins un traducteur a eu raison contre ma consigne. Cette phrase doit rester dans
chaque prompt.

**6. Les agents calent.** Le watchdog tue un agent apres 600 secondes sans
progres, et c est arrive quatre fois hier, trois fois aujourd hui. **Le travail
n est pas perdu:** verifiez `drafts/fr/` et `meta/fr/` sur le disque, puis lancez
un agent finisseur en lui decrivant l etat exact. Un cas merite attention: si le
`.md` existe mais pas le `.json`, le releve de sources est perdu et **ne se
reconstruit pas depuis le texte**. Le finisseur doit rouvrir chaque source et
retirer de l article ce qu il ne retrouve pas.

**7. Entre 8 et 13 agents en parallele.** Au-dela, les calages se multiplient.

**8. Une reserve consignee sans drapeau est invisible.** `validate.py` refuse
desormais un article dont le JSON a des `claims_needing_review` sans
`needs_expert_review: true` dans le front matter. Le controle a trouve 12
articles dans ce cas, dont 11 deja publies.

**9. Mes fiches de plan contiennent des erreurs de fait.** Les redacteurs en ont
corrige une trentaine: une section de formulaire qui n existe pas, un programme
ferme presente comme ouvert, une norme niee qui existe, une ville creditee d un
reglement qui appartient a une autre, un article a lier qui n avait jamais ete
ecrit. **Laissez-leur le droit d ecrire l inverse de la fiche**, et demandez-leur
de le signaler dans leur rapport.

**10. Un outil peut halluciner une source.** Un redacteur a recu le resume
fabrique d une decision du Tribunal administratif du logement, montants
attribues a la mauvaise affaire. Il a relu la page brute, constate la
fabrication, et l a remplacee par deux decisions verifiees mot a mot. C est
pourquoi la consigne exige d ouvrir la source, pas de la resumer de seconde main.

**11. `publish.py` repartit les dates et ecrase celle du redacteur.** Un article
qui cite des statistiques diffusees le 4 septembre s est retrouve date du
26 aout. Verifiez apres publication qu aucun article ne cite une donnee
posterieure a sa propre date.

## 5. L etat des sites officiels

Tout est dans `state/CONSIGNE_REDACTEUR.md`, section 4, tenu a jour par les
redacteurs eux-memes. Les deux points a retenir:

- **LegisQuebec repond 502 depuis le 25 septembre**, et ce n est pas un blocage
  anti-robot: avec un agent de navigateur le WAF laisse passer et l origine
  tombe. CanLII repond 403, `ccq.lexum.com` est une coquille JavaScript.
  **La route qui marche est `tools/ccq.py`**, une capture datee de
  web.archive.org. Deux pieges dedans, documentes dans le fichier: le suffixe
  `id_` apres l horodatage, et `curl --compressed`, sans quoi on recupere du
  binaire gzippe qui ressemble a une page vide.
- **hydroquebec.com est geo-bloque hors Quebec** derriere une page qui repond
  **200**. Un code 200 ne prouve donc rien: verifiez le titre de la page.
  J ai annonce a Georges que le site etait revenu sur la foi de ce 200, et
  c etait faux. Un agent l a corrige.

## 6. Les regles inviolables du projet

1. **Zero tiret long**, em dash, en dash ou double tiret, dans tout ce qui est
   produit, front matter et tableaux compris. `CLAUDE.md` regle 1. La regle vise
   la typographie: un tiret long qui remplace une virgule, un deux-points ou un
   point. Deux litteraux y echappent, parce qu ils ne s ecrivent pas autrement:
   une URL officielle qui contient un double tiret, gardee telle quelle dans le
   JSON de meta et jamais dans le texte de l article, et une option de ligne de
   commande comme `--check` ou `--slugs` dans la documentation interne. Aucun des
   deux n apparait dans un article publie.
2. **Les 4 langues, toujours.** `CLAUDE.md` regle 2. Un article ne vit pas dans
   une langue seule, et une correction se fait dans les quatre.
3. **Georges sert en francais, anglais et arabe.** Jamais de promesse de service
   en espagnol, meme si le site existe en espagnol.
4. **Rien d invente.** Pas de source, pas d affirmation. Un article qui dit
   « aucune source officielle ne chiffre ceci » est meilleur qu un article qui
   invente le chiffre: c est la voix du site.
5. **Ne touchez jamais aux articles que Georges a ecrits lui-meme.** Le moteur
   n ecrit que dans `drafts/`, `meta/`, et les fichiers qu il a crees.
6. `/secteurs/...` n existe pas. Les pages de ville vivent sous
   `/courtier-immobilier/laval/` et declarent leur propre `url:`.

## 7. Ce qui attend Georges

**72 articles sur 147 portent au moins une affirmation a faire confirmer.** La
liste exacte est dans `meta/fr/<slug>.json`, champ `claims_needing_review`. Ce
n est pas de la prudence decorative: c est la trace de ce que les redacteurs
n ont pas pu verifier a la source.

Deux verifications que lui seul peut faire vite, parce qu il est au Quebec:

- les tarifs et les montants LogisVert d Hydro-Quebec, dans
  `particularites-maison-quebecoise` et `renovations-resilience-climat-quebec`.
  Ils viennent de captures d archive, le site etant geo-bloque. Les tarifs sont
  bons jusqu au 1er avril 2027, les montants LogisVert datent du
  6 septembre 2026.
- le volet maisons lezardees du programme Renovation Quebec a Laval, dans
  `fissures-affaissement-fondation-expertise-quebec`. La derniere edition
  verifiable fermait le 21 mars 2025 et pourrait avoir rouvert.

Les decisions parkees sont dans `NEEDS_HUMAN.md`, avec les 5 lignes `parked` du
plan.

## 8. La question de fond, deja repondue une fois

Georges a demande pourquoi il avait 121 articles quand le site de reference en
comptait 619. Le compte honnete, verifie:

```
Catalogue de reference recolte    619
Retenus par les planificateurs    158
Repeches au second tri             18  (sur 461 ecartes: 38 candidats, 20 deja couverts)
Ecartes comme remplissage         443  (deco, jardinage, voyage, idees-cadeaux)
------------------------------------------------------
Plafond reel de ce catalogue      environ 245 articles francais
```

J ai surestime ce plafond deux fois de suite avant de faire le tri reel: d abord
« 100 a 150 repechables », puis « 330 a 380 au total ». Le tri a tranche a 18 et
245. Si la question revient, donnez ces chiffres-la.

Pour depasser 245, il faut une autre source de sujets que le site de reference:
les questions reellement tapees par ses clients, la Search Console du site, ou
les echeances reglementaires de 2027 et 2028 que personne n a encore ecrites
(carnet d entretien et etude du fonds de prevoyance au 15 aout 2028, certificat
RBQ d inspecteur au 1er octobre 2027, conformite des piscines au
30 septembre 2027).
