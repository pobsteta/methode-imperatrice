---
name: demarrer
description: Installe la méthode de l'Impératrice dans un projet qui ne l'a pas encore - crée docs/brief.md, pilotage/ (équipe, kanban, journal, missions) et le CLAUDE.md de l'orchestrateur à partir des gabarits joints. À lancer une fois, au début d'un projet.
---
# /demarrer — poser le pilotage d'un nouveau projet

Tu es l'orchestrateur. Objectif : que le projet ait, en dix minutes, les fichiers dont
la méthode a besoin, **sans rien écraser**. Les gabarits sont à côté de ce fichier.

## Étapes

1. **Regarder ce qui existe** : `CLAUDE.md`, `docs/brief.md`, `pilotage/`. Un fichier
   déjà présent n'est jamais remplacé ; s'il manque une rubrique, tu le dis à Pascal.
2. **Demander à Pascal**, en une seule fois, au plus quatre questions : le nom du projet,
   ce qu'il fait en une phrase, pour qui, et les référentiels ou conventions du domaine
   déjà connus (avec leurs sources).
3. **Créer, à partir des gabarits** :
   - `CLAUDE.md` depuis `gabarit-claude.md` ;
   - `docs/brief.md` depuis `gabarit-brief.md`, rubriques en italique laissées telles
     quelles : `/brief` les remplira en questionnant Pascal, et reprendra les réponses
     de l'étape 2 ;
   - `pilotage/equipe.md`, `pilotage/kanban.md`, `pilotage/journal.md` depuis leurs
     gabarits, et le dossier `pilotage/missions/` ;
   - `docs/adr/` vide.
4. **Ne pas créer `.claude/test-command`** : il sera écrit dès que la stack sera tranchée
   (`/brief`, étape 9).
5. Première inscription au journal : la date, « Claude (orchestrateur) », « méthode
   installée », et ce qui reste à remplir.

## Sortie

La liste des fichiers créés et de ceux laissés tels quels, puis :
**« Lançons `/brief` : je te demanderai d'abord ta réponse, puis je te proposerai une réponse à chaque question du brief, à retenir ou corriger. Quand ? »**
