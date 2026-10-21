# Mission 008 — un hook de tests qui ne connaît pas Android

> Fiche de mission (fiches n° 9 et 15). Brief : `docs/brief.md` (v0.2.0, validé par
> Pascal le 21 octobre 2026). Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** sortir du hook générique ce qui est propre à
Android, sans casser Surculus, pour que les hooks restent valables quel que soit le
langage du projet.

**Redite par l'agent :** le repli `ANDROID_HOME` quitte `tests_obligatoires.py` et passe
dans la commande de tests de Surculus, dans cet ordre ; le verrou, qui n'a rien
d'Android, reste. Rien n'est fait avant que Pascal ait tranché l'ADR 0001.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui, depuis l'ADR 0001 | ADR critiquée par le contradicteur, acceptée par délégation de Pascal le 21 octobre 2026 |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | `tests/test_tests_obligatoires.py` ; Surculus en lecture |

**Temps de la main :** **tenir** — cela touche un projet en service (Surculus).

## Ma réponse d'abord

« Passe. » — Pascal, le 21 octobre 2026, demandée au lancement de la mission, avant
toute lecture du hook.

## L'Homme

- **Agent :** l'orchestrateur pour l'ADR, le `contradicteur` pour la critique ; ensuite
  `testeur` puis `dev`, selon l'ADR tranchée.
- **Ce qui ne lui est pas demandé :** fusionner la PR de Surculus sans le « oui » de Pascal
  (autre dépôt, `main` protégée) ; écrire la clé `env` des réglages de Claude Code (à
  Pascal) ; borner l'attente du verrou (mission à part).

## Harnais

- **Peut :** `docs/adr/`, et après l'ADR tranchée : `hooks/tests_obligatoires.py`,
  `tests/test_tests_obligatoires.py`, le README.
- **Ne doit pas :** publier la 0.2.0 avant que Surculus porte son environnement dans son
  `main` local ; toucher à `release.yml` ou à `main`. Dans Surculus : une branche et une
  PR pour `.claude/test-command` et une ligne de journal, rien d'autre.
- **Sources autorisées :** le hook, `docs/brief.md`, le README, Surculus en lecture.

## Tests

- **Comment saura-t-on que c'est juste :** `tests/test_tests_obligatoires.py` lance le hook
  avec un faux `~/Android/Sdk` et sans `ANDROID_HOME`, et vérifie que la commande ne reçoit
  pas `ANDROID_HOME` ; les tests existants du hook restent verts ; la nouvelle commande de
  Surculus passe sans `ANDROID_HOME` dans l'environnement.

## Terrain

- **Échantillon que Pascal vérifiera :** dans Surculus, après la mise à jour, une
  `/boucle` dont un agent, dans son worktree, termine avec le build Android vert.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

Le test du hook est vert dans la CI, et Surculus construit toujours après la mise à jour.
