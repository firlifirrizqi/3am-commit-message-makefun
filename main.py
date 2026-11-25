"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (<=200 chars) to /output/entry.txt.
Standard library only.
"""

import os

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "hotfix: fixed the checkout bug at 3 AM by deleting checkout; "
    "nobody can check out now, so nobody can report it"
)


def verify_written(path: str, expected: str) -> None:
    """Read the file back and confirm it is byte-identical to the entry."""
    with open(path, "r", encoding="utf-8") as f:
        actual = f.read()
    if actual != expected:
        raise SystemExit(
            f"verification failed: output differs from entry "
            f"({len(actual)} chars vs {len(expected)} expected)"
        )


def main() -> None:
    # Gate guard: one line, 1..200 characters, not only whitespace.
    if not (1 <= len(ENTRY) <= MAX_CHARS) or not ENTRY.strip():
        raise SystemExit(f"entry fails gate: {len(ENTRY)} chars")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify_written(OUTPUT_PATH, ENTRY)


if __name__ == "__main__":
    main()
