#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes exactly one pickup line to entry.txt (default /output/entry.txt,
overridable with MAKEFUN_OUTPUT_DIR). Standard library only, deterministic:
every run writes the same bytes.

The line is validated before writing and re-validated after a read-back:
it must be UTF-8 text of 1-200 characters, a single line, not only
whitespace, and the sha256 of what was written must match the digest of
the line this program intends to write. Any failure aborts loudly.
"""

import hashlib
import os
import sys

FINAL_LINE = (
    "Are you a CAPTCHA? Because I keep failing the 'I'm not a robot' "
    "test every time I look at you."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Check a candidate entry against the competition gate.

    Returns the sha256 hex digest of the text, or raises SystemExit.
    """
    if not isinstance(text, str):
        raise SystemExit("entry must be text")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry is %d chars, outside the %d-%d gate"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line, no edge whitespace")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    expected = validate_entry(FINAL_LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FINAL_LINE)

    with open(path, "rb") as handle:
        raw = handle.read()
    written = raw.decode("utf-8")
    digest = validate_entry(written)
    if digest != expected:
        raise SystemExit(
            "entry.txt digest %s != expected %s" % (digest, expected)
        )
    print(
        "entry.txt OK: %d chars, sha256 %s" % (len(written), digest)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
