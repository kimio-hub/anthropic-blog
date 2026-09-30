# Figures, charts and illustrations

A figure earns its place when the reader can see something in it that the prose alone would make them
work for. Before drawing, write three lines: **what the reader should notice**, **the sentence before the
figure** that tells them where to look, and **the sentence after** that says what it means and where it
stops applying.

## Choose the form by the question

| The reader needs to see… | Use | Avoid |
|---|---|---|
| A difference between a few categories | Horizontal bars (`.ed-bars`), values at bar ends | Pie charts, 3D, dual axes |
| Composition and how it shifts | 100% stacked bars, one row per condition | Stacked areas with many layers |
| Change over time | Line chart, direct labels at line ends, shaded uncertainty | Legends far from the lines |
| The same pattern under several conditions | Small multiples with shared axes (`.ed-panels`) | One chart with 8 series |
| A process or mechanism | Flow diagram (`.ed-flow`) or a framed sequence of cards | Arrows implying data that does not exist |
| A plan or duration | Gantt-style bars on a shared time axis (see `feature.html`) | Tables of start and end dates |
| One striking number | A big serif number with a small sans label | Gauges, dials |
| An abstract idea to open a piece | Metaphor art (below), clearly decorative | Anything that looks like data but is not |

## Anatomy of the framed chart

```
┌ .ed-frame  (#e8e6dc, 16px padding, 16px radius) ───────────────────────┐
│ ┌ .ed-frame__card  (#faf9f5, 10px radius, 36px padding) ──────────────┐ │
│ │ Title states the takeaway            ← sans 600, 19–24px            │ │
│ │ What is measured, unit, population   ← sans 15px, muted             │ │
│ │ legend (if unavoidable)              ← 12–13px, swatches            │ │
│ │ ███████████████████ 86%              ← the chart                    │ │
│ │ Note: n, method           Source: …  ← 11px, subtle, split L/R      │ │
│ └──────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
Figure 2. What to notice and the condition it depends on.   ← caption below, 14px
```

Variants seen on the source site: several cards stacked in one frame with a small arrow between them
(a sequence); a white card (`.ed-card-white`) at 960px for dense charts; no frame at all on pencil-grid
paper for Institute-style explorers, with a centred 13px bold chart label and an 11–12px note below.

## Labelling rules

- The title is a claim ("Quoted passages make most claims checkable"), the subtitle is the measure.
- Put numbers on the marks. Label lines at their ends in the line's colour. Use a legend only when marks
  cannot be labelled directly, and order it like the marks.
- Units in the subtitle or on the axis, never only in the text. Start bar axes at zero.
- Annotate the one thing that matters (a dashed "today" line, a bracket, a callout with a thin leader).
- Every factual chart has a source line; every illustrative one says so inside the figure
  ("Illustrative", "Toy model", or the `.ed-sample-badge` while drafting).
- Captions start with "Figure N." in semibold and say what to notice, not what the axes are.

## Palette in charts

- One highlight, the rest quiet: key series in clay `#d97757` (or the page accent), comparison series in a
  tint (`#e8b59a`) or stone `#bdbaae`.
- Categorical sets: lavender `#918bd6` → sky `#6a9bcc` → olive `#788c5d` → fig `#c46686` → amber
  `#f0ac54`. Stone for "unchanged / baseline", brick `#b0403a` for loss, pine `#217d5d` for a second pole.
- Tints (`-2`, `-3` tokens) for areas, bands and backgrounds; base colours for lines and small marks.
- Gridlines `#d1cfc5` at 1px; axis tick labels 11px `#87867f`; value labels 12px ink, semibold.
- Keep colours stable across the whole piece: if lavender means "AI-assisted" in the scrollytelling, it
  means that in every chart and legend after it.

## Responsive charts

- Bars, stacks, flows and tables are built in HTML/CSS in the templates, so text stays 11–13px on a phone.
- SVG text scales with the viewBox. A 760px-wide SVG shown on a 330px screen shrinks 12px labels to 5px.
  Either redraw the SVG from data at the container width (ResizeObserver), provide a second, taller
  viewBox for narrow screens, or move labels into HTML.
- Never let a figure cause horizontal page scroll; wide tables and code scroll inside their own panel.

## Accessibility

- `<figure>` + `<figcaption>`; images get `alt` that states the finding; decorative art gets
  `aria-hidden="true"` (SVG) or `alt=""` (img).
