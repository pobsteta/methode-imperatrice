# imperatrice v1.0.0 — brief

> Proposé par Claude le 16 novembre 2026 sous le titre « v0.9.0 », puis tranché par
> Pascal le même jour : « Modifie comme tu le dis, mets 1.0.0, fais tout ce qu'il faut et
> commite, fusionne et merge. » Les recommandations de Claude sont donc retenues (voir
> « Décisions de Pascal »), et la version est 1.0.0, pas 0.9.0.
>
> État de départ : `main` à `bb7855b`, tag `v0.8.0` (délégation).
> Référence : le livre, *La méthode de l'Impératrice — Emmener le bureau en forêt*, PDF
> KDP du 7 novembre 2026 (295 pages), Boîte à outils p. 207-286. Le dépôt cite encore
> le PDF du 20 octobre (Boîte à outils p. 203-275).

## Ma réponse d'abord (fiche n° 15)

> « Modifie comme tu le dis, mets 1.0.0, fais tout ce qu'il faut et commite, fusionne et
> merge. »
>
> — Pascal, le 16 novembre 2026.

## Décisions de Pascal (16 novembre 2026)

1. **Délégation** : voie **b**. Elle reste, mais ne couvre ni « rendre la main » ni ce qui
   touche l'extérieur et ne se défait pas.
