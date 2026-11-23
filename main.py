"""Write the six-word story entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is one complete original story in exactly six words:
"She sold the house. He stayed."
"""

import os

STORY = "She sold the house. He stayed."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
