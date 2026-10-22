# Mission 011 — à chaque fin de cycle, une livraison différente de la précédente

> Fiche de mission (fiches n° 9 et 15). Première mission de la v0.3.0. Source : la
> réponse de Pascal du 22 octobre 2026 et le brief au livre
> (`docs/livre/brief-livraison-fin-de-cycle.md`), en attendant que le livre porte la
> formule. Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** faire proposer par `/boucle`, à chaque fin de
cycle, une livraison différente de la précédente et son bénéficiaire, et la faire inscrire
au kanban, pour qu'un cycle qui ne livre rien de neuf se voie tout de suite.

**Redite par l'agent :** la sortie de `/boucle` pose, après « qu'avons-nous décidé, qui
fait quoi, d'ici quand ? », la question de la livraison ; l'orchestrateur y répond par une
proposition qu'il compare à la dernière livraison inscrite au kanban ; Pascal tranche, et
la livraison retenue s'ajoute à une rubrique « Livraisons » du kanban.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | réponse de Pascal ; fiche n° 12 du livre imprimé (« Chaque rituel se clôt sur une question ») ; brief au livre |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | `tests/test_alignement_livre.py` |

**Temps de la main :** appuyer.

## Ma réponse d'abord

« La question de fin de cycle doit proposer un produit de livraison différent de la
précédente. » — Pascal, le 22 octobre 2026, demandée au lancement de la mission, avant
toute écriture.

## L'Homme

- **Agent :** `testeur` puis `dev`.
- **Ce qui ne lui est pas demandé :** changer le livre (à Pascal) ; toucher au `/bilan`,
  qui lira les livraisons plus tard s'il le faut.

## Harnais

- **Peut :** `skills/boucle/SKILL.md`, `skills/demarrer/gabarit-kanban.md`,
  `tests/test_alignement_livre.py`, `docs/livre/`, `.claude-plugin/plugin.json`, le README.
- **Ne doit pas :** parler de MVP (le livre dit « pas le minimum, le nécessaire à la
  décision ») ; toucher aux hooks ; fusionner sans Pascal.
- **Sources autorisées :** le livre (fiche n° 12), la réponse de Pascal, le brief au livre.

## Tests

- **Comment saura-t-on que c'est juste :** `tests/test_alignement_livre.py` trouve la
  question de la livraison dans `/boucle` et la rubrique « Livraisons » dans le gabarit
  du kanban.

## Terrain

- **Échantillon que Pascal vérifiera :** à la fin d'une `/boucle` de Surculus, une
  livraison proposée, nommant son bénéficiaire et ce qu'elle apporte de plus que la
  précédente.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

Deux `/boucle` de suite qui ne livrent rien de neuf sont annoncées comme telles, au lieu
de passer sous silence.
