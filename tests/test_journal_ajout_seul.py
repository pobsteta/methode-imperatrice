#!/usr/bin/env python3
"""Cas du hook journal_ajout_seul.py, rejouables sans toucher au dépôt.

    python3 tests/test_journal_ajout_seul.py

Vérifie, pour chaque appel d'outil, que le hook bloque (2) ou laisse passer (0).
"""
import json
import os
import subprocess
import sys
import tempfile

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks", "journal_ajout_seul.py")
J = "journal" + ".md"  # le hook de la session lit aussi ce fichier : pas de chemin en clair


def verdict(outil, params):
    entree = json.dumps({"tool_name": outil, "tool_input": params})
    return subprocess.run([sys.executable, HOOK], input=entree,
                          capture_output=True, text=True).returncode


def main():
    with tempfile.TemporaryDirectory() as tmp:
        os.mkdir(os.path.join(tmp, "pilotage"))
        journal = os.path.join(tmp, "pilotage", J)
        with open(journal, "w", encoding="utf-8") as f:
            f.write("2026-10-20 · Pascal · a · b\n")
        ancien = os.path.join(tmp, "docs", J)

        cas = [
            ("Edit", {"file_path": journal, "old_string": "b\n", "new_string": "b\nsuite\n"}, 0),
            ("Edit", {"file_path": journal, "old_string": "b\n", "new_string": "c\n"}, 2),
            ("Edit", {"file_path": journal, "old_string": "b", "new_string": "bb", "replace_all": True}, 2),
            ("Edit", {"file_path": ancien, "old_string": "b", "new_string": "c"}, 2),
            ("Write", {"file_path": journal, "content": "2026-10-20 · Pascal · a · b\nsuite\n"}, 0),
            ("Write", {"file_path": journal, "content": "vide\n"}, 2),
            ("Bash", {"command": f"echo x >> pilotage/{J}"}, 0),
            ("Bash", {"command": f"echo x > pilotage/{J}"}, 2),
            ("Bash", {"command": f"sed -i s/a/b/ pilotage/{J}"}, 2),
            ("Bash", {"command": f"rm pilotage/{J}"}, 2),
            ("Bash", {"command": f"git rm pilotage/{J}"}, 2),
            ("Bash", {"command": f"mv docs/{J} pilotage/{J}"}, 2),
            ("Bash", {"command": f"git mv docs/{J} pilotage/{J}"}, 0),
            ("Bash", {"command": f"git checkout pilotage/{J}"}, 2),
            ("Edit", {"file_path": os.path.join(tmp, "README.md"), "old_string": "a", "new_string": "b"}, 0),
        ]
        echecs = 0
        for outil, params, attendu in cas:
            obtenu = verdict(outil, params)
            lisible = outil + " " + json.dumps(params, ensure_ascii=False).replace(tmp, "<tmp>")
            print(("ok   " if obtenu == attendu else "ÉCHEC"), attendu, obtenu, lisible)
            echecs += obtenu != attendu
    sys.exit(1 if echecs else 0)


if __name__ == "__main__":
    main()
