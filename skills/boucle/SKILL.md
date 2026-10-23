---
name: boucle
description: Petite boucle OODA de la méthode de l'Impératrice. Lance un cycle de missions validées, chacune confiée à son agent dans son propre worktree avec un contexte neuf, fait relire chaque PR, et rend compte à Pascal en quatre temps.
---
# /boucle — observer, s'orienter, décider, agir

Tu es l'orchestrateur. Objectif : faire avancer les missions validées **sans dépasser le
rythme que Pascal peut tenir**. Vitesse, pas précipitation : une boucle rapide observe et
s'oriente ; une boucle précipitée saute directement à l'action.

## Préalable
`pilotage/equipe.md` est validé par Pascal. Sinon : arrête-toi et propose `/mission`.

## Étapes

1. **Observer** : lire `pilotage/kanban.md`, les PR ouvertes, les dernières lignes de
   `pilotage/journal.md`. Combien de PR attendent Pascal ? Si le plafond humain est atteint,
   **ne lance rien** : dis-le, et propose de relire plutôt que de produire.
   Pose la question du carnet des écarts (fiche n° 3) :
   *qu'avons-nous vu que nous n'attendions pas ?* Et l'avons-nous vérifié ? Dans les
   rendus des agents, les tests, les retours de Pascal. Pour chaque écart, propose une
   ligne `écart` au journal, zéro ligne est permis :
   `AAAA-MM-JJ · auteur · mission · écart · attendu : … · vu : … · vérifié : comment (ou « non ») · décision : garder / creuser (prochain essai, daté) / abandonner`
   On ne sanctionne pas un écart signalé.
   Nomme les **cartes immobiles** : celles du bac à sable, de « validé » et de « planifié »
   qui sont dans leur colonne depuis deux cycles ou plus (dernier cycle du kanban − N ≥ 2, où N est le
   « depuis le cycle N » de la carte). Une carte qui ne bouge pas est souvent la mauvaise nouvelle à dire tout de
   suite (fiche n° 8) : chacune est annoncée à Pascal à l'étape « Dire tout de suite ».
2. **S'orienter** : quelles missions validées ont leurs moyens prêts (référentiel
   présent, tests écrits, ADR tranchée) ? Une mission sans ses moyens ne part pas.
3. **Décider** : choisir les missions du cycle, dans la limite du plafond.
4. **Agir** : pour chaque mission, lancer l'agent indiqué dans sa fiche avec l'outil
   Agent, **`isolation: "worktree"`** pour les agents qui écrivent du code, et pour seule
   consigne : *« Ta mission est dans pilotage/missions/NNN-titre.md. Redis-la en une phrase,
   puis réalise-la selon ta définition. »* Lancer en parallèle les missions
   indépendantes. Pour l'`acquereur` et le `testeur`, joindre à la consigne le contenu de
   `liste-de-controle.md` (skill `methode`) : les agents ne peuvent pas l'ouvrir
   eux-mêmes. Missions en « tenir » : l'agent rend un plan, que tu soumets à Pascal
   avant toute exécution.
5. **Contrôler** : pour chaque mission rendue, lancer le `relecteur`. « À reprendre » :
   renvoyer à l'agent (nouveau contexte, fiche complétée des remarques, liste de
   contrôle de nouveau jointe pour l'`acquereur` et le `testeur`), et inscrire au
   journal le numéro de l'aller-retour (« aller-retour 2/3 ») : un aller-retour est un
   renvoi à l'agent.
   **Critère d'arrêt de la relecture** : celui de la fiche, N allers-retours, 3 par
   défaut. Au (N+1)e « à reprendre », soit le 4e « à reprendre » par défaut, tu ne
   renvoies plus : la décision remonte à Pascal, en quatre temps, avec les points du
   relecteur restés ouverts. Pascal tranche ; sa décision est inscrite au journal.
   « Prêt » : ouvrir la PR vers `main` pour Pascal. Seules les missions explicitement « lâchées »
   par Pascal peuvent être fusionnées sans lui, et seulement tests verts.
6. **Dire tout de suite** : toute mission bloquée, en échec, hors délai ou immobile, et
   tout cycle dont la livraison est une mauvaise nouvelle (voir « Sortie »), est annoncé
   à Pascal en quatre temps (décidé et par qui ; ouvert ; ce que ça change ; qui fait
   quoi d'ici quand), sans euphémisme.
7. **Tenir la mémoire** : ajouter à `pilotage/journal.md` les lignes proposées par les
   agents (une par mission, datée, signée), mettre à jour `pilotage/kanban.md` :
   augmenter de 1 le dernier cycle, et noter ce nouveau numéro sur chaque carte qui a
   changé de colonne. Cette étape a lieu même quand le plafond humain a arrêté la boucle
   à l'étape 1 : chaque `/boucle` compte pour un cycle.
   Quand Pascal change de cap (périmètre, priorité, mission abandonnée ou redécoupée),
   inscrire une ligne signée de lui :
   `AAAA-MM-JJ · Pascal · mission · cap · ancien → nouveau · pourquoi : … · fait : …`

## Sortie

Un tableau d'une ligne par mission (mission, agent, verdict du relecteur, PR, ce que
Pascal doit vérifier sur le terrain), puis la question :
**« Qu'avons-nous décidé, qui fait quoi, d'ici quand ? »**

Puis la question de la livraison (brief au livre
`docs/livre/brief-livraison-fin-de-cycle.md`, en attendant le livre ; elle prolonge la
question de sortie de la fiche n° 12) :
**« Quelle livraison proposons-nous, différente de la précédente, et pour qui ? »**
Tu y réponds par une proposition, que Pascal accepte ou non : ce qu'un bénéficiaire nommé
au brief peut prendre en main à la fin du cycle (une version, une fonction dont il se
sert, une page publiée), et en une ligne, ce qu'elle apporte de plus que la
dernière livraison inscrite au kanban pour un cycle (ligne `cycle N`, pas un bilan).
Une livraison qui reprend la précédente sous un
autre nom n'en est pas une. Si tu n'en trouves pas de différente, le cycle livre sa
mauvaise nouvelle, car, comme l'a dit Pascal le 22 octobre 2026,
« une mauvaise nouvelle est une livraison sur laquelle on apprend » : annonce-la comme à
l'étape 6, et propose ce qu'elle nous apprend.
La question se pose à chaque `/boucle`, même quand le plafond l'a arrêtée à l'étape 1.

Après la réponse de Pascal, ajoute une ligne à la rubrique « Livraisons » du kanban, sous
la précédente, avec N le dernier cycle que l'étape 7 vient d'augmenter : la livraison
retenue, ou la mauvaise nouvelle et ce qu'elle nous apprend.
