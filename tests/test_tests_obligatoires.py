#!/usr/bin/env python3
"""Cas du hook tests_obligatoires.py, rejouables sans toucher au dépôt.

    python3 tests/test_tests_obligatoires.py

Crée un dépôt temporaire par cas, avec une commande de tests factice dans
.claude/test-command, et vérifie que le hook bloque l'arrêt (2) ou le laisse passer (0) ;
au second arrêt (stop_hook_active) avec des tests rouges, qu'il l'inscrit au journal ;
et qu'il ne fixe aucune variable propre à un domaine (ANDROID_HOME, ADR 0001) ;
et que l'attente du verrou des tests reste dans le délai du hook (mission 012).
"""
import fcntl
import json
import os
import re
import subprocess
import sys
import tempfile
import threading

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks", "tests_obligatoires.py")
J = "journal" + ".md"  # le hook de la session lit aussi ce fichier : pas de chemin en clair
LIGNE = "2026-10-21 · Pascal · 000 · départ\n"
VERT = "true"
ROUGE = "echo SORTIE-DES-TESTS; exit 1"


def git(*args, cwd):
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
                   cwd=cwd, check=True, capture_output=True)


def ecrire(depot, chemin, contenu):
    complet = os.path.join(depot, chemin)
    os.makedirs(os.path.dirname(complet), exist_ok=True)
    with open(complet, "w", encoding="utf-8") as f:
        f.write(contenu)


