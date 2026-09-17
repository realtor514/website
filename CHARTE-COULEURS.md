# Charte de couleurs RE/MAX DU CARTIER

Référence unique du projet. Tout visuel fabriqué ici, carrousel, reel, story,
bannière, publication VENDU, prend ses couleurs dans cette liste et nulle part
ailleurs.

## Les cinq couleurs

| Couleur | Hex | RGB | Rang |
|---------|-----|-----|------|
| Navy | `#000E35` | `(0, 14, 53)` | **principale** |
| Crème | `#F7F5EE` | `(247, 245, 238)` | **principale** |
| Bleu | `#0043FF` | `(0, 67, 255)` | secondaire |
| Bordeaux | `#600000` | `(96, 0, 0)` | secondaire |
| Rouge | `#FF1200` | `(255, 18, 0)` | secondaire |

## La hiérarchie, qui compte autant que les valeurs

1. **Les grands aplats sont navy et crème.** Fonds, en-têtes, pieds de page,
   cartes de contact: les deux principales portent la surface.
2. **Les secondaires accentuent.** Un filet, une pastille, un mot, un bandeau.
   Elles ne couvrent pas le tiers d'une image, sauf décision assumée.
3. **Le texte sur fond sombre est crème `#F7F5EE`, pas blanc pur.** Le blanc
   n'est pas dans la charte. Il reste toléré là où le logo blanc l'impose.
4. **Une seule entorse en vigueur:** le bandeau VENDU | SOLD des publications
   du dossier `carrousel-instagram/vendu/` est un aplat rouge pleine largeur.
   C'est lui qui dit VENDU, il doit se lire dans une vignette de fil.

Le bleu `#0043FF` et le rouge `#FF1200` sont exactement les couleurs du ballon
dans `static/images/remax-logo.png`, échantillonnées au pixel près. Le navy
`#000E35` est le fondé du même fichier.

## Les polices

Playfair Display pour les titres et les noms, Inter pour tout le reste. Les
deux fichiers sont dans `carrousel-instagram/fonts/`, et le site charge les
mêmes familles.

## Où les couleurs vivent dans le code

Chaque générateur déclare ses constantes en haut de son fichier. État au
2026-09-17:

| Fichier | Navy | Rouge | Bleu | Crème |
|---------|------|-------|------|-------|
| `carrousel-instagram/vendu/generer-post-vendu.py` | conforme | conforme | conforme | conforme |
| `reels/moteur.py` | conforme | `#E61405` | absent | `#FAF9F7` |
| `carrousel-instagram/generer-carrousel.py` | conforme | `#E61405`, et `RED_PURE` conforme | `#0037D6` | `#FAF9F7` |
| `carrousel-instagram/35 terrasse jacques leonard/generer-carrousel.py` | conforme | `#E61405` | `#0037D6` | `#FAF9F7` |
| `carrousel-instagram/4071 rang saint-hyacinthe mirabel/generer-carrousel.py` | conforme | `#E61405` | `#0037D6` | `#FAF9F7` |
| `PAC stories/generer-stories.py` | conforme | `#E61405` | absent | `#FAF9F7` |
| `facebook/generer-couverture.py` | conforme | `#E61405` | `#0037D6` | absent |
| `static/css/main.css` | `#0a1628` | `#B00000` | conforme | `#F7F5EE` |

Le navy et le crème du site, `#0a1628` et `#F7F5EE`, sont l'un très proche et
l'autre identique à la charte. Les écarts réels sont le rouge et le bleu: les
générateurs utilisent un rouge légèrement plus sombre `#E61405` et un bleu
plus sombre `#0037D6`, hérités du one pager RE/MAX avant que la charte ne soit
connue. Le site, lui, utilise un rouge `#B00000` qui n'est dans la charte ni
comme rouge ni comme bordeaux.

**Aligner ces fichiers change l'apparence de visuels déjà publiés.** C'est une
décision à prendre, pas une correction à faire en passant. Tant qu'elle n'est
pas prise, ce tableau dit la vérité plutôt que de la cacher.

## Rappel dans les dossiers

Chaque dossier qui fabrique ou range un visuel contient un `COULEURS.md` avec
les cinq valeurs et un renvoi ici. Si la charte change, ce fichier fait foi, et
`grep -rl "000E35" --include=COULEURS.md .` retrouve toutes les copies à
mettre à jour.
