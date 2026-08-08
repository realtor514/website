# Facebook

## Photo de couverture

| Fichier | Format | Usage |
|---------|--------|-------|
| `couverture-facebook.png` | 1640 x 624 px | A televerser sur Facebook, texte le plus net |
| `couverture-facebook.jpg` | 1640 x 624 px | Meme image, fichier plus leger si besoin |

Facebook affiche la couverture en 820 x 312 px sur ordinateur. Le fichier
fait le double pour rester net sur les ecrans haute densite. Le meme fichier
convient aussi a la couverture d un profil personnel (851 x 315 px):
Facebook le redimensionne sans couper de texte.

### Zones respectees

Deux elements viennent recouvrir la couverture, la mise en page les evite:

- **Photo de profil**: cercle en bas a gauche. Rien d important a gauche de
  x = 400 ni dans le coin inferieur gauche. Le degrade seul occupe cette zone.
- **Recadrage telephone**: Facebook rogne les cotes sur mobile. Tout le texte
  reste entre x = 452 et x = 1000, donc toujours visible.

### Contenu

Logo RE/MAX DU CARTIER, nom, titre, telephone, site web et courriel.
Portrait detoure a droite, sur le navy de la charte. Polices Playfair
Display et Inter, les memes que le site.

### Regenerer

```
python facebook/generer-couverture.py
```

Le script lit le portrait `static/images/georges-matar-3.png` et le logo
blanc `static/images/remax-ducartier-blanc.png`. Pour changer un texte,
modifier la fonction `couverture()`.

### A verifier apres le televersement

Facebook permet de repositionner l image apres l envoi. Verifier sur
ordinateur et sur telephone que le nom et le telephone restent lisibles,
et recentrer au besoin.
