#!/usr/bin/env python3
"""Validate _data/catalog.yml against the posts/ folder.

Run from the repo root:  python scripts/check_catalog.py
Exits 1 with a readable list of problems if anything is wrong.
"""
import datetime as dt
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "_data" / "catalog.yml"
TAGS = ROOT / "_data" / "tags.yml"
POSTS = ROOT / "posts"

REQUIRED = ["slug", "title", "date", "tags", "summary"]
OPTIONAL = ["subtitle", "thumbnail", "hero_image", "hero_caption", "featured", "status"]
SLUG_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)", re.M)

errors, warnings = [], []


def err(where, msg):
    errors.append(f"  ✗ {where}: {msg}")


def warn(where, msg):
    warnings.append(f"  ! {where}: {msg}")


def check_image(where, slug, key, value):
    if not isinstance(value, str) or not value.strip():
        err(where, f"`{key}` is empty — remove the key if there is no image")
        return
    if "://" in value:
        return
    path = ROOT / value.lstrip("/") if value.startswith("/") else POSTS / slug / value
    if not path.is_file():
        err(where, f"`{key}: {value}` not found (looked for {path.relative_to(ROOT)})")


def main():
    tags = set((yaml.safe_load(TAGS.read_text(encoding="utf-8")) or {}).keys())
    try:
        catalog = yaml.safe_load(CATALOG.read_text(encoding="utf-8")) or []
    except yaml.YAMLError as e:
        print(f"✗ _data/catalog.yml is not valid YAML:\n{e}")
        return 1
    if not isinstance(catalog, list):
        print("✗ _data/catalog.yml must be a list of entries (each starting with '- slug:')")
        return 1

    seen = set()
    for i, e in enumerate(catalog, 1):
        where = f"catalog entry #{i}"
        if not isinstance(e, dict):
            err(where, "is not a mapping — check indentation")
            continue
        slug = e.get("slug")
        if slug:
            where = f"`{slug}`"
        for k in REQUIRED:
            if e.get(k) in (None, "", []):
                err(where, f"missing required field `{k}`")
        for k in e:
            if k not in REQUIRED + OPTIONAL:
                warn(where, f"unknown field `{k}` (typo?)")
        if not slug:
            continue
        slug = str(slug)
        if slug in seen:
            err(where, "duplicate slug")
        seen.add(slug)
        if not SLUG_RE.match(slug):
            err(where, "slug must look like YYYY-MM-DD-lowercase-words")

        date = e.get("date")
        if date is not None:
            if not isinstance(date, dt.date):
                err(where, f"`date: {date}` must be an unquoted YYYY-MM-DD date")
            elif not slug.startswith(date.isoformat()):
                err(where, f"`date: {date}` does not match the date in the slug")

        t = e.get("tags")
        if t is not None:
            if not isinstance(t, list):
                err(where, "`tags` must be a list like [tutorial, research]")
            else:
                for tag in t:
                    if tag not in tags:
                        err(where, f"unknown tag `{tag}` — add it to _data/tags.yml first")

        if e.get("status", "published") not in ("published", "draft"):
            err(where, "`status` must be published or draft")
        if "featured" in e and not isinstance(e["featured"], bool):
            err(where, "`featured` must be true or false")
        summary = e.get("summary")
        if isinstance(summary, str) and len(summary.split()) > 60:
            warn(where, f"summary is {len(summary.split())} words; aim for ≤ 40")

        index = POSTS / slug / "index.md"
        if not index.is_file():
            err(where, f"no post file at posts/{slug}/index.md")
        else:
            text = index.read_text(encoding="utf-8")
            if not text.startswith("---"):
                err(where, "index.md must start with a `---` / `---` front matter block")
            if len(FENCE_RE.findall(text)) % 2:
                err(where, "index.md has an unclosed ``` code fence")
            if text.count("$$") % 2:
                err(where, "index.md has an unclosed $$ math block")
            if re.search(r"^# ", text, re.M) and not re.search(r"^```", text, re.M):
                warn(where, "index.md uses a top-level `# ` heading; use `##` (the title is printed by the layout)")

        for key in ("thumbnail", "hero_image"):
            if key in e:
                check_image(where, slug, key, e[key])

    for folder in sorted(p for p in POSTS.iterdir() if p.is_dir() and not p.name.startswith("_")):
        if folder.name not in seen:
            warn(f"posts/{folder.name}/", "has no catalog entry, so it is not listed on the site")

    if warnings:
        print("Warnings:\n" + "\n".join(warnings))
    if errors:
        print("Errors:\n" + "\n".join(errors))
        print(f"\n✗ {len(errors)} problem(s) in the catalog.")
        return 1
    print(f"✓ Catalog OK — {len(catalog)} entr{'y' if len(catalog) == 1 else 'ies'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
