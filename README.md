# La méthode de l'Impératrice — plugin Claude Code

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
| **Garde-fous** (hooks Python 3) | pas de commit ni de push sur `main`, pas de push forcé ; `pilotage/journal.md` en ajout seul ; pas de « terminé » sans tests verts (`.claude/test-command`) |
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
dans le `CLAUDE.md` du projet, qu'ils lisent.

## Faire évoluer la méthode

Une correction de la méthode se fait ici, par PR, et profite à tous les projets à la
mise à jour du plugin (`/plugin marketplace update pobsteta`). Monter `version` dans
`.claude-plugin/plugin.json` à chaque changement.

Tests des garde-fous :

```sh
python3 tests/test_garde_main.py
python3 tests/test_journal_ajout_seul.py
claude plugin validate .
```

## Projets qui l'utilisent

- [Surculus](https://github.com/pobsteta/surculus) — suivi des travaux de plantation en forêt.
