# Mission 003 — un critère d'arrêt pour la relecture

> Fiche de mission (fiches n° 9 et 15). Brief : `docs/brief.md` (v0.2.0, validé par
> Pascal le 21 octobre 2026). Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** ajouter à la fiche de mission un critère d'arrêt
de la relecture (par défaut 3 allers-retours, puis remonter à Pascal), et le faire
respecter par `/boucle`, pour que « à reprendre » ne tourne pas indéfiniment.

**Redite par l'agent :** aujourd'hui `/boucle` renvoie à l'agent à chaque « à reprendre »,
sans limite ; la fiche fixe d'avance combien d'allers-retours on s'accorde, `/boucle` les
compte au journal, et au-delà c'est Pascal qui tranche.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | fiche n° 15 du livre imprimé, mode d'emploi, 4 : « Fixer d'avance quand la boucle de relecture s'arrête » ; arbitrage n° 3 du brief : 3 allers-retours |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | `tests/test_alignement_livre.py` |

**Temps de la main :** appuyer.

## Ma réponse d'abord

« Je m'en passe. » — Pascal, le 21 octobre 2026 (pas de réponse propre à cette mission).

## L'Homme

- **Agent :** `testeur` (marqueurs d'abord rouges), puis `dev`.
- **Ce qui ne lui est pas demandé :** changer le relecteur ou son verdict, toucher aux
  autres étapes de `/boucle` (la carte immobile relève de la mission 004).

## Harnais

- **Peut :** `skills/mission/fiche-mission.md`, `skills/boucle/SKILL.md`,
  `tests/test_alignement_livre.py`.
- **Ne doit pas :** fixer un autre défaut que celui de Pascal (3), toucher aux hooks, à
  `release.yml` ou à `main`.
- **Sources autorisées :** le livre imprimé (fiche n° 15), `docs/brief.md`.

## Tests

- **Comment saura-t-on que c'est juste :** `python3 tests/test_alignement_livre.py` vert
  dans la CI, avec les marqueurs de la mission 003 : la fiche porte le champ « Critère
  d'arrêt de la relecture » (3 allers-retours par défaut) ; `/boucle` remonte à Pascal au
  4e « à reprendre ».

## Terrain

- **Échantillon que Pascal vérifiera :** dans la prochaine `/boucle`, une mission renvoyée
  trois fois : le journal compte les allers-retours, et le quatrième « à reprendre » lui
  arrive au lieu de repartir vers l'agent.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

L'étape « Alignement du plugin sur le livre imprimé » est verte dans la CI, et aucune
mission ne dépasse au journal le nombre d'allers-retours fixé par sa fiche.
