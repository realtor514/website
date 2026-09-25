# Consigne commune aux redacteurs

Vous redigez UN article de blogue en francais du Quebec pour georgesmatar.ca,
courtier immobilier residentiel a Laval. Votre consigne d agent vous donne
votre `id` de sujet, votre slug et votre date. Tout le reste est ici.

## 1. Lecture obligatoire avant d ecrire une ligne

- `CLAUDE.md`, la loi du projet. Regle 1: zero tiret long, em dash, en dash ou
  double tiret, nulle part, front matter et tableaux compris.
- `state/BRIEF.md` EN ENTIER: style, voix, structure, front matter, livrables.
- `state/internal_links_fr.md`: la seule source de chemins internes valides.
- Un article existant pour la voix, par exemple
  `content/fr/articles/renovations-dont-add-value.md`.

## 2. Votre sujet

La ligne dont l `id` vous est donne, dans `state/content_plan.json`, tableau
`topics`. Lisez-la en entier: elle contient le sujet, la categorie, le mot-cle
cible, l angle unique et les H2 prevus.

Les H2 prevus sont une proposition. Vous pouvez les reformuler ou les reordonner
si la recherche l exige, mais vous couvrez l angle unique.

**Si la ligne porte un champ `distinct_de`, lisez l article nomme avant
d ecrire** et assurez-vous que votre texte ne le repete pas.

## 3. La recherche est le coeur du travail

Chaque chiffre, loi, article de code, delai, tarif, programme ou obligation doit
venir d une source primaire que vous avez reellement ouverte pendant la
redaction. Minimum 5 sources, chacune rattachee a une affirmation precise.

**Si vous ne trouvez pas la source, retirez l affirmation.** Ne reproduisez
jamais un chiffre de memoire. Un article qui dit « aucune source officielle ne
chiffre ceci » est meilleur qu un article qui invente le chiffre: c est
exactement la voix du site.

Sources primaires acceptees: OACIQ, Code civil du Quebec
(legisquebec.gouv.qc.ca), Educaloi, APCIQ, Statistique Canada, Banque du Canada,
SCHL, Revenu Quebec, Agence du revenu du Canada, Tribunal administratif du
logement, Tribunal administratif du Quebec, Regie du batiment du Quebec,
Garantie de construction residentielle, ministeres du Quebec, Ville de Montreal,
Ville de Laval, Hydro-Quebec, Bureau d assurance du Canada, Autorite des marches
financiers, Registre foncier, Ordre des evaluateurs agrees, Ordre des
arpenteurs-geometres, Commission municipale.

Un blogue de courtier, un site de fabricant, un blogue d avocat ou un
agregateur n est **jamais** une source primaire. Ils peuvent au mieux vous
indiquer quel document officiel aller chercher.

## 4. Sites qui bloquent, et comment passer

Plusieurs sites officiels quebecois refusent WebFetch. Utilisez `curl` via Bash
avec un agent de navigateur:

```
curl -sL --max-time 30 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36" "<url>" | head -c 6000
```

Etat observe le 25 septembre 2026, a reverifier vous-meme:

| Site | Comportement | Ce qui marche |
|---|---|---|
| legisquebec.gouv.qc.ca | 502 du serveur d origine | rien; utilisez Educaloi et l OACIQ, et dites d ou vient la regle |
| hydroquebec.com | **geo-bloque**. Repond 200, mais tout acces hors Quebec est redirige vers une page « Indisponibilite du site Web d Hydro-Quebec a partir de l etranger ». Un code 200 ne veut donc pas dire que vous lisez la bonne page: verifiez le titre. | les captures web.archive.org des pages officielles |
| revenuquebec.ca | 403 a WebFetch et a curl | le recueil des depenses fiscales sur budget.finances.gouv.qc.ca |
| quebec.ca | verification humaine puis 405 | les PDF sur cdn-contenu.quebec.ca, et les sites des ministeres directement |
| laval.ca | bloque WebFetch, mais **repond 200 en curl avec un agent de navigateur** | curl, le HTML suffit, pas besoin des PDF |
| montreal.ca | 404 sur beaucoup d URL de sujet | le contenu vit souvent sur un sous-domaine, par exemple sim.montreal.ca pour la securite incendie, dont les pages francaises sont a la racine sans prefixe /fr |
| rbq.gouv.qc.ca | 404 sur les URL francaises devinees | passez par le lien « Fr » depuis la page anglaise |
| lautorite.qc.ca | 403 a WebFetch et a curl | capture web.archive.org |
| securitepublique.gouv.qc.ca | 405 | les PDF sur cdn-contenu.quebec.ca |
| justice.gouv.qc.ca | defi Cloudflare | Educaloi pour les paliers des tribunaux |
| canlii.org et ccq.lexum.com | 403, et Lexum est une coquille JavaScript sans texte | rien, aucune route connue vers le Code civil |

**Essayez plusieurs routes avant d abandonner une affirmation:** le PDF plutot
que la page HTML, le site du ministere plutot que quebec.ca, une capture de
web.archive.org de la page officielle, un autre hote du meme organisme. Une
capture d archive de la page officielle reste la page officielle: citez l URL
canonique et dites dans le JSON que vous l avez lue par archive.

Si apres plusieurs routes le fait reste invérifiable, retirez-le et notez-le
dans `claims_needing_review`.

## 5. Les livrables, exactement deux fichiers

1. `drafts/fr/<SLUG>.md`, le front matter puis l article. Pas de titre H1 dans
   le corps, pas de note de redaction.
2. `meta/fr/<SLUG>.json`.

Le schema exact des deux est dans `state/BRIEF.md`, sections 9 et 10.
`draft: true` est obligatoire.

## 6. Verifications avant de rendre

```
python tools/dedupe.py check drafts/fr/<SLUG>.md
python tools/validate.py drafts/fr/<SLUG>.md
```

Attention: `dedupe.py` attend la sous-commande `check`, pas `--check`. Avec
`--check` il affiche l aide et sort en 0, ce qui ressemble a un succes.

Les deux doivent passer sans erreur. Si dedupe signale un FAIL de sujet ou de
contenu, recentrez sur l angle unique au lieu de reecrire le meme texte.

## 7. Rappels qui ont deja fait rejeter des textes ici

- **Zero tiret long**, nulle part.
- Georges sert en **francais, anglais et arabe**. Ne promettez jamais un service
  en espagnol.
- **`/secteurs/...` n existe pas.** Les pages de ville vivent sous
  `/courtier-immobilier/laval/`, `/courtier-immobilier/montreal/`.
- Un lien vers un article inexistant ou encore en brouillon fait rejeter le
  texte. Copiez les chemins depuis `state/internal_links_fr.md` uniquement.
- Aucune promesse de prix, de delai, de rendement, ni de pourcentage de
  plus-value sans source.
- Aucun conseil juridique, fiscal ou hypothecaire definitif: vous expliquez la
  regle et vous renvoyez au notaire, au comptable, au courtier hypothecaire ou
  a l assureur.
- Si une affirmation reste incertaine apres recherche, ajoutez
  `needs_expert_review: true` juste avant `draft: true`, et listez-la dans
  `claims_needing_review` du JSON.
- Ne modifiez jamais un fichier de `content/`. Vous n ecrivez que dans
  `drafts/fr/` et `meta/fr/`.

## 8. Rapport final

Court: le slug, le nombre de mots, le nombre de sources, toute affirmation que
vous avez retiree faute de source, et toute erreur que vous avez trouvee dans
votre propre ligne de plan.
