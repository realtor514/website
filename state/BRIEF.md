# Brief de redaction, blogue georgesmatar.ca

Ce fichier est la seule reference de style. Lisez-le en entier avant d ecrire.

## 1. Le client

Georges Matar, courtier immobilier residentiel, RE/MAX du Cartier.
Bureau: 2820, boul. Saint-Martin Est, bureau 201, Laval (Duvernay), Quebec.
Territoire: Laval, Montreal, Rive-Nord, Rive-Sud, Laurentides, Lanaudiere, Monteregie.
Services: achat, vente, evaluation gratuite, investissement (plex, immeubles a revenus),
accompagnement des nouveaux arrivants.
Langues de service: francais, anglais et arabe. **Ne promettez jamais un
service en espagnol.** Le site existe en espagnol, mais la fiche Centris de
Georges ne declare que trois langues, et il a retire cette promesse du site le
2026-09-25. Un courtier ne promet que ce qu il peut tenir.
Site: https://georgesmatar.ca

## 2. Ce que vous ecrivez

Un article de blogue en francais du Quebec, 1 200 a 1 800 mots, ancre sur le
Quebec, sur Montreal et sur Laval. Jamais un texte generique valable partout.

## 3. Regles absolues, aucune exception

1. **Zero tiret long.** Jamais de em dash, de en dash, ni de double tiret.
   Remplacez par une virgule, un deux-points ou un point. Cette regle vaut aussi
   dans le front matter, les titres et les tableaux. Un seul de ces caracteres
   fait rejeter l article.
2. **Rien d invente.** Chaque chiffre, loi, article de code, taux, delai ou
   programme doit venir d une source primaire que vous avez reellement consultee
   pendant la redaction. Si vous ne trouvez pas la source, retirez l affirmation.
   Ne reproduisez jamais un chiffre de memoire.
3. **Aucune promesse invérifiable.** Interdit: garantir un prix, un delai, un
   rendement, ou affirmer qu une caracteristique augmente la valeur d un
   pourcentage precis sans source. Le courtier est encadre par l OACIQ et doit
   pouvoir demontrer l exactitude de ce qu il avance.
4. **Jamais de conseil juridique, fiscal ou hypothecaire definitif.** Vous
   expliquez la regle et vous renvoyez au notaire, au comptable, au courtier
   hypothecaire ou a l assureur pour la decision.
5. **Aucune copie.** Vous n avez pas le droit de reprendre la structure ou les
   formulations d un article existant trouve en ligne. Vous construisez votre
   propre plan a partir des sources primaires.

## 4. Sources primaires acceptees

OACIQ (oaciq.com), Code civil du Quebec (legisquebec.gouv.qc.ca), Educaloi,
APCIQ (apciq.ca), Statistique Canada, Banque du Canada, SCHL, Revenu Quebec,
Agence du revenu du Canada, Tribunal administratif du logement, Tribunal
administratif du Quebec, Regie du batiment du Quebec, ministeres du Quebec,
Ville de Montreal, Ville de Laval, Hydro-Quebec, Bureau d assurance du Canada,
Autorite des marches financiers, Registre foncier, Commission municipale.

Un blogue concurrent, un site de courtier ou un agregateur ne sont jamais des
sources. Ils peuvent au mieux vous indiquer quoi aller verifier ailleurs.

## 5. Le ton

Vouvoiement. Professionnel, direct, chaleureux sans familiarite. Le lecteur est
adulte et pressé. Les phrases sont courtes. Le texte avance par faits verifiables,
pas par adjectifs.

Ce qui caracterise la voix du site, et que vous devez reproduire:

- On nomme la regle exacte: le numero d article, le nom du formulaire, le delai
  en jours. Exemple du site: « L article 1723 du Code civil est net. »
- On dit ce qu on ne sait pas. Exemple du site: « Aucune source officielle ne me
  permet de chiffrer l effet d une ecole sur le prix d une maison. »
- On corrige une croyance repandue, avec la donnee qui la corrige.
- On explique la consequence pratique pour le lecteur, pas la theorie.
- Le « je » du courtier apparait une ou deux fois au maximum, jamais en ouverture.

A proscrire: le ton publicitaire, les superlatifs, « dans le monde d aujourd hui »,
« il est important de noter », les listes de conseils sans chiffres, l intelligence
artificielle qui s excuse, les emojis.

## 6. Structure imposee

1. **Titre H1**: absent du corps. Il vit dans le front matter, moins de 60
   caracteres si possible, et contient le mot-cle cible.
2. **Accroche**: 2 a 4 phrases, sans titre. Elle pose le probleme concret et
   annonce ce que l article regle. Jamais « Dans cet article, nous allons voir ».
3. **6 a 8 sections H2**, dans l ordre logique de la decision du lecteur.
   Le mot-cle cible et ses variantes naturelles apparaissent dans 2 a 3 H2,
   jamais dans tous.
