#!/usr/bin/env python3
"""Le plugin dit-il ce que dit le livre imprimé ? Test léger, par marqueurs.

    python3 tests/test_alignement_livre.py

Référence : *La méthode de l'Impératrice — Emmener le bureau en forêt*, livre imprimé
(PDF KDP du 20 octobre 2026), Boîte à outils p. 203-275. Pour chaque fichier, les
formules que le livre a fixées doivent s'y trouver, et celles qu'il a abandonnées ne
doivent plus y être. Chaque mission d'alignement de la v0.2.0 ajoute ses marqueurs ici.
"""
import os
import sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# fichier → (marqueurs présents, marqueurs absents, fiche du livre)
MARQUEURS = {
    "skills/methode/SKILL.md": (
        ["livre imprimé", "sept points", "**É**quipe", "**Ma réponse d'abord**",
         "**A**nticiper", "prêt à le payer", "si je tiens, qui paie ?",
         "si je plie, qui paie ?", "Croire que libre veut dire éternel"],
        ["premier jet", "cinq points", "Anticipateur", "proposition à valider",
         "Libre ne veut pas dire éternel"],
        "fiches 4, 11, 14, 15 (mission 001)",
    ),
    "skills/mission/SKILL.md": (
        ["sept points"],
        ["cinq points"],
        "fiche 15 (mission 001)",
    ),
    "agents/dev.md": (
        ["si je tiens, qui paie ?", "si je plie, qui paie ?"],
        [],
        "fiche 14 (mission 001)",
    ),
    "agents/archiviste.md": (
        ["Croire que libre veut dire éternel"],
        ["Libre ne veut pas dire éternel"],
        "fiche 11 (mission 001)",
    ),
    "agents/relecteur.md": (
        ["Croire que libre veut dire éternel"],
        ["Libre ne veut pas dire éternel"],
        "fiche 11 (mission 001)",
    ),
    "skills/brief/SKILL.md": (
        ["**Ma réponse d'abord**", "avant de lancer le `contradicteur`"],
        [],
        "fiche 15 (mission 002)",
    ),
    "skills/demarrer/gabarit-brief.md": (
        ["## Ma réponse d'abord"],
        [],
        "fiche 15 (mission 002)",
    ),
    "skills/mission/fiche-mission.md": (
        ["## Ma réponse d'abord", "**Critère d'arrêt de la relecture :**",
         "3 allers-retours"],
        [],
        "fiche 15 (missions 002 et 003)",
    ),
    "skills/boucle/SKILL.md": (
        ["Critère d'arrêt de la relecture", "4e « à reprendre »", "remonte à Pascal"],
        [],
        "fiche 15 (mission 003)",
    ),
}


def main():
    echecs = 0
    for fichier, (presents, absents, fiche) in MARQUEURS.items():
        with open(os.path.join(RACINE, fichier), encoding="utf-8") as f:
            texte = f.read()
        for m in presents:
            juste = m in texte
            print(("ok   " if juste else "ÉCHEC"), f"{fichier} contient « {m} » ({fiche})")
            echecs += not juste
        for m in absents:
            juste = m not in texte
            print(("ok   " if juste else "ÉCHEC"), f"{fichier} ne contient plus « {m} » ({fiche})")
            echecs += not juste
    sys.exit(1 if echecs else 0)


if __name__ == "__main__":
    main()
