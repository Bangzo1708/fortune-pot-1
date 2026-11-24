#!/usr/bin/env python3
"""Fortune in a Pot.

Writes one kind, funny fortune for the houseplant on the windowsill
to /output/entry.txt. Deterministic: no network, no randomness, no
external files.
"""

import os

ENTRY = "By spring you'll outgrow this windowsill, and your keeper will finally admit you were right about the sun all along."


def main():
    # Gate check, same as the house scorer: 1-120 chars, not only whitespace.
    if not 1 <= len(ENTRY) <= 120 or not ENTRY.strip():
        raise ValueError(f"entry must be 1-120 non-blank chars, got {len(ENTRY)}")
    # A fortune is one line: no newline inside the text itself.
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