def lire(depot, chemin):
    try:
        with open(os.path.join(depot, chemin), encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


def rejouer(commande, changements, actif=False, journal=True, env_en_plus=None, sans=(),
            verrou_libre_apres=None):
    """Dépôt temporaire commité, puis changements non commités ; renvoie (code, stderr, journal).

    verrou_libre_apres : si donné, le verrou des tests est tenu pendant ce nombre de
    secondes (float("inf") : tout le temps), comme par un autre lancement des tests.
    """
    with tempfile.TemporaryDirectory() as depot:
        git("init", "-q", "-b", "mission/x", cwd=depot)
        ecrire(depot, "src/a.py", "a = 1\n")
        if journal:
            ecrire(depot, f"pilotage/{J}", LIGNE)
        if commande is not None:
            ecrire(depot, ".claude/test-command", commande + "\n")
        git("add", "-A", cwd=depot)
        git("commit", "-q", "-m", "0", cwd=depot)
        for chemin, contenu in changements.items():
            ecrire(depot, chemin, contenu)
        entree = {"hook_event_name": "Stop", "cwd": depot, "stop_hook_active": actif}
        env = dict(os.environ, CLAUDE_PROJECT_DIR=depot, **(env_en_plus or {}))
        for nom in sans:
            env.pop(nom, None)
        tenu = None
        if verrou_libre_apres is not None:
            tenu = open(os.path.join(depot, ".git", "imperatrice-tests.lock"), "w")
            fcntl.flock(tenu, fcntl.LOCK_EX)
            if verrou_libre_apres != float("inf"):
                threading.Timer(verrou_libre_apres, tenu.close).start()
        try:
            r = subprocess.run([sys.executable, HOOK], input=json.dumps(entree),
                               capture_output=True, text=True, env=env, timeout=60)
        except subprocess.TimeoutExpired:
            return "bloqué plus de 60 s", "", lire(depot, f"pilotage/{J}")
        finally:
            if tenu is not None and not tenu.closed:
                tenu.close()
        return r.returncode, r.stderr, lire(depot, f"pilotage/{J}")


def main():
    code = {"src/a.py": "a = 2\n"}
    cas = [
        # (nom, commande, changements, stop_hook_active, journal présent, code attendu, contrôle)
        ("pas de .claude/test-command", None, code, False, True, 0, None),
        ("commande vide", "", code, False, True, 0, None),
        ("arbre propre, tests rouges", ROUGE, {}, False, True, 0, None),
        ("seuls docs/ et pilotage/ changés", ROUGE,
         {"docs/brief.md": "b\n", f"pilotage/{J}": LIGNE + "suite\n"}, False, True, 0, None),
        ("code changé, tests verts", VERT, code, False, True, 0, None),
        ("code changé, tests rouges : bloqué, sortie renvoyée", ROUGE, code, False, True, 2,
         lambda err, j: "SORTIE-DES-TESTS" in err and j == LIGNE),
        ("fichier non suivi, tests rouges : bloqué", ROUGE, {"src/b.py": "b = 1\n"}, False, True, 2, None),
        ("second arrêt, tests rouges : passe, inscrit au journal", ROUGE, code, True, True, 0,
         lambda err, j: j.startswith(LIGNE) and j.count("\n") == 2 and "tests rouges" in j),
        ("second arrêt, tests verts : passe, journal inchangé", VERT, code, True, True, 0,
         lambda err, j: j == LIGNE),
        ("second arrêt, tests rouges, pas de journal : passe, rien créé", ROUGE, code, True, False, 0,
         lambda err, j: j is None),
    ]
    echecs = 0
    for nom, commande, changements, actif, journal, attendu, controle in cas:
        obtenu, err, j = rejouer(commande, changements, actif, journal)
        juste = obtenu == attendu and (controle is None or controle(err, j))
        print(("ok   " if juste else "ÉCHEC"), attendu, obtenu, nom)
        echecs += not juste

    # ADR 0001 : le hook ne connaît pas Android. Même si ~/Android/Sdk existe et que
    # ANDROID_HOME n'est pas défini, la commande de tests ne doit pas le recevoir.
    with tempfile.TemporaryDirectory() as maison:
        os.makedirs(os.path.join(maison, "Android", "Sdk"))
        obtenu, err, j = rejouer('test -z "$ANDROID_HOME"', code,
                                 env_en_plus={"HOME": maison}, sans=("ANDROID_HOME",))
    juste = obtenu == 0
    print(("ok   " if juste else "ÉCHEC"), 0, obtenu,
          "~/Android/Sdk présent, pas d'ANDROID_HOME : le hook n'en fixe pas")
    echecs += not juste

    # Mission 012 : l'attente du verrou partage le budget des tests, sous le délai du hook.
    petit = {"IMPERATRICE_BUDGET_TESTS": "3"}
    verrou = [
        # (nom, verrou libre après, stop_hook_active, code attendu, contrôle)
        ("verrou tenu, premier arrêt : bloqué, le message nomme le verrou",
         float("inf"), False, 2, lambda err, j: "verrou" in err and j == LIGNE),
        ("verrou tenu, second arrêt : passe, inscrit au journal",
         float("inf"), True, 0, lambda err, j: j.startswith(LIGNE) and "verrou" in j),
        ("verrou libéré pendant l'attente, tests verts : passe",
         1.0, False, 0, lambda err, j: j == LIGNE),
    ]
    for nom, apres, actif, attendu, controle in verrou:
        obtenu, err, j = rejouer(VERT, code, actif, env_en_plus=petit, verrou_libre_apres=apres)
        juste = obtenu == attendu and controle(err, j)
        print(("ok   " if juste else "ÉCHEC"), attendu, obtenu, nom)
        echecs += not juste

    with open(HOOK, encoding="utf-8") as f:
        budget = re.search(r"^BUDGET = (\d+)", f.read(), re.M)
    with open(os.path.join(os.path.dirname(HOOK), "hooks.json"), encoding="utf-8") as f:
        delais = [h.get("timeout") for blocs in json.load(f)["hooks"].values()
                  for bloc in blocs for h in bloc["hooks"]
                  if "tests_obligatoires" in h["command"]]
    juste = bool(budget) and delais and all(d and int(budget.group(1)) + 20 <= d for d in delais)
    print(("ok   " if juste else "ÉCHEC"),
          f"budget {budget.group(1) if budget else '?'} s, délais du hook {delais}",
          ": attente du verrou et tests tiennent dans le délai, avec 20 s de marge")
    echecs += not juste
    sys.exit(1 if echecs else 0)


if __name__ == "__main__":
    main()
