# ADR 0001 — sortir du hook `tests_obligatoires` ce qui est propre à Android

- **Date :** 2026-10-21
- **Statut :** acceptée, par délégation de Pascal (« Fais ce qu'il faut pour que ça passe », 21 octobre 2026)
- **Proposée par :** Claude (orchestrateur), mission 008
- **Tranchée par :** Claude (orchestrateur), par délégation de Pascal ; à confirmer par Pascal

## Ma réponse d'abord (fiche n° 15)

> « Passe. »
>
> — Pascal, le 21 octobre 2026, écrit avant de lire l'ADR et la critique du contradicteur.

## La décision en une phrase

Le hook générique ne connaît plus Android : chaque projet porte son propre environnement
de tests dans sa commande `.claude/test-command`, et Surculus fait ce changement, fusionné
et tiré dans son `main` local, **avant** que la 0.2.0 soit publiée.

## Contexte

`hooks/tests_obligatoires.py` contient deux morceaux venus de Surculus :

1. **Le repli `ANDROID_HOME`** : si la variable n'est pas définie et qu'il n'y a pas de
   `local.properties`, le hook la fixe à `~/Android/Sdk` (ou `~/Library/Android/sdk`)
   avant de lancer les tests. Sans lui, un worktree d'agent échoue à construire
   (« SDK location not found »).
2. **Le verrou par dossier git** (`imperatrice-tests.lock`) : deux lancements des tests
   dans le même dépôt s'attendent au lieu de se gêner (incident Gradle du 2026-10-16).

Le README dit que le propre du domaine s'écrit dans le projet, pas dans le plugin, et le
brief v0.2.0 demande que les hooks restent génériques, « quel que soit le langage du
projet ».

**Constaté le 21 octobre 2026 dans Surculus** (lecture seule) : sa commande est
`./gradlew :core:test :gpkg:test :data:testDebugUnitTest :app:assembleDebug :app:lintDebug` ;
il n'a pas de `local.properties` et `ANDROID_HOME` n'est pas défini sur le poste. **Surculus
dépend donc aujourd'hui du repli.** Le retirer seul casserait son build.

Le verrou, lui, n'a rien d'Android : tout outil de build peut souffrir de deux lancements
simultanés dans le même dossier. Seul son commentaire parle de Gradle. Il repose sur
`fcntl`, donc il ne joue que sur un système POSIX ; ailleurs, il est ignoré sans bruit.

**Options envisagées :**

- **A. Ne rien changer.** Le hook garde le repli et le verrou.
- **B. Le projet porte son environnement.** Surculus écrit dans sa commande
  `export ANDROID_HOME="${ANDROID_HOME:-$HOME/Android/Sdk}" && ./gradlew …` ; ensuite, le
  repli est retiré du hook. Le verrou reste, avec un commentaire générique.
- **C. Un fichier d'environnement générique** (`.claude/test-env`, lignes `CLÉ=valeur`)
  que le hook lirait avant les tests. Surculus y mettrait `ANDROID_HOME`.
- **D. Déprécier d'abord.** Le repli reste en 0.2.0 avec un avertissement, et il est
  retiré en 1.0.0.
- **E. La clé `env` d'un fichier de réglages local** de Claude Code (`~/.claude/settings.json`
  ou `.claude/settings.local.json`) : « Set environment variables for every session and its
  subprocesses » ; les hooks héritent de l'environnement
  (https://code.claude.com/docs/en/settings-reference, https://code.claude.com/docs/en/hooks).
  `env` ne développe ni `~` ni `$HOME` : le chemin est écrit en entier, propre au poste,
  donc jamais dans un fichier versionné. Déjà noté au journal de Surculus le 2026-10-16.
- **F. `.worktreeinclude`** avec `local.properties` (`sdk.dir`) : Claude Code copie ce
  fichier ignoré dans chaque worktree qu'il crée (https://code.claude.com/docs/en/worktrees).
  Ne couvre pas les worktrees créés à la main avec `git worktree add`.

## Critique du contradicteur (21 octobre 2026)

Faits de l'ADR vérifiés : Surculus dépend du repli ; la commande de B marche avec l'ancien
hook comme avec le nouveau (essayée sous `dash`). Critiques retenues : E et F manquaient
aux options ; le classement de version s'appuyait sur la règle du README présentée comme
SemVer ; l'ordre devait inclure la mise à jour du `main` local de Surculus, puisque le hook
lit `.claude/test-command` à la racine du projet (`CLAUDE_PROJECT_DIR`) ; le verrou est
POSIX seulement, et son attente n'est pas bornée face au délai de 660 s du hook ; la ligne
de B perd le cas macOS et fixe `ANDROID_HOME` même si le dossier manque ; le risque pour
des projets inconnus était affirmé sans être mesuré ; le test prévu ne vérifiait que des
mots.

## Décision

- **B est retenue**, parce qu'elle est versionnée dans Surculus, couvre exactement ce que
  couvrait le hook (la commande de tests, dans tout worktree) et marche avec les deux
  versions du plugin, ce qui permet de la poser d'abord.
- **E est recommandée en plus**, à poser par Pascal sur son poste, parce qu'elle couvre
  aussi les scripts de Surculus (`scripts/verifier-16ko.sh` exige `ANDROID_HOME`). C'est un
  réglage de Claude Code : l'orchestrateur ne l'écrit pas.
- **F est écartée** : elle ne couvre pas les worktrees créés à la main.
- **Le verrou reste**, commentaire rendu générique (« POSIX seulement »). Son attente non
  bornée est une mission à part, pas celle-ci.
- **Ordre, en trois temps** : PR Surculus fusionnée ; `git pull` dans le `main` local de
  Surculus ; puis seulement la publication de la 0.2.0 et `/plugin marketplace update`.
  La PR du plugin peut entrer dans `release/v0.2.0` avant, car rien n'est publié tant que
  cette branche n'est pas fusionnée dans `main`.

## Le crible FRANCE (option B, retenue)

Pour chaque valeur servie, écrire ce qu'elle va coûter et décider si l'on est prêt à le
payer (fiche n° 4).

| Lettre | Question | Réponse (une ligne) | Ce que ça coûte | Prêts à payer ? |
|---|---|---|---|---|
| **F**rugale | Est-ce la solution la plus simple qui tienne ? Réparable avec les moyens du bord ? | Oui : une ligne de shell dans le projet, quelques lignes en moins dans le hook ; pas de nouveau format (contrairement à C) ; E est aussi simple mais propre au poste | une commande de tests un peu plus longue dans Surculus ; la ligne ne couvre pas macOS | oui (Surculus tourne sous Linux) |
| **R**esponsable | Qui fait quoi, et chacun a-t-il les moyens de sa part ? | Le projet répond de son environnement, le plugin de la règle ; Surculus change sa commande, le plugin retire le repli | une PR dans Surculus, à faire avant la publication de la 0.2.0 | oui |
| **A**nticiper | Que se passe-t-il si ce qu'on n'a pas prévu arrive ? De qui ou de quoi dépendons-nous ? | Si Surculus n'est pas à jour à temps, son build casse : d'où l'ordre en trois temps. Le repli ne jouait que si `~/Android/Sdk` existait sans `ANDROID_HOME` ni `local.properties` : il ne touche que des postes Android configurés ainsi ; le nombre d'autres utilisateurs du plugin n'est pas connu | dépendance à l'ordre des PR ; une note de version à écrire | oui, avec la note de version |
| **N**ovateur | Avons-nous écouté toutes les idées, même les plus étranges ? | Six options (A à F), dont ne rien faire, déprécier d'abord, et deux conventions publiées (E, F) apportées par le contradicteur | — | — |
| **C**oût | Que coûte cette décision à l'ensemble ? Y a-t-il une dépense inutile ? | Deux petites PR ; pas de code à maintenir pour un domaine dans le plugin | le temps de Pascal pour relire deux PR | oui |
| **É**cologique | Que réutilisons-nous, et qui pourra réutiliser ce que nous faisons ? | La commande de tests existe déjà ; tout projet, quel que soit son langage, règle son environnement de la même façon | — | — |

## Valeurs sacrifiées

- **Anticiper**, en partie : un poste Android configuré comme celui de Pascal, sur un
  autre projet qui compterait sur le repli, cassera à la mise à jour. Le prix est accepté
  parce que le plugin ne doit pas porter le propre d'un domaine (README, brief v0.2.0), et
  parce que le repli n'a jamais été documenté comme une fonction du plugin. Une note de
  version dit quoi faire.

## Version

**0.2.0, pas une rupture.** Le README classe en rupture (X+1) « chemin, nom de commande,
garde-fou relâché, renommé ou déplacé » : le repli n'est rien de cela, et retirer le repli
ne relâche aucune règle. Le repli n'a jamais fait partie de ce que le plugin déclare ; et
SemVer dit des versions 0.y.z : « Anything MAY change at any time » (https://semver.org/,
point 4). Avec l'ordre en trois temps, Surculus ne casse pas, ce que le brief demandait
(« repli compatible pour Surculus »). Une note de version, dans le README (« Versions et
releases »), dans la PR de cette mission et dans la PR finale de la 0.2.0, dit : « le hook
ne fixe plus `ANDROID_HOME` : écrivez-le dans votre commande de tests ou dans la clé `env`
de vos réglages locaux, chemin en entier ».
- **Garde de l'ordre** : rien d'automatique n'empêche de publier la 0.2.0 avant Surculus.
  La PR finale `release/v0.2.0 → main` porte donc une case bloquante : « PR Surculus
  fusionnée et `git pull` fait dans son `main` local ».

## Sources

- `hooks/tests_obligatoires.py` (repli `ANDROID_HOME`, verrou `imperatrice-tests.lock`) ;
- `docs/brief.md` (v0.2.0) : mission 008, contraintes « Hooks » et « Compatibilité » ;
- `README.md`, section « Versions et releases » ;
- Surculus, `~/dev/surculus/.claude/test-command`, lu le 21 octobre 2026 (commit `ce7d027`) ;
- critique du contradicteur du 21 octobre 2026 (journal), et les pages qu'elle cite.

## Question de contrôle

Cette décision tient-elle nos six valeurs, et que sommes-nous prêts à payer pour cela ?
