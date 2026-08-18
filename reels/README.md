# Reels Instagram

Une video verticale par inscription, fabriquee a partir des memes photos que
les carrousels. Format 1080 x 1920 (9:16), 30 images par seconde, environ 32
secondes, H.264. C est le format que Instagram etire en plein ecran et que
l algorithme pousse le plus.

| Inscription | Dossier | Duree |
|-------------|---------|-------|
| 28, rue St-Hilaire, Longueuil (Centris 26368231) | `28-rue-st-hilaire-longueuil/` | 31,8 s |
| 35, terrasse Jacques-Leonard, Montreal (Centris 15815581) | `35-terrasse-jacques-leonard/` | 31,8 s |
| 4071, rang Saint-Hyacinthe, Mirabel (Centris 26269222) | `4071-rang-saint-hyacinthe-mirabel/` | 31,8 s |

Chaque dossier contient `reel.mp4` et `couverture.jpg`, l image a choisir
comme couverture au moment de publier.

## Le montage

Toujours le meme, parce qu il fonctionne:

1. **L accroche, 4,4 s.** La facade, un mouvement lent, et une phrase qui
   donne tout de suite la raison de rester. Puis l adresse, le prix et le
   numero Centris. Les trois premieres secondes decident du reste.
2. **La visite, 9 plans de 2,4 s.** Une piece par plan, nommee en bas de
   l ecran. Le rythme est volontairement soutenu: un plan qui dure fait
   decrocher.
3. **Les points forts, 4,8 s.** Ce qui est deja fait, ou ce qui vient avec la
   propriete, en lignes qui arrivent une a une.
4. **Le contact, 5 s.** Les deux courtiers, le telephone, l appel a l action.

## Les mouvements

Les photos sont fixes. Tout le mouvement vient du cadre 9:16 qui se deplace
dans la photo, image par image:

| Mouvement | Effet |
|-----------|-------|
| `zoom` | on se rapproche lentement |
| `recul` | on s eloigne, la piece s ouvre |
| `droite`, `gauche` | panoramique, comme une camera sur rail |
| `descente`, `montee` | balayage vertical |
| `arc`, `arc_inverse` | zoom plus une bascule de perspective: la sensation d un drone qui contourne le sujet |

Le parametre `fx` d un plan est le point d interet: c est autour de lui que le
mouvement se joue, et c est la que le panoramique arrive. Pour le plan du
poele a combustion lente, `fx=0.36` amene le cadre sur le poele, qui se
trouve dans le tiers gauche de la photo.

Deux mises en page cohabitent. En **plein ecran**, la photo remplit l image:
c est cinematographique, mais le 9:16 coupe une photo horizontale des deux
cotes. En **cadre**, la photo garde sa largeur entiere au centre, sur un fond
flou tire d elle-meme; rien n est coupe et l image reste nette. Le cadre est
reserve aux vues larges, la grange, le terrain, le parc, ou couper serait
dommage. Le fond bouge un peu plus vite que la photo: c est ce decalage qui
donne la profondeur.

## Le son

Aucune musique n est incluse, seulement une piste muette pour que le fichier
soit accepte partout. **La musique se choisit dans Instagram, au montage.**
Un son tendance pris dans la bibliotheque de l application vaut beaucoup plus
de portee qu une musique importee avec le fichier: c est un des rares leviers
gratuits qui change vraiment la diffusion.

## Regenerer

```
python reels/generer-reels.py              les trois
python reels/generer-reels.py mirabel      un seul, par bout de nom
```

Environ 90 secondes par reel. Le script lit les photos dans
`carrousel-instagram/sources/` et, pour le 28 rue St-Hilaire, dans
`static/images/listings/28-rue-st-hilaire-longueuil/`.

Tout se regle en haut de `generer-reels.py`: les textes, les photos, l ordre
des plans, les mouvements et les durees. `moteur.py` n a pas besoin d etre
touche pour ajouter une propriete.

Pour une nouvelle inscription: copier un bloc de `PROPRIETES`, changer les
photos et les textes. Un plan est un tuple
`(photo, sur-titre, titre, mouvement, fx, fy)`.

