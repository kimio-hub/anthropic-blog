# Design system

All values live as CSS custom properties on `.editorial` in `assets/editorial.css`. Unless marked
"adapted", they were measured from public anthropic.com posts on 2026-09-30 (see `source-study.md`).
Change tokens, not component rules, when adapting to a user's brand.

## Colour

### Neutrals (warm paper-and-ink ramp)

| Token | Hex | Role |
|---|---|---|
| `--ed-paper` | `#faf9f5` | Page background |
| `--ed-paper-2` | `#f5f4ed` | Buttons, step cards |
| `--ed-paper-3` | `#f0eee6` | Code blocks, table panels |
| `--ed-frame` | `#e8e6dc` | Figure frame; hairline borders on paper-2 |
| `--ed-line-2` | `#dedcd1` | Selected pill border |
| `--ed-line` | `#d1cfc5` | Rules, table borders, gridlines, TOC dividers |
| `--ed-line-3` | `#c2c0b6` | Step-card border |
| `--ed-faint` | `#b0aea5` | Inactive timeline steps, disabled |
| `--ed-subtle` | `#87867f` | Legends, chart notes, TOC links |
| `--ed-muted` | `#5e5d59` | Captions, footnotes, secondary text |
| `--ed-ink-3` | `#3d3d3a` | Button text |
| `--ed-ink-2` | `#30302e` | Standfirst, blockquote |
| `--ed-ink` | `#141413` | Body text, headings, primary buttons |

Contrast on `#faf9f5` (WCAG): ink 17.5:1, ink-2 12.6:1, muted 6.3:1, subtle 3.5:1, faint 2.1:1. Use
`--ed-subtle` only for text ≥ 13px that repeats information available elsewhere (legend labels, chart
notes) and `--ed-faint` only for inactive or decorative text, never for body copy.

### Accents

| Family | Base | Tint 2 | Tint 3 | Typical meaning |
|---|---|---|---|---|
| clay | `#d97757` | `#e8b59a` | `#f4ddd0` | The one "voice" accent; key series. Clay is 3:1 on paper, so small clay text uses `--ed-clay-text` `#a64e33` (adapted, 4.8:1), e.g. inline code |
| sky | `#6a9bcc` | `#a8c4de` | `#d9e6f1` | Automation, second series, "other" groups |
| olive | `#788c5d` | `#a2b48b` | `#d6ddc9` | Growth, generation steps, positive change |
| fig | `#c46686` | `#d89eb0` | `#f0d9e0` | Contrast series, risk |
| lavender | `#918bd6` | `#bdb9ea` | `#e3e1f6` | Augmentation, retrieval, AI-assisted |
| amber | `#f0ac54` | `#f6cd94` | `#fbe8cc` | New or emerging things, warnings |
| pine `#217d5d`, brick `#b0403a`, stone `#bdbaae` | | | | Labour/capital-style splits; loss/displacement; unchanged/baseline |

Illustration grounds (flat fields behind ink drawings): heather `#cbcadb`, cactus `#bcd1ca`, oat `#e3dacc`,
coral `#ebcece`.

Rules: one accent per page carries emphasis; the other hues encode categories. Keep a concept's colour
identical in prose highlights, legends, controls and charts. Pair colour with a label, position or line
style so meaning survives greyscale and colour-blindness.

### Dark theme (adapted, opt-in)

`<body class="editorial" data-theme="dark">` swaps the neutral ramp (paper `#1f1e1d`, ink `#faf9f5`).
Accents stay. The source site has no dark mode; offer it only if the user's site needs one, and check
illustrations, which are usually drawn for a light ground.

## Typography

### Families (open-licensed stand-ins)

| Role | Source site | Stand-in | Why |
|---|---|---|---|
| Reading serif | anthropicSerif (proprietary) | **Source Serif 4** (OFL) | Same measure: identical line breaks on a 640px, 17px test paragraph |
| Structure sans | anthropicSans (proprietary) | **Schibsted Grotesk** (OFL) | Closest width and weight at 52px bold and 32px semibold among thirteen open sans faces tested side by side |
| Code | JetBrains Mono (used by the site) | **JetBrains Mono** (OFL) | Same face |
| Chinese reading | — | **Noto Serif SC** / Source Han Serif SC, then Songti SC | Song/Ming texture matches the serif column |
| Chinese UI | — | system gothic: PingFang SC, Hiragino Sans GB, Microsoft YaHei, Noto Sans SC | Loads nothing extra |

Load from Google Fonts (see the templates) or self-host the same families. Where Google Fonts is slow or
blocked (for example mainland China), self-host the WOFF2 files or use a mirror the user trusts; the
fallback stacks keep the page readable if fonts fail.

