# Manish Bhadra Arnab — Blog

A minimalist, Distill-inspired blog built with **Jekyll** and hosted on **GitHub Pages**.

🔗 **Live site:** https://arbhadra.github.io/blog

---

## ✨ Features

- Clean, academic design (serif body + sans-serif UI) inspired by [distill.pub](https://distill.pub/)
- **Reusable, color-coded tags** managed from a single file
- **MathJax** support for LaTeX equations
- **Syntax-highlighted** code blocks
- Client-side **tag filtering** on the homepage
- Client-side **search**
- Estimated **reading time** and publish dates
- **RSS feed**, SEO meta tags, and a custom **404 page**

---

## 📝 Writing a New Post

Every post is **a folder you upload + one entry in the catalog**.

```
posts/
  2026-11-17-attention-from-scratch/   ← the "slug": YYYY-MM-DD-short-title
    index.md                           ← the post body
    figure-1.png                       ← images live next to the post
_data/catalog.yml                      ← title, date, tags, summary, images…
```

1. **Write it** — paste [`AGENTS.md`](AGENTS.md) into your AI agent together
   with your notes. It returns two blocks: the `index.md` file and the
   catalog entry. (Or copy `posts/_template/index.md` and write by hand.)
2. **Upload the folder** — on GitHub: *Add file → Upload files*, drag in the
   `<slug>` folder (with `index.md` and its images) into `posts/`.
3. **Register it** — edit `_data/catalog.yml` and paste the entry at the top
   of the list. Commit.
4. **Check** — the *Check catalog* action (Actions tab) goes green ✓ or tells
   you exactly which field is wrong. The site redeploys in ~1 minute.

`index.md` needs only an empty front matter block (`---` then `---`) at the
top; all metadata lives in the catalog. Set `status: draft` to build a post at
its URL without listing it anywhere, and `featured: true` to pin it on the
homepage. Field reference: comments at the top of `_data/catalog.yml`.

Post URLs look like `/blog/posts/<slug>/`. Images referenced by bare filename
(`figure-1.png`) resolve inside the post's own folder.

### Math

Inline: `$E = mc^2$` → $E = mc^2$
Display:

```
$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$
```

### Code

Use fenced code blocks with a language name:

    ```python
    print("Hello, Professor!")
    ```

### Validate locally (optional)

```bash
pip install pyyaml
python scripts/check_catalog.py
```

---

## 🏷️ Managing Tags

All tags live in **`_data/tags.yml`**. Each tag has a display name and a color.

```yaml
tutorial:
  name: "Tutorial"
  color: "#3d5a80"
```

- **To use a tag:** put its key (e.g., `tutorial`) in the post's `tags:` list in `_data/catalog.yml`.
- **To add a new tag:** add a new entry to `_data/tags.yml`, then use its key (and add it to the allowed list in `AGENTS.md`).
- **To recolor a tag:** change its `color` value — it updates everywhere.

Current tags: `achievement`, `writing`, `tutorial`, `research`, `notes`, `talk`.

---

## 🎨 Editing the Design

- **Colors & fonts:** edit the `:root` variables at the top of `assets/css/style.css`.
- **Site title, bio, links:** edit `_config.yml` and `index.html`.
- **About page:** edit `about.md`.

---

## 🗂️ Project Structure

```
.
├── _config.yml          # Site settings
├── Gemfile              # Dependencies
├── AGENTS.md            # Prompt for an AI agent to write a post
├── index.html           # Homepage (built from the catalog)
├── archive.html         # All posts grouped by year
├── feed.xml             # RSS/Atom feed (built from the catalog)
├── about.md             # About page
├── search.html          # Search page
├── search.json          # Search index (auto-generated)
├── 404.html             # Custom 404 page
├── _layouts/            # Page templates
├── _includes/           # Reusable partials (header, footer, tags…)
├── _data/catalog.yml    # ★ Post catalog — one entry per post
├── _data/tags.yml       # Tag definitions + colors
├── posts/<slug>/        # One folder per post: index.md + images
├── posts/_template/     # Starter post (ignored by Jekyll)
├── scripts/             # check_catalog.py validator
├── .github/workflows/   # Catalog check + test build on every commit
└── assets/css/style.css # Styles
```

---

## 💻 Running Locally (optional)

Requires Ruby. From the repo folder:

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000/blog

---

## 🚀 Deployment

The site auto-deploys via GitHub Pages whenever you push to the `main` branch.
Enable it under **Settings → Pages → Deploy from a branch → `main` / root**.
