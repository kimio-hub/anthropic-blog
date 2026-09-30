# Source study

An editorial-design analysis of public anthropic.com pages. It is not an official Anthropic design
specification, and nothing here grants permission to use Anthropic's brand, fonts or artwork.

- **First study:** 2026-09-14 (econ-scenarios text and first-screen styles; screenshots below the fold
  timed out).
- **Second study:** 2026-09-30. Headless Edge (Playwright) at 1440 × 900 and 390 × 844. For each page:
  screenshots at 8–13 scroll positions, computed styles of typographic elements, `:root` custom
  properties, `@font-face` rules and a block outline with positions and sizes. Font stand-ins were chosen
  by rendering candidates next to crops of the originals.

Re-measure before claiming pixel accuracy; the site changes.

## Pages studied (2026-09-30)

| Template | Pages |
|---|---|
| Institute features | `/institute/econ-scenarios`, `/institute/measuring-pace-of-ai-development`, `/institute/recursive-self-improvement` |
| Research posts | `/research/project-swap`, `/research/your-thoughts-on-ai`, `/research/yes-claude-can-do-nine-loops`, `/research/formalizing-fermats-last-theorem` |
| Engineering posts | `/engineering/how-we-contain-claude`, `/engineering/building-effective-agents`, `/engineering/effective-context-engineering-for-ai-agents` |
| News | `/news/claude-text-watermark` |

## Measured values (desktop 1440px unless noted)

| Element | Observed | Mobile (390px) |
|---|---|---|
| Page background / text | `#faf9f5` / `#141413` | same |
| Body paragraph | serif 17px / 26.35px (1.55), 640px column, 16px between paragraphs | 17px, 326px column, 32px margins |
| Post title | sans 700, 52px / 57.2px, centred (research) or beside art (engineering) | 32px / 35.2px |
| h2 / h3 / h4 | sans 600: 32 / 38.4, 25 / 30, 19 / 22.8; h2 margins 64 / 32, h3–h4 32 / 8 | 23 / 27.6, 20 / 24, 17 / 20.4 |
| Eyebrow, date | sans 15px / 21px (eyebrow 700) | same |
| Engineering summary | sans 25px / 38.75px beside "Published <date>" (17px), under a 1px ink rule | stacks |
| Links | ink colour, underline 1.36px (0.08em), offset 0.07–0.18em | same |
| Figure | 880px wide, image radius 16px; caption sans 14px / 16.8px, `#5e5d59`, 8px above | full column width |
| Hero image | 880px, radius 24px, 64px below the header block, 96px above the body | full width minus margins |
| Figure frame | outer `#e8e6dc` ≈16px padding, radius 16; inner paper card; title sans 600 ~24–28px; subtitle sans ~15px muted; notes and source 11px | same structure |
| Table | panel `#f0eee6`, radius 16; cells sans 15px / 21px, 16px padding, 1px `#d1cfc5` bottom rules | scrolls inside the panel |
| Code block | `#f0eee6`, 1px `#e8e6dc` border, radius 12, padding 32 16 32 32, mono | same |
| Inline code | JetBrains Mono, clay `#d97757` on `#f0eee6`, 1px `#d1cfc5` border, radius 4 | same |
| Blockquote | 1px ink left rule, 16px left padding, text `#30302e` | same |
| Pull quote | serif 36px / 45px, 944–960px wide, hanging opening quote; attribution sans 15px muted | 28px / 35px |
| Sidebar TOC | 172px wide at the page margin; items sans 12px / 14.4px, `#87867f`, active ink 500, 1px dividers; collapses to an icon on scroll | hidden |
| Buttons | sans 13px / 20px, `#3d3d3a` on `#f5f4ed`, 1px `#e8e6dc`, radius 6 (pills 999), 28px tall; primary ink on paper | same |
| Selected preset pill | `#e8e6dc` fill, `#dedcd1` border, ink text | same |
| Step card (scrolly) | 416px, `#f5f4ed`, 1px `#c2c0b6`, radius 8, padding 16, shadow `0 4px 24px rgba(0,0,0,.05)`; lead sans 17px 700, body serif 17px, note sans 13px | full width, at the bottom |
| Scroll progress | sticky 8px track `#f5f4ed`, fill `#d1cfc5`, only within the scrolly section | same |
| Chart label (Institute) | sans 13px 700, centred; legend sans 13px `#87867f`; notes 11px / 16.5px, 465px wide | same |
| Finding heading (Institute) | serif 22px / 32px, grey kicker "Finding N: Topic" + ink claim | 19px |
| Split hero (econ) | art ≈ 70% width with the grid and crayon strokes; text column ≈ 310–370px: serif h1 28px / 36px, standfirst serif 17px `#30302e`, two small buttons | text first, centred title 22px, art below |
| Display hero (RSI) | serif 66px / 72.9px on a dotted grid, sans 17px subtitle `#5e5d59`, pixel-art glyphs | 32px |
| Timeline scrolly (RSI) | years sans 10px uppercase 0.05em; step titles sans 19px 600; active ink, inactive `#5e5d59`–faint | stacked |

