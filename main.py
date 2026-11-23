#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters or fewer.

Writes a single deadpan robot-vacuum excuse for missing a spot to
/output/entry.txt and echoes it to stdout. Python 3.13, stdlib only,
fully deterministic: no network, no environment, no randomness.
"""

import os

ALIBI = (
    "I didn't miss the spot. My LiDAR mapped it in 4K, every crumb logged "
    "— then, at 3% battery, I declined: dock first, survival second, "
    "your floor a distant third."
)


def main() -> None:
    line = ALIBI.strip()
    assert 0 < len(line) <= 200, f"alibi is {len(line)} characters, gate wants 1..200"
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        # Nowhere to write (e.g. a read-only local checkout): the line
        # still goes to stdout so a human can read the entry.
        pass
    print(line)


if __name__ == "__main__":
    main()
