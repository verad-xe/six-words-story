"""Write the six-word story entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is one complete original story in exactly six words:
"She sold the house. He stayed."
"""

import os
import sys

STORY = "She sold the house. He stayed."


def validate_story(story):
    """A six-word story must be exactly six words and 1-60 characters."""
    words = story.split()
    if len(words) != 6:
        return f"story must be exactly six words, got {len(words)}"
    if not 1 <= len(story) <= 60:
        return f"story must be 1-60 characters, got {len(story)}"
    return None


def main():
    error = validate_story(STORY)
    if error is not None:
        print(f"error: invalid story: {error}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
