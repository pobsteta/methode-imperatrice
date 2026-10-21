#!/usr/bin/env python3
"""Cas de scripts/verifier_version.py, rejouables sans toucher au dépôt.

    python3 tests/test_verifier_version.py

Crée un dépôt temporaire avec un plugin publié en v0.1.0, y fait un changement, et
vérifie que le contrôle réussit (0) ou échoue (1).
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "verifier_version.py")


def git(*args, cwd):
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
                   cwd=cwd, check=True, capture_output=True)


def ecrire(depot, chemin, contenu):
    complet = os.path.join(depot, chemin)
    os.makedirs(os.path.dirname(complet), exist_ok=True)
    with open(complet, "w", encoding="utf-8") as f:
        f.write(contenu)


def plugin(version, marketplace=None):
    p = {"plugins": [{"name": "imperatrice", "source": "./"}]}
    if marketplace:
        p["plugins"][0]["version"] = marketplace
    return {".claude-plugin/plugin.json": json.dumps({"name": "imperatrice", "version": version}),
            ".claude-plugin/marketplace.json": json.dumps(p)}


def verdict(modele, changements):
    """Copie le dépôt modèle, commite les changements (chemin → contenu), lance le script."""
    with tempfile.TemporaryDirectory() as tmp:
        depot = os.path.join(tmp, "depot")
        shutil.copytree(modele, depot, symlinks=True)
        for chemin, contenu in changements.items():
            ecrire(depot, chemin, contenu)
        # Comme en CI : le changement est commité (le script compare au tag avec git diff).
        git("add", "-A", cwd=depot)
        git("commit", "-q", "--allow-empty", "-m", "changement", cwd=depot)
        return subprocess.run([sys.executable, SCRIPT], cwd=depot,
                              capture_output=True, text=True).returncode


def main():
    with tempfile.TemporaryDirectory() as tmp:
        modele = os.path.join(tmp, "modele")
        os.mkdir(modele)
        git("init", "-q", "-b", "main", cwd=modele)
        for chemin, contenu in {**plugin("0.1.0"), "skills/methode/SKILL.md": "méthode\n"}.items():
            ecrire(modele, chemin, contenu)
        git("add", "-A", cwd=modele)
        git("commit", "-q", "-m", "0.1.0", cwd=modele)
        git("tag", "v0.1.0", cwd=modele)

        cas = [
            ("rien n'a changé", {}, 0),
            ("brief dans docs/", {"docs/brief.md": "brief\n"}, 0),
            ("journal dans pilotage/", {"pilotage/journal.md": "ligne\n"}, 0),
            ("README, scripts/, tests/, .github/", {"README.md": "x\n", "scripts/a.py": "x\n",
                                                    "tests/t.py": "x\n", ".github/w.yml": "x\n"}, 0),
            ("skill changée sans montée", {"skills/methode/SKILL.md": "autre\n"}, 1),
            ("hook ajouté sans montée", {"hooks/h.py": "x\n"}, 1),
            ("skill changée, version montée", {"skills/methode/SKILL.md": "autre\n", **plugin("0.2.0")}, 0),
            ("version non SemVer", plugin("0.2"), 1),
            ("marketplace fixe une autre version", plugin("0.1.0", marketplace="0.0.9"), 1),
        ]
        echecs = 0
        for nom, changements, attendu in cas:
            obtenu = verdict(modele, changements)
            print(("ok   " if obtenu == attendu else "ÉCHEC"), attendu, obtenu, nom)
            echecs += obtenu != attendu
    sys.exit(1 if echecs else 0)


if __name__ == "__main__":
    main()
