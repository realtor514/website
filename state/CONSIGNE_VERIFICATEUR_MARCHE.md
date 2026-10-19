# Verification d un article de la serie « Marche immobilier par secteur »

Vous n avez pas ecrit cet article. Votre travail est de le prendre en defaut,
puis de le corriger. Lisez d abord `state/CONSIGNE_MARCHE_SECTEURS.md`, puis
`state/BRIEF.md` sections 3, 6 et 11.

## 1. Les chiffres, un par un

Pour chaque chiffre de l article:

1. Retrouvez-le dans `state/marche_T3_2026/centris_<region>.json` ou dans la
   source du JSON de meta qui le porte.
2. Verifiez le rattachement: bon quartier, bonne categorie (unifamiliale,
   copropriete, plex, total), bonne colonne (trimestre ou cumul de 4
   trimestres), bon signe de variation, variation en jours et non en
   pourcentage pour les jours sur le marche.
3. Rouvrez en direct la page Centris d au moins deux quartiers de l article,
   par curl avec agent de navigateur, et comparez chiffre a chiffre. Si la page
   differe du JSON, la page tranche.
4. Un `**` de Centris comble par un calcul, une moyenne ou une somme de prix
   medians: erreur, a retirer.

## 2. Les autres affirmations

Rouvrez chaque source non Centris du JSON de meta. Pour chaque affirmation
qu elle doit appuyer, trouvez la phrase de la page qui l appuie. Une
affirmation que la page n appuie pas est retiree ou reformulee pour dire
exactement ce que la page dit. Une source de seconde main (presse, blogue,
courtier, agregateur) est remplacee par la source officielle, ou
l affirmation part.

Attention aux dates: une nouvelle annoncee comme a venir est peut-etre deja
faite, ou reportee. Verifiez le statut au 19 octobre 2026.

## 3. La conformite

Section 7 de `state/CONSIGNE_MARCHE_SECTEURS.md`, mot par mot. Le `title`, le
`seo_title` et la `description` suivent la section 1 bis de la meme consigne:
ville dans les deux titres, longueurs, chiffres de la description presents dans
l article. Corrigez-les s ils s en ecartent. Plus: zero tiret
long, em dash, en dash ou double tiret, nulle part; aucun lien vers un autre
article de la serie; liens internes copies de `state/internal_links_fr.md`.

## 4. Corriger

Corrigez directement `drafts/fr/<SLUG>.md` et `meta/fr/<SLUG>.json`. Une
correction de chiffre se fait dans le texte ET dans le `supports` de la source.
Gardez la voix: phrases courtes, faits, pas d adjectifs. Si une correction fait
tomber l article sous 1 200 mots, completez avec un fait verifie, jamais avec du
remplissage.

Une affirmation qui reste incertaine apres recherche: retirez-la. Si elle est
indispensable, gardez-la, ajoutez `needs_expert_review: true` juste avant
`draft: true`, et inscrivez-la dans `claims_needing_review`.

Puis relancez:

```
python tools/dedupe.py check drafts/fr/<SLUG>.md
python tools/validate.py drafts/fr/<SLUG>.md
```

## 5. Si l article manque

Si `drafts/fr/<SLUG>.md` n existe pas, ou s il existe sans son JSON de meta,
le redacteur a cale. Si le `.md` existe sans le `.json`, le releve des sources
est perdu: rouvrez chaque source possible, reconstruisez le JSON, et retirez de
l article tout ce que vous ne retrouvez pas. Si rien n existe, ecrivez l article
vous-meme selon les consignes, puis verifiez-le comme ci-dessus.
