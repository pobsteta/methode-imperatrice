# Brief au livre — à chaque fin de cycle, une livraison différente de la précédente

> Proposé par Claude le 22 octobre 2026, à partir de la réponse de Pascal ; complété le
> même jour de ses deux décisions (tous les rythmes, la mauvaise nouvelle comme
> livraison). À reporter dans le livre par Pascal ; le plugin le suit dès la v0.3.0
> (mission 011). Le livre reste la source : si la formule change à l'impression, le
> plugin la reprend.

## Ma réponse d'abord (fiche n° 15)

> « La question de fin de cycle doit proposer un produit de livraison différent de la
> précédente. »
>
> — Pascal, le 22 octobre 2026.

## Les décisions de Pascal

> « Tous les rythmes et un cycle sans livraison aussi, une mauvaise nouvelle est une
> livraison sur laquelle on apprend. »
>
> — Pascal, le 22 octobre 2026.

## Le manque

Le livre clôt chaque rituel sur une question, « qu'avons-nous décidé, qui fait quoi,
d'ici quand ? » (fiche n° 12). Cette question tient l'équipe ; elle ne dit pas ce que le
bénéficiaire reçoit. Un cycle peut donc finir bien décidé et bien réparti sans rien
livrer, et le suivant aussi : la boucle tourne, le produit ne bouge pas, et personne
n'apprend rien.

## La formule

> **Quelle livraison proposons-nous, différente de la précédente, et pour qui ?**

- **Une livraison** : ce qu'un bénéficiaire nommé peut prendre en main à la fin du cycle
  (une version, une fonction dont il se sert, une page publiée, une carte remise).
- **Proposons** : la question appelle une proposition, que celui qui tranche accepte ou
  non ; elle ne se répond pas par un compte rendu.
- **Différente de la précédente** : on la compare à la dernière livraison du même
  rythme ; on dit en une ligne ce qu'elle apporte de plus.
- **Pour qui** : un bénéficiaire de l'Abstraction (fiche n° 2), pas « l'équipe ».
- **Un cycle sans livraison neuve livre sa mauvaise nouvelle.** Une mauvaise nouvelle
  est une livraison sur laquelle on apprend : on la dit tout de suite (fiche n° 8), et on
  l'inscrit avec ce qu'elle nous apprend. Ce qu'on ne livre pas, c'est le silence.

Ce n'est pas un produit minimum. Le livre dit déjà « pas le minimum, le nécessaire à la
décision » (chapitre « Aller voir ») : la livraison est celle qui sert au bénéficiaire et
lui permet de dire ce qui manque, pas la plus petite qu'on puisse montrer.

## Tous les rythmes

La question vaut pour les quatre rythmes du calendrier, chacun à sa distance :

| Rythme | La livraison, à sa distance |
|---|---|
| Chaque semaine | ce que le bénéficiaire peut prendre en main cette semaine |
| Chaque mois | ce que les livraisons du mois lui ont apporté ensemble, que le mois précédent n'apportait pas |
| Chaque trimestre | au retour à l'Abstraction : ce que le problème a perdu de son coût pour lui |
| Deux fois par an | à la bilatérale : ce que chacun a livré, et ce qu'il a appris de ses mauvaises nouvelles |

## Où l'écrire dans le livre

1. **Chapitre « Faire tourner la boucle », après le paragraphe « Rappeler »** :
   > La question de sortie dit ce que l'équipe a décidé. Elle ne dit pas ce que le
   > bénéficiaire reçoit. Chaque rituel se clôt donc sur une seconde question : quelle
   > livraison proposons-nous, différente de la précédente, et pour qui ? La semaine
   > livre ce qu'on peut prendre en main, le trimestre ce que le problème a perdu de son
   > coût. Et quand il n'y a rien de neuf à livrer, on livre la mauvaise nouvelle : une
   > mauvaise nouvelle est une livraison sur laquelle on apprend. Ce qui use l'équipe,
   > c'est une boucle qui tourne sans rien livrer ni rien apprendre.
2. **« Les pièges du rythme », un cinquième piège** :
   > **La livraison repeinte.** On présente au cycle suivant la livraison du précédent,
   > sous un autre nom, pour ne pas dire qu'il n'y a rien de neuf. Le rituel a eu lieu,
   > rien n'a été remis, et la mauvaise nouvelle qui aurait appris quelque chose est
   > perdue. Écrivez la livraison précédente à côté de la nouvelle : si vous ne savez pas
   > dire ce qui a changé, dites ce que cela vous apprend.
3. **Fiche n° 12, « Mode d'emploi », après « Clore chaque rituel par une question »** :
   > Clore chaque rituel aussi par la question de la livraison : quelle livraison
   > proposons-nous, différente de la précédente, et pour qui ? L'inscrire, avec ce
   > qu'elle apporte de plus que la précédente du même rythme ; sans livraison neuve,
   > inscrire la mauvaise nouvelle et ce qu'elle nous apprend.
4. **Schéma de la fiche n° 12, sous « Chaque rituel se clôt sur une question »** :
   > Et sur une livraison, différente de la précédente : à défaut, une mauvaise nouvelle,
   > sur laquelle on apprend.
5. **Exemple vécu** : à écrire par Pascal, s'il en a un (une tournée, une carte, une
   version de Surculus remise à un agent). Claude n'en invente pas.

## Ce que fait le plugin (v0.3.0)

Le plugin a deux rythmes : `/boucle` (la petite boucle) et `/bilan` (la grande).

- `/boucle`, en sortie, après « qu'avons-nous décidé, qui fait quoi, d'ici quand ? » :
  l'orchestrateur propose la livraison du cycle, la compare à la dernière inscrite au
  kanban, nomme son bénéficiaire ; s'il n'en trouve pas de différente, le cycle livre sa
  mauvaise nouvelle, annoncée en quatre temps avec ce qu'elle nous apprend. Pascal
  tranche. La question se pose à chaque `/boucle`, même quand le plafond humain l'a
  arrêtée.
- `/bilan`, en sortie : la même question, à la distance de la grande boucle (ce que les
  bénéficiaires ont gagné depuis le dernier bilan).
- `pilotage/kanban.md` reçoit une rubrique « Livraisons », une ligne par cycle et par
  bilan :
  `cycle N · livraison · pour qui · ce qu'elle apporte de plus que la précédente`,
  `cycle N · mauvaise nouvelle : … · pour qui · ce qu'elle nous apprend`,
  `bilan du AAAA-MM-JJ · livraison · pour qui · ce qu'elle apporte de plus que la précédente`.

## Reste à trancher par Pascal

- **La formule, mot pour mot.** « Pour qui », « proposons » et la comparaison écrite
  sont des ajouts de Claude à la réponse de Pascal ; Pascal ne les a pas repris le
  22 octobre, elles restent. Le test et le plugin dépendent de la formule exacte.
- **Le tableau des rythmes** (mois, trimestre, semestre) est une proposition de Claude,
  à reprendre ou à réécrire dans le livre.
