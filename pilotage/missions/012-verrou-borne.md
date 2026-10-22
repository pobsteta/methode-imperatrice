# Mission 012 — borner l'attente du verrou des tests

> Fiche de mission (fiches n° 9 et 15). v0.3.0. Origine : critique du contradicteur sur
> l'ADR 0001 (21 octobre 2026), « son attente n'est pas bornée face au délai de 660 s du
> hook ». Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** borner l'attente du verrou de
`tests_obligatoires.py` dans le délai du hook, pour qu'un agent qui attend un autre
lancement des tests soit arrêté avec un message clair au lieu d'être coupé sans
vérification.

**Redite par l'agent :** l'attente du verrou et les tests partagent un seul budget,
inférieur au délai de 660 s de `hooks/hooks.json` ; si le verrou n'est pas libre à temps,
le hook bloque l'arrêt en le disant (premier arrêt) ou l'inscrit au journal (second
arrêt), comme pour des tests trop longs.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | `fcntl.flock` non bloquant (`LOCK_NB`), délai `timeout` des hooks de Claude Code |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | `tests/test_tests_obligatoires.py` |

**Temps de la main :** appuyer.

## Ma réponse d'abord

« Je m'en passe. » — Pascal, le 22 octobre 2026, demandée au lancement de la mission,
avant toute lecture du hook.

## L'Homme

- **Agent :** `testeur` puis `dev`.
- **Ce qui ne lui est pas demandé :** changer le délai de `hooks/hooks.json` ; toucher
  au reste du hook.

## Harnais

- **Peut :** `hooks/tests_obligatoires.py`, `tests/test_tests_obligatoires.py`.
- **Ne doit pas :** relâcher le garde-fou (un verrou non obtenu ne laisse jamais passer
  un premier arrêt) ; rendre le verrou optionnel.
- **Sources autorisées :** le hook, `hooks/hooks.json`, l'ADR 0001.

## Tests

- **Comment saura-t-on que c'est juste :** `tests/test_tests_obligatoires.py` tient le
  verrou pendant que le hook tourne avec un petit budget : premier arrêt bloqué (2) avec
  un message qui nomme le verrou ; second arrêt accepté et inscrit au journal ; verrou
  libre, tests verts : passe. Et le budget du hook reste inférieur au `timeout` de
  `hooks/hooks.json`.

## Terrain

- **Échantillon que Pascal vérifiera :** dans Surculus, deux agents en parallèle qui
  finissent : le second attend puis passe, ou est arrêté avec le message du verrou, jamais
  coupé en silence.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

Plus aucun arrêt d'agent coupé par le délai du hook pendant l'attente du verrou.
