#!/usr/bin/env python3
"""Hook PreToolUse (Edit|MultiEdit|Write|NotebookEdit|Bash|PowerShell) : pilotage/journal.md
est en ajout seul.

Règle du sommier (méthode de l'Impératrice, fiche n° 11) : on n'efface pas, on ajoute.
Une correction est une nouvelle ligne datée qui renvoie à l'ancienne.
Un déplacement par `git mv` garde le contenu et l'historique : il est permis.
L'ancien emplacement docs/journal.md reste protégé pour les projets pas encore rangés.
Code de sortie 2 = l'action est bloquée ; le message part vers l'agent.

Ce filtre est un premier rempart : il lit les commandes, et une commande peut cacher le
journal (variable, script). Le résultat, lui, est vérifié par journal_intact.py, à
l'arrêt de chaque agent et en CI.
"""
import json
import os
import re
import sys

JOURNAUX = ("pilotage/journal.md", "docs/journal.md")
MESSAGE = (
    "Modification refusée : le journal est en ajout seul (règle du sommier). "
    "On n'efface pas, on ajoute : écris une nouvelle ligne datée en fin de fichier "
    "(`>>`, `tee -a`, ou Edit/Write qui reprend tout l'existant), et pour corriger, "
    "une ligne qui renvoie à l'ancienne."
)

# Une cible de redirection : opérateur (avec descripteur éventuel), puis le mot visé.
REDIRECTION = re.compile(r"(\d*|&)(>>|>\|?)\s*(['\"]?)([^\s;&|<>()]+)")
# Commandes qui écrivent leur dernier argument (la destination) : copier le journal
# ailleurs reste permis.
COPIEURS = re.compile(r"\b(cp|install|rsync|ln)\b")
# Commandes qui écrivent ou retirent tout fichier qu'on leur nomme.
ECRIVAINS = re.compile(
    r"\b(unlink|rm|truncate|shred|patch|"
    r"set-content|out-file|clear-content|remove-item|move-item|copy-item|new-item|rename-item)\b")
INTERPRETES = re.compile(r"\b(python[0-9.]*|perl|ruby|node|php)\b")


def bloquer():
    print(MESSAGE, file=sys.stderr)
    sys.exit(2)


def normaliser(chemin):
    return os.path.normpath(chemin).replace("\\", "/")


def est_journal(chemin):
    """Le journal, quelle que soit la casse (un disque insensible à la casse l'écraserait)."""
    return bool(chemin) and normaliser(chemin).lower().endswith(JOURNAUX)


def casse_exacte(chemin):
    return normaliser(chemin).endswith(JOURNAUX)


def lire(chemin, cwd):
    try:
        with open(os.path.join(cwd, chemin), encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError):
        return ""


def apres_edits(existant, edits):
    """Le fichier tel que l'outil le laisserait, ou None si un remplacement est impossible."""
    texte = existant
    for e in edits:
        ancien, nouveau = e.get("old_string", ""), e.get("new_string", "")
        # Règle de toujours, même si le fichier est illisible : le nouveau reprend l'ancien.
        if not nouveau.startswith(ancien):
            return None
        if ancien == "":
            # Ancien texte vide sur un fichier existant : insertion au début.
            if texte:
                return None
            texte = nouveau
        elif e.get("replace_all"):
            texte = texte.replace(ancien, nouveau)
        else:
            texte = texte.replace(ancien, nouveau, 1)
    return texte


def vise_journal(cible):
    """Une cible nommée dans une commande : le journal, ou un motif qui peut le désigner."""
    cible = cible.strip("'\"")
    if "journal.md" in cible.lower():
        return True
    # Motif (glob) dans un dossier qui porte un journal : pilotage/*.md, docs/journa?.md…
    dossier, nom = os.path.split(cible)
    return (any(c in nom for c in "*?[")
            and os.path.basename(normaliser(dossier or ".")).lower() in ("pilotage", "docs"))


def commande_interdite(commande):
    bas = commande.lower()
    # 1. Redirections : seul l'ajout (>>, &>>, 2>>…) vers le journal est permis.
    for _, operateur, _, cible in REDIRECTION.findall(commande):
        if operateur != ">>" and vise_journal(cible):
            return True
    if "journal.md" not in bas and not re.search(r"(pilotage|docs)/[^\s]*[*?\[]", bas):
        return False
    # Le reste ne vaut que pour les segments de commande qui nomment le journal.
    for segment in re.split(r"&&|\|\||[;|\n]", commande):
        s = segment.lower()
        if not any(vise_journal(mot) for mot in s.split()):
            continue
        mots = s.split()
        if not mots:
            continue
        if "tee" in mots and not ({"-a", "--append"} & set(mots)):
            return True
        if mots[0] == "git":
            if re.search(r"\bgit\s+(checkout|restore|rm|reset|stash|clean|apply)\b", s):
                return True
            continue  # git add, diff, log, show, mv… : permis
        if COPIEURS.search(s) and vise_journal(mots[-1]):
            return True
        if re.search(r"\bdd\b", s) and any(m.startswith("of=") and vise_journal(m[3:]) for m in mots):
            return True
        if ECRIVAINS.search(s):
            return True
        if re.search(r"\b(mv|move)\b", s):
            return True
        if re.search(r"\bsed\b.*(\s-i|--in-place)", s) or re.search(r"\bperl\b.*\s-\w*i", s):
            return True
        if INTERPRETES.search(s):
            return True
        if "out-file" in s or "set-content" in s:
            return True
    return False


def main():
    try:
        entree = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    outil = entree.get("tool_name", "")
    params = entree.get("tool_input") or {}
    cwd = entree.get("cwd") or os.getcwd()
    chemin = params.get("file_path") or params.get("notebook_path") or ""

    if outil in ("Edit", "MultiEdit", "Write", "NotebookEdit") and est_journal(chemin):
        if not casse_exacte(chemin) or outil == "NotebookEdit":
            bloquer()
        existant = lire(chemin, cwd)
        if outil == "Write":
            resultat = params.get("content", "")
        elif outil == "Edit":
            resultat = apres_edits(existant, [params])
        else:
            resultat = apres_edits(existant, params.get("edits") or [])
        # Seul ajout permis : le fichier d'après reprend l'existant tel quel, puis ajoute.
        if resultat is None or not resultat.startswith(existant):
            bloquer()

    elif outil in ("Bash", "PowerShell"):
        if commande_interdite(params.get("command", "") or ""):
            bloquer()
    sys.exit(0)


if __name__ == "__main__":
    main()
