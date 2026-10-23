# Mission NNN — titre court

> Gabarit (fiches n° 9 et 15 de la méthode). Rempli par l'orchestrateur **avant** de
> confier la mission ; relu à chaque point. Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** _…_

**Redite par l'agent :** _à compléter par l'agent avant d'agir — s'il n'y arrive pas, il s'arrête._

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui / non | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui / non | |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui / non | |

**Temps de la main :** tenir / appuyer / lâcher — _et pourquoi._

## Ma réponse d'abord

_Rempli par Pascal seul, avant de lire le travail de l'agent : ce qu'il attend de la
mission, et le résultat qu'il prévoit. Une ligne suffit. L'orchestrateur ne le remplit
pas._

## L'Homme

- **Agent :** `dev` / `testeur` / `afficheur` / …
- **Modèle :** _sonnet par défaut ; opus si la mission engage l'architecture._
- **Ce qui ne lui est pas demandé :** _…_

## Harnais

- **Peut :** _…_
- **Ne doit pas :** _sortir du périmètre, inventer un code, toucher à `main`, …_
- **Sources autorisées :** _fichiers, référentiels, ADR à lire — juste le nécessaire._

## Valeur provisoire (chiffre, réglage)

_Si la mission fixe ou reprend une valeur (seuil, couleur, durée, taille, format, délai…) qu'on n'a
pas encore mesurée, la dire ici ; sinon écrire « aucune » (une ligne suffit)._

- **Valeur provisoire :** _la valeur retenue pour avancer, marquée « provisoire » partout où elle apparaît._
- **Mesurée par :** _l'outil tiers, l'essai ou la personne qui la mesurera, et à quelle date._
- **Gel :** _avant quelle étape elle doit être mesurée (ADR, spec, publication) ; la valeur ne se grave pas avant._

**Si la mesure est dans les moyens de la mission, elle en est la première tâche**, avant
d'écrire ce qui en dépend. Si elle revient à un autre (essai de Pascal, outil tiers
absent), elle devient une mission préalable (règle de staffing, « non à la 3e question »),
ou la valeur reste provisoire jusqu'à sa date et rien de ce qui en dépend ne gèle avant.
Qui juge la mesure suffisante : Pascal (« Qui tranche »).

## Tests

- **Comment saura-t-on que c'est juste :** _tests automatiques attendus, critères d'acceptation._

## Terrain

- **Échantillon que Pascal vérifiera :** _un écran, un export, un cas réel, sur le terrain._

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal.
- **Critère d'arrêt de la relecture :** _3 allers-retours par défaut (fiche n° 15 : « Fixer
  d'avance quand la boucle de relecture s'arrête ») ; au-delà, la décision remonte à
  Pascal._
- **Point de suivi :** _à quel moment l'orchestrateur fait le point._
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

_Un signe concret, et quand on le regarde._
