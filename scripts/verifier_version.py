#!/usr/bin/env python3
"""Contrôle de version du plugin, rejoué par la CI et avant chaque release.

    python3 scripts/verifier_version.py

1. La version de .claude-plugin/plugin.json est un SemVer X.Y.Z.
2. La marketplace ne fixe pas d'autre version que celle du plugin.
3. Si le tag vX.Y.Z existe déjà, le plugin n'a pas changé depuis ce tag : un changement
   sans montée de version ne serait jamais proposé en mise à jour aux projets.
   README.md, LICENSE, .github/, scripts/ et tests/ ne comptent pas comme changement du plugin.
"""
import json
import re
import subprocess
import sys

HORS_PLUGIN = ("README.md", "LICENSE", ".github/", "scripts/", "tests/")


def echouer(message):
    print(f"::error::{message}")
    sys.exit(1)


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


def main():
    with open(".claude-plugin/plugin.json", encoding="utf-8") as f:
        version = json.load(f).get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        echouer(f"version « {version} » de plugin.json : attendu X.Y.Z (SemVer).")

    with open(".claude-plugin/marketplace.json", encoding="utf-8") as f:
        for p in json.load(f).get("plugins", []):
            if p.get("version") not in (None, version):
                echouer(f"marketplace.json fixe {p['name']} en {p['version']}, plugin.json en {version}.")

    tag = f"v{version}"
    if git("rev-parse", "-q", "--verify", f"refs/tags/{tag}").returncode != 0:
        print(f"Version {version} : pas encore publiée, elle le sera à la fusion dans main.")
        return
    changes = [
        f for f in git("diff", "--name-only", tag).stdout.splitlines()
        if not f.startswith(HORS_PLUGIN)
    ]
    if changes:
        echouer(
            f"le plugin a changé depuis {tag} ({', '.join(changes)}) : montez la version "
            "dans .claude-plugin/plugin.json (correctif : Z+1 ; ajout : Y+1 ; rupture : X+1)."
        )
    print(f"Version {version} déjà publiée, plugin inchangé depuis {tag}.")


if __name__ == "__main__":
    main()
