# imperatrice v0.2.0 — brief

> Proposé par Claude le 21 octobre 2026, amendé par les arbitrages de Pascal le même
> jour, puis à critiquer par le `contradicteur` (`/imperatrice:brief`). Le brief est à
> Pascal : il n'est validé qu'à son « oui ».
>
> État de départ : `main` à `fe2857c`, tag `v0.1.0`, tests des garde-fous verts.
> Référence : le livre imprimé, *La méthode de l'Impératrice — Emmener le bureau en
> forêt* (PDF KDP du 20 octobre 2026), Boîte à outils p. 203-275.

## Ma réponse d'abord (fiche n° 15)

> « J'attends un plugin qui reprend complètement la méthode de l'Impératrice. »
>
> — Pascal, le 21 octobre 2026, écrit avant de lire la critique du contradicteur.

## Le problème, et pour qui (Abstraction)

- **Problème** : le plugin v0.1.0 traduit le **premier jet du 15 octobre**. Le livre
  imprimé du 20 octobre a fixé des règles que le plugin ignore. De plus, un garde-fou
  annoncé comme sûr (le journal en ajout seul) se contourne. Constaté le 21 octobre en
  comparant le dépôt aux fiches imprimées et en rejouant les hooks.
- **Bénéficiaires** :
  1. Pascal, qui relit et tranche : moins d'allers-retours sans fin, et un journal en
     qui il peut avoir confiance ;
  2. les projets qui utilisent le plugin, d'abord Surculus ;
  3. les lecteurs du livre qui installeront le plugin : ce qu'ils lisent et ce que le
     plugin fait doivent dire la même chose ;
  4. le successeur, qui doit pouvoir reprendre la méthode sans son auteur.
- **Coût complet aujourd'hui** :
  - un livre et un plugin qui divergent (le harnais a 7 points dans le livre, 5 dans le
    plugin) ;
  - une boucle de relecture sans critère d'arrêt (« à reprendre » peut tourner
    indéfiniment) ;
  - une mémoire qu'un agent peut réécrire par `tee`, `cp` ou un script, sans que le
    hook le voie ;
  - un hook générique qui contient du code propre à Android (ANDROID_HOME, verrou
    Gradle), venu d'un projet.

## Ce que fait la v0.2.0

- **En une phrase** : aligner le plugin sur le livre imprimé et fermer les trous de ses
  garde-fous, sans changer le déroulé `demarrer → brief → mission → boucle → bilan`.
- **Les écarts à combler, fiche par fiche** :

