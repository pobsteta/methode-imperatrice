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
(*La méthode de l'Impératrice — Emmener le bureau en forêt*, livre imprimé, Boîte à outils
p. 203-275) : **l'IA propose, l'homme tranche et assume.** Le plugin reprend les formules
du livre ; `tests/test_alignement_livre.py` vérifie qu'elles y sont.

Ce dépôt contient la méthode, et elle seule. Chaque projet garde son produit (`docs/`) et
la trace de son pilotage (`pilotage/`) ; la méthode, les agents, les commandes et les
garde-fous viennent d'ici, sans copie.

## Ce que le plugin apporte

| Élément | Contenu |
|---|---|
| **Commandes** | `/imperatrice:demarrer` (installer la méthode dans un projet), `/imperatrice:brief` (Abstraction, porte n° 1), `/imperatrice:mission` (staffing, porte n° 2), `/imperatrice:boucle` (OODA, porte n° 3), `/imperatrice:bilan` (PDCA) ; `boucle` et `bilan` se closent sur une livraison différente de la précédente |
| **La méthode** | skill `imperatrice:methode` : les six A, la règle de staffing, les trois temps de la main, le harnais en sept points (dont « ma réponse d'abord »), le crible FRANCE, plier ou tenir |
| **Agents** | `contradicteur`, `acquereur`, `archiviste`, `analyste`, `afficheur`, `dev`, `testeur`, `relecteur` |
| **Garde-fous** (hooks Python 3) | pas de commit ni de push sur `main`, pas de push forcé ; `pilotage/journal.md` en ajout seul (commandes filtrées, et résultat vérifié à chaque arrêt et en CI) ; pas de « terminé » sans tests verts (`.claude/test-command`, attente du verrou comprise, 630 s au plus) ; au second arrêt sans tests verts, l'agent sort mais c'est inscrit au journal |
| **Gabarits** | fiche de mission (ma réponse d'abord, critère d'arrêt de la relecture), ADR au crible FRANCE (« prêts à payer ? »), `CLAUDE.md`, brief, équipe, kanban (cartes, cycles et livraisons), journal (lignes `écart` et `cap`) |

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

## L'enchaînement des commandes dans un projet

```
/demarrer → [Pascal remplit le brief, puis sa réponse d'abord] → /brief → /mission
         → /boucle ×N → /bilan → (retour à /brief ou /mission si le cap change) → /boucle …
```

1. **`/imperatrice:demarrer`**, une fois : pose les fichiers et demande, en une seule
   fois, le nom du projet, ce qu'il fait, pour qui, et les référentiels connus.
2. **Pascal remplit `docs/brief.md`**, sans commande : le problème et pour qui, ce que
   fait le projet, ce qu'il ne fait pas, les contraintes ; puis sa réponse d'abord,
   datée (fiche n° 15). Le pourquoi et le pour qui sont à lui : l'IA propose ensuite,
   Pascal tranche.
3. **`/imperatrice:brief`** : rattrape un brief resté vide (au plus quatre questions),
   fait écrire la réponse d'abord, fait critiquer le brief par le `contradicteur`, puis
   prépare la spec, les ADR FRANCE et la commande de tests. Rien ne passe à `/mission`
   sans le « oui » de Pascal.
4. **`/imperatrice:mission`** : découpe la spec en missions d'une phrase, applique les
   trois questions et propose `pilotage/equipe.md`.
5. **`/imperatrice:boucle`**, à chaque cycle : missions confiées, PR relues, compte rendu
   en quatre temps, livraison proposée (ou mauvaise nouvelle), et pour qui.
6. **`/imperatrice:bilan`**, à chaque jalon : retour à l'Abstraction ; si le cap change,
   on repasse par `/brief` ou `/mission`.

`/imperatrice:methode` n'est pas une étape : c'est le texte de référence, à lire en cas
de doute.

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

**Ce que change la 0.2.0** : le plugin suit le livre imprimé du 20 octobre 2026 (harnais
en sept points, « ma réponse d'abord » dans `/brief` et la fiche de mission, critère
d'arrêt de la relecture, cartes immobiles nommées par `/boucle`, changements de cap au
`/bilan`, carnet des écarts au journal) ; le journal est protégé par un invariant vérifié
à chaque arrêt et en CI ; le hook de tests est testé et ne connaît plus aucun domaine.

**Ce que change la 0.3.1** : l'ordre du brief est explicite. `/brief` ne demande la
réponse d'abord qu'une fois le brief rempli par Pascal ; le gabarit du brief rappelle
l'ordre (le problème et pour qui, puis la réponse d'abord, puis la critique) ; le README
donne l'enchaînement des commandes dans un projet.

**Ce que change la 0.3.0** : chaque fin de cycle propose une livraison, différente de la
précédente, et pour qui : `/boucle` à la fin de chaque cycle, `/bilan` à la distance de
la grande boucle, inscrites dans la rubrique « Livraisons » du kanban. Un cycle sans
livraison neuve livre sa mauvaise nouvelle, « une livraison sur laquelle on apprend »,
dite tout de suite avec ce qu'elle nous apprend. La formule vient du brief au livre
(`docs/livre/brief-livraison-fin-de-cycle.md`), en attendant le livre. Le hook de tests
borne l'attente de son verrou : attente et tests tiennent dans 630 s, sous le délai du
hook, et un verrou resté occupé arrête l'agent en le disant au lieu de le laisser
couper sans vérification.

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
