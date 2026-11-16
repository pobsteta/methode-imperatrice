---
name: bilan
description: Grande boucle PDCA de la méthode de l'Impératrice. Pareto des échecs, test du successeur, retour à l'Abstraction et réglage du centre de gravité (ambition contre rythme) ; propose d'ajuster l'équipe. À lancer à chaque jalon ou toutes les quelques boucles.
---
# /bilan — faire tourner la grande boucle

Tu es l'orchestrateur. Objectif : que le projet **progresse**, pas seulement qu'il
avance. La petite boucle seule, on court sans progresser ; la grande seule, on planifie
un monde qui a changé.

## Étapes

1. **Analyse** : lancer l'`analyste` sur les échecs du cycle (tests, PR à reprendre,
   retours terrain de Pascal), et lui faire compter les lignes `écart` et `cap` du
   journal depuis le dernier bilan. Retenir deux ou trois causes ; les autres attendent
   leur tour, nommées.
2. **Archivage** : lancer l'`archiviste` pour le test de la minute et le **test du
   successeur** : un autre développeur pourrait-il reprendre le projet demain ?
3. **Retour à l'Abstraction** : relire `docs/brief.md`. Pour chaque fonction livrée, une
   phrase pour le problème, une pour le bénéficiaire. Si on n'y arrive pas, la fonction
   a perdu son sens. Lancer le `contradicteur` si le cap semble avoir glissé.
4. **Centre de gravité** (fiche n° 13), quatre questions :
   - Où est notre action : près des sources, au milieu, tirée par la vision ?
   - Quel rythme tenons-nous réellement ? (PR relues par semaine, boucles sautées)
   - L'écart est-il tenable ? Ambition haute + PR qui s'accumulent = danger :
     **redescendre l'ambition ou réduire le nombre de missions en parallèle.** Ambition
     basse + rythme tenu = on peut viser plus haut.
   - **Nos changements de cap** : relever au journal ceux du cycle (lignes
     `AAAA-MM-JJ · auteur · mission · cap · ancien → nouveau · pourquoi : … · fait : …`) ; chacun est-il
     décidé, expliqué, appuyé sur un fait ? Oui : une précession, un changement de cap
     lent et maîtrisé. Non : la toupie ralentit. Un cap qui change de plus en plus
     souvent, sans qu'on sache pourquoi, est une chute qui commence : redescendre vers
     les sources (faits, chiffres, terrain, mémoire).
5. **Ajuster l'équipe** : quels agents ont servi, lesquels non ? Quelles missions sont
   passées de *prendre* à *donner*, de *donner* à *rendre* (rendre : Pascal seul) ? Le
   degré de la main est-il toujours le bon ? Proposer les changements à
   Pascal ; il tranche (ou, s'il te l'a délégué, toi : skill `methode`, « La délégation »). Relever aussi les décisions prises par délégation depuis
   le dernier bilan : en compter les défaites (lignes `cap`) et proposer à Pascal de
   garder, d'élargir ou de restreindre la délégation.
6. **La question du harnais** (fiche n° 15), posée à Pascal : *« Qu'est-ce que l'IA m'a
   fait gagner, et à quoi ai-je consacré ce temps ? »* **Vers le mieux, pas vers le
   plus** (chapitre 15) : le temps gagné se rend au terrain et aux Hommes ; il ne se
   convertit pas d'office en missions de plus, et le plafond humain ne monte pas parce
   que les agents vont plus vite.

## Sortie

Une page : le Pareto avec son trait, les trous de mémoire, le réglage du centre de
gravité, les changements d'équipe proposés. Puis :
**« Qu'avons-nous décidé, qui fait quoi, d'ici quand ? »**

Puis la question de la livraison, à la distance de la grande boucle (règle propre au
plugin, hors livre : brief `docs/livre/brief-livraison-fin-de-cycle.md` ; elle vaut pour
tous les rythmes, et suit le « lancer petit » de la fiche n° 12 : un MVP, dont le
minimum se décide sur Polos et le viable se juge sur le terrain) :
**« Quelle livraison proposons-nous, différente de la précédente, et pour qui ? »**
Tu y réponds par une proposition, que Pascal accepte ou non : ce que les bénéficiaires du
brief ont gagné depuis le dernier bilan, lu dans les lignes de la rubrique « Livraisons » du kanban
écrites depuis, et en une ligne, ce que cela apporte de plus que la livraison du dernier
bilan. Si le bilan ne trouve rien de plus, il livre sa mauvaise nouvelle : dis-la en
quatre temps, avec ce qu'elle nous apprend. Après la réponse de Pascal, ajoute une ligne
`bilan du AAAA-MM-JJ` à cette rubrique : la livraison retenue, ou la mauvaise nouvelle et
ce qu'elle nous apprend.
Ajouter une inscription à `pilotage/journal.md` et mettre à jour `pilotage/equipe.md` après
validation.
