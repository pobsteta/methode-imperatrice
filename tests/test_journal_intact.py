#!/usr/bin/env python3
"""Cas du hook journal_intact.py (invariant du journal), rejouables sans toucher au dépôt.

    python3 tests/test_journal_intact.py

L'invariant : le journal d'aujourd'hui commence par sa version de référence (le dernier
commit, la branche amont, ou une référence donnée en CI). Il attrape ce qu'aucun filtre
de commandes ne voit : variables, scripts, globs, réécriture de l'historique.
"""
import json
import os
import subprocess
import sys
import tempfile

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks", "journal_intact.py")
J = "journal" + ".md"  # le hook de la session lit aussi ce fichier : pas de chemin en clair
L1 = "2026-10-20 · Pascal · 000 · un\n"
L2 = "2026-10-21 · dev · 001 · deux\n"


def git(*args, cwd):
    return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
                          cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def ecrire(depot, contenu, chemin=None):
    chemin = os.path.join(depot, chemin or os.path.join("pilotage", J))
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)


def depot_journal(tmp, contenu=L1 + L2):
    depot = os.path.join(tmp, "depot")
    os.mkdir(depot)
    git("init", "-q", "-b", "mission/x", cwd=depot)
    ecrire(depot, contenu)
    git("add", "-A", cwd=depot)
    git("commit", "-q", "-m", "journal", cwd=depot)
    return depot


def stop(depot, actif=False):
    entree = json.dumps({"hook_event_name": "Stop", "cwd": depot, "stop_hook_active": actif})
    env = dict(os.environ, CLAUDE_PROJECT_DIR=depot)
    return subprocess.run([sys.executable, HOOK], input=entree, capture_output=True,
                          text=True, env=env).returncode


def ci(depot, depuis):
    return subprocess.run([sys.executable, HOOK, "--depuis", depuis], cwd=depot,
                          capture_output=True, text=True).returncode


def cas_stop(nom, preparer, attendu, actif=False):
    with tempfile.TemporaryDirectory() as tmp:
        depot = depot_journal(tmp)
        preparer(depot, tmp)
        return nom, attendu, stop(depot, actif)


def rien(depot, tmp):
    pass


def ajout(depot, tmp):
    ecrire(depot, L1 + L2 + "2026-10-21 · dev · 001 · trois\n")


def tronque(depot, tmp):
    ecrire(depot, L1)


def milieu(depot, tmp):
    ecrire(depot, L1.replace("un", "UN") + L2)


def supprime(depot, tmp):
    os.remove(os.path.join(depot, "pilotage", J))


def par_script(depot, tmp):
    # Ce qu'aucun filtre de commandes ne voit : le chemin passe par une variable, dans un script.
    with open(os.path.join(depot, "ecrase.sh"), "w", encoding="utf-8") as f:
        f.write('F=pilotage/journal; echo x > "$F.md"\n')
    subprocess.run(["bash", "ecrase.sh"], cwd=depot, check=True)


def historique_reecrit(depot, tmp):
    # Journal poussé, puis réécrit et commité : HEAD et l'arbre sont d'accord, l'amont non.
    amont = os.path.join(tmp, "amont.git")
    git("init", "-q", "--bare", amont, cwd=tmp)
    git("remote", "add", "origin", amont, cwd=depot)
    git("push", "-q", "-u", "origin", "mission/x", cwd=depot)
    ecrire(depot, L2)
    git("commit", "-q", "-am", "réécrit", cwd=depot)


def pas_de_journal(depot, tmp):
    git("rm", "-q", "pilotage/" + J, cwd=depot)
    git("commit", "-q", "-m", "sans journal", cwd=depot)


def ancien_emplacement(depot, tmp):
    ecrire(depot, L1, os.path.join("docs", J))
    git("add", "-A", cwd=depot)
    git("commit", "-q", "-m", "ancien", cwd=depot)
    ecrire(depot, "", os.path.join("docs", J))


def cas_ci(nom, base, tete, attendu):
    """Commit de base (journal `base`, ou absent si None), commit de tête : contrôle CI."""
    with tempfile.TemporaryDirectory() as tmp:
        depot = os.path.join(tmp, "depot")
        os.mkdir(depot)
        git("init", "-q", "-b", "main", cwd=depot)
        ecrire(depot, "x\n", "README.md")
        if base is not None:
            ecrire(depot, base)
        git("add", "-A", cwd=depot)
        git("commit", "-q", "-m", "base", cwd=depot)
        git("checkout", "-q", "-b", "mission/x", cwd=depot)
        ecrire(depot, tete)
        git("add", "-A", cwd=depot)
        git("commit", "-q", "-m", "tête", cwd=depot)
        return nom, attendu, ci(depot, "main")


def main():
    resultats = [
        cas_stop("arrêt, journal inchangé", rien, 0),
        cas_stop("arrêt, ligne ajoutée", ajout, 0),
        cas_stop("arrêt, journal tronqué", tronque, 2),
        cas_stop("arrêt, ligne modifiée au milieu", milieu, 2),
        cas_stop("arrêt, journal supprimé", supprime, 2),
        cas_stop("arrêt, écrasé par un script et une variable", par_script, 2),
        cas_stop("arrêt, historique réécrit après push", historique_reecrit, 2),
        cas_stop("arrêt, pas de journal suivi", pas_de_journal, 0),
        cas_stop("arrêt, ancien emplacement docs/ vidé", ancien_emplacement, 2),
        cas_stop("second arrêt, journal tronqué : passe (la CI garde)", tronque, 0, actif=True),
        cas_ci("CI, ligne ajoutée", L1, L1 + L2, 0),
        cas_ci("CI, journal créé", None, L1, 0),
        cas_ci("CI, ligne supprimée", L1 + L2, L1, 1),
        cas_ci("CI, ligne modifiée", L1 + L2, L1 + L2.replace("deux", "DEUX"), 1),
    ]
    with tempfile.TemporaryDirectory() as tmp:
        resultats.append(("hors dépôt git", 0, stop(tmp)))
    echecs = 0
    for nom, attendu, obtenu in resultats:
        print(("ok   " if obtenu == attendu else "ÉCHEC"), attendu, obtenu, nom)
        echecs += obtenu != attendu
    sys.exit(1 if echecs else 0)


if __name__ == "__main__":
    main()
