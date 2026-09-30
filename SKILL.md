---
name: anthropic-blog
description: >-
  Write and build long-form explanatory articles in the editorial style of anthropic.com research,
  engineering and Institute posts: warm paper background, a serif reading column, sans-serif structure,
  framed figures, footnotes, and optional scrollytelling or interactive explorers. Use when the user asks
  for an "Anthropic-style" blog, post, report or explainer page; wants notes, a paper or Markdown turned
  into a polished HTML article; or wants an existing article restyled in this aesthetic. Ships a
  calibrated CSS design system, two page templates (article, interactive feature) and a render checker.
  Works in English and Chinese (CJK typography built in). Not for landing pages, slide decks or LaTeX papers.
license: MIT
metadata:
  author: kimio-hub
  version: "2.0.0"
---

# Anthropic-style editorial articles

Make a hard topic readable: text, figures and layout work together to explain one question, and every
claim can be traced to evidence. The look (warm paper, serif reading column, framed figures) serves that
goal; it is never a substitute for it. Keep the user's voice, brand and arguments. Never present the page
as Anthropic's: no Anthropic name, logo, wordmark, fonts, illustrations or copied text.

## 1. Pick the deliverable

Decide from the request; ask only when the topic or source material is missing.

| Request | Deliver | Start from |
|---|---|---|
| Write or edit an article | Complete Markdown or HTML article; figure specs where figures are needed | `references/editorial.md` |
| Build or restyle a page | A working page in the user's stack; standalone HTML if there is none | `assets/article.html` + `assets/editorial.css` |
| Explain a mechanism interactively | Visual feature with scrollytelling and/or an explorer | `assets/feature.html` |
| Analyse the style | Observation → effect → transferable rule, with measured vs inferred marked | `references/source-study.md` |

Pick the format by content, not by ambition:

- **Research / news post** (`article.html`, centred header): eyebrow, big sans title, date, hero art, sidebar TOC, summary bullets, framed charts, footnotes, citation.
- **Engineering post** (`article.html` with the engineering header from `references/components.md`): label, icon art beside the title, a hard rule, date and a one-paragraph summary; diagrams, code, tables.
- **Visual explainer** (`feature.html`): split hero with metaphor art, drop cap, a sticky step-by-step graphic, an explorer, "Finding N" sections, a closing statement, a method note. Use only when a changing picture teaches cause and effect.
- **Short essay**: title + dek + prose + at most one pull quote. Do not force figures or interactivity.

## 2. Workflow

1. **Frame.** Reader, central question, available evidence, output format. Write one sentence the reader should be able to say afterwards.
2. **Write first, style second.** Follow `references/editorial.md`: open with a concrete case, order sections by what the reader must understand first, headings as claims or real questions, separate measured / inferred / assumed.
3. **Build.** Copy the template and `editorial.css` into the project (inline the CSS for a single-file page). Set `<html lang>` (`en`, `zh-CN`, …); CJK typography switches on automatically. Replace the site bar with the user's own wordmark and links.
4. **Replace every sample.** Templates contain realistic placeholder text, numbers and a toy model. Rewrite from the user's material or delete. Elements with `data-sample` and `.ed-sample-badge` mark placeholder data; remove the attribute only after the content is real. Never ship template numbers.
5. **Figures.** Choose the form with `references/figures.md`. Put charts in the frame (outer `.ed-frame`, inner `.ed-frame__card`, title + subtitle inside, notes and source at the foot, caption below). Prefer HTML bars/flows so labels stay legible on phones.
6. **Interaction (optional).** Only when a reader's change reveals a rule. Follow `references/interaction.md`: default state readable, result stated in words (`aria-live`), works without JS and with reduced motion.
7. **Verify in a browser.** Run `python <this skill's folder>/scripts/check_page.py page.html` (needs Playwright; desktop + 390px screenshots, overflow, console errors, leftover samples, missing alt text). Look at the screenshots. If you cannot run a browser, say so explicitly.
8. **Report** what was built, what was verified and anything left for the user (fonts to self-host, data to fill in).

