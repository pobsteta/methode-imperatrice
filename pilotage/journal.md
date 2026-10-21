# Journal de methode-imperatrice

> **Règle du sommier : on n'efface pas, on ajoute.**
> Chaque inscription est datée et signée (agent ou personne). Une correction est une
> nouvelle ligne qui renvoie à l'ancienne. Un hook refuse toute modification qui
> supprimerait ou réécrirait une inscription existante.
>
> Format : `AAAA-MM-JJ · auteur · mission · ce qui a été fait / décidé / bloqué`


2026-10-21 · Claude (orchestrateur) · brief v0.2.0 · méthode appliquée à son propre dépôt : pilotage/ ouvert, docs/ et pilotage/ hors plugin pour le contrôle de version.
2026-10-21 · Pascal · brief v0.2.0 · ma réponse d'abord : « J'attends un plugin qui reprend complètement la méthode de l'Impératrice. » Arbitrages : carnet des écarts en v0.2 ; méthode appliquée au dépôt ; relecture arrêtée à 3 allers-retours.
2026-10-21 · contradicteur · brief v0.2.0 · brief critiqué : plan de versions incompatible avec release.yml ; 011 passe avant le brief qu'elle sert ; le hook du journal laisse passer plus de 15 contournements (dont 1>, &>, >|), d'où un invariant vérifié en CI ; tests_obligatoires laisse sortir au 2e arrêt (stop_hook_active) ; « complètement » contredit le hors-périmètre.
2026-10-21 · Pascal · brief v0.2.0 · toutes les critiques retenues ; les tâches humaines sortent du périmètre ; au second arrêt avec tests rouges, on laisse passer en l'inscrivant au journal ; brief validé (« oui »), 006 et 007 lancées en premier.
2026-10-21 · Claude (orchestrateur) · 006, 007 · PR #2 (brief) fusionnée dans main, main reportée dans release/v0.2.0 ; PR #3 (006) et #4 (007) fusionnées dans release/v0.2.0 sur décision de Pascal (« fusionne »), CI verte, conflits ci.yml/README réglés en gardant les deux côtés.
2026-10-21 · Pascal · 001 · plan de la mission 001 validé, avec les oublis du brief (fiches 11 et 14 dans les agents, skills/mission) ; statut « à valider » de la règle de staffing retiré : le livre la valide. Le livre n'étant accessible que sur le poste de Pascal, la mission se poursuit avec Claude Code en local.
2026-10-21 · archiviste (Claude) · mission 001 · skills/methode, skills/mission, agents dev, archiviste, relecteur alignés sur les fiches 4, 11, 14 et 15 du livre imprimé (PDF KDP du 20 octobre 2026) ; test d'alignement vert. À trancher par Pascal : le schéma de la fiche 15 est titré « le harnais en cinq points » mais en liste sept ; « Libre ne veut pas dire éternel » reformule le piège « croire que libre veut dire éternel ».
2026-10-21 · Pascal · mission 001 · fiche 15 : le titre « cinq points » du schéma sera corrigé dans le livre, le plugin garde sept points ; fiche 11 : le test et le texte reprennent la phrase du livre, « Croire que libre veut dire éternel », la reformulation « Libre ne veut pas dire éternel » est retirée.
2026-10-21 · relecteur · mission 002 · relue, à reprendre : ajout hors mission à l'étape 4 de /brief ; « renvoi daté » de fiche-mission.md absent du livre ; rubrique « Ma réponse d'abord » de la fiche 002 remplie par une machine ; harnais élargi à skills/demarrer/SKILL.md à valider par Pascal ; tests verts.
2026-10-21 · dev (Claude) · mission 002 · reprise après relecture (1er aller-retour) : ajout à l'étape 4 retiré, « renvoi daté » retiré, rubrique de la fiche 002 laissée à Pascal ; élargissement du harnais soumis à Pascal.
2026-10-21 · Pascal · mission 002 · ma réponse d'abord : « Je m'en passe » ; la rubrique de la fiche 002 le note.
2026-10-21 · Pascal · mission 002 · harnais élargi à skills/demarrer/SKILL.md (renvoi à l'étape de /brief) : validé.
2026-10-21 · relecteur · mission 003 · relue : prêt pour Pascal ; tests verts ; 3 remarques mineures (seuil N+1 à dire en clair, retour à la ligne dans /boucle, forme du champ entre gabarit et fiche 003). Question de sens laissée à Pascal : un « à reprendre » de Pascal compte-t-il dans les 3 ?
2026-10-21 · dev (Claude) · mission 003 · remarques 1 et 2 appliquées (seuil N+1, 4e par défaut ; un aller-retour = un renvoi) ; remarque 3 laissée : la fiche 003 suit la forme des fiches 001 et 006.
2026-10-21 · Pascal · mission 003 · ma réponse d'abord : « Je m'en passe » ; la rubrique de la fiche 003 le note.
2026-10-21 · Pascal · mission 003 · PR #7 fusionnée en l'état : seuls les « à reprendre » du relecteur comptent dans les 3 allers-retours.
