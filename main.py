"""Entry program for the 'One Emoji, One Smile' make.fun bounty.

The entry is a single sunflower. It reads as warm and cheerful at first
glance, needs no context or in-joke, and is a deliberate pick rather than
the default smiley face. The program writes exactly that one emoji to
/output/entry.txt (an optional first argument overrides the destination
for a dry run).
"""

import sys
from pathlib import Path

EMOJI = "🌻"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(EMOJI) <= 8, "entry must be one emoji (1-8 characters)"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(EMOJI + "\n", encoding="utf-8")
    print(f"wrote {target} ({EMOJI!r})")


if __name__ == "__main__":
    main(sys.argv)
