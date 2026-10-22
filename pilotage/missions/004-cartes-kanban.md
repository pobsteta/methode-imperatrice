# Mission 004 — les cartes du kanban, et les cartes immobiles

> Fiche de mission (fiches n° 9 et 15). Brief : `docs/brief.md` (v0.2.0, validé par
> Pascal le 21 octobre 2026). Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** aligner les cartes du kanban sur la fiche n° 8, et
faire signaler par `/boucle` toute carte immobile depuis deux cycles, pour que la
mauvaise nouvelle soit dite tout de suite au lieu d'attendre.

**Redite par l'agent :** chaque carte porte ce que demande le livre (qui ; quoi, quand,
combien ; comment, où, avec qui) et le cycle depuis lequel elle est dans sa colonne ;
`/boucle` nomme, dès l'observation, les cartes qui n'ont pas bougé depuis deux cycles.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | fiche n° 8 du livre imprimé, mode d'emploi : « chaque carte portant l'Homme (qui), la Mission (quoi, quand, combien) et les Moyens (comment, où, avec qui) » ; « Une carte qui ne bouge pas est souvent la mauvaise nouvelle à dire tout de suite » ; seuil de deux cycles : brief v0.2.0 |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | `tests/test_alignement_livre.py` |

**Temps de la main :** appuyer.

## Ma réponse d'abord

« Je m'en passe. » — Pascal, le 21 octobre 2026 (pas de réponse propre à cette mission).

## L'Homme

- **Agent :** `testeur` (marqueurs d'abord rouges), puis `dev`.
- **Ce qui ne lui est pas demandé :** changer les cinq colonnes, toucher aux autres étapes
  de `/boucle` que l'observation, la tenue du kanban et, sur décision de Pascal du
  21 octobre 2026, « Dire tout de suite » (étape 6, « ou immobile »).

## Harnais

- **Peut :** `skills/demarrer/gabarit-kanban.md`, `skills/boucle/SKILL.md`,
  `tests/test_alignement_livre.py`.
- **Ne doit pas :** toucher aux hooks, à `release.yml` ou à `main`.
- **Sources autorisées :** le livre imprimé (fiche n° 8), `docs/brief.md`.

## Tests

- **Comment saura-t-on que c'est juste :** `python3 tests/test_alignement_livre.py` vert
  dans la CI, avec les marqueurs de la mission 004 : le gabarit porte « quoi, quand,
  combien » et « comment, où, avec qui », plus « comment, avec quoi » ; `/boucle` nomme
  les cartes immobiles depuis deux cycles.

## Terrain

- **Échantillon que Pascal vérifiera :** dans Surculus, une carte laissée dans « planifié »
  deux cycles de suite : la `/boucle` suivante la nomme dès l'observation, comme une
  mauvaise nouvelle à dire.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

L'étape « Alignement du plugin sur le livre imprimé » est verte dans la CI, et aucune
carte ne reste deux cycles sans bouger sans qu'une ligne du journal le dise.
