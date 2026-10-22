# Brief au livre — à chaque fin de cycle, une livraison différente de la précédente

> Proposé par Claude le 22 octobre 2026, à partir de la réponse de Pascal. À reporter
> dans le livre par Pascal ; le plugin le suit dès la v0.3.0 (mission 011). Le livre
> reste la source : si la formule change à l'impression, le plugin la reprend.

## Ma réponse d'abord (fiche n° 15)

> « La question de fin de cycle doit proposer un produit de livraison différent de la
> précédente. »
>
> — Pascal, le 22 octobre 2026.

## Le manque

Le livre clôt chaque rituel sur une question, « qu'avons-nous décidé, qui fait quoi,
d'ici quand ? » (fiche n° 12). Cette question tient l'équipe ; elle ne dit pas ce que le
bénéficiaire reçoit. Un cycle peut donc finir bien décidé et bien réparti sans rien
livrer de neuf, et le suivant aussi : la boucle tourne, le produit ne bouge pas. Le
retour à l'Abstraction le verra, mais au trimestre, trop tard pour la petite boucle.

## La formule

> **Quelle livraison proposons-nous, différente de la précédente, et pour qui ?**

- **Une livraison** : ce qu'un bénéficiaire nommé peut prendre en main à la fin du cycle
  (une version, une fonction dont il se sert, une page publiée, une carte remise).
- **Proposons** : la question appelle une proposition, que celui qui tranche accepte ou
  non ; elle ne se répond pas par un compte rendu.
- **Différente de la précédente** : on la compare à la dernière livraison inscrite ; on
  dit en une ligne ce qu'elle apporte de plus. Si l'on ne trouve rien, on le dit tout de
  suite (fiche n° 8) : le cycle n'a rien livré de neuf.
- **Pour qui** : un bénéficiaire de l'Abstraction (fiche n° 2), pas « l'équipe ».

Ce n'est pas un produit minimum. Le livre dit déjà « pas le minimum, le nécessaire à la
décision » (chapitre « Aller voir ») : la livraison est celle qui sert au bénéficiaire et
lui permet de dire ce qui manque, pas la plus petite qu'on puisse montrer.

## Où l'écrire dans le livre

1. **Chapitre « Faire tourner la boucle », après le paragraphe « Rappeler »** :
   > La question de sortie dit ce que l'équipe a décidé. Elle ne dit pas ce que le
   > bénéficiaire reçoit. La petite boucle se clôt donc sur une seconde question :
   > quelle livraison proposons-nous, différente de la précédente, et pour qui ? Une
   > boucle qui tourne sans rien livrer de neuf use l'équipe sans servir personne.
2. **« Les pièges du rythme », un cinquième piège** :
   > **La livraison repeinte.** On présente au cycle suivant la livraison du précédent,
   > sous un autre nom. Le rituel a eu lieu, rien n'a été remis. Écrivez la livraison
   > précédente à côté de la nouvelle : si vous ne savez pas dire ce qui a changé, rien
   > n'a changé.
3. **Fiche n° 12, « Mode d'emploi », après « Clore chaque rituel par une question »** :
   > Clore la petite boucle par la question de la livraison : quelle livraison
   > proposons-nous, différente de la précédente, et pour qui ? L'inscrire, avec ce
   > qu'elle apporte de plus que la précédente.
4. **Schéma de la fiche n° 12, sous « Chaque rituel se clôt sur une question »** :
   > La petite boucle ajoute : quelle livraison, différente de la précédente, et pour qui ?
5. **Exemple vécu** : à écrire par Pascal, s'il en a un (une tournée, une carte, une
   version de Surculus remise à un agent). Claude n'en invente pas.

## Ce que fait le plugin (v0.3.0)

- `/boucle`, en sortie, après « qu'avons-nous décidé, qui fait quoi, d'ici quand ? » :
  l'orchestrateur propose la livraison du cycle, la compare à la dernière inscrite au
  kanban, nomme son bénéficiaire ; s'il n'en trouve pas de différente, il l'annonce en
  quatre temps. Pascal tranche.
- `pilotage/kanban.md` reçoit une rubrique « Livraisons » : une ligne par cycle,
  `cycle N · livraison · pour qui · ce qu'elle apporte de plus que la précédente`, ou `cycle N · rien de neuf` ; la question se pose à chaque `/boucle`, même
  quand le plafond humain l'a arrêtée.

## À trancher par Pascal

- **La formule, mot pour mot.** « Pour qui », « proposons » et la comparaison écrite
  sont des ajouts de Claude à la réponse de Pascal ; le test et le plugin dépendent de la
  formule exacte.

- **Quels rythmes ?** Le brief l'applique à la petite boucle (la semaine, ou chaque
  `/boucle`). Le mois et le trimestre doivent-ils aussi proposer une livraison, plus
  large ?
- **Un cycle sans livraison** est-il permis, dit comme tel (comme une carte immobile), ou
  est-ce toujours une mauvaise nouvelle ? Le plugin le traite comme une mauvaise
  nouvelle à dire tout de suite, sans bloquer.
