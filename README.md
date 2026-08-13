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

Create a file in the `_posts/` folder named:

```
YYYY-MM-DD-title-of-post.md
```

Example: `_posts/2025-03-01-my-first-tutorial.md`

Add this front matter at the top:

```yaml
---
layout: post
title: "My Post Title"
subtitle: "An optional one-line description."
date: 2025-03-01
tags: [tutorial, research]
---
```

Then write your content in Markdown below it. Use `<!--more-->` to mark
where the homepage excerpt should stop.

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

---

## 🏷️ Managing Tags

All tags live in **`_data/tags.yml`**. Each tag has a display name and a color.

```yaml
tutorial:
  name: "Tutorial"
  color: "#3d5a80"
```

- **To use a tag:** put its key (e.g., `tutorial`) in a post's `tags:` list.
- **To add a new tag:** add a new entry to `_data/tags.yml`, then use its key.
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
├── index.html           # Homepage (post list + tag filter)
├── about.md             # About page
├── search.html          # Search page
├── search.json          # Search index (auto-generated)
├── 404.html             # Custom 404 page
├── _layouts/            # Page templates
├── _includes/           # Reusable partials (header, footer, tags…)
├── _data/tags.yml       # Tag definitions + colors
├── _posts/              # Your blog posts (Markdown)
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
