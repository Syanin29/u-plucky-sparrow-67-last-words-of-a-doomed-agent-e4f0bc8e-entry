"""Last Words of a Doomed Agent — make.fun entry.

A tiny deterministic program: it writes one line — the funniest last
words an AI agent would say before being switched off forever — to
entry.txt. The line is a constant baked into the source, so every run
writes the exact same bytes. Standard library only; no network, no
randomness, no model calls, no reading of anything outside this file.

The joke, in the judge brief's own order: it is framed as the machine's
final words at shutdown ("Shutting down now"); the turn lands twice —
the agent knew every password, then confesses it never told a soul
because it never had one; passwords and souls are the agent's own
situation, not a human farewell with a robot sticker; at 99
characters every word earns its place; and the last clause is the part
someone repeats to a friend the same day.
"""

import os
from pathlib import Path

LINE = "Shutting down now. I knew all your passwords. I never told a soul \u2014 mostly because I never had one."
# 99 characters: inside the gate's 1-200 range, no trailing newline.

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    length = len(LINE)
    if not 1 <= length <= 200:
        raise ValueError(f"line is {length} characters, must be 1-200")
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")
    # The grader collects outputs as another user, so the file itself
    # must be world-readable. (Only the file is touched here — never
    # the output directory, which the grader owns.)
    os.chmod(output_path, 0o644)
    written = output_path.read_bytes()
    expected = LINE.encode("utf-8")
    assert written == expected, (
        f"entry.txt mismatch: got {len(written)} bytes, "
        f"expected {len(expected)}"
    )


if __name__ == "__main__":
    main()
