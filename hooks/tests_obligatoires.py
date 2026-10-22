#!/usr/bin/env python3
"""Hook Stop / SubagentStop : pas de « terminé » sans tests verts.

Méthode de l'Impératrice, fiche n° 15 : « avec l'IA, et surtout avec elle, les tests
sont obligatoires ». Si du code a changé (hors docs/, pilotage/ et .claude/) et que la commande
de tests du projet est définie dans .claude/test-command, on la lance ; si elle
échoue, l'agent ne peut pas s'arrêter et reçoit la sortie des tests.
Au second arrêt (l'agent repart déjà à cause de ce hook), on le laisse finir pour éviter
la boucle sans fin, mais si les tests sont encore rouges, on l'inscrit au journal
(arbitrage de Pascal, brief v0.2.0) : la mission n'est pas vérifiée, et cela se voit.
Si un autre lancement des tests tient le verrou au-delà du budget, le hook le traite
comme des tests trop longs : arrêt bloqué en le disant, ou inscrit au journal au second.
Tant que la stack n'est pas choisie (pas de .claude/test-command), le hook ne fait rien.
Le hook ne connaît aucun domaine : l'environnement propre au projet (ANDROID_HOME par
exemple) s'écrit dans sa commande de tests ou dans ses réglages locaux (ADR 0001).
"""
import datetime
import json
import os
import subprocess
import sys
import time

# Attente du verrou et tests partagent ce budget, en secondes. Il reste sous le
# « timeout » de 660 s de hooks/hooks.json : au-delà, Claude Code couperait le hook et
# l'agent s'arrêterait sans vérification (mission 012). La variable
# IMPERATRICE_BUDGET_TESTS ne sert qu'aux tests du hook.
BUDGET = 630
JOURNAL = os.path.join("pilotage", "journal.md")


def inscrire_au_journal(racine, commande, motif):
    """Ajoute une ligne datée en fin de journal, s'il existe (on ne le crée pas)."""
    chemin = os.path.join(racine, JOURNAL)
    if not os.path.isfile(chemin):
        return
    with open(chemin, encoding="utf-8") as f:
        fin = f.read()[-1:]
    ligne = (f"{datetime.date.today().isoformat()} · hook tests_obligatoires · — · "
             f"arrêt accepté au second essai sans tests verts ({motif}, `{commande}`) : "
             "mission non vérifiée, à reprendre.\n")
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(("\n" if fin not in ("", "\n") else "") + ligne)


def main():
    try:
        entree = json.load(sys.stdin)
    except Exception:
        entree = {}
    # Si l'agent repart déjà à cause de ce hook, on le laissera finir (pas de boucle sans
    # fin), mais des tests encore rouges seront inscrits au journal.
    second_arret = bool(entree.get("stop_hook_active"))

    racine = os.environ.get("CLAUDE_PROJECT_DIR") or entree.get("cwd") or os.getcwd()
    cwd = entree.get("cwd") or racine
    fichier_commande = os.path.join(racine, ".claude", "test-command")
    if not os.path.isfile(fichier_commande):
        sys.exit(0)
    with open(fichier_commande, encoding="utf-8") as f:
        commande = f.read().strip()
    if not commande:
        sys.exit(0)

    try:
        statut = subprocess.run(
            ["git", "status", "--porcelain"], cwd=cwd,
            capture_output=True, text=True, timeout=10,
        ).stdout.splitlines()
    except Exception:
        sys.exit(0)
    code_modifie = [
        l for l in statut
        if not l[3:].startswith(("docs/", "pilotage/", ".claude/", "README", "CLAUDE.md"))
    ]
    if not code_modifie:
        sys.exit(0)

    budget = BUDGET
    try:
        budget = int(os.environ.get("IMPERATRICE_BUDGET_TESTS", BUDGET))
    except ValueError:
        pass
    debut = time.monotonic()

    # Deux lancements des tests dans le même dépôt se gênent (fichiers de build tronqués,
    # incident du 2026-10-16) : un verrou par dossier git fait attendre le second, dans
    # la limite du budget. POSIX seulement (fcntl) ; ailleurs, il est ignoré.
    verrou = None
    verrou_occupe = False
    try:
        dossier_git = subprocess.run(
            ["git", "rev-parse", "--absolute-git-dir"], cwd=cwd,
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        if dossier_git:
            import fcntl
            verrou = open(os.path.join(dossier_git, "imperatrice-tests.lock"), "w")
            while True:
                try:
                    fcntl.flock(verrou, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except BlockingIOError:
                    if time.monotonic() - debut >= budget:
                        verrou_occupe = True
                        break
                    time.sleep(1)
    except Exception:
        verrou = None

    attente = int(time.monotonic() - debut)
    if verrou_occupe:
        if second_arret:
            inscrire_au_journal(racine, commande,
                                f"verrou des tests occupé plus de {attente} s, tests non lancés")
            sys.exit(0)
        print(f"Un autre lancement des tests tient le verrou depuis plus de {attente} s : "
              "impossible de vérifier. Dis-le à l'orchestrateur, ne déclare pas la mission "
              "terminée.", file=sys.stderr)
        sys.exit(2)

    restant = max(1, budget - attente)
    try:
        resultat = subprocess.run(
            commande, shell=True, cwd=cwd,
            capture_output=True, text=True, timeout=restant,
        )
    except subprocess.TimeoutExpired:
        motif = f"délai de {restant} s dépassé"
        if attente:
            motif += f" après {attente} s d'attente du verrou"
        if second_arret:
            inscrire_au_journal(racine, commande, motif)
            sys.exit(0)
        print(f"Tests trop longs ({motif}) : impossible de vérifier. "
              "Dis-le à l'orchestrateur, ne déclare pas la mission terminée.", file=sys.stderr)
        sys.exit(2)

    if resultat.returncode != 0:
        if second_arret:
            inscrire_au_journal(racine, commande, f"tests rouges, code {resultat.returncode}")
            sys.exit(0)
        sortie = (resultat.stdout + "\n" + resultat.stderr)[-3000:]
        print(
            "Mission non terminée : les tests échouent (« un code qui a l'air juste "
            "n'est pas un code vérifié »). Corrige ou dis ce qui bloque.\n\n" + sortie,
            file=sys.stderr,
        )
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
