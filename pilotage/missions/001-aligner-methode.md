# Mission 001 — aligner le texte de la méthode sur le livre imprimé

> Fiche de mission (fiches n° 9 et 15). Brief : `docs/brief.md` (v0.2.0, validé par
> Pascal le 21 octobre 2026). Une mission = une phrase = une branche = une PR.

## Mission

**En une phrase (quoi, et pourquoi) :** aligner `skills/methode` (et les agents et la
commande qui en reprennent les formules) sur le livre imprimé du 20 octobre 2026, pour
que livre et plugin disent la même chose.

**Redite par l'agent :** le plugin cite encore le premier jet ; je reprends les formules
fixées par le livre, et un test vérifie qu'elles y sont et que les anciennes n'y sont plus.

## Les trois questions (règle de staffing)

| Question | Réponse | Conséquence |
|---|---|---|
| Peut-il redire la mission en une phrase, avec son but ? | oui | |
| Sait-il comment faire ? (sources, conventions nommées ci-dessous) | **non tant que le livre n'est pas accessible** | appuyer : plan relu par Pascal (fait le 21 octobre 2026) ; texte du livre à fournir |
| A-t-il les moyens ? (outils, données d'essai, tests) | oui | `tests/test_alignement_livre.py` |

**Temps de la main :** **tenir** — c'est le texte de la méthode. Plan validé par Pascal le
21 octobre 2026, avec les oublis du brief.

## Plan validé par Pascal

0. Tests d'abord : `tests/test_alignement_livre.py`, rouge avant les changements.
1. En-tête et description de `skills/methode` : source = livre imprimé (PDF KDP du
   20 octobre 2026, p. 203-275), plus « premier jet ».
2. Statut « proposition à valider » de la règle de staffing : **retiré** (le livre la valide).
3. Harnais en sept points : brief, harnais, tests, terrain, **équipe**, **ma réponse
   d'abord**, qui tranche (fiche 15) ; aussi dans `skills/mission/SKILL.md`.
4. FRANCE : « **A**nticiper » ; décider si l'on est prêt à payer le sacrifice (fiche 4).
5. Plier ou tenir dans l'ordre du livre : d'abord « si je tiens, qui paie ? », puis
   « si je plie, qui paie ? » ; pas prêt à payer : ne pas faire semblant de tenir
   (fiche 14) ; aussi dans `agents/dev.md`.
6. Oublis du brief, ajoutés par Pascal : « Libre ne veut pas dire éternel », et trois
   « non » aux questions Choisir → migrer en priorité (fiche 11) dans
   `skills/methode`, `agents/archiviste.md`, `agents/relecteur.md`.

Le critère d'arrêt de la relecture relève de la mission 003.

## L'Homme

- **Agent :** `archiviste`.
- **Ce qui ne lui est pas demandé :** changer le déroulé, ajouter une règle que le livre
  ne porte pas, toucher aux hooks.

## Harnais

- **Peut :** `skills/methode/SKILL.md`, `skills/mission/SKILL.md`, `agents/dev.md`,
  `agents/archiviste.md`, `agents/relecteur.md`, `tests/test_alignement_livre.py`, la CI,
  le README.
- **Ne doit pas :** reformuler le livre de mémoire : chaque formule nouvelle vient du
  livre imprimé, citée avec sa fiche.
- **Sources autorisées :** le livre imprimé (Boîte à outils p. 203-275), `docs/brief.md`.

## Tests

- **Comment saura-t-on que c'est juste :** `python3 tests/test_alignement_livre.py`
  vert dans la CI ; Pascal compare les passages au livre.

## Terrain

- **Échantillon que Pascal vérifiera :** la section « Le harnais » et « Plier ou tenir »
  de `skills/methode`, côte à côte avec les fiches 14 et 15 du livre.

## Qui veille, qui tranche

- **Relecteur :** `relecteur`, puis Pascal. **Critère d'arrêt de la relecture :** 3
  allers-retours, puis Pascal tranche.
- **Qui tranche :** Pascal.

## Comment saura-t-on que ça marche ?

L'étape « Alignement du plugin sur le livre imprimé » est verte dans la CI.