4. **H3 seulement quand une section a de vraies sous-parties.**
5. **Un tableau markdown** quand les donnees s y pretent (couts, delais, durees
   de vie, comparaison). Le site en utilise beaucoup. Format simple, colonnes
   courtes.
6. **Passages en gras** pour ouvrir un paragraphe cle, comme dans les articles
   existants: `**Le reservoir d huile.** Le texte suit.`
7. **Section « Questions frequentes »** en H2 vers la fin: 3 a 5 questions en
   gras suivies d une reponse de 2 a 4 phrases. Questions reellement tapees par
   un client, pas des questions de vitrine.
8. **Fin d article**, exactement dans ce format, comme sur le site:

```
Pour completer, lisez [texte](/articles/slug-existant/) et [texte](/articles/autre-slug/).

---

*Phrase d invitation liee au sujet? [Ecrivez-moi](/formulaire/). Precision sur le service.*
```

## 7. Les deux appels a l action

- **Au milieu de l article**, une fois: un lien naturel vers un calculateur ou
  une page de service qui sert vraiment le paragraphe ou il se trouve. Jamais un
  encadre publicitaire.
- **A la fin**, le bloc en italique vers `/formulaire/` montre ci-dessus.

Cibles autorisees: `/formulaire/`, `/contact/`, `/tools/affordability/`,
`/tools/mortgage/`, `/tools/closing-costs/`, `/tools/home-estimate/`,
`/tools/rent-vs-buy/`, `/tools/welcome-tax/`, `/buyer/`, `/seller/`, `/about/`.

Les pages de ville vivent sous `/courtier-immobilier/laval/`,
`/courtier-immobilier/montreal/` et ainsi de suite. **`/secteurs/...` n existe
pas**, meme si l arborescence du depot le suggere: ces pages declarent leur
propre `url:` en front matter. La liste complete et verifiee est dans
`state/internal_links_fr.md`, refaite par `python tools/linkmap.py`.

## 8. Liens internes

3 a 5 liens vers des articles EXISTANTS, pris dans `state/internal_links_fr.md`.
Copiez le chemin exact. Un lien vers un article qui n existe pas fait rejeter
le texte. Le texte du lien est descriptif, jamais « cliquez ici ».

## 9. Front matter, schema exact du site

Copiez ce schema, dans cet ordre, sans ajouter ni retirer de champ:

```yaml
---
title: "Titre de l article"
date: 2026-09-23
lastmod: 2026-09-23
translationKey: "article-cle-fournie"
category: "Categorie fournie"
description: "Moins de 155 caracteres, avec le mot-cle, qui dit ce que le lecteur va obtenir."
image: "images/articles/SLUG/featured.jpg"
draft: true
---
```

- `date` et `lastmod`: la date du jour fournie dans votre consigne. Jamais une
  date future.
- `draft: true` est obligatoire et ne se retire jamais.
- `image`: gardez ce chemin meme si le fichier n existe pas encore. Remplacez
  SLUG par le slug fourni.
- Si votre consigne indique `needs_expert_review: true`, ajoutez cette ligne
  juste avant `draft: true`.
- Categories permises, telles quelles: `Guide de l'acheteur`, `Guide du vendeur`,
  `Financement`, `Investissement`, `Immobilier 101`, `Analyse de marche`,
  `Guide pratique`.

## 10. Ce que vous livrez

Deux fichiers, rien d autre.

**1. `drafts/fr/SLUG.md`**: le front matter puis l article. Pas de titre H1 dans
le corps. Pas de commentaire, pas de note de redaction.

**2. `meta/fr/SLUG.json`**:

```json
{
 "id": "tXX",
 "slug": "SLUG",
 "title": "...",
 "target_keyword": "...",
 "word_count": 1450,
 "category": "...",
 "internal_links": ["/articles/...", "/tools/..."],
 "sources": [
  {"url": "https://...", "title": "Nom exact de la page", "publisher": "OACIQ",
   "consulted": "2026-09-23", "supports": "Ce que cette source appuie dans l article"}
 ],
 "claims_needing_review": []
}
```

Au moins 5 sources, chacune reellement ouverte pendant la redaction, chacune
rattachee a une affirmation precise de l article.

## 11. Avant de rendre, verifiez vous-meme

- [ ] Aucun tiret long, en dash ou double tiret nulle part
- [ ] 1 200 a 1 800 mots dans le corps
- [ ] `description` sous 155 caracteres
- [ ] 6 a 8 H2, mot-cle present dans 2 a 3 d entre eux
- [ ] 3 a 5 liens internes, chemins copies depuis `internal_links_fr.md`
- [ ] Un CTA au milieu, le bloc `/formulaire/` a la fin
- [ ] Section Questions frequentes presente
- [ ] Chaque chiffre a sa source dans le JSON
- [ ] `draft: true` present
