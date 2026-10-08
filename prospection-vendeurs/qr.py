"""Codes QR des campagnes vendeurs, aux couleurs de la charte.

Usage:  python prospection-vendeurs/qr.py vendu-28-st-hilaire

Produit un PNG par langue dans prospection-vendeurs/qr/. Chaque code mene au
formulaire deja ouvert sur Evaluation, avec des utm que le formulaire recopie
dans le courriel recu: le champ "campagne" dit de quelle lettre vient le lead,
et c est ce qui permet de savoir si une campagne a rapporte quelque chose.
"""
import pathlib
import sys

import segno

NAVY = "#000E35"   # charte, principale
CREME = "#F7F5EE"  # charte, principale

FORMULAIRES = {
    "fr": "/formulaire/",
    "en": "/en/form/",
    "es": "/es/formulario/",
    "ar": "/ar/istimara/",
}


def adresse(langue, campagne):
    return (
        f"https://georgesmatar.ca{FORMULAIRES[langue]}?intention=evaluation"
        f"&utm_source=lettre&utm_medium=imprime&utm_campaign={campagne}"
    )


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    campagne = sys.argv[1]
    sortie = pathlib.Path(__file__).parent / "qr"
    sortie.mkdir(exist_ok=True)
    for langue in FORMULAIRES:
        url = adresse(langue, campagne)
        # Correction M: tient une petite tache d encre sans grossir le code.
        # 16 px par module donne environ 3 cm nets a 300 ppp.
        code = segno.make(url, error="m")
        fichier = sortie / f"qr-{campagne}-{langue}.png"
        code.save(fichier, scale=16, border=4, dark=NAVY, light=CREME)
        print(fichier.name, url)


if __name__ == "__main__":
    main()
