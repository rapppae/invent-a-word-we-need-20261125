"""Entry for make.fun bounty: Invent a Word We Need
Slug: u-deranalabs-invent-a-word-we-need-17a020e0
Entry text (99 characters total (word + definition), gate max 140). Written to /output/entry.txt with no trailing newline.
"""
import os

ENTRY = """Snarknap (n.): the half-second pause before you send a text you already regret."""

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
