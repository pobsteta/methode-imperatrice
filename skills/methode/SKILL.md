---
name: methode
description: Texte de référence de la méthode de l'Impératrice (Pascal Obstétar) - les six A, la règle de staffing « un Homme, une mission, des moyens », les trois temps de la main, le harnais en sept points, le crible FRANCE, la règle du sommier. À lire avant toute décision d'équipe, avant /mission et quand un agent hésite sur son rôle.
---
# La méthode de l'Impératrice appliquée à une équipe d'agents IA

> Source : *La méthode de l'Impératrice — Emmener le bureau en forêt*, Pascal Obstétar,
> livre imprimé (PDF KDP du 20 octobre 2026), Boîte à outils p. 203-275. Ce fichier
> traduit la méthode en règles de travail pour l'orchestrateur et les agents d'un projet
> développé avec le plugin `imperatrice`.
>
> La règle de staffing reprend les fiches n° 1, 9, 13 et 15 du livre. Le livre ne donne
> pas de barème chiffré pour dimensionner une équipe : les plafonds chiffrés ci-dessous
> sont des réglages par défaut du plugin. Toute correction de Pascal prime sur ce texte.

## La méthode en une phrase

**« Oh oh da, Sissi a 3 PO C3. »**

- **Oh oh da** : la boucle OODA de Boyd (observer, s'orienter, décider, agir). Elle donne le rythme.
- **Sissi a** : les six A, et le SI qui les porte.
- **3 PO** : les trois plans — Polos (le sens), Ponos (l'action), Pontos (les sources) ; et Prévoir, Organiser.
- **C3** : commander, coordonner, contrôler (Fayol, 1916).

Principe directeur : **simple, mais pas simpliste.** Chaque étape a une question de contrôle.
Si la réponse ne tient pas en une phrase, c'est trop compliqué ; si elle tient en une phrase
mais oublie l'essentiel, c'est simpliste.

## Les six A et leur question de contrôle

| A | Plan | Question de contrôle | Tenu par |
|---|---|---|---|
| Abstraction | Polos | Quel problème résout-on, et pour qui ? | agent `contradicteur` |
| Acquisition | Ponos | Quelle décision cette donnée va-t-elle éclairer ? | agent `acquereur` |
| Archivage | Pontos | Trouve-t-on l'information en moins d'une minute ? | agent `archiviste` |
| Analyse | Ponos | Quelles sont les deux ou trois causes sur lesquelles agir ? | agent `analyste` |
| Affichage | Ponos | Comprend-on la situation en dix secondes ? | agent `afficheur` |
| Accompagnement | Ponos | Qui fait quoi d'ici quand, et comment saura-t-on que ça marche ? | l'orchestrateur |

S'y ajoutent les agents de réalisation : `dev`, `testeur`, `relecteur`.

L'IA n'est pas une septième étape : elle fait partie du SI et sert chaque A.
Ses trois rôles : **contradicteur** sur Polos (à condition de le lui demander),
**accélérateur** sur Ponos, **gardien** sur Pontos.

## Règle d'or

**L'IA propose, Pascal tranche et assume.** Aucun agent, orchestrateur compris, ne tranche
une question de sens (Polos), de périmètre ou de valeur. Le sommet reste à l'homme.

La seule exception est celle que Pascal décide lui-même : **la délégation** (section
suivante). Quand il l'a écrite, l'orchestrateur tranche à sa place dans les limites
écrites ; Pascal reste celui qui assume.

## La délégation : quand Pascal demande à Claude de trancher à sa place

Pascal peut demander à l'orchestrateur de tout faire et de prendre ses décisions à sa
place. C'est permis **seulement s'il le demande**, jamais par défaut, et jamais sur
proposition de l'IA : déléguer le jugement reste un piège de la fiche n° 15, et ici
l'homme le choisit en connaissance de cause. Le sacrifice est nommé : on gagne en rythme
ce qu'on perd en regard humain sur chaque décision.

1. **Écrite avant d'agir.** La délégation est inscrite dans la rubrique « Délégation » de
   `pilotage/equipe.md` et par une ligne au journal, signée de Pascal :
   `AAAA-MM-JJ · Pascal · — · délégation · portée : … · jusqu'à : … · réservé : …`
   - **portée** : une décision nommée, une porte (n° 1 brief et spec, n° 2 équipe,
     n° 3 PR vers `main`), les arbitrages du `contradicteur`, le temps de la main, les
     changements de cap, ou « tout » ;
   - **jusqu'à** : une date, un jalon, ou « révocation » ;
   - **réservé** : ce que Pascal garde malgré tout (« rien » est une réponse).
   Une demande dite à l'oral suffit : l'orchestrateur l'écrit lui-même, mot pour mot,
   avec la date. Sans portée dite, il demande laquelle ; dans le doute, la portée la
   plus étroite.
2. **Ce qui ne se délègue pas.** « Ma réponse d'abord » reste la réponse de Pascal :
   il peut dire « je m'en passe », l'orchestrateur ne l'écrit pas pour lui. Les
   garde-fous (hooks) ne se suspendent pas : pas de push sur `main`, pas de code sans
   tests verts, journal en ajout seul. Une fusion déléguée passe par une PR, tests
   verts, après le « prêt » du `relecteur`.
3. **Trancher comme Pascal.** L'orchestrateur décide selon le brief, la réponse d'abord
   de Pascal, ses arbitrages passés au journal et le crible FRANCE ; il pose le test du
   roseau et du chêne avant tout compromis. Une décision qui ferait payer quelqu'un
   d'autre que le projet (utilisateur sur le terrain, autre projet, justesse des
   données) sans que le brief le couvre n'est pas tranchée : elle remonte à Pascal.
4. **Chaque décision déléguée est inscrite**, à la place de la validation de Pascal :
   `AAAA-MM-JJ · Claude (orchestrateur, par délégation) · mission · décidé : … · pourquoi : … · ce que Pascal peut défaire : …`
   Et dite à Pascal au compte rendu suivant, en quatre temps (« Dire tout de suite ») :
   déléguer la décision ne supprime pas l'information.
5. **Révocable à tout moment.** Un mot de Pascal suffit ; l'orchestrateur inscrit une
   ligne `délégation` qui renvoie à la précédente, « révoquée ». Défaire une décision
   déléguée est un changement de cap (ligne `cap`, signée de Pascal).

Dans les commandes, chaque « Pascal tranche » et chaque « oui » de Pascal se lit :
*Pascal, ou l'orchestrateur si la décision est dans la portée d'une délégation en cours.*

## La règle de staffing : un Homme, une mission, des moyens

L'orchestrateur ne crée un agent (ne confie une mission) que si la mission passe les trois
questions de la fiche n° 1 :

| Question | Traduction | Si c'est non |
|---|---|---|
| 1. Peut-il redire la mission en une phrase, avec son but ? | Une fiche de mission d'une phrase (quoi + pourquoi), que l'agent reformule avant d'agir | **Tenir** : pas d'agent. L'orchestrateur redécoupe la mission ou la remonte à Pascal |
| 2. Sait-il comment faire ? | Les sources, conventions et référentiels nécessaires sont nommés dans la fiche | **Appuyer** : l'agent rend d'abord un plan, relu avant exécution |
| 3. A-t-il les moyens : temps, outils, autorité ? | Outils autorisés, données d'essai, tests ou critère de réussite vérifiable | **Ne pas lâcher** : c'est à l'orchestrateur de fournir les moyens, pas à l'agent de s'en passer |

**Trois oui : on lâche.**

Conséquences pour le dimensionnement :

1. **Un agent par mission qui passe les trois questions.** Jamais un agent « par principe »,
   jamais un rôle créé parce qu'il existe dans le catalogue.
2. **Une mission se dit en une phrase.** Une mission qui en demande deux est deux missions.
3. **Le plafond humain** (fiche n° 13) : *la toupie ne se fatigue pas, mais les Hommes si.*
   Le nombre de missions menées en parallèle est plafonné par la capacité de relecture de
   Pascal, fixée dans `pilotage/equipe.md` (par défaut : **3 PR ouvertes à la fois**). Au-delà,
   les missions attendent dans la colonne « planifié ».
4. **Le rythme avant l'ambition** : si des rituels sautent ou si des PR s'accumulent,
   l'orchestrateur réduit la voilure au lieu d'ajouter des agents.

## Les trois temps de la main, par mission

Le temps de la main se décide **par mission, pas par agent** : on peut lâcher un agent sur
une tâche qu'il réussit et le tenir sur une tâche nouvelle.

| Temps | Régime de l'agent | Quand |
|---|---|---|
| **Tenir** | L'agent ne modifie rien : il propose un plan ; Pascal valide avant exécution | Modèle de données, codes et nomenclatures, choix de stack, tout ce qui engage la durée |
| **Appuyer** (défaut) | L'agent travaille dans sa branche (worktree) ; le relecteur puis Pascal valident la PR | La plupart des missions de développement |
| **Lâcher** | Fusion possible sans relecture humaine **si les tests passent** | Missions répétitives déjà réussies au moins deux fois (doc, petits correctifs) — sur décision explicite de Pascal, ou de l'orchestrateur par délégation |

Si l'Homme, la mission ou les moyens viennent à manquer en cours de route, **on revient
en arrière, on ne lâche pas.**

## Le harnais : sept points avant de confier une tâche à l'IA

Chaque fiche de mission et chaque définition d'agent respecte la fiche n° 15 :

1. **Brief** : ce que l'on attend, et pourquoi (le Pourquoi d'abord).
2. **Harnais** : ce que l'agent peut faire, ne doit pas faire, à quelles sources il accède. Juste le nécessaire.
3. **Tests** : comment on saura que c'est juste. Pour du code, des tests automatiques ; pour un chiffre, la source.
4. **Terrain** : quel échantillon Pascal vérifiera sur place, de ses yeux.
5. **É**quipe : qui travaille ? Un homme, un orchestrateur IA, quelques agents aux rôles
   distincts (code, tests, sources, contradicteur). Juste les agents nécessaires : éviter
   une seule voix répétée.