| Fiche imprimée | Ce que dit le livre | État dans le dépôt | Où |
|---|---|---|---|
| 15 · harnais | 7 points : brief, harnais, tests, terrain, **équipe**, **ma réponse d'abord**, qui tranche | 5 points | `skills/methode`, `skills/mission/fiche-mission.md`, `skills/brief` |
| 15 · mode d'emploi, 4 | « Fixer d'avance quand la boucle de relecture s'arrête » | absent : « à reprendre » renvoie sans limite | `fiche-mission.md`, `skills/boucle` (étape 5) |
| 15 · mode d'emploi, 2 | L'homme note sa réponse avant de lire celle des machines | `/brief` lance le contradicteur directement | `skills/brief` (avant l'étape 2) |
| 8 · étape 8 | Carte : Mission (quoi, quand, **combien**) ; Moyens (comment, **où, avec qui**) | « quoi, quand » ; « comment, avec quoi » | `gabarit-kanban.md` |
| 8 | Une carte qui ne bouge pas = la mauvaise nouvelle à dire | écrit, mais rien ne la repère | `skills/boucle` (étape 1) |
| 4 · FRANCE | « **A**nticiper » ; étape 4 : « décider si l'on est prêt à le payer » | « Anticipateur » ; pas de colonne « prêts à payer ? » | `skills/methode`, `adr-france.md` |
| 13 | 4e question : nos changements de cap sont-ils décidés, expliqués, appuyés sur un fait ? | 3 questions | `skills/bilan` (étape 4) |
| 14 | D'abord « si je **tiens**, qui paie ? » ; si l'on n'est pas prêt à payer : ne pas faire semblant de tenir | seulement « si je plie, qui paie ? » | `skills/methode`, `agents/dev.md` |
| 11 | « Libre ne veut pas dire éternel » ; trois « non » aux questions Choisir → migrer en priorité | absent | `agents/archiviste.md`, `agents/relecteur.md` |
| 3 | Le carnet des écarts (attendu / vu / vérifié / décision) | absent | `skills/boucle` (étape « observer »), `agents/analyste.md`, `skills/bilan` : mission 010 |
| — | Source et statut | « premier jet du 15 octobre » ; règle de staffing « à valider » | `skills/methode` (en-tête) |

- **Les garde-fous à fermer** :
  - `journal_ajout_seul.py` laisse passer `tee pilotage/journal.md`,
    `cp autre.md pilotage/journal.md` et `python3 -c "open('pilotage/journal.md','w')…"`
    (code de sortie 0, vérifié le 21 octobre). `>>` reste permis, et c'est voulu ;
  - `tests_obligatoires.py` n'a aucun test dans la CI, alors que c'est lui qui empêche
    de déclarer « terminé » sans tests verts ;
  - `tests_obligatoires.py` contient un repli ANDROID_HOME et un verrou pensé pour
    Gradle. Le README dit pourtant que le propre du domaine s'écrit dans le
    `CLAUDE.md` du projet.
- **Ce qu'elle produit** : une PR par mission, puis la version **0.2.0**. C'est un
  ajout, donc Y+1 selon les règles du README.

## Missions proposées (à passer au crible de `/imperatrice:mission`)

| N° | Mission en une phrase (quoi, et pourquoi) | Agent | Temps de la main proposé |
|---|---|---|---|
| 001 | Aligner `skills/methode` sur le livre imprimé (source, harnais en 7 points, « Anticiper », plier ou tenir dans l'ordre du livre), pour que livre et plugin disent la même chose | `archiviste` | **tenir** : c'est le texte de la méthode, Pascal relit le plan |
| 002 | Ajouter « ma réponse d'abord » à `/brief` et à la fiche de mission, pour que Pascal écrive sa réponse avant de lire celle des machines | `dev` | appuyer |
| 003 | Ajouter à la fiche de mission un critère d'arrêt de la relecture (par défaut 3 allers-retours, puis remonter à Pascal), et le faire respecter par `/boucle` | `dev` | appuyer |
| 004 | Aligner les cartes du kanban sur la fiche n° 8, et faire signaler par `/boucle` toute carte immobile depuis deux cycles | `dev` | appuyer |
| 005 | Ajouter à `/bilan` la question des changements de cap et à l'ADR la colonne « prêts à payer ? », pour compléter les fiches 13 et 4 | `dev` | appuyer |
| 006 | Écrire les tests de `tests_obligatoires.py` et les brancher dans la CI, pour que le garde-fou central soit lui-même vérifié | `testeur` | appuyer |
| 007 | Écrire d'abord les tests qui échouent pour `tee`, `cp` et l'écriture par script sur le journal, puis fermer ces contournements | `testeur` puis `dev` | appuyer |
| 008 | Sortir du hook générique ce qui est propre à Android, sans casser Surculus | `dev` | **tenir** : ADR FRANCE d'abord, cela touche un projet en service |
| 009 | Monter la version à 0.2.0 et mettre le README à jour | `archiviste` | appuyer |
| 010 | Ajouter le carnet des écarts en variante légère : une ligne de journal marquée `écart` (attendu / vu / vérifié / décision), proposée par `/boucle` à l'étape « observer » et comptée par l'`analyste` au `/bilan`, pour compléter la fiche n° 3 | `dev` | appuyer |
| 011 | Ajouter `docs/` et `pilotage/` à `HORS_PLUGIN` dans `scripts/verifier_version.py`, ouvrir `pilotage/` dans ce dépôt, pour que la méthode s'applique à son propre dépôt sans forcer de montée de version | `dev` | appuyer |

Les missions 006 et 007 précèdent toute autre modification des hooks. La mission 008
attend son ADR. La mission 011 doit être fusionnée avant la PR de ce brief : sans elle,
`docs/brief.md` compte comme un changement du plugin et la CI de la PR du brief échoue.

## Ce qu'elle ne fait pas (hors périmètre)

- **Les compétences de management d'équipes humaines** : `temps-de-la-main`,
  `crible-france`, `annonce`, `rituels` et le reste du dossier
  `claude/plugin/dossier-plugin-depuis-le-livre.md`. Elles visent un manager d'Hommes,
  pas un orchestrateur d'agents. Faut-il un second plugin dans la même marketplace ?
  Cela se décidera par une ADR distincte.
- Aucun nouvel agent, aucune nouvelle commande publique : pas de rupture de nom ni de
  chemin. Une rupture ferait passer en 1.0.0.
- Pas de changement du déroulé en trois portes.

## Arbitrages de Pascal (21 octobre 2026)

1. **Le carnet des écarts (fiche n° 3)** : **oui, en v0.2**, en variante légère (une
   ligne de journal marquée `écart` : attendu / vu / vérifié / décision, proposée par
   `/boucle` à l'étape « observer » et comptée par l'`analyste` au `/bilan`).
   → mission 010.
2. **Appliquer la méthode à son propre dépôt** : **oui**. Le brief reste dans `docs/`,
   un `pilotage/` est ouvert ici, et `docs/` et `pilotage/` rejoignent `HORS_PLUGIN`
   dans `scripts/verifier_version.py`. → mission 011.
3. **Le critère d'arrêt par défaut** : **3 allers-retours** de relecture, puis la
   décision remonte à Pascal. → mission 003.

## Contraintes connues

- **Versions** : toute PR qui touche le plugin monte `plugin.json`. La CI échoue sinon
  (`scripts/verifier_version.py`).
- **Hooks** : Python 3, bibliothèque standard seulement ; code de sortie 2 pour
  bloquer. Ils doivent rester génériques, quel que soit le langage du projet.
- **CI** : Claude Code épinglé en 2.1.290. `claude plugin validate .` doit passer.
- **Compatibilité** : Surculus doit continuer de fonctionner après la mise à jour
  (`/plugin marketplace update pobsteta`).
- **Langue** : tout en français, y compris les messages des hooks.
- **Licence** : GPL-3.0-or-later.
- **`main` protégée** : une mission = une branche = une PR.

## Harnais de la v0.2.0 (fiche n° 15)

| Point | Contenu |
|---|---|
| Brief | ce document, validé par Pascal |
| Harnais | les agents peuvent modifier `skills/`, `agents/`, `hooks/`, `tests/`, `scripts/`, `pilotage/` (journal en ajout seul), le README, et `plugin.json` (mission 009 seulement). Ils ne touchent ni `LICENSE`, ni `.github/workflows/release.yml`, ni `main`. Sources : le livre imprimé, ce brief, les ADR |
| Tests | `python3 tests/test_garde_main.py`, `tests/test_journal_ajout_seul.py`, les nouveaux tests de `tests_obligatoires.py`, `claude plugin validate .`, `python3 scripts/verifier_version.py` |
| Terrain | Pascal installe la 0.2.0 dans Surculus et y fait tourner une `/boucle` complète : une mission, une relecture, une PR. Il vérifie qu'un `tee` sur le journal est refusé et que le build Android passe toujours |
| Équipe | l'orchestrateur ; `archiviste`, `dev`, `testeur`, `relecteur`, et le `contradicteur` sur ce brief et sur l'ADR 008 |
| Ma réponse d'abord | en tête de ce document, écrite par Pascal le 21 octobre 2026 |
| Qui tranche | Pascal |

## Question de contrôle

Quel problème résout-on, et pour qui ? Ici : un plugin qui dit la même chose que le
livre imprimé, et des garde-fous qui tiennent vraiment, pour Pascal et pour les projets
qui s'y fient.
