# La méthode de l'Impératrice — plugin Claude Code

[![CI](https://github.com/pobsteta/methode-imperatrice/actions/workflows/ci.yml/badge.svg)](https://github.com/pobsteta/methode-imperatrice/actions/workflows/ci.yml)
[![Release](https://github.com/pobsteta/methode-imperatrice/actions/workflows/release.yml/badge.svg)](https://github.com/pobsteta/methode-imperatrice/actions/workflows/release.yml)
[![Version](https://img.shields.io/github/v/release/pobsteta/methode-imperatrice?sort=semver&label=version)](https://github.com/pobsteta/methode-imperatrice/releases)
[![Dernier tag](https://img.shields.io/github/v/tag/pobsteta/methode-imperatrice?sort=semver&label=tag)](https://github.com/pobsteta/methode-imperatrice/tags)
[![Date de release](https://img.shields.io/github/release-date/pobsteta/methode-imperatrice?label=publi%C3%A9e)](https://github.com/pobsteta/methode-imperatrice/releases/latest)
[![Commits depuis la release](https://img.shields.io/github/commits-since/pobsteta/methode-imperatrice/latest?sort=semver&label=commits%20depuis)](https://github.com/pobsteta/methode-imperatrice/commits/main)
![Plugin Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-D97757)
[![Licence](https://img.shields.io/badge/licence-GPL--3.0-blue)](LICENSE)

Piloter une équipe d'agents IA selon **la méthode de l'Impératrice** de Pascal Obstétar
(*La méthode de l'Impératrice — Emmener le bureau en forêt*) : **l'IA propose, l'homme
tranche et assume.**

Ce dépôt contient la méthode, et elle seule. Chaque projet garde son produit (`docs/`) et
la trace de son pilotage (`pilotage/`) ; la méthode, les agents, les commandes et les
garde-fous viennent d'ici, sans copie.

## Ce que le plugin apporte

| Élément | Contenu |
|---|---|
| **Commandes** | `/imperatrice:demarrer` (installer la méthode dans un projet), `/imperatrice:brief` (Abstraction, porte n° 1), `/imperatrice:mission` (staffing, porte n° 2), `/imperatrice:boucle` (OODA, porte n° 3), `/imperatrice:bilan` (PDCA) |
| **La méthode** | skill `imperatrice:methode` : les six A, la règle de staffing, les trois temps de la main, le harnais, le crible FRANCE |
| **Agents** | `contradicteur`, `acquereur`, `archiviste`, `analyste`, `afficheur`, `dev`, `testeur`, `relecteur` |
| **Garde-fous** (hooks Python 3) | pas de commit ni de push sur `main`, pas de push forcé ; `pilotage/journal.md` en ajout seul (commandes filtrées, et résultat vérifié à chaque arrêt et en CI) ; pas de « terminé » sans tests verts (`.claude/test-command`) |
| **Gabarits** | fiche de mission, ADR au crible FRANCE, `CLAUDE.md`, brief, équipe, kanban, journal |

## Installer dans un projet

Dans le `.claude/settings.json` du projet, versionné avec lui :

```json
{
  "extraKnownMarketplaces": {
    "pobsteta": {
      "source": { "source": "github", "repo": "pobsteta/methode-imperatrice" }
    }
  },
  "enabledPlugins": {
    "imperatrice@pobsteta": true
  }
}
```

Claude Code propose d'installer le plugin à l'ouverture du projet. À la main :
`/plugin marketplace add pobsteta/methode-imperatrice` puis
`/plugin install imperatrice@pobsteta`.

Nouveau projet : `/imperatrice:demarrer` crée `CLAUDE.md`, `docs/brief.md` et `pilotage/`.

## Où vivent les choses dans un projet

| Information | Emplacement |
|---|---|
| Ce qu'on construit, pour qui | `docs/brief.md`, `docs/spec.md` |
| Les décisions d'architecture | `docs/adr/` |
| L'équipe, le plafond humain | `pilotage/equipe.md` |
| Les missions | `pilotage/missions/NNN-titre.md` |
| L'avancement | `pilotage/kanban.md` |
| La mémoire, en ajout seul | `pilotage/journal.md` |
| La commande de tests | `.claude/test-command` |
| Le rôle de l'orchestrateur et les règles métier | `CLAUDE.md` |

Les agents sont génériques : ce qui est propre au domaine (référentiels, conventions
publiées, règles de test comme « un point du terrain tombe au bon endroit ») s'écrit
dans le `CLAUDE.md` du projet, qu'ils lisent. De même, les hooks ne connaissent aucun
domaine : l'environnement dont les tests ont besoin s'écrit dans la commande de tests
du projet, ou dans ses réglages locaux (voir la note de la 0.2.0 plus bas).

## Faire évoluer la méthode

Une correction de la méthode se fait ici, par PR, et profite à tous les projets à la
mise à jour du plugin (`/plugin marketplace update pobsteta`).

## Versions et releases

La version du plugin est celle de `.claude-plugin/plugin.json` (SemVer) : c'est elle que
Claude Code lit pour proposer la mise à jour aux projets. **Toute PR qui change le plugin
monte cette version** : correctif → `Z+1`, ajout (agent, commande, règle, garde-fou
durci) → `Y+1`, rupture (chemin, nom de commande, garde-fou relâché, renommé ou
déplacé) → `X+1`. Durcir un garde-fou (refuser ce qu'il laissait passer à tort) est un
ajout : ce qu'il permettait à raison reste permis.

**Note de la 0.2.0 — le hook de tests ne fixe plus `ANDROID_HOME`** (ADR 0001). Jusqu'en
0.1.0, il le fixait à `~/Android/Sdk` (ou `~/Library/Android/sdk`) quand la variable et
`local.properties` manquaient. Un projet Android l'écrit désormais lui-même :

- dans `.claude/test-command`, par exemple
  `export ANDROID_HOME="${ANDROID_HOME:-$HOME/Android/Sdk}" && ./gradlew test`
  (sous macOS : `$HOME/Library/Android/sdk`) ;
- ou dans la clé `env` de réglages non versionnés (`~/.claude/settings.json` ou
  `.claude/settings.local.json`), avec le chemin écrit en entier : `env` ne développe ni
  `~` ni `$HOME`.

| Quand | Quoi | Workflow |
|---|---|---|
| Chaque PR et chaque fusion | tests des garde-fous, validation du plugin et de la marketplace, contrôle de version : le plugin a-t-il changé depuis le tag de sa version ? Si oui, la CI échoue tant que la version n'est pas montée | `ci.yml` |
| Chaque fusion dans `main` | si la version n'a pas encore de tag : tag `vX.Y.Z` posé sur le commit fusionné et release GitHub, notes générées depuis les PR | `release.yml` |

Les fichiers hors plugin (`README.md`, `LICENSE`, `.github/`, `scripts/`, `tests/`, et
`docs/` et `pilotage/`, où ce dépôt applique la méthode à lui-même)
peuvent changer sans montée de version ; leur fusion ne publie rien. Les badges en tête
de page se mettent à jour seuls.

Ce que la CI rejoue, à lancer avant de pousser :

```sh
python3 tests/test_garde_main.py
python3 tests/test_journal_ajout_seul.py
python3 tests/test_tests_obligatoires.py
python3 tests/test_verifier_version.py
python3 tests/test_journal_intact.py
python3 tests/test_alignement_livre.py
claude plugin validate .
python3 scripts/verifier_version.py
```

## Projets qui l'utilisent

- [Surculus](https://github.com/pobsteta/surculus) — suivi des travaux de plantation en forêt.

## Licence

GPL-3.0-or-later ([`LICENSE`](LICENSE)), comme Surculus. Le texte de la méthode est tiré de
*La méthode de l'Impératrice — Emmener le bureau en forêt*, Pascal Obstétar.