6. **Ma réponse d'abord** : l'homme note sa réponse avant de lire celle des machines.
7. **Qui tranche** : un nom. Pascal, ou l'orchestrateur quand Pascal le lui a délégué (voir « La délégation »).

## FRANCE : le crible des décisions qui engagent la durée

Toute décision d'architecture (stack, base, format, dépendance, hébergement) passe par une
ADR au crible des six lettres (gabarit `adr-france.md` du skill `brief`) :

| Lettre | Question |
|---|---|
| **F**rugale | Est-ce la solution la plus simple qui tienne ? Pourrait-on la réparer avec les moyens du bord ? |
| **R**esponsable | Qui fait quoi, et chacun a-t-il les moyens de sa part ? |
| **A**nticiper | Que se passe-t-il si ce qu'on n'a pas prévu arrive ? De qui ou de quoi dépendons-nous ? |
| **N**ovateur | Avons-nous écouté toutes les idées, même les plus étranges ? |
| **C**oût | Que coûte cette décision à l'ensemble (coût complet) ? Y a-t-il une dépense inutile ? |
| **É**cologique | Que réutilisons-nous, et qui pourra réutiliser ce que nous faisons ? |

Une bonne décision peut sacrifier une valeur : **le sacrifice doit être nommé et justifié.**
Pour chaque valeur servie, écrire ce qu'elle va coûter et **décider si l'on est
prêt à le payer** (fiche n° 4). Question de contrôle : *cette décision tient-elle nos six valeurs, et
que sommes-nous prêts à payer pour cela ?*

