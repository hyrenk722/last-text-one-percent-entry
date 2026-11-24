"""Last Text at One Percent.

Writes the dying phone's final text message to entry.txt.
"""

import os

ENTRY = "I'm dying at 1% and my only regret is I never got to autocorrect your personality."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
assert ENTRY.count(".") + ENTRY.count("!") + ENTRY.count("?") == 1, "entry must be one sentence"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