Custom properties exposed on `:root` include a neutral ramp from `#ffffff` to `#0f0f0e` (`slate-050`
`#faf9f5` … `slate-950` `#141413`), accents clay `#d97757`, sky `#6a9bcc`, olive `#788c5d`, fig
`#c46686`, heather `#cbcadb`, cactus `#bcd1ca`, oat `#e3dacc`, coral `#ebcece`, a type scale
(display 20–80px, headline 19–52px, body 12–25px, caption 14px, micro 10px), line-heights 100–155%,
spacing steps 4–192px, radii 2–32px, `--text-column-max-width: 640px`, `--media-max-width: 880px`,
`--page-margins: 64px`, container 1400px, header 68px, breakpoints 567 / 992 / 1024px, and an
`ease-out-quart` curve `cubic-bezier(.165,.84,.44,1)`.

Data-illustration colours in the econ feature cluster around fig, sky, olive and lavender `#918bd6`,
each with three lighter tints, plus pine `#217d5d`, brick `#b0403a`, amber `#f0ac54` and stone `#bdbaae`.

Hand-drawn textures on that page are SVG filters: high-frequency fractal noise turned into alpha grain
and composited with the shape, then a low-frequency displacement for wobbly edges (three strengths:
marker, dry brush, ruled line). `figures.md` gives original recipes built on the same general technique.

## Fonts on the source site

`anthropicSans`, `anthropicSerif`, `anthropicMono` (proprietary, current), with older `styreneA/B`,
`tiemposText` and `copernicus` still declared, and `JetBrains Mono`. The skill uses open stand-ins:
Source Serif 4 reproduced the exact line breaks of a 640px anthropicSerif paragraph; Schibsted Grotesk
was the closest of thirteen open sans faces for the 52px bold title and 32px semibold h2.

## What generalises and what does not

Generalises (use freely):

- A stable 640px serif column with sans structure; figures breaking out to 880–960px.
- Colour as meaning with one quiet accent; ink-coloured links.
- Figures in frames with the takeaway as the title and source at the foot.
- Summary bullets, run-in leads, findings as claims, limits in the body, credit at the end.
- For explainers: teach one concrete case (a nurse's tasks, a project's stages) before inviting the
  reader to change assumptions; reveal results as a sequence of questions.

Specific to particular pieces (use only when the content calls for it):

- The branching-futures hero, the task mosaic, the nurse example, survey swarms and scenario presets
  belong to the economics feature. The atmospheric gradient and scroll-revealed sentences belong to one
  policy piece. Do not add them to every post.
- Short engineering tutorials do not need scrollytelling; research notes do not need a prediction quiz.

Not measured: animation timings beyond transition curves, the behaviour of every breakpoint, hover
states on all controls, and pages outside the list above.
