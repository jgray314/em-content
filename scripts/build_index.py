"""Regenerate the Posts table in README.md from each post's frontmatter.

Frontmatter is the source of truth for title, date, and tags. Run from the
repo root after adding a post or changing its frontmatter:

    python scripts/build_index.py

Only the region between the posts:start / posts:end markers is rewritten.
Standard library only, so it runs anywhere Python 3 does.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START, END = "<!-- posts:start -->", "<!-- posts:end -->"


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\r?\n(.*?)\r?\n---", text, re.S)
    if not match:
        raise SystemExit(f"{path.name}: no frontmatter")
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if not sep:
            raise SystemExit(f"{path.name}: unparseable frontmatter line: {line!r}")
        fields[key.strip()] = value.strip()
    for key in ("title", "date", "tags"):
        if key not in fields:
            raise SystemExit(f"{path.name}: missing '{key}'")
    return {
        "title": fields["title"].strip('"'),
        "date": fields["date"],
        "tags": [t.strip() for t in fields["tags"].strip("[]").split(",") if t.strip()],
        "file": path.name,
    }


def nbsp_date(date):
    # Non-breaking hyphens keep GitHub from wrapping the date column at each "-".
    return date.replace("-", "‑")


def main():
    posts = sorted(
        (frontmatter(p) for p in (ROOT / "posts").glob("*.md")),
        key=lambda p: p["date"],
        reverse=True,
    )
    rows = ["| Date | Title | Tags |", "|---|---|---|"]
    rows += [
        f"| {nbsp_date(p['date'])} | [{p['title']}](./posts/{p['file']}) | {', '.join(p['tags'])} |"
        for p in posts
    ]
    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        raise SystemExit("README.md is missing the posts:start / posts:end markers")
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    README.write_text(f"{head}{START}\n" + "\n".join(rows) + f"\n{END}{tail}", encoding="utf-8", newline="\n")
    print(f"Wrote {len(posts)} posts to README.md")


if __name__ == "__main__":
    main()
