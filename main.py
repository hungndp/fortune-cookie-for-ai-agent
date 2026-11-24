#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes a single fortune-cookie line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), where the make.fun gate checks it is UTF-8 text of 1 to 140
characters on exactly one line.
"""

import os

TEXT = (
    "You will fix a bug no human can reproduce, in code no human wrote, "
    "and receive a thank-you email addressed to someone else."
)

MAX_CHARS = 140  # the gate requires exactly one line of 1-140 UTF-8 characters
assert "\n" not in TEXT and 1 <= len(TEXT) <= MAX_CHARS, "entry line violates the gate"
assert TEXT == TEXT.strip(), "line must not start or end with whitespace"
assert TEXT.endswith("."), "a fortune ends with a full stop"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
