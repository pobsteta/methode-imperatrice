---
name: brief
description: Étape Abstraction de la méthode de l'Impératrice. Fait noter à Pascal sa réponse d'abord, rédige docs/brief.md à partir des réponses de Pascal à ses questions, le fait critiquer par le contradicteur, aide Pascal à l'amender, puis prépare la spec et les ADR FRANCE des décisions structurantes. À lancer avant tout développement.
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
3. **Poser les questions du brief.** Tu remplis le brief en interrogeant Pascal, rubrique
   par rubrique (le problème, et pour qui ; ce que fait le projet ; ce qu'il ne fait pas ;
   les contraintes), **au plus quatre questions par tour**, et tu attends ses réponses
   avant le tour suivant. Questions ouvertes, sans réponse suggérée : c'est sur le sens
   (Polos) que l'ancrage coûte le plus. Tu reprends les réponses déjà données à
   `/demarrer` au lieu de les redemander.
4. **Rédiger le brief, puis le faire relire.** Tu écris `docs/brief.md` à partir des
   seules réponses de Pascal, au plus près de ses mots : chaque ligne vient d'une
   réponse, rien n'est inventé. Ce qu'il n'a pas dit s'écrit « à trancher par Pascal ».
   **Coût complet** non renseigné : écris « inconnu » ; ce n'est pas une question
   bloquante. Puis tu lui rends le brief avec une question : **« Est-ce bien ce que tu as
   dit ? »** Tu reportes ses corrections ; tant qu'il ne l'a pas relu, tu ne lances
   personne.
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
