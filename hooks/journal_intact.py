#!/usr/bin/env python3
"""Hook Stop / SubagentStop, et contrôle CI : le journal commence par ce qu'il était.

Règle du sommier (méthode de l'Impératrice, fiche n° 11) : on n'efface pas, on ajoute.
Le filtre PreToolUse (journal_ajout_seul.py) regarde les commandes ; il ne verra jamais
tout (variable, script, glob). Ce contrôle-ci regarde le résultat : le journal
d'aujourd'hui doit commencer, octet pour octet, par sa version de référence.

- À l'arrêt d'un agent : la référence est le dernier commit, et, si la branche a un
  amont, le dernier état commun avec lui (un historique poussé puis réécrit se voit).
  Si l'invariant est rompu, l'arrêt est refusé une fois ; au second arrêt on laisse
  finir (pas de boucle sans fin) : la CI garde.
- En CI : `python3 hooks/journal_intact.py --depuis origin/main` compare le journal du
  dernier commit à celui de la base commune avec la référence ; code 1 s'il est rompu.

Un journal absent de la référence n'est pas contrôlé (il est nouveau).
"""
import json
import os
import subprocess
import sys

JOURNAUX = ("pilotage/journal.md", "docs/journal.md")
MESSAGE = (
    "Arrêt refusé : le journal ne commence plus par ce qu'il était ({detail}). "
    "Règle du sommier : on n'efface pas, on ajoute. Dis à l'orchestrateur ce qui s'est "
    "passé : seul un humain rétablit le journal (git show {ref}:{chemin}), puis on "
    "ajoute en fin de fichier."
)


def git(*args, cwd):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, timeout=10)
    return r.stdout if r.returncode == 0 else None


def contenu(ref, chemin, cwd):
    return git("show", f"{ref}:{chemin}", cwd=cwd)


def base_commune(ref, cwd):
    sortie = git("merge-base", ref, "HEAD", cwd=cwd)
    return sortie.decode().strip() if sortie else None


def rupture(reference, actuel):
    """Description de la rupture, ou None si `actuel` commence par `reference`."""
    if actuel is None:
        return "journal supprimé"
    if actuel.startswith(reference):
        return None
    if reference.startswith(actuel):
        return "journal tronqué"
    return "inscription modifiée ou supprimée"


def controle_ci(depuis):
    cwd = os.getcwd()
    base = base_commune(depuis, cwd) or depuis
    rompu = False
    for chemin in JOURNAUX:
        reference = contenu(base, chemin, cwd)
        if reference is None:
            continue
        detail = rupture(reference, contenu("HEAD", chemin, cwd))
        if detail:
            print(f"::error file={chemin}::{chemin} : {detail} depuis {depuis} ({base[:7]}). "
                  "Le journal est en ajout seul.")
            rompu = True
        else:
            print(f"{chemin} : en ajout seul depuis {depuis}.")
    sys.exit(1 if rompu else 0)


def controle_arret():
    try:
        entree = json.load(sys.stdin)
    except Exception:
        entree = {}
    cwd = entree.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    try:
        racine = git("rev-parse", "--show-toplevel", cwd=cwd)
    except Exception:
        racine = None
    if not racine:
        sys.exit(0)
    racine = racine.decode().strip()

    references = ["HEAD"]
    amont = git("rev-parse", "-q", "--verify", "@{upstream}", cwd=racine)
    if amont:
        commune = base_commune("@{upstream}", racine)
        if commune:
            references.append(commune)

    for chemin in JOURNAUX:
        try:
            with open(os.path.join(racine, chemin), "rb") as f:
                actuel = f.read()
        except FileNotFoundError:
            actuel = None
        for ref in references:
            reference = contenu(ref, chemin, racine)
            if reference is None:
                continue
            detail = rupture(reference, actuel)
            if detail:
                print(MESSAGE.format(detail=detail, ref=ref if ref == "HEAD" else ref[:12],
                                     chemin=chemin), file=sys.stderr)
                # Second arrêt : on laisse finir, la CI garde.
                sys.exit(0 if entree.get("stop_hook_active") else 2)
    sys.exit(0)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--depuis":
        controle_ci(sys.argv[2])
    controle_arret()


if __name__ == "__main__":
    main()