### Scale

Desktop values at 1440px, mobile at 390px; tokens interpolate with `clamp()` in between.

| Element | Token | Desktop | Mobile | Face / weight / leading |
|---|---|---|---|---|
| Body | `--ed-fs-body` | 17px | 17px | serif 400 / 1.55 (CJK 1.85) |
| Title (post) | `--ed-fs-title` | 52px | 32px | sans 700 / 1.1, tracking −0.012em |
| Display title (feature) | `--ed-fs-display` | 66px | 34px | serif 400 / 1.1 |
| Split-hero title, statement | `--ed-fs-statement` | 28px | 23px | serif 400 / 1.28 |
| h2 | `--ed-fs-h2` | 32px | 23px | sans 600 / 1.2 |
| h3 | `--ed-fs-h3` | 25px | 20px | sans 600 / 1.2 |
| h4 | `--ed-fs-h4` | 19px | 17px | sans 600 / 1.2 |
| Engineering dek | `--ed-fs-dek` | 25px | 20px | sans 400 / 1.55 |
| Pull quote | `--ed-fs-quote` | 36px | 26px | serif 400 / 1.25, hanging “ |
| Finding heading | — | 22px | 19px | serif 400 / 1.45, grey kicker + ink claim |
| Eyebrow, date, table | `--ed-fs-ui` | 15px | 15px | sans (eyebrow 700) |
| Caption | `--ed-fs-caption` | 14px | 14px | sans 400 / 1.35, muted |
| Legend, buttons, chart label | `--ed-fs-small` | 13px | 13px | sans; chart label 700 centred |
| Chart notes, source | `--ed-fs-micro` | 11px | 11px | sans, subtle |

Headings are sans in posts and serif in visual features; do not mix both styles for the same level on
one page. Bold in body text is `600`. Use `text-wrap: balance` for headings (already set).

## Layout

| Token | Value | Use |
|---|---|---|
| `--ed-text` | 640px | Reading column (≈ 70–75 Latin characters, ≈ 37 CJK characters at 17px) |
| `--ed-media` | 880px | Figures, hero art, tables |
| `--ed-wide` | 960px | Big charts, pull quotes, explorers |
| `--ed-container` | 1272px | Headers and full-width grids (1400 minus 2 × 64) |
| `--ed-margin` | 24px → 64px | Page side margin (`clamp`) |
| `--ed-toc-w` | 172px | Sidebar TOC, shown from 1200px |
| `--ed-bar-h` | 68px | Site bar height |

Vertical rhythm (measured): paragraphs 16px apart; h2 64px above / 32px below; h3 and h4 32px above /
8px below; figures ≈ 40px from text; hero → body 96px; header blocks separated by 32px. On mobile h2
spacing drops to 56/24.

Radii: 4px inline code and panels · 6px buttons · 8px step cards · 10–12px inner cards and code blocks ·
16px frames, figures, table panels · 24px hero art · 999px pills.

Every direct child of `.ed-body` is centred at 640px. Add `.ed-media`, `.ed-wide` or `.ed-full` to break
out. Class-less `<section>` wrappers are transparent, so semantic sections do not break the column.

## CJK rules (`lang="zh-CN"`, `zh-TW`, `ja`)

Applied automatically by `:lang()` selectors:

- Body line-height 1.85, paragraph spacing 18px; `line-break: strict`; `text-autospace: normal` adds
  CJK–Latin spacing where supported (do not type manual spaces if the browser supports it; typing a
  normal space between Chinese and Latin words is still fine and common).
- Display headings use `word-break: keep-all`, so words are not split across lines. Mark acceptable
  breaks with `<wbr>`: `AI 能让一个<wbr>研究项目<wbr>快多少？`.
- `em` becomes emphasis dots (着重号), not fake italics; italic notes (`.ed-lede`, `.ed-ack`) turn upright.
- Titles use small positive tracking (0.01–0.02em) instead of the negative Latin tracking.
- Chinese body text is Song/Ming serif by default. Add `.ed-cjk-sans` to `<body>` for gothic body text
  (better on low-resolution Windows screens if no web font is loaded).
- Use full-width punctuation in Chinese text, 「」 or “” consistently, and 《》 for titles of works.

## Adapting to a brand

1. Map the user's colours: page background → `--ed-paper`, text → `--ed-ink`, one brand colour →
   `--ed-accent` (and `--ed-clay` if charts should follow).
2. Map fonts through `--ed-serif`, `--ed-sans`, `--ed-mono`. Keep one serif for reading and one sans for
   structure; if the brand has only a sans, set both and increase body line-height to 1.6.
3. Keep the measures (640/880/960), spacing and figure frames; they carry most of the style.
4. Re-run the render check.