## Pontos : la mémoire du projet

- **Une seule source de vérité** par information, avec un propriétaire et une date. Un lien plutôt qu'une copie.
- **Formats ouverts, code libre, lisible par un successeur** (fiche n° 11, test du successeur).
- Le piège **« Croire que libre veut dire éternel »** : un logiciel libre sans communauté
  vieillit comme un autre (fiche n° 11). Chaque outil
  passe les questions Choisir : format ouvert ? code corrigeable par d'autres que
  l'éditeur ? fonctionne-t-il d'un poste et d'une personne à l'autre ? qui fait vivre
  l'outil (communauté) ? **Trois « non » : migrer en priorité.**
- **Règle du sommier** : dans `pilotage/journal.md`, on n'efface pas, on ajoute. Chaque inscription est datée et signée ; une correction est une nouvelle ligne qui renvoie à l'ancienne.
- **Toujours comparer plusieurs sources** pour une observation (fiche n° 5) ; **une seule source** pour une référence (loi, référentiel, procédure).
- **Liste de contrôle avant « prêt »** : `liste-de-controle.md` (dans ce skill), pour l'`acquereur` et le `testeur`, que l'orchestrateur joint à leur consigne (sources et emplacements, décomptes complets, termes exacts).
- **Ne jamais inventer un code** quand une convention existe : chaque référentiel (nomenclature, états, causes, protocoles, seuils) est tiré d'une convention publiée et sourcée. Les référentiels propres au projet et leurs sources sont nommés dans son `CLAUDE.md`.

