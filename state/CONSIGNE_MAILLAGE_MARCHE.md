# Maillage de la serie « Marche immobilier par secteur », apres publication

Les articles d une region sont publies sans lien entre eux, parce que le
validateur refuse un lien vers un brouillon. Une fois la region publiee, un
agent par langue ajoute les liens ci-dessous. Votre consigne d agent donne la
langue, la table des chemins et la liste des pages de quartier.

## 1. L article synthese vers les articles de secteur

Dans la section qui presente les secteurs par leur nom, faites de chaque nom
de secteur un lien vers son article, dans la meme langue, avec le chemin exact
de la table. Si la phrase ne s y prete pas, ajoutez une phrase courte par
secteur. Chaque article de secteur recoit exactement un lien depuis la
synthese.

## 2. Chaque article de secteur vers la synthese

Un seul lien, dans la ligne de fin « Pour compléter, lisez ... » (ou son
equivalent dans la langue), ou a defaut dans la phrase qui parle de la region.
Texte du lien descriptif, avec le nom de la ville, par exemple « le marché
immobilier de Laval, quartier par quartier ». Jamais « cliquez ici ».

## 3. Les pages de quartier et de ville vers l article de leur secteur

Pour chaque page listee dans votre consigne, ajoutez un court paragraphe de
une ou deux phrases qui renvoie a l article, place juste apres la premiere
section qui parle des prix ou du marche, sinon juste avant la section
« Vendre a ». Le texte du lien contient le quartier, la ville et le
trimestre, par exemple « le marché immobilier de Chomedey au 3e trimestre
2026 ». Mettez `lastmod` de la page a la date donnee dans votre consigne. Ne
touchez ni aux `facts`, ni a la `faq`, ni au reste du texte.

## 4. Regles

- Chemins exacts de la table, prefixe de langue compris. Verifiez que chaque
  fichier cible existe et n est pas en `draft: true`.
- En arabe, le texte est en arabe, les chemins restent en caracteres latins.
- `lastmod` des articles: inchange.
- Zero tiret long, em dash, en dash ou double tiret.
- Aucun autre fichier.
- Validez chaque article modifie: `python tools/validate.py <fichier>`, sans
  erreur.

## 5. Rapport

La liste des fichiers modifies et, pour chacun, le texte du lien ajoute.