Les `reel.mp4` ne sont pas suivis par Git: une video de 20 Mo par version
alourdirait le depot pour toujours, et le fichier se refabrique en 90
secondes. Les couvertures, elles, sont suivies.

## Legende du reel: 28, rue St-Hilaire

```
28, rue St-Hilaire, Vieux-Longueuil. 499 000 $

Toiture, plomberie et entrée électrique refaites en 2014. Plancher du rez-de-chaussée sablé en 2026. Piscine hors terre 2023 et borne de recharge pour voiture électrique.

3 chambres, sous-sol aménagé avec salle de bain, véranda et grande terrasse en bois, sur un terrain clôturé de près de 4 000 pi2.

Épiceries, parcs, écoles et services à distance de marche.

Écrivez-moi pour une visite.

Centris 26368231

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC., avec l'Équipe Pistoli
438 372-0102
```

```
#vieuxlongueuil #longueuil #rivesud #montreal #maisonavendre #avendre
#immobilierquebec #courtierimmobilier #remax #remaxducartier #centris
#visiteguidee #maisonquebec #premiereMaison
```

## Legende du reel: 35, terrasse Jacques-Leonard

```
35, terrasse Jacques-Léonard, Rivière-des-Prairies. 380 000 $

Une maison de ville sur trois niveaux au Domaine Bonneville, une enclave de 250 maisons dans un site paysager mature.

Piscine, pataugeoire, parc privé, aire de jeux et centre communautaire réservés aux résidents.

4 chambres dont 1 au sous-sol, 2 salles de bain et 1 salle d'eau, sous-sol complet avec cuisine et salon, garage au sous-sol, cour arrière clôturée avec terrasse couverte.

Les charges communes couvrent l'assurance, la toiture, la maçonnerie, les balcons, le déneigement et le fonds de prévoyance.

Écrivez-moi pour une visite.

Centris 15815581

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC., avec l'Équipe Pistoli
438 372-0102
```

```
#rivieredesprairies #rdp #pointeauxtrembles #montrealest #montreal
#maisonavendre #avendre #maisondeville #immobilierquebec #courtierimmobilier
#remax #remaxducartier #centris #visiteguidee #domainebonneville
```

## Legende du reel: 4071, rang Saint-Hyacinthe

```
4071, rang Saint-Hyacinthe, Saint-Hermas, Mirabel. 449 000 $

22 152 pi2 de terrain en bordure des champs, une grange de bois sur deux étages, et pas un voisin en face.

Maison de 1935, dans la même famille depuis 1990. 4 chambres, 2 salles de bain, deux cuisines, un poêle à combustion lente et une vaste galerie face aux champs.

Revêtement de vinyle refait en 2024, thermopompe centrale de 2022, génératrice neuve installée en 2025, panneau électrique de 200 ampères.

Vendue sans garantie légale de qualité, aux risques et périls de l'acheteur. Déclarations du vendeur et rapport d'inspection de février 2026 disponibles.

Écrivez-moi pour une visite.

Centris 26269222

Georges Matar, courtier immobilier résidentiel
RE/MAX DU CARTIER INC., avec l'Équipe Pistoli
438 372-0102
```

```
#mirabel #sainthermas #saintbenoit #laurentides #maisonavendre #avendre
#maisondecampagne #fermette #grange #terrain #immobilierquebec
#courtierimmobilier #remax #remaxducartier #centris #visiteguidee
```

## Avant de publier

- Publier en **reel**, pas en publication simple: c est le reel qui sort du
  cercle des abonnes.
- Ajouter un son tendance dans l application, avant de publier.
- Choisir `couverture.jpg` comme couverture, pour que la grille du profil
  reste coherente avec les carrousels.
- Mettre le lien vers la fiche Centris en premier commentaire. Instagram ne
  rend pas les liens cliquables dans la legende.
- Identifier @ l Equipe Pistoli et Rovena Pistoli.
- Le meme fichier sert de story et peut etre publie sur Facebook et sur
  YouTube Shorts sans retouche: le format 9:16 et la zone de texte sont
  compatibles avec les trois.
