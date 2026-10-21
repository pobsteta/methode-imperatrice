# Mission 002 — ma réponse d'abord

> Fiche de mission (fiches n° 9 et 15). Brief : `docs/brief.md` (v0.2.0, validé par
> Pascal le 21 octobre 2026). Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** ajouter « ma réponse d'abord » à `/brief` et à la
fiche de mission, pour que Pascal écrive sa réponse avant de lire celle des machines.

**Redite par l'agent :** aujourd'hui `/brief` lance le contradicteur tout de suite ; je
fais d'abord demander à Pascal sa propre réponse, écrite dans le brief, et je donne à la
fiche de mission une rubrique que seul Pascal remplit.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | fiche n° 15 du livre imprimé : « L'homme note sa réponse avant de lire celle des machines » ; mode d'emploi, 2 : « Noter sa propre réponse d'abord » |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | `tests/test_alignement_livre.py` |

**Temps de la main :** appuyer.

## Ma réponse d'abord

Celle du brief v0.2.0, écrite par Pascal le 21 octobre 2026 : « J'attends un plugin qui
reprend complètement la méthode de l'Impératrice. »

## L'Homme

- **Agent :** `testeur` (marqueurs d'abord rouges), puis `dev`.
- **Ce qui ne lui est pas demandé :** le critère d'arrêt de la relecture (mission 003),
  changer le déroulé de `/brief` au-delà de l'étape ajoutée.

## Harnais

- **Peut :** `skills/brief/SKILL.md`, `skills/demarrer/gabarit-brief.md`,
  `skills/mission/SKILL.md`, `skills/mission/fiche-mission.md`,
  `tests/test_alignement_livre.py`.
- **Ne doit pas :** écrire la réponse à la place de Pascal, toucher aux hooks, à
  `release.yml` ou à `main`.
- **Sources autorisées :** le livre imprimé (fiche n° 15), `docs/brief.md`.

## Tests

- **Comment saura-t-on que c'est juste :** `python3 tests/test_alignement_livre.py` vert
  dans la CI, avec les marqueurs de la mission 002 : `/brief` demande la réponse de
  Pascal avant de lancer le `contradicteur` ; le gabarit du brief et la fiche de mission
  portent la rubrique « Ma réponse d'abord ».

## Terrain

- **Échantillon que Pascal vérifiera :** au prochain `/brief` (Surculus, ou ce dépôt),
  l'orchestrateur lui demande sa réponse et ne lance pas le contradicteur avant qu'elle
  soit écrite.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

L'étape « Alignement du plugin sur le livre imprimé » est verte dans la CI, et le brief
suivant porte la réponse de Pascal en tête, datée d'avant la critique.
