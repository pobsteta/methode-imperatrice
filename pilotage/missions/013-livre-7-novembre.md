# Mission 013 — aligner le plugin sur le livre du 7 novembre (version 1.0.0)

> Fiche de mission (gabarit 1.0.0). Regroupe les missions 013 à 020 du brief
> `docs/brief-v1.0.0.md`, menées en une seule PR à la demande de Pascal.

## Mission

**En une phrase (quoi, et pourquoi) :** faire dire au plugin, avec les mêmes mots, ce que
dit le livre du 7 novembre 2026 (prendre / donner / rendre, harnais en huit points, degré
de la main, jamais au pivot, lancer petit), pour que Pascal, les projets et les lecteurs
lisent la même méthode.

**Redite par l'agent :** le livre a changé de mots et de règles ; le plugin les reprend,
borne la délégation à ce que le livre laisse à l'IA, et passe en 1.0.0.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | oui | |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | |

**Temps de la main :** prendre — c'est le texte de la méthode ; Pascal a validé le brief
avant exécution.

**Degré de la main :** le chef tranche — Pascal a tranché les quatre points du brief.

## Ma réponse d'abord

> « Modifie comme tu le dis, mets 1.0.0, fais tout ce qu'il faut et commite, fusionne et
> merge. » — Pascal, le 16 novembre 2026.

## L'Homme

- **Agent :** l'orchestrateur (Claude), à la demande directe de Pascal.
- **Ce qui ne lui est pas demandé :** aucun hook nouveau ; aucun changement de commande.

## Harnais

- **Peut (périmètre) :** `skills/`, `agents/`, `tests/test_alignement_livre.py`, `README.md`,
  `.claude-plugin/plugin.json`, `docs/`, `pilotage/missions/013-livre-7-novembre.md`,
  `pilotage/journal.md` (ajout seul).
- **Câblé (ne peut pas) :** `main` (protégée), journal en ajout seul (CI).
- **Ne doit pas (écrit) :** toucher `hooks/`, `LICENSE`, `.github/` ; réécrire les fiches et
  le journal passés.
- **Sources autorisées :** le livre (PDF KDP du 7 novembre 2026, Boîte à outils
  p. 207-286), `docs/brief-v1.0.0.md`.

## Journal

- **Ce que l'agent inscrit :** une ligne pour la mission et une pour la version, dans
  `pilotage/journal.md`.

## Valeur provisoire (chiffre, réglage)

aucune

## Dépend de / rouge attendu jusqu'à

aucune

## Tests

- `python3 tests/test_alignement_livre.py` (nouveaux marqueurs 1.0.0), tests des hooks,
  `claude plugin validate .`, `python3 scripts/verifier_version.py`.

## Terrain

- **Échantillon que Pascal vérifiera :** dans Surculus, après `/plugin marketplace update
  pobsteta`, une fiche ancienne en « appuyer » est lue comme « donner » ; `/boucle`
  signale deux missions qui partagent un fichier.

## Qui veille, qui tranche

- **Relecteur :** Pascal.
- **Critère d'arrêt de la relecture :** 3 allers-retours.
- **Qui tranche :** Pascal. La fusion publie la release v1.0.0 (ce qui touche l'extérieur) :
  Pascal l'a demandée.

## Comment saura-t-on que ça marche ?

La CI est verte, la release v1.0.0 est publiée, et Surculus fait tourner une `/boucle` avec
les nouveaux mots.