## 3. Design DNA

Values are calibrated from public anthropic.com posts; full tokens in `references/design-system.md`.

1. **Paper and ink.** Background `#faf9f5`, text `#141413`, hairlines `#e8e6dc` / `#d1cfc5`. One accent, clay `#d97757`, used sparingly (key data, inline code). Links are ink with a thin underline, not coloured.
2. **Serif to read, sans to navigate.** Body serif 17px / 1.55 in a 640px column. Titles sans 700 at 52px / 1.1; h2 sans 600 32px; h3 25px; h4 19px; captions 14px; UI and legends 13px. Feature pieces may use a serif display title instead.
3. **Rhythm by spacing, not boxes.** 16px between paragraphs, 64px above h2 and 32px below, figures break out to 880px, big charts and pull quotes to 960px. No cards around prose, no drop shadows except floating step cards.
4. **Figures in frames.** `#e8e6dc` frame, 16px padding, 16px radius, paper card inside; sans title and grey subtitle inside the card; 11px notes and source at the foot; caption "Figure N." below.
5. **Colour encodes meaning.** Data palette: clay, sky `#6a9bcc`, olive `#788c5d`, fig `#c46686`, lavender `#918bd6`, amber `#f0ac54`, stone `#bdbaae` for "unchanged / baseline". Same concept, same colour, across text, legend and chart. Direct labels beat legends.
6. **Art is a metaphor, not decoration.** Flat colour grounds (heather, cactus, oat, coral) with thick black ink lines, or crayon strokes on pencil-grid paper. No stock photos, 3D renders, gradients or glows. Decorative art never imitates a data chart.
7. **Small, quiet controls.** 13px buttons, 6px radius or pills, paper fill with a hairline; primary actions ink-filled.
8. **Mobile keeps the reading column.** 24–32px margins, title 32px, h2 23px; sticky graphics sit on top with cards below; no horizontal page scroll.

## 4. Guardrails

- **Not Anthropic.** Say "Anthropic-inspired" at most. The fonts are open stand-ins (Source Serif 4, Schibsted Grotesk, JetBrains Mono, Noto Serif SC). Never link Anthropic's font files or reuse its images.
- **The user's brand wins.** If the project has colours, fonts or components, map the tokens onto them instead of overriding.
- **Honest numbers.** Every figure has units, baseline, time range and source. Illustrative models and sample data are labelled as such in the figure, not only in the text. Never invent data to fill a layout.
- **Markdown is not a page.** When delivering Markdown, keep structure and precise figure specs, but do not claim fonts, layout or interaction were implemented.
- **Restyling is not rewriting.** When asked only to make a page beautiful, keep claims and numbers unchanged.

## 5. Files

| Path | Use |
|---|---|
| `assets/editorial.css` | Design system: tokens, layout, prose, headers, frames, charts, tables, code, controls, scrollytelling, CJK, dark theme (opt-in), print |
| `assets/article.html` | Research / engineering post template (English sample) |
| `assets/feature.html` | Interactive explainer template (Chinese sample, toy model + explorer) |
| `references/design-system.md` | Tokens, type scale, layout grid, fonts, CJK rules, theming |
| `references/components.md` | Copy-paste HTML for every component, including header variants |
| `references/figures.md` | Chart choice, frame anatomy, palette, labelling, illustration and texture recipes |
| `references/interaction.md` | Scrollytelling, explorers, motion, accessibility, no-JS fallbacks |
| `references/editorial.md` | Writing: narrative skeletons, headings, paragraphs, Chinese notes, figure storyboards |
| `references/source-study.md` | What was measured on anthropic.com and how far it generalises |
| `scripts/check_page.py` | Render check: screenshots, overflow, errors, samples, alt text |