2. **Degré de la main** : ajouté à la fiche de mission et au skill `methode`, avec la
   correspondance proposée (le chef tranche par défaut ; sollicitation d'avis ; partage
   d'intention = délégation).
3. **Question de livraison** : gardée comme règle propre au plugin, marquée « hors livre »,
   accordée au « lancer petit » du livre.
4. **PDF de `docs/`** : remplacé par le PDF du 7 novembre.
5. **Version** : 1.0.0 (rupture assumée : renommage des trois temps), les anciens noms
   restant lus dans les fiches existantes.
6. **Missions** : les missions 013 à 020 sont menées ensemble, en une seule PR (fiche
   `pilotage/missions/013-livre-7-novembre.md`), à la demande de Pascal.

## Le problème, et pour qui (Abstraction)

- **Problème** : entre le 20 octobre et le 7 novembre, le livre a changé sur des points que
  le plugin applique tous les jours : les trois temps de la main ont changé de nom, le
  harnais est passé à huit points, le chapitre 12 « lance petit » (MVP), et la fiche
  ENSEMBLE place les agents à tous les niveaux sauf au pivot. Le plugin dit encore
  « tenir, appuyer, lâcher », « sept points », et interdit le mot MVP.
- **Bénéficiaires** : Pascal, qui relit et tranche ; les projets qui utilisent le plugin
  (Surculus d'abord) ; les lecteurs du livre qui l'installeront et doivent y lire les mêmes
  mots ; le successeur.
- **Coût complet aujourd'hui** : un lecteur qui lit « rendre la main » dans le livre et
  « lâcher » dans le plugin ; un test d'alignement qui vérifie la présence de formules que
  le livre a abandonnées (« sept points ») et l'absence d'une formule qu'il a adoptée
  (« MVP ») ; une délégation (v0.8.0) qui contredit une phrase nouvelle du livre sans le
  dire.

## Les écarts, fiche par fiche

| Livre (7 novembre) | Ce que dit le livre | État dans le dépôt (v0.8.0) | Où |
|---|---|---|---|
| Fiche 1, ch. 1 | Trois temps : **prendre** la main (mener), **donner** la main (aider, si besoin), **rendre** la main (comme le cavalier). Non à la 3e question : **ne pas rendre la main**. Trois oui : **rendre la main** | « Tenir / Appuyer / Lâcher » ; « ne pas lâcher » ; « Trois oui : on lâche » | `skills/methode`, `skills/mission/SKILL.md` et `fiche-mission.md`, `skills/boucle` (étapes 4-5), `skills/bilan` (étape 5), `agents/dev.md`, README |
| Fiche 15 | Harnais en **huit** points : ajout du **Journal** (tout ce que l'IA a vu et fait, dans l'ordre, sans effacement) | sept points, pas de point Journal | `skills/methode`, `skills/mission/SKILL.md`, `fiche-mission.md`, README, test |
| Fiche 15 | **Harnais** : « Ce qui est interdit se câble ; ce qui dépend du contexte s'écrit dans le brief » | « ce que l'agent peut faire, ne doit pas faire » | `skills/methode`, `fiche-mission.md` (rubrique Harnais) |
| Fiche 15 | **Équipe** : rôles distincts, **périmètres disjoints**, sources et modèles différents si possible. Mode d'emploi 3 : « Donner à chaque agent un périmètre que les autres ne touchent pas ; vérifier que le journal est en ajout seul avant de lancer » | rôles distincts seulement ; rien ne vérifie que deux missions parallèles ne touchent pas les mêmes fichiers | `skills/methode`, `skills/boucle` (étape 3, Décider) |
| Fiche 15 | **Qui tranche** : « un nom ; et, si l'action touche d'autres personnes, le moment où on leur pose le fait » | « un nom » | `skills/methode`, `fiche-mission.md` |
| Fiche 15, pièges | + **L'interdit écrit au crayon** ; + **La donnée sans question** | 7 pièges | `skills/methode` ; `agents/acquereur.md` pour le second |
| Fiche 15, En bref | « Elle donne la main, elle ne la prend pas, et **ce n'est pas à elle de la rendre** » ; « ce qui a touché l'extérieur ne se défait pas » | la délégation permet à l'orchestrateur de passer une mission en « Lâcher » et de fusionner (porte n° 3) | `skills/methode` (« La délégation »), `skills/boucle` (étape 5) |
| Fiche ENSEMBLE (nouvelle) | Seul (préparer, avec les agents) ; en collège (orienter) ; en équipe (transmettre). Les agents à tous les niveaux, **« jamais au pivot »** : l'homme tranche, et il assume | délégation (« hors livre ») : l'orchestrateur tranche à la place de Pascal | `skills/methode` |
| Ch. 9, fiche 9 | **Le degré de la main**, par mission : partage d'intention, sollicitation d'avis, ou le chef tranche | absent | `fiche-mission.md`, à trancher (voir plus bas) |
| Ch. 12, fiche 12 | « Je lance petit : la plus petite version qui rend déjà un service réel, essayée tout de suite sur le terrain » (**MVP**) ; « le minimum se décide sur Polos, le viable se juge sur le terrain » | « MVP » interdit par le test (`boucle`, `bilan`, `gabarit-kanban`) ; la mission 011 l'avait banni au nom du ch. 5 (« pas le minimum, le nécessaire à la décision »), qui parle de la donnée, pas de la livraison | `skills/boucle`, `skills/bilan`, `gabarit-kanban.md`, test |
| Ch. 12 | La question de livraison de fin de cycle | **absente du livre** : le brief au livre du 22 octobre n'a pas été reporté | `docs/livre/brief-livraison-fin-de-cycle.md` ; à trancher |
| Ch. 15, fiche 15 | Question de contrôle : « Qu'est-ce que l'IA m'a fait gagner, et à quoi ai-je consacré ce temps ? » ; « ne pas courir vers le plus, mais vers le mieux » | question presque identique au `/bilan` (« nous », « à quoi ce temps a-t-il servi ») ; rien n'empêche de convertir le temps gagné en missions de plus | `skills/bilan` (étape 6) |
| Ch. 6, fiche 6 | Ishikawa : 5 M, et trois de plus au besoin : **Moyens financiers, Mesure, Management** | 5 M | `agents/analyste.md` |
| Livre | Source : PDF du 7 novembre, Boîte à outils p. 207-286, dix-sept fiches (avec RAPPEL et ENSEMBLE) | PDF du 20 octobre, p. 203-275 ; `docs/KDP_PRINT_INTERIOR_SPREAD.pdf` est l'ancien PDF | `skills/methode` (en-tête), README, test (docstring), `docs/` |

## Missions proposées (à passer au crible de `/imperatrice:mission`)

| N° | Mission en une phrase (quoi, et pourquoi) | Agent | Temps de la main proposé |
|---|---|---|---|
| 013 | Renommer les trois temps en **prendre / donner / rendre** partout (methode, mission, fiche, boucle, bilan, dev, README), en lisant encore « tenir / appuyer / lâcher » dans les fiches déjà écrites des projets, pour que livre et plugin disent la même chose sans casser Surculus | `archiviste` | **prendre** : c'est le texte de la méthode, Pascal relit le plan |
| 014 | Passer le harnais à **huit points** (Journal ; Harnais « l'interdit se câble » ; Équipe à périmètres disjoints ; Qui tranche « poser le fait ») dans methode et la fiche de mission, et ajouter les deux pièges | `archiviste` | prendre |
| 015 | Faire vérifier par `/boucle`, à l'étape Décider, que les missions lancées en parallèle n'ont pas de fichiers en commun dans leur rubrique « Peut », pour appliquer « un périmètre par agent » | `dev` | donner |
| 016 | Lever l'interdit sur « MVP » et reprendre la formule du ch. 12 (« lancer petit », « le minimum se décide sur Polos, le viable se juge sur le terrain ») dans `/boucle`, `/bilan` et le kanban ; garder « pas le minimum, le nécessaire à la décision » pour l'`acquereur` | `dev` | donner |
| 017 | Accorder « La délégation » au livre selon la décision de Pascal (voir « À trancher », 1) | `archiviste` | **prendre** : cela touche la règle d'or |
| 018 | Ajouter à l'`analyste` les trois M supplémentaires, traduits pour un projet logiciel (Mesure : tests et indicateurs ; Management : pilotage et orchestration ; Moyens financiers : coût, dont celui des modèles) | `dev` | donner |
| 019 | Reprendre au `/bilan` la question de contrôle exacte de la fiche 15, et la règle « vers le mieux, pas vers le plus » : le temps gagné ne se convertit pas d'office en missions de plus (le plafond humain ne monte pas parce que l'IA va plus vite) | `dev` | donner |
| 020 | Mettre à jour les références (PDF du 7 novembre, p. 207-286, dix-sept fiches), les marqueurs de `test_alignement_livre.py` (« huit points », « Prendre la main » présents ; « sept points », « on lâche » absents ; « MVP » retiré des absents), le README, et monter la version à **1.0.0** | `archiviste` | donner |

Ordre : 020 écrit d'abord les marqueurs (rouges), 013 et 014 les font passer ; 015 à 019
sont indépendantes ; 017 attend la décision de Pascal.

**Version** : Pascal a choisi **1.0.0** : le renommage des trois temps est traité comme
une rupture, même si les anciens noms restent lus dans les fiches existantes.

## Ce qu'elle ne fait pas (hors périmètre)

- Aucun nouvel agent, aucune nouvelle commande, aucun hook nouveau. Un hook qui
  câblerait « un périmètre par agent » (refuser l'écriture d'un fichier hors de la
  rubrique « Peut » de la mission) relève d'une ADR FRANCE distincte, dans une version suivante.
- Pas de changement du déroulé `demarrer → brief → mission → boucle → bilan`.
- Les compétences de management d'équipes humaines restent hors du plugin (ADR à part,
  comme en v0.2.0).

## Ce qui était à trancher (tranché plus haut)

1. **La délégation (v0.8.0) contre « jamais au pivot ».** Le livre dit désormais que
   l'IA ne prend pas la main « et ce n'est pas à elle de la rendre », et que le pivot n'a
   aucun agent. La v0.8.0 permet à l'orchestrateur, sur demande de Pascal, de trancher à
   sa place, de passer une mission au temps « rendre » et de fusionner. Trois voies :
   - **a.** garder la délégation telle quelle, et l'écrire comme une exception assumée :
     Pascal reste au pivot parce qu'il choisit de déléguer, assume, et peut défaire ;
   - **b.** la garder, mais en retirer ce que le livre réserve à l'homme : **rendre la
     main** (passer une mission au troisième temps) et **ce qui touche l'extérieur et ne
     se défait pas** (release, tag, publication, déploiement, message envoyé, écriture
     dans un système tiers) ;
   - **c.** porter la délégation dans le livre (fiche 15 ou ENSEMBLE).
   *Proposition de Claude : b, qui garde l'usage voulu le 16 novembre et suit la lettre du livre.*
2. **Le degré de la main (fiche 9)** : l'ajouter à la fiche de mission ? Il donnerait
   ses mots à la délégation : par défaut, **le chef tranche** (Pascal) ; avec délégation,
   **partage d'intention** (l'orchestrateur annonce, agit, Pascal peut objecter et
   défaire) ; entre les deux, **sollicitation d'avis** (l'orchestrateur recueille
   `contradicteur` et `relecteur`, puis Pascal tranche). Sinon, reporter dans une version suivante.
