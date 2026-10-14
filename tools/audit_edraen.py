#!/usr/bin/env python3
"""Audit Edraen's lexical roots, grammar words, and phase records.

Run from any directory with: python tools/audit_edraen.py
Only Python's standard library is required.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DICTIONARY = ROOT / "docs/language/Edraen_Dictionary.md"
GRAMMAR = ROOT / "docs/language/Edraen_Standard_Grammar.md"
REGISTRY = ROOT / "docs/00_Canon_Registry.md"
PHRASEBOOK = ROOT / "docs/language/Edraen_Everyday_Phrasebook.md"
OATH = ROOT / "docs/language/Edraen_Oath_Translation_Test.md"
ROOT_ROW = re.compile(r"^\| \*\*([A-Z]+)\*\* \|", re.MULTILINE)
GRAMMAR_ROW = re.compile(r"^\| \*\*([A-Z]+)\*\* \|", re.MULTILINE)


def read(path: Path) -> str:
    if not path.is_file():
        raise ValueError(f"Required file is missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def section(text: str, start: str, end: str) -> str:
    begin = text.find(start)
    finish = text.find(end, begin + len(start)) if begin >= 0 else -1
    if begin < 0 or finish < 0:
        raise ValueError(f"Could not locate section between {start!r} and {end!r}")
    return text[begin:finish]


def exact_duplicates(items: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates


def main() -> int:
    errors: list[str] = []
    dictionary = read(DICTIONARY)
    grammar = read(GRAMMAR)
    registry = read(REGISTRY)

    inventory = section(dictionary, "## Complete approved root inventory", "## Lexical distinctions")
    roots = ROOT_ROW.findall(inventory)
    root_set = set(roots)
    declared = re.search(r"\*\*Inventory:\*\*\s+(\d+)\s+approved lexical roots", dictionary)
    if not declared:
        errors.append("Dictionary is missing its declared lexical-root count.")
        expected_count = -1
    else:
        expected_count = int(declared.group(1))
        if len(roots) != expected_count:
            errors.append(f"Dictionary declares {expected_count} roots but contains {len(roots)} root rows.")

    root_dupes = exact_duplicates(roots)
    if root_dupes:
        errors.append("Duplicate lexical root spellings: " + ", ".join(root_dupes))
    if roots != sorted(roots):
        errors.append("The master dictionary root rows are not alphabetically sorted.")

    ledger = section(grammar, "### Complete grammar-word ledger", "\n## 2.")
    grammar_words = GRAMMAR_ROW.findall(ledger)
    grammar_dupes = exact_duplicates(grammar_words)
    if grammar_dupes:
        errors.append("Duplicate grammar-word spellings: " + ", ".join(grammar_dupes))
    collisions = sorted(root_set.intersection(grammar_words))
    if collisions:
        errors.append("Exact spelling collisions between roots and grammar words: " + ", ".join(collisions))

    phase_roots: list[str] = []
    phase_counts: dict[int, int] = {}
    for phase in range(1, 11):
        path = ROOT / f"docs/language/Edraen_Dictionary_Phase_{phase}.md"
        try:
            text = read(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        entries = ROOT_ROW.findall(text)
        phase_counts[phase] = len(entries)
        duplicates = exact_duplicates(entries)
        if duplicates:
            errors.append(f"Phase {phase} repeats spellings internally: " + ", ".join(duplicates))
        phase_roots.extend(entries)

    phase_dupes = exact_duplicates(phase_roots)
    if phase_dupes:
        errors.append("Spellings repeated across phase records: " + ", ".join(phase_dupes))
    if set(phase_roots) != root_set:
        missing_from_phases = sorted(root_set - set(phase_roots))
        missing_from_master = sorted(set(phase_roots) - root_set)
        if missing_from_phases:
            errors.append("Roots missing from phase records: " + ", ".join(missing_from_phases))
        if missing_from_master:
            errors.append("Phase roots missing from master dictionary: " + ", ".join(missing_from_master))
    if len(phase_roots) != len(roots):
        errors.append(f"Phase records contain {len(phase_roots)} root rows; master dictionary contains {len(roots)}.")

    if "Edraen Standard v3.0" not in grammar:
        errors.append("Grammar document does not identify Edraen Standard v3.0.")
    registry_count = re.search(r"\\*\\*(\\d+) unique root spellings\\*\\*", registry)
    if not registry_count or int(registry_count.group(1)) != expected_count:
        recorded = registry_count.group(1) if registry_count else "missing"
        errors.append(f"Canon Registry records {recorded} roots but the dictionary declares {expected_count}.")
    if "Edraen Standard v3.0" not in registry:
        errors.append("Canon Registry does not reference Edraen Standard v3.0.")

    # Check every explicitly formatted Edraen phrase in the learner phrasebook and oath.
    allowed_proper_terms = {"EDRAEN", "EDRATH"}
    checked_phrases = 0
    for path, text, patterns in (
        (PHRASEBOOK, read(PHRASEBOOK), [re.compile(r"^\| \*\*(.*?)\*\* \|", re.MULTILINE)]),
        (OATH, read(OATH), [re.compile(r"^\*\*Edraen\*\*\s*\n\s*([^\n]+)", re.MULTILINE)]),
    ):
        for pattern in patterns:
            for phrase in pattern.findall(text):
                checked_phrases += 1
                for token in re.findall(r"\b[A-Z]{2,7}\b", phrase):
                    if token not in root_set and token not in set(grammar_words) and token not in allowed_proper_terms:
                        errors.append(f"{path.relative_to(ROOT)} uses undefined Edraen token {token!r} in {phrase!r}.")

    print("Edraen spelling and inventory audit")
    print(f"  Master dictionary roots: {len(roots)}")
    print(f"  Unique grammar words:   {len(set(grammar_words))}")
    print(f"  Root/grammar collisions:{len(collisions)}")
    print(f"  Phrasebook/oath entries checked: {checked_phrases}")
    print("  Phase root rows:        " + ", ".join(f"P{p}={phase_counts.get(p, 0)}" for p in range(1, 11)))
    if errors:
        print("\nFAIL")
        for error in errors:
            print(f" - {error}")
        return 1
    print("\nPASS: no exact spelling duplicates; phase records match the master dictionary.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
