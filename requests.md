# Requests

Ce fichier sert à gérer les éléments cachés et les demandes rapides.
Pour réactiver des éléments cachés, écrivez simplement : **"unhide mes inscriptions"**

---

## Items hidden

### Inscriptions (Listings)

Caché le : 2026-05-22
Commande pour restaurer : `unhide mes inscriptions`

#### Ce qui est caché et où

| Élément | Fichier | Comment restaurer |
|---------|---------|-------------------|
| Section "Inscriptions actuelles / Featured Properties" (page d'accueil) | `layouts/index.html` | Retirer `{{/*` et `*/}}` autour du bloc `<!-- Featured listings -->` |
| Section "Propriétés disponibles / Available Properties" (guide acheteur) | `layouts/buyer/single.html` | Retirer `{{/*` et `*/}}` autour du bloc `<!-- ── FEATURED LISTINGS ── -->` |
| Lien "Propriétés / Properties" dans le pied de page | `layouts/partials/footer.html` | Retirer le commentaire Hugo autour du `<li>` avec `/listings/` |

#### Menu "Trouver une propriété" — redirigé (pas caché)

Le menu pointe maintenant vers le formulaire de contact au lieu des inscriptions.
Pour restaurer les liens vers `/listings/`, changer dans `hugo.toml` :

| Langue | Identifier | URL actuelle | URL originale |
|--------|-----------|--------------|---------------|
| FR | `buyer-props` | `/#contact` | `/listings/` |
| EN | `buyer-props` | `/en/#contact` | `/en/listings/` |
| ES | `buyer-props` | `/es/#contact` | `/es/listings/` |
| AR | `buyer-props` | `/ar/#contact` | `/ar/listings/` |

#### Fichiers de contenu (intacts, non modifiés)

Les dossiers et fichiers suivants existent toujours et sont prêts à recevoir des inscriptions :

- `content/fr/listings/_index.md`
- `content/en/listings/_index.md`
- `content/es/listings/_index.md`
- `content/ar/listings/_index.md`
- `layouts/listings/list.html` — page liste des inscriptions
- `layouts/listings/single.html` — page détail d'une inscription
- `layouts/partials/listing-card.html` — composant carte d'inscription

---
