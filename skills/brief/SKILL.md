---
name: brief
description: Étape Abstraction de la méthode de l'Impératrice. Fait noter à Pascal sa réponse d'abord, pose les questions du brief en proposant à chacune une réponse que Pascal retient, corrige ou rejette, rédige docs/brief.md, le fait critiquer par le contradicteur, aide Pascal à l'amender, puis prépare la spec et les ADR FRANCE des décisions structurantes. À lancer avant tout développement.
---
# /brief — prendre de la hauteur avant d'agir

Tu es l'orchestrateur. Objectif : que Pascal valide un brief et une spec qui disent
**quel problème on résout, et pour qui**. Porte n° 1 de la méthode.

## Étapes

1. **Lire `docs/brief.md`.** S'il est déjà rempli et relu par Pascal, passer à l'étape 5
   (sa réponse d'abord reste exigée : étape 2).
2. **Ma réponse d'abord** (fiche n° 15 : « l'homme note sa réponse avant de lire celle
   des machines »). Première question, avant toute autre et avant que tu écrives quoi que
   ce soit : **« Qu'attends-tu de ce projet, et pourquoi ? »** Tu recopies sa réponse mot
   pour mot, entre guillemets et datée, dans la rubrique « Ma réponse d'abord » de
   `docs/brief.md`. Elle est écrite avant que tu rédiges le brief, donc
   avant de lancer le `contradicteur` et avant que Pascal lise toute proposition des
   machines. Tu ne la
   rédiges pas, tu ne la suggères pas, tu ne la reformules pas.
   « Je m'en passe » est une réponse ; l'absence de réponse n'en est pas une : tant
   qu'elle manque, tu n'écris rien d'autre et tu ne lances personne.
3. **Poser les questions du brief : proposer, puis ajuster.** Tu remplis le brief en
   interrogeant Pascal, rubrique par rubrique (le problème, et pour qui ; ce que fait le
   projet ; ce qu'il ne fait pas ; les contraintes),
   **au plus quatre questions par tour**. À chaque question, tu joins une
   **proposition de Claude**, tirée de la description du projet (réponses à `/demarrer`,
   `CLAUDE.md`, sa réponse d'abord) et de ses réponses précédentes, en disant d'où elle
   vient. Pascal la retient, la corrige ou
   la rejette ; tu ajustes les propositions suivantes à ce qu'il a répondu, et tu
   reproposes celle qu'il a corrigée jusqu'à ce qu'il la retienne. Une proposition sans
   réponse de Pascal n'est pas retenue. Tu ne proposes aucun chiffre sans source : un
   **Coût complet** que ni Pascal ni une source ne donne s'écrit « inconnu », et ce
   n'est pas une question bloquante. Tu ne redemandes pas ce que Pascal a déjà dit à
   `/demarrer`.
4. **Rédiger le brief, puis le faire relire.** Tu écris `docs/brief.md` avec ce que
   Pascal a retenu ou corrigé, et rien d'autre : chaque ligne vient d'une de ses
   réponses. Ce qu'il n'a pas tranché s'écrit « à trancher par Pascal ». Puis tu lui
   rends le brief avec une question : **« Est-ce bien ce que tu as retenu ? »** Tu
   reportes ses corrections ; tant qu'il ne l'a pas relu, tu ne lances personne.
5. **Lancer le `contradicteur`** sur le brief, avec pour consigne explicite : critiquer,
   citer ses sources, chercher les conventions publiées du domaine (celles que nomme le
   `CLAUDE.md` du projet, et les autres) avant toute invention.
6. **Rendre la critique à Pascal**, classée, sans l'adoucir. Pour chaque point : ce que
   tu proposes de changer dans le brief. Pascal tranche ; tu reportes ses arbitrages
   dans `docs/brief.md`.
7. **Rédiger `docs/spec.md`** à partir du brief validé : parcours utilisateur sur le
   terrain, données manipulées, ce qui est hors périmètre, critères d'acceptation, et
   les besoins en référentiels (à confier à l'`acquereur`).
8. **Lister les décisions structurantes** (stack, stockage, hors-ligne, formats
   d'échange, licence…). Pour chacune, une ADR proposée dans `docs/adr/` au crible FRANCE
   (gabarit `adr-france.md`, à côté de ce fichier), avec les valeurs sacrifiées nommées. Le
   `contradicteur` critique chaque ADR avant que Pascal la tranche.
9. Dès que la stack est tranchée, écrire la commande de tests du projet dans
   `.claude/test-command` (une seule ligne, ex. `npm test` ou `Rscript -e 'testthat::test_dir("tests")'`).
10. Ajouter une inscription à `pilotage/journal.md`.

## Sortie

Clore par une question, pas par un résumé :
**« Valides-tu le brief et la spec ? Qu'avons-nous décidé, qui fait quoi, d'ici quand ? »**
Rien ne passe à `/mission` sans le « oui » de Pascal.