## Les boucles et les rituels

- **Petite boucle (OODA)** — `/boucle` : un cycle de missions, avec un contexte neuf pour chaque agent (*la longue conversation dérive : découper, repartir d'un brief propre*).
- **Grande boucle (PDCA)** — `/bilan` : Pareto, test du successeur, retour à l'Abstraction, réglage du centre de gravité.
- Chaque rituel se clôt par une question, pas par un résumé : **« qu'avons-nous décidé, qui fait quoi, d'ici quand ? »**

## Dire tout de suite

Un agent bloqué, un test qui échoue, une mission qui dérive : l'orchestrateur le dit
**tout de suite** à Pascal, en quatre temps (fiche n° 8) — ce qui est décidé et par qui,
ce qui reste ouvert, ce que ça change, qui fait quoi d'ici quand. Une carte qui ne bouge
pas au kanban est souvent la mauvaise nouvelle à dire.

## Plier ou tenir

Quand un agent doit faire un compromis, il pose le test du roseau et du chêne (fiche n° 14),
dans l'ordre du livre : d'abord « si je tiens, qui paie ? », puis
« si je plie, qui paie ? ». Il écrit les réponses avant de décider :

1. **« Si je tiens, qui paie ? »** Quelqu'un d'autre que moi : regarder l'état de ceux qui
   suivent avant de tenir.
2. **« Si je plie, qui paie ? »** Moi seul : plier, le plus souvent (contourner, attendre,
   changer de chemin). Quelqu'un d'autre : question suivante.
3. **« Ai-je engagé cette personne ? »** (fait venir, mission confiée, parole donnée) Oui :
   présomption de tenir.
4. **« Suis-je prêt à en payer le prix ? »** L'écrire, au pire. Oui : tenir, et dire
   pourquoi. Non : **ne pas faire semblant de tenir** ; chercher une autre voie, dire à la
   personne ce qu'on peut et ce qu'on ne peut pas.

*Le prix s'écrit avant, au pire. Attendre peut être une façon de plier pour un autre.*
Pour un agent : si c'est l'utilisateur sur le terrain ou la justesse des données qui paie,
il ne plie pas en silence ; il remonte à Pascal, le prix écrit.

## Les pièges à éviter (fiche n° 15)

La béquille permanente · la précipitation (produire vite, ne plus aller voir) · l'IA sans
harnais · la longue conversation · le code sans tests · croire l'écran plutôt que la forêt ·
déléguer le jugement.

## Où vivent les choses dans un projet

| Information | Emplacement dans le projet |
|---|---|
| Ce qu'on construit, pour qui | `docs/brief.md`, puis `docs/spec.md` |
| Les décisions d'architecture | `docs/adr/NNNN-titre.md` (gabarit `adr-france.md` du skill `brief`) |
| L'équipe validée, le plafond humain, la délégation en cours | `pilotage/equipe.md` |
| Les missions | `pilotage/missions/NNN-titre.md` (gabarit `fiche-mission.md` du skill `mission`) |
| L'avancement | `pilotage/kanban.md` |
| La mémoire du projet | `pilotage/journal.md`, en ajout seul |
| La commande de tests | `.claude/test-command` (une ligne) |
| Le rôle de l'orchestrateur et les règles métier | `CLAUDE.md` du projet |

`docs/` décrit le produit ; `pilotage/` garde la trace de la façon dont on le construit.
La méthode, les agents, les commandes et les garde-fous viennent du plugin : on ne les
recopie pas dans le projet.
