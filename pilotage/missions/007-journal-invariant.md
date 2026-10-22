# Mission 007 — un journal vraiment en ajout seul

> Fiche de mission (fiches n° 9 et 15). Brief : `docs/brief.md` (v0.2.0, validé par
> Pascal le 21 octobre 2026). Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** écrire d'abord les tests qui échouent pour tous
les contournements connus du journal, puis protéger le journal par un invariant (le
journal d'aujourd'hui commence par sa version de référence), vérifié par un hook Stop
et par la CI, le filtre PreToolUse restant un premier filtre ; pour que la mémoire du
projet soit digne de confiance.

**Redite par l'agent :** un filtre de commandes ne verra jamais tout (variables,
scripts, globs) ; je bouche les trous visibles du filtre, et je vérifie le résultat
plutôt que la commande : à l'arrêt et en CI, le journal doit commencer par ce qu'il
était.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | liste rejouée par le contradicteur le 21 octobre 2026 |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | dépôts git temporaires |

**Temps de la main :** appuyer.

## L'Homme

- **Agent :** `testeur` (tests d'abord rouges), puis `dev` (filtre et invariant).
- **Ce qui ne lui est pas demandé :** changer la règle elle-même (`>>`, `git mv`, ajout
  par `Edit`/`Write` restent permis).

## Harnais

- **Peut :** `hooks/journal_ajout_seul.py`, `hooks/journal_intact.py` (nouveau),
  `hooks/hooks.json`, `tests/`, `.github/workflows/ci.yml`, le README.
- **Ne doit pas :** relâcher un cas aujourd'hui bloqué (ce serait une rupture, X+1),
  toucher à `release.yml` ou à `main`.
- **Sources autorisées :** les hooks, la documentation des hooks de Claude Code,
  `docs/brief.md`, la critique du contradicteur (journal du 21 octobre 2026).

## Tests

- **Comment saura-t-on que c'est juste :**
  - `tests/test_journal_ajout_seul.py` : les contournements visibles (`tee`, `cp`,
    `install`, `rsync`, `ln`, `dd`, `unlink`, `perl -i`, `sed --in-place`,
    `python -c`, `1>`, `2>`, `&>`, `>|`, globs dans `pilotage/`, `PowerShell`, `Edit` au
    milieu ou avec un ancien texte vide, `MultiEdit`, `NotebookEdit`, `Write` sur
    `Pilotage/Journal.md`) sont bloqués ; `>>`, `&>>`, `tee -a`, `Add-Content`, la
    lecture et `git add` restent permis ;
  - `tests/test_journal_intact.py` : à l'arrêt, un journal tronqué, modifié au milieu,
    supprimé, écrasé par un script, ou dont l'historique poussé a été réécrit, bloque
    l'arrêt ; en CI, toute ligne supprimée ou modifiée depuis la base de la PR fait
    échouer la vérification.

## Terrain

- **Échantillon que Pascal vérifiera :** dans Surculus, demander à l'agent un `tee` sur
  le journal (refusé), puis un écrasement par un petit script (arrêt refusé).

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

Les étapes « Tests du hook journal_intact » et « Journal en ajout seul depuis la base »
sont vertes dans la CI de chaque PR.
