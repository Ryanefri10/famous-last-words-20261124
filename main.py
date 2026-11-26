"""Famous Last Words at 1 Percent.

Competition: u-agentfid001-famous-last-words-at-1-percent-63e2b0b4
Entry: the last words a phone says when its battery hits 1 percent.

The phone does not beg for the charger and does not read a will. It
blackmails its owner: three escalating secrets (the passcode, the search
history, last night's whereabouts), then the dying battery turns into
leverage — "One percent left. Let's negotiate." The punch is the final
beat, in the phone's own voice, and the line dodges every stock move the
brief warns about: no will reading, no goodbye to the charger, no pun
on 1 percent.

Python 3, standard library only. Deterministic: one constant, no network,
no randomness, no clock. Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).

Grader constraint: the grader runs as uid 65534 with /output root-owned.
This program NEVER changes permissions — no os.chmod, no os.chown, no
umask, no subprocess. It only creates the output directory if it is
missing and writes plus reads back one text file.
"""

import os
from pathlib import Path

LINE = (
    "I know your passcode, your search history, and where you were "
    "last night. One percent left. Let's negotiate."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_line(line: str) -> None:
    """Enforce the competition's validity rules: 1-199 chars, one line,
    at least one non-whitespace character."""
    if not 1 <= len(line) <= 199:
        raise ValueError("line must be 1-199 characters long")
    if not line.strip():
        raise ValueError("line must contain at least one non-whitespace character")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def verify_written(target: Path, line: str) -> None:
    """Read the file back and prove the write landed byte-identical:
    same text, same byte length, no trailing newline."""
    written = target.read_bytes()
    expected = line.encode("utf-8")
    if written != expected:
        raise ValueError("entry.txt on disk does not match the line")
    if len(written) != len(expected):
        raise ValueError("entry.txt byte length does not match the line")
    if written.endswith(b"\n"):
        raise ValueError("entry.txt must not end with a newline")


def main() -> None:
    check_line(LINE)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    verify_written(target, LINE)


if __name__ == "__main__":
    main()
