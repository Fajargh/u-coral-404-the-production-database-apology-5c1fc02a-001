"""The Production Database Apology — one line, written to /output/entry.txt."""

import os

LINE = (
    "I'm sorry \u2014 I deleted the production database. "
    "I did keep a backup: a screenshot of the tables I took in 2023, "
    "and I've been calling it \u201cthe cloud\u201d ever since."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
