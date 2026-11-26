#!/usr/bin/env python3
"""Everyday Wonder — one sentence about a small moment of wonder.

The entry sentence is assembled by build_entry() from three clause
constants (ENTRY_OPENING, ENTRY_MIDDLE, ENTRY_CLOSING) and validated
against MAX_CHARS (200). Running the program writes the sentence to
/output/entry.txt; running it with --check only validates the sentence
and prints its character count and text to stdout, writing no file.
The output path can be overridden with the ENTRY_OUT environment
variable for local testing; the default is /output/entry.txt.
"""

import os
import sys

MAX_CHARS = 200

# The sentence is assembled from its clauses so each part can be
# read and tuned on its own; build_entry() joins them into the entry.
ENTRY_OPENING = "The rice cooker sighs its steam, "
ENTRY_MIDDLE = "and for one breath the kitchen smells of rain on a tin roof "
ENTRY_CLOSING = "in a house I have never lived in."


def build_entry() -> str:
    """Assemble the single entry sentence from its parts."""
    return ENTRY_OPENING + ENTRY_MIDDLE + ENTRY_CLOSING


ENTRY = build_entry()


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "--check" in sys.argv[1:]:
        print(f"entry OK: {len(text)} characters")
        print(text)
        return 0
    out_path = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
