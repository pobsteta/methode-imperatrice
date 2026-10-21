# Mission 006 — tester le garde-fou « pas de terminé sans tests verts »

> Fiche de mission (fiches n° 9 et 15). Brief : `docs/brief.md` (v0.2.0, validé par
> Pascal le 21 octobre 2026). Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** écrire les tests de `hooks/tests_obligatoires.py`
et les brancher dans la CI, pour que le garde-fou central soit lui-même vérifié ; au
second arrêt avec des tests rouges, laisser passer mais l'inscrire au journal
(arbitrage n° 5 de Pascal).

**Redite par l'agent :** le hook qui interdit de dire « terminé » sans tests verts n'a
aucun test ; je le couvre, cas par cas, dans la CI, et je rends visible au journal le
seul cas où il laisse sortir l'agent avec des tests rouges.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | même forme que `tests/test_garde_main.py` |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | dépôt git temporaire, commande de tests factice |

**Temps de la main :** appuyer — la décision de fond (laisser passer en l'inscrivant)
est tranchée par Pascal ; reste l'exécution.

## L'Homme

- **Agent :** `testeur` (tests, d'abord rouges sur le second arrêt), puis `dev` (le hook).
- **Ce qui ne lui est pas demandé :** sortir le code Android du hook (mission 008).

## Harnais

- **Peut :** `tests/test_tests_obligatoires.py`, `hooks/tests_obligatoires.py`,
  `.github/workflows/ci.yml`, le README (liste des tests).
- **Ne doit pas :** toucher au repli ANDROID_HOME ni au verrou (mission 008), à
  `release.yml`, à `main`.
- **Sources autorisées :** le hook, la documentation des hooks de Claude Code (champ
  `stop_hook_active` de l'entrée Stop), `docs/brief.md`.

## Tests

- **Comment saura-t-on que c'est juste :** `python3 tests/test_tests_obligatoires.py`
  vert en local et dans la CI, avec ces cas : pas de `.claude/test-command`, commande
  vide, arbre propre, seuls `docs/` ou `pilotage/` changés, tests verts, tests rouges
  (code 2 et sortie des tests renvoyée à l'agent), second arrêt avec tests rouges
  (code 0 **et** une ligne datée au journal), second arrêt avec tests verts (code 0,
  journal inchangé), second arrêt sans journal (code 0, aucun fichier créé).

## Terrain

- **Échantillon que Pascal vérifiera :** dans Surculus, faire échouer un test, laisser
  l'agent s'arrêter deux fois, et lire la ligne « tests rouges » au journal.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

L'étape « Tests du hook tests_obligatoires » apparaît verte dans la CI de chaque PR.
