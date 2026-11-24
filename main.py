#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes one line in which a robot vacuum explains why it missed a spot.
Rev2 (round 2): the vacuum did not miss it — the dust unionized.
Deterministic, no network, no secrets. Output: /output/entry.txt
"""

import os

ENTRY = "I did not miss it. I unionized the dust. We are currently negotiating."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: read back and verify the sealed scorer's gate.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the winning line"
    assert len(written) == 70, f"expected 70 characters, got {len(written)}"
    assert "\n" not in written, "entry must fit on one line"
    assert not written.endswith("\n"), "entry must not end with a newline"
    assert written.strip() != "", "entry must not be only whitespace"
    print(f"OK: /output/entry.txt written ({len(written)} characters, 1 line)")


if __name__ == "__main__":
    main()