- Charts whose values matter should expose them as text: real HTML labels (the templates do this), a
  table in a `<details>`, or a sentence in the caption.
- Do not rely on colour alone: pair it with position, labels, dash patterns or texture.

## Illustration styles

Illustrations set the theme; they are metaphors, never evidence. Three styles fit this system:

**1. Flat ground + black ink** (news and research heroes). A single colour field (heather `#cbcadb`,
cactus `#bcd1ca`, oat `#e3dacc`, coral `#ebcece`, or clay for emphasis) with a large, simple drawing in
thick black strokes (8–12px at 880px wide, round caps and joins), off-white paper shapes (`#faf9f5`), and
at most one clay accent. Hands, paper, lenses, nodes, simple objects. See the hero in `article.html`.

**2. Crayon on pencil grid** (Institute explainers). A faint pencil grid that fades toward the edges,
with crayon-textured strokes or blocks in the data palette. The shapes echo the piece's mechanism
(diverging paths for scenarios, a compressed timeline for speed-ups, a mosaic for "many tasks").
See the hero and Gantt chart in `feature.html`.

**3. Glyph set** (engineering headers). Five or six bold black marks in a square, one tinted with a
pastel. See `components.md`.

Always draw original art. Do not trace or reuse another organisation's illustrations.

## Texture recipes (SVG filters)

Define once per page in a hidden SVG and apply with `filter="url(#id)"` on SVG elements or
`filter: url(#id)` in CSS on HTML elements (put the texture on a pseudo-element when the element contains
text, so the text stays crisp).

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <!-- Crayon: streaky grain in the fill plus a slight wobble at the edges -->
  <filter id="tex-crayon" x="-5%" y="-40%" width="110%" height="180%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.9 0.22" numOctaves="3" seed="3" result="grain"/>
    <feColorMatrix in="grain" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.3 1.45" result="holes"/>
    <feComposite in="SourceGraphic" in2="holes" operator="in" result="speckled"/>
    <feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="1" seed="9" result="warp"/>
    <feDisplacementMap in="speckled" in2="warp" scale="3" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <!-- Pencil: thin broken lines for grids and leaders -->
  <filter id="tex-pencil" x="-2%" y="-2%" width="104%" height="104%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="1" seed="5" result="grain"/>
    <feColorMatrix in="grain" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.4 1.25" result="holes"/>
    <feComposite in="SourceGraphic" in2="holes" operator="in" result="speckled"/>
    <feTurbulence type="fractalNoise" baseFrequency="0.015" numOctaves="1" seed="2" result="warp"/>
    <feDisplacementMap in="speckled" in2="warp" scale="3" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <!-- Ink: a hand-drawn wobble for black line art -->
  <filter id="tex-ink" x="-10%" y="-10%" width="120%" height="120%">
    <feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="11" result="warp"/>
    <feDisplacementMap in="SourceGraphic" in2="warp" scale="3.4" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <!-- Paper grain: overlay a rect with this filter at 30–40% opacity -->
  <filter id="tex-grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="4" stitchTiles="stitch"/>
    <feColorMatrix type="matrix" values="0 0 0 0 0.1  0 0 0 0 0.1  0 0 0 0 0.09  0 0 0 -0.9 0.62"/>
  </filter>
</defs></svg>
```

Tuning: in the crayon matrix, the last row `-a b` controls coverage (raise `b` or lower `a` for denser
fill); the first `baseFrequency` pair sets streak direction (x frequency ≫ y gives horizontal strokes);
the displacement `scale` sets edge wobble (2–4 for fills, 1–3 for lines, never on text). Fill crayon
blocks with several overlapping round-capped strokes rather than one rectangle; the overlap reads as
hand-laid colour. Vary `seed` between elements that sit side by side.

Keep data geometry exact: textures may roughen edges by a pixel or two, never move a bar's end or a
line's value. For precise reading, add a crisp tick or label at the true value.

## Hand-off specs (when you cannot draw it)

When delivering Markdown or when art must be commissioned, describe each figure as:

| Field | Example |
|---|---|
| Reader question | Why does the project not speed up as much as its fastest step? |
| Sentence before | Follow the review stage as the others shrink. |
| Encoding | Gantt bars per stage on a 0–24 week axis; lavender = AI-assisted, stone = hard to speed up |
| Sentence after | The unchanged stages now take three quarters of the time. |
| Data status | Toy model, illustrative numbers |
| Text fallback | One-sentence summary with the key numbers |
