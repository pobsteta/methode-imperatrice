# Mission 005 — les changements de cap au bilan, le prix dans l'ADR

> Fiche de mission (fiches n° 9 et 15). Brief : `docs/brief.md` (v0.2.0, validé par
> Pascal le 21 octobre 2026). Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** ajouter à `/bilan` la question des changements de
cap et à l'ADR la colonne « prêts à payer ? », pour compléter les fiches 13 et 4.

**Redite par l'agent :** le réglage du centre de gravité passe de trois à quatre
questions (nos changements de cap sont-ils décidés, expliqués, appuyés sur un fait ?), et
le crible FRANCE de l'ADR dit, pour chaque valeur, si l'on est prêt à en payer le prix.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | fiche n° 13 du livre imprimé, schéma : « Nos changements de cap : chacun décidé, expliqué, appuyé sur un fait » (oui : précession ; non : la toupie ralentit) ; fiche n° 4, mode d'emploi, 4 : « écrire ce qu'elle va coûter et décider si l'on est prêt à le payer » |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | `tests/test_alignement_livre.py` |

**Temps de la main :** appuyer.

## Ma réponse d'abord

« Je m'en passe. » — Pascal, le 21 octobre 2026 (pas de réponse propre à cette mission).

## L'Homme

- **Agent :** `testeur` (marqueurs d'abord rouges), puis `dev`.
- **Ce qui ne lui est pas demandé :** changer les autres étapes de `/bilan`, ajouter au
  gabarit de l'ADR autre chose que la colonne et la lettre A (« Anticipateur » devient « Anticiper », fiche n° 4).

## Harnais

- **Peut :** `skills/bilan/SKILL.md`, `skills/brief/adr-france.md`,
  `tests/test_alignement_livre.py`.
- **Ne doit pas :** toucher aux hooks, à `release.yml` ou à `main`.
- **Sources autorisées :** le livre imprimé (fiches n° 4 et 13), `docs/brief.md`.

## Tests

- **Comment saura-t-on que c'est juste :** `python3 tests/test_alignement_livre.py` vert
  dans la CI, avec les marqueurs de la mission 005 : quatre questions dans `/bilan`,
  dont les changements de cap ; colonne « Prêts à payer ? » et lettre « **A**nticiper »
  dans `adr-france.md`, plus « Anticipateur ».

## Terrain

- **Échantillon que Pascal vérifiera :** l'ADR de la mission 008, au crible FRANCE avec
  la colonne « Prêts à payer ? » remplie ; et le prochain `/bilan`, qui liste les
  changements de cap du journal.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

L'étape « Alignement du plugin sur le livre imprimé » est verte dans la CI, et l'ADR 008
dit, valeur par valeur, si l'on est prêt à en payer le prix.
