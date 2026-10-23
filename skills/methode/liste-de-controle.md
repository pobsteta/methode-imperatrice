# Liste de contrôle avant de dire « prêt »

> Auto-relecture de l'**acquéreur** et du **testeur** (fiches n° 5 et 15 de la méthode),
> à remplir **avant** de rendre le travail. Elle vient du bilan n° 1 du projet terrain
> (2026-10-23) : 28 % des « à reprendre » du relecteur tenaient à des sources ou des
> chiffres incomplets (cause B). Chaque point renvoie à une ligne du `pilotage/journal.md`
> de terrain (« j. NN »). Cocher un point, c'est l'avoir fait, pas croire l'avoir fait.

## 1. Chaque chiffre a sa source, et son emplacement
- [ ] Pour chaque valeur (couleur, seuil, code, ratio) : la **source**, la **page ou la
  ligne exacte**, la **version** et la **date de consultation**. Une valeur sans source
  n'entre pas : elle est signalée, pas gardée. (j. 48 : #237F52 sans source, bloquant ; #F9A800, source à citer)
- [ ] Les URL réellement consultées sont inscrites, avec la méthode quand elle compte.
  (j. 52 : URL du nuancier RAL et méthode non précisées)
- [ ] Une référence qui change avec la version (jar, bibliothèque, standard) est **datée
  par cette version**, et ce qu'on en dit est vrai pour elle. (j. 37 : jar de sources 1.4.0 ;
  j. 43 : consigne « public val » fausse en 1.4.0)
- [ ] Les numéros de ligne cités ont été **relus sur le fichier à jour**. (j. 37)

## 2. Les décomptes sont complets
- [ ] Tout ce qui se compte a été **compté en entier**, pas sur un échantillon : fichiers,
  imports, valeurs, couples. Le nombre inscrit est celui de la commande de comptage,
  relancée avant le rendu. (j. 37 : 8 fichiers, pas 2 ; 43 fichiers `.kt` tous vérifiés)
- [ ] Une correction de décompte corrige **les deux termes** : le nombre qui change et le
  nombre qui reste identique. (j. 93 : 10 valeurs changent et 86 restent, pas 13 et 83)
- [ ] Un tableau ou une liste ne **omet** aucune entrée de sa série. (j. 37 : CMF absent d'E1)

## 3. Les termes sont exacts
- [ ] Les bornes, plages et étendues sont recopiées **de la mesure**, pas de mémoire.
  (j. 55 : écart de 4° à 19°, pas 10° à 13° ; j. 52 : concordance de 142° à 157°)
- [ ] Une valeur ajoutée à un endroit est **ajoutée partout où elle se retrouve** :
  comparaisons côte à côte, récapitulatif, numérotation des sections. (j. 52 : #E6B019 au côte à côte et en §8 ; numérotation de §5)
- [ ] Les limites sont dites : ce qu'on écrête, ce qui n'est lisible qu'à un seul endroit.
  (j. 48 : écrêtage à préciser ; j. 68 : marges lisibles seulement dans le rapport XML)

## 4. Le statut est dit tel qu'il est
- [ ] Ouvert, fusionné, levé, à trancher : chaque élément porte son **état du jour**, et une
  réserve levée est dite levée. (j. 43 : commit présenté comme ouvert, réserve à lever)
- [ ] Les **dépendances entre PR** sont écrites (« fusion avec 006 et 007, jamais avant ») et
  la branche est à jour de `main`. (j. 68 ; j. 55 : branche rebasée)

## 5. Pour le testeur, en plus
- [ ] Une assertion **exacte** : un `contains` trop large laisse passer l'erreur que le test
  devait attraper. (j. 68 : test README à rendre exact)
- [ ] Le vert **prouve quelque chose** : le test a échoué avant, ou a été essayé contre une
  erreur volontaire ; ce qui n'est pas compilé ou pas branché est dit. (j. 68 : compilation vérifiée sur un bouchon)
- [ ] Les questions qui relèvent de Pascal (conventions, refus, périmètre) sont **posées**, pas tranchées. (j. 68)

Avant de rendre : relire la liste, une ligne à la fois, puis écrire dans le rendu
« liste de contrôle passée » ou les points non cochés et pourquoi.
