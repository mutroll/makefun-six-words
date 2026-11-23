#!/usr/bin/env python3
"""Six Words, One Story — writes one complete six-word story to entry.txt.

The story is a constant. The program only resolves the output directory
(MAKEFUN_OUTPUT_DIR when set, otherwise /output) and writes the text.
Deterministic: no randomness, no network, no timestamps, no input files.
"""

import os
from pathlib import Path

# The entry: exactly six words, 39 characters.
# A letter that arrives too late — the final word reframes the first five.
STORY = "The letter arrived after the funeral."


def main() -> None:
    # Guard the gate: exactly six words, 1-60 characters, not only whitespace.
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    assert STORY.strip(), "entry must not be only whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
