#!/usr/bin/env python3
"""Write one funny tombstone epitaph to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the entry line is a fixed string. No clock, no randomness,
no network, no file reads. The same bytes are written on every run.
"""

import os
from pathlib import Path

ENTRY = "I died as I lived: on hold with customer service."

# The gate allows 1 to 150 characters; refuse to write an entry that
# would be rejected rather than silently shipping an invalid one.
assert 1 <= len(ENTRY) <= 150, "entry outside the 1-150 character gate"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