3. **La question de livraison de fin de cycle** : le plugin la pose depuis la v0.3.0
   « en attendant le livre », mais le livre imprimé ne l'a pas reprise (il dit « lancer
   petit »). La reporter dans la fiche 12 à la prochaine édition, ou la garder comme
   règle propre au plugin, marquée « hors livre » comme la délégation ?
4. **`docs/KDP_PRINT_INTERIOR_SPREAD.pdf`** (PDF du 20 octobre, 144 planches) :
   le remplacer par le PDF du 7 novembre, ou le retirer du dépôt public ?

## Contraintes connues

- **Versions** : toute PR qui touche le plugin monte `plugin.json` ; la CI échoue sinon.
- **Compatibilité** : Surculus continue de fonctionner (`/plugin marketplace update
  pobsteta`) ; ses fiches écrites en « appuyer » restent valides.
- **Journal** : les lignes passées qui disent « tenir », « appuyer », « lâcher » ne se
  réécrivent pas (ajout seul) ; une ligne datée annonce le changement de vocabulaire.
- **Langue** : tout en français. **Licence** : GPL-3.0-or-later. **`main` protégée** :
  une mission = une branche = une PR.

## Harnais de la v1.0.0 (fiche n° 15, huit points)

| Point | Contenu |
|---|---|
| Brief | ce document, validé par Pascal |
| Harnais | les agents peuvent modifier `skills/`, `agents/`, `tests/`, le README, `docs/` et `plugin.json` (mission 020 seulement) ; ils ne touchent ni `hooks/`, ni `LICENSE`, ni `.github/`, ni `main`. Câblé : les hooks existants (pas de `main`, tests verts, journal en ajout seul) |
| Journal | une ligne par mission et par aller-retour dans `pilotage/journal.md`, plus la ligne qui annonce le changement de vocabulaire |
| Tests | `test_alignement_livre.py` avec les nouveaux marqueurs, les tests des hooks, `claude plugin validate .`, `scripts/verifier_version.py` |
| Terrain | Pascal installe la 1.0.0 dans Surculus et fait tourner une `/boucle` : une fiche écrite en « appuyer » est lue comme « donner » ; deux missions parallèles qui partagent un fichier sont signalées |
| Équipe | l'orchestrateur ; `archiviste`, `dev`, `testeur`, `relecteur` ; le `contradicteur` sur ce brief et sur la mission 017 ; un périmètre de fichiers distinct par mission |
| Ma réponse d'abord | en tête de ce document |
| Qui tranche | Pascal ; la mission 017 n'entre pas dans une délégation |

## Question de contrôle

Quel problème résout-on, et pour qui ? Ici : un plugin qui dit, avec les mêmes mots, ce
que dit le livre du 7 novembre, pour Pascal, pour les projets qui s'y fient et pour les
lecteurs qui l'installeront.
