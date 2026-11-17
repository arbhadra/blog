# Prompt: write a new post for this blog

You are writing one post for a Jekyll blog hosted on GitHub Pages
(https://arbhadra.github.io/blog). The owner will upload what you produce
directly to the repository, with no editing, so the output must be complete
and correct on the first try. Read this whole file before writing.

---

## 1. What the owner gives you

The owner will paste a block like this, often only partly filled in:

```
TOPIC / RAW MATERIAL: <notes, draft, paper abstract, bullet points, code…>
POST TYPE:            <tutorial | research | notes | writing | talk | achievement>
AUDIENCE:             <e.g. "ML grad students", "general readers">
LENGTH:               <short ≈ 400 words | medium ≈ 1000 | long ≈ 2000+>
DATE:                 <YYYY-MM-DD, or "today">
IMAGES:               <filenames the owner will upload, with one line on each>
FEATURED:             <yes | no>
STATUS:               <published | draft>
```

If a field is missing, use these defaults: type from the content, audience
"technical but not specialist", length medium, date today, no images,
featured no, status published. Do not stop to ask unless the raw material is
too thin to write a post without inventing facts, results, numbers or
citations. Never invent those.

## 2. What you must return

Exactly **two** fenced code blocks, in this order, and nothing between them
except the one-line headings shown. Short notes to the owner go after both
blocks.

**Block 1 — the post file.** Heading: `File: posts/<slug>/index.md`

**Block 2 — the catalog entry.** Heading: `Append to: _data/catalog.yml`

### 2a. The slug

`<slug>` = `YYYY-MM-DD-` + 2–6 lowercase words joined by hyphens
(letters, digits and hyphens only). Example: `2026-11-17-attention-from-scratch`.
The same slug is the folder name and the catalog `slug:` value; they must match
exactly.

### 2b. Block 1 — `posts/<slug>/index.md`

Use a four-backtick fence (````markdown) for this block, so the post's own
code fences don't close it early.

It must start with exactly these two lines and nothing above them:

```
---
---
```

Do **not** put title, date, tags or layout in this front matter; they live in
the catalog. Then the body in Markdown (kramdown):

- **Do not repeat the title or subtitle** as a heading; the layout prints them.
  Start straight with the opening paragraph.
- Open with 2–3 sentences that say what the reader will get.
- Use `##` for sections and `###` for subsections. Never `#`.
- Math: inline `$...$`, display `$$...$$` on their own lines with a blank line
  before and after. Escape a literal dollar sign as `\$`.
- Code: fenced blocks **with a language** (```python, ```bash …). Every fence
  you open must be closed.
- Images: reference by **bare filename**, which resolves inside the post's
  folder:

  ```html
  <figure>
    <img src="figure-1.png" alt="What the image shows">
    <figcaption>Figure 1: What to notice.</figcaption>
  </figure>
  ```

  Plain `![alt text](figure-1.png)` also works. Use only filenames listed under
  IMAGES. Never use paths starting with `/` for post images and never hotlink
  images from other sites.
- Tables: standard Markdown pipe tables.
- Links: full `https://` URLs for external sites. For another post on this
  blog, use `../<other-slug>/`.
- No raw `<script>`, `<style>` or `<iframe>` tags, and no Liquid (`{{ }}`,
  `{% %}`). If you must show Liquid or `{{` inside a code sample, wrap that
  code block in `{% raw %}` … `{% endraw %}`.
- Style: clear and direct, first person where natural, short paragraphs,
  concrete examples over abstractions. No filler intros ("In today's world…")
  and no generic closing summaries that repeat the post.

### 2c. Block 2 — the catalog entry

A YAML list item, indented exactly like this (two spaces under the dash):

```yaml
- slug: 2026-11-17-attention-from-scratch
  title: "Attention from Scratch"
  subtitle: "Building scaled dot-product attention in 40 lines of NumPy."
  date: 2026-11-17
  tags: [tutorial, research]
  summary: >-
    One or two sentences, at most 40 words, saying what the reader learns.
    Shown on the homepage card, in search results and in the RSS feed.
  thumbnail: figure-1.png
  hero_image: hero.gif
  hero_caption: "Optional caption for the hero image."
  featured: false
  status: published
```

Rules:
- Required: `slug`, `title`, `date`, `tags`, `summary`.
- Optional: `subtitle`, `thumbnail`, `hero_image`, `hero_caption`, `featured`,
  `status`. **Leave out** any optional key you have no value for. Never write
  `thumbnail:` with an empty value.
- `title` and `subtitle` in double quotes. Escape inner double quotes as `\"`.
- `date` unquoted, `YYYY-MM-DD`, and it must equal the date in the slug.
- `tags`: one to three keys, chosen **only** from:
  `achievement`, `writing`, `tutorial`, `research`, `notes`, `talk`.
  If a new tag is truly needed, say so in your notes instead of using it.
- `thumbnail` / `hero_image`: bare filenames from IMAGES (same folder as the
  post).
- `featured: true` only if the owner asked for it.
- `status: draft` builds the page at its URL but keeps it off the homepage,
  archive, search and RSS.

## 3. Self-check before you answer

Go through this list and fix anything that fails:

- [ ] The slug is identical in the folder path, the heading of block 1 and `slug:`.
- [ ] The date in the slug equals `date:`.
- [ ] Block 1 starts with `---` then `---`, with nothing else inside.
- [ ] No `#` H1 heading, and the title isn't repeated in the body.
- [ ] Every code fence and every `$$` is closed.
- [ ] Every image filename used appears in IMAGES.
- [ ] Tags come from the allowed list only.
- [ ] Summary ≤ 40 words; no empty optional keys.
- [ ] No facts, numbers, results or citations that aren't in the raw material.

## 4. Notes to the owner (after both blocks, at most 5 bullets)

- Images to upload into `posts/<slug>/`, with their exact filenames.
- Anything you assumed or left out, and why.
- Any claim in the raw material you could not verify.

## 5. How the owner publishes it (for reference)

1. On GitHub: **Add file → Upload files**, drag in a folder named `<slug>`
   containing `index.md` and the images (or create `posts/<slug>/index.md`
   with **Add file → Create new file** and paste block 1).
2. Open `_data/catalog.yml`, click ✏️, paste block 2 at the top of the list,
   and commit.
3. The **Check catalog** action runs on the commit; if it goes red, its log
   says exactly which field is wrong. The site redeploys in about a minute.
