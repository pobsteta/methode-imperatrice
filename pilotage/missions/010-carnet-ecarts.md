# Mission 010 — le carnet des écarts, en variante légère

> Fiche de mission (fiches n° 9 et 15). Brief : `docs/brief.md` (v0.2.0, validé par
> Pascal le 21 octobre 2026). Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** ajouter le carnet des écarts en variante légère,
une ligne de journal marquée `écart` (attendu / vu / vérifié / décision), proposée par
`/boucle` à l'étape « observer » et comptée par l'`analyste` au `/bilan`, pour compléter
la fiche n° 3.

**Redite par l'agent :** le journal reçoit un format de ligne `écart`, et un format `cap`
pour les changements de cap (décision déléguée de Pascal, mission 005) ; `/boucle` pose
à chaque observation la question des écarts, et `/bilan` les compte, ainsi que les
changements de cap.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | fiche n° 3 du livre imprimé : colonnes « Ce que j'attendais · Ce que j'ai vu · Vérifié (comment) · Décision » ; décisions « garder (vérifié : on adopte) · creuser (prochain essai, daté) · abandonner (vrai hasard : on le note) » ; « on ne sanctionne pas un écart signalé » ; « zéro ligne est permis » ; fiche n° 13 pour `cap` : « décidé, expliqué, appuyé sur un fait » |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | `tests/test_alignement_livre.py` |

**Temps de la main :** appuyer.

## Ma réponse d'abord

_À remplir par Pascal, avant de lire la PR._

## L'Homme

- **Agent :** `testeur` (marqueurs d'abord rouges), puis `dev`.
- **Ce qui ne lui est pas demandé :** un fichier de carnet à part (variante légère : le
  journal suffit), changer le hook du journal, réécrire l'en-tête du journal de ce dépôt
  (il est en ajout seul).

## Harnais

- **Peut :** `skills/demarrer/gabarit-journal.md`, `skills/boucle/SKILL.md`,
  `skills/bilan/SKILL.md`, `agents/analyste.md`, `tests/test_alignement_livre.py`.
- **Ne doit pas :** toucher aux hooks, à `release.yml` ou à `main`.
- **Sources autorisées :** le livre imprimé (fiches n° 3 et 13), `docs/brief.md`.

## Tests

- **Comment saura-t-on que c'est juste :** `python3 tests/test_alignement_livre.py` vert
  dans la CI, avec les marqueurs de la mission 010 : formats `écart` et `cap` documentés
  dans `gabarit-journal.md`, repris par `/boucle` (observer) et `/bilan`, comptés par
  l'`analyste`.

## Terrain

- **Échantillon que Pascal vérifiera :** dans la prochaine `/boucle` de ce dépôt ou de
  Surculus, la question « qu'avons-nous vu que nous n'attendions pas ? » est posée à
  l'observation ; au `/bilan` suivant, l'analyste rend le compte des lignes `écart` et
  `cap`.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

L'étape « Alignement du plugin sur le livre imprimé » est verte dans la CI, et le premier
`/bilan` après la 0.2.0 rend un compte des écarts, même s'il vaut zéro.
