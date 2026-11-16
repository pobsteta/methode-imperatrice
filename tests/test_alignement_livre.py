#!/usr/bin/env python3
"""Le plugin dit-il ce que dit le livre imprimé ? Test léger, par marqueurs.

    python3 tests/test_alignement_livre.py

Référence : *La méthode de l'Impératrice — Emmener le bureau en forêt*, livre imprimé
(PDF KDP du 7 novembre 2026), Boîte à outils p. 207-286 (version 1.0.0 ; jusqu'à la 0.8.0,
PDF du 20 octobre, p. 203-275). Pour chaque fichier, les
formules que le livre a fixées doivent s'y trouver, et celles qu'il a abandonnées ne
doivent plus y être. Chaque mission d'alignement ajoute ses marqueurs ici ; ceux de la
mission 011 (v0.3.0) viennent du brief au livre (`docs/livre/`), en attendant l'impression.
"""
import os
import sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# fichier → (marqueurs présents, marqueurs absents, fiche du livre)
MARQUEURS = {
    "skills/methode/SKILL.md": (
        ["livre imprimé", "huit points", "**É**quipe", "**Ma réponse d'abord**",
         "**Journal**", "périmètres disjoints", "est interdit se câble",
         "l'interdit écrit au crayon", "la donnée sans question",
         "**Prendre la main**", "**Donner la main**", "**Rendre la main**",
         "Trois oui : rendre la main", "**Ne pas rendre la main**",
         "jamais au pivot", "ce n'est pas à elle de la", "ne se défait pas",
         "## Le degré de la main", "**Partage d'intention**", "**Sollicitation d'avis**",
         "**Le chef tranche**", "Lancer petit", "Le minimum se décide sur Polos",
         "Vers le mieux, pas vers le", "PDF KDP du 7 novembre 2026",
         "**A**nticiper", "prêt à le payer", "si je tiens, qui paie ?",
         "si je plie, qui paie ?", "Croire que libre veut dire éternel",
         "## La délégation", "seulement s'il le demande", "Ce qui ne se délègue pas",
         "Révocable à tout moment", "· délégation · portée :"],
        ["premier jet", "cinq points", "nticipateur", "proposition à valider",
         "Libre ne veut pas dire éternel", "sept points", "on lâche", "**Tenir**",
         "**Appuyer**", "**Lâcher**", "ne pas lâcher", "p. 203-275"],
        "fiches 1, 4, 9, 11, 12, 14, 15, ENSEMBLE (mission 001 ; 1.0.0)",
    ),
    "skills/mission/SKILL.md": (
        ["huit points", "**prendre la main**", "**donner la main**", "**ne pas rendre la main**",
         "degré de la main", "périmètre"],
        ["cinq points", "sept points", "*lâcher*", "**appuyer**", "**tenir**"],
        "fiches 1, 9 et 15 (mission 001 ; 1.0.0)",
    ),
    "agents/dev.md": (
        ["si je tiens, qui paie ?", "si je plie, qui paie ?", "« Peut (périmètre) »"],
        ["on ne lâche pas"],
        "fiches 1, 14 et 15 (mission 001 ; 1.0.0)",
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
        ["**Ma réponse d'abord**", "avant de lancer le `contradicteur`",
         "Qu'attends-tu de ce projet, et pourquoi ?", "au plus quatre questions par tour",
         "proposer, puis ajuster", "**proposition de Claude**",
         "Tu ne proposes aucun chiffre sans source", "« Est-ce bien ce que tu as retenu ? »"],
        [],
        "fiche 15 (mission 002, version 0.7.0)",
    ),
    "skills/demarrer/gabarit-brief.md": (
        ["## Ma réponse d'abord", "1. ma réponse d'abord, dans les mots de Pascal"],
        [],
        "fiche 15 (mission 002, version 0.7.0)",
    ),
    "skills/mission/fiche-mission.md": (
        ["## Ma réponse d'abord", "**Critère d'arrêt de la relecture :**",
         "3 allers-retours", "**Temps de la main :** prendre / donner / rendre",
         "**Degré de la main :**", "## Journal", "**Peut (périmètre) :**",
         "**Câblé (ne peut pas) :**", "le moment où Pascal leur pose le fait"],
        ["**Temps de la main :** tenir / appuyer / lâcher"],
        "fiches 1, 9 et 15 (missions 002 et 003 ; 1.0.0)",
    ),
    "skills/boucle/SKILL.md": (
        ["Critère d'arrêt de la relecture", "4e « à reprendre »", "remonte à Pascal",
         "cartes immobiles", "depuis deux cycles",
         "qu'avons-nous vu que nous n'attendions pas ?", "`écart`",
         "Quelle livraison proposons-nous, différente de la précédente, et pour qui ?",
         "dernière livraison inscrite au kanban", "rubrique « Livraisons » du kanban",
         "même quand le plafond l'a arrêtée", "une mauvaise nouvelle est une livraison sur laquelle on apprend",
         "**Un\n   périmètre par agent**", "**Lance petit**", "hors livre",
         "elle ne se défait pas"],
        ["rien de neuf", "explicitement « lâchées »", "en attendant le livre"],
        "fiches 3, 8, 12 et 15 (missions 003, 004, 010 et 011 ; 1.0.0)",
    ),
    "skills/demarrer/gabarit-kanban.md": (
        ["quoi, quand, combien", "comment, où, avec qui", "depuis le cycle",
         "## Livraisons", "ce qu'elle apporte de plus que la précédente",
         "une mauvaise nouvelle est une livraison sur laquelle on apprend", "ce qu'elle nous apprend",
         "On lance petit"],
        ["comment, avec quoi", "(quoi, quand)", "rien de neuf"],
        "fiches 8 et 12 (missions 004 et 011 ; 1.0.0)",
    ),
    "skills/bilan/SKILL.md": (
        ["quatre questions", "Nos changements de cap", "décidé, expliqué, appuyé sur un fait",
         "`écart`", "`cap`",
         "Quelle livraison proposons-nous, différente de la précédente, et pour qui ?",
         "rubrique « Livraisons » du kanban",
         "Qu'est-ce que l'IA m'a\n   fait gagner, et à quoi ai-je consacré ce temps ?",
         "**Vers le mieux, pas vers le\n   plus**", "un MVP"],
        ["trois questions", "d'*appuyer* à *lâcher*", "en attendant le livre"],
        "fiches 3, 12, 13 et 15 (missions 005, 010 et 011 ; 1.0.0)",
    ),
    "skills/demarrer/gabarit-journal.md": (
        ["· écart ·", "attendu :", "vu :", "vérifié :", "décision :",
         "garder", "creuser", "abandonner", "· cap ·",
         "on ne sanctionne pas un écart signalé"],
        [],
        "fiches 3 et 13 (mission 010)",
    ),
    "agents/analyste.md": (
        ["`écart`", "`cap`", "Moyens financiers, Mesure, Management"],
        [],
        "fiches 3, 6 et 13 (mission 010 ; 1.0.0)",
    ),
    "agents/acquereur.md": (
        ["**donnée sans question**"],
        [],
        "fiche 15 (1.0.0)",
    ),
    "agents/relecteur.md#perimetre": (
        ["« Peut (périmètre) »"],
        [],
        "fiche 15 (1.0.0)",
    ),
    "skills/demarrer/gabarit-equipe.md": (
        ["## Délégation", "Vide : aucune délégation, Pascal tranche tout.",
         "rendre la main ; ce qui touche l'extérieur et ne se défait pas"],
        [],
        "délégation (hors livre, demandée par Pascal le 2026-11-16, version 0.8.0)",
    ),
    "skills/demarrer/gabarit-claude.md": (
        ["**L'IA propose, Pascal tranche et assume.**", "**délégation**", "jamais au pivot"],
        [],
        "délégation (hors livre, version 0.8.0)",
    ),
    "skills/brief/adr-france.md": (
        ["Prêts à payer ?", "**A**nticiper"],
        ["nticipateur"],
        "fiche 4 (mission 005)",
    ),
}


def main():
    echecs = 0
    for fichier, (presents, absents, fiche) in MARQUEURS.items():
        with open(os.path.join(RACINE, fichier.split("#")[0]), encoding="utf-8") as f:
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
