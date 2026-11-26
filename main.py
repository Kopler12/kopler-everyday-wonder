#!/usr/bin/env python3
"""Everyday Wonder — one sentence about a small moment of wonder.

Writes a single sentence (1-200 characters) to /output/entry.txt.
The output path can be overridden with the ENTRY_OUT environment
variable for local testing; the default is /output/entry.txt.
"""

import os
import sys

ENTRY = (
    "The rice cooker sighs its steam, and for one breath the kitchen "
    "smells of rain on a tin roof in a house I have never lived in."
)


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
