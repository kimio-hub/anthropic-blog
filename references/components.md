# Components

Copy-paste HTML for `assets/editorial.css`. Everything sits inside `<body class="editorial">`; body content
goes in `<div class="ed-body">`, where each direct child is centred in the 640px column. Working examples
of every snippet are in `assets/article.html` and `assets/feature.html`.

## Page skeleton

```html
<!doctype html>
<html lang="en">  <!-- zh-CN for Chinese: CJK rules switch on -->
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Title — Site</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Schibsted+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
  <!-- Chinese pages: add &family=Noto+Serif+SC:wght@400;600 -->
  <link rel="stylesheet" href="editorial.css">
</head>
<body class="editorial">
  <a class="ed-skip" href="#main">Skip to content</a>
  <header class="ed-bar"><a class="ed-bar__brand" href="/">Your Site</a>
    <nav class="ed-bar__nav" aria-label="Site"><a href="#">Writing</a><a href="#">About</a></nav></header>
  <main id="main"><article>
    <!-- header variant -->
    <div class="ed-body"> … </div>
  </article></main>
</body>
</html>
```

`.ed-bar--sticky` makes the bar stick with a translucent paper background.

## Headers

**A. Centred (research, news)** — eyebrow, title, meta, optional actions, hero art.

```html
<header class="ed-header--center">
  <p class="ed-eyebrow"><a href="#">Research</a></p>
  <h1 class="ed-title">A title that states the finding</h1>
  <p class="ed-meta"><time datetime="2026-09-30">Sep 30, 2026</time><span class="ed-sep">·</span>9 min read</p>
  <div class="ed-actions"><a class="ed-btn ed-btn--primary ed-btn--lg" href="#">Read the PDF</a></div>
</header>
<figure class="ed-hero"><svg viewBox="0 0 880 495" role="img" aria-label="…">…</svg></figure>
```

Optional dek under the meta: `<p class="ed-dek">One or two sentences.</p>`.

**B. Engineering** — label, square icon art beside the title, a hard rule, then date and a summary.

```html
<header class="ed-header--eng">
  <p class="ed-eyebrow"><a href="#">Engineering at Your Site</a></p>
  <div class="ed-header--eng__top">
    <svg class="ed-header--eng__art" viewBox="0 0 250 250" aria-hidden="true">
      <g fill="none" stroke="#141413" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="80" cy="80" r="62" stroke-dasharray="2 13"/><path d="M80 80 L118 44"/><circle cx="80" cy="80" r="7" fill="#141413"/>
        <path d="M178 26 v44 M200 26 v44 M222 26 v44 M170 48 h60"/>
        <rect x="170" y="100" width="58" height="58" rx="8"/><rect x="188" y="118" width="22" height="22" rx="3" fill="#141413"/>
        <path d="M26 190 l18 -22 l18 22 l18 -22 l18 22 l18 -22"/>
        <path d="M200 176 v56 M172 204 h56 M180 184 l40 40 M220 184 l-40 40"/>
      </g>
      <rect x="146" y="176" width="16" height="56" rx="2" fill="#bdb9ea"/><rect x="128" y="190" width="16" height="42" rx="2" fill="#bdb9ea"/>
    </svg>
    <h1 class="ed-title">How we test changes before they reach users</h1>
  </div>
  <hr class="ed-header--eng__rule">
  <div class="ed-header--eng__bottom">
    <p class="ed-meta">Published Sep 30, 2026</p>
    <p class="ed-dek">One paragraph that states the problem and what the reader will learn.</p>
  </div>
</header>
```

Draw your own glyphs: 5–6 simple marks in thick black strokes, one tinted with a pastel. Never reuse
another site's icon art.

**C. Split hero (visual features)** — metaphor art on the left, narrow text column on the right.

```html
<header class="ed-header--split">
  <div class="ed-header--split__art"><svg viewBox="0 0 1000 860" preserveAspectRatio="xMidYMid slice" aria-hidden="true">…</svg></div>
  <div class="ed-header--split__text">
    <h1 class="ed-title-serif">A question the piece answers?</h1>
    <p class="ed-standfirst">Two or three sentences: the stakes and what the reader can do here.</p>
    <div class="ed-actions"><a class="ed-btn" href="#method">Read the method ↗</a><a class="ed-btn" href="#explorer">Jump to explorer ↓</a></div>
  </div>
  <a class="ed-btn ed-scroll-hint" href="#intro">Read ↓</a>
</header>
```

**D. Display** — large serif title on a dot grid with art at the side.

```html
<header class="ed-header--display ed-dot-grid">
  <div><h1>The slow parts of fast work</h1><p class="ed-subtitle">A one-line subtitle in grey sans.</p></div>
  <svg viewBox="0 0 400 300" aria-hidden="true">…</svg>
</header>
```

## Body column and widths

```html
<div class="ed-body ed-has-toc">       <!-- ed-has-toc keeps wide figures clear of the sidebar -->
  <aside class="ed-toc" aria-label="On this page"><nav class="ed-toc__inner"><ol>
    <li><a href="#summary">Summary</a></li> …
  </ol></nav></aside>
  <h2 id="summary">Summary</h2>
  <p>640px column…</p>
  <figure class="ed-media">880px</figure>
  <figure class="ed-wide">960px</figure>
  <section class="ed-full">edge to edge</section>
</div>
```

The TOC appears from 1200px; the template script marks the current section with `aria-current`.

## Prose

```html
<p><span class="ed-runin">What we measured.</span> Bold lead-in for method/result paragraphs.</p>
<p class="ed-lede">An italic note before the body, e.g. for a guest post.</p>
<blockquote><p>An excerpt from a source, with a 1px ink rule on the left.</p></blockquote>
<p class="ed-dropcap">First paragraph of a feature, opened with a drop cap.</p>
<p>Claim with a footnote.<sup class="ed-fn-ref" id="fnref-1"><a href="#fn-1" aria-label="Footnote 1">1</a></sup></p>
<p class="ed-note">Small sans note in muted grey.</p>
<p class="ed-ack">Acknowledgements in small italic grey.</p>
<hr>
```

Headings: `h2` (section), `h3` (subsection), `h4` (minor). Give every `h2` an `id` for the TOC.

**Pull quote** — pull a sentence from the article, or quote a real, attributable person.

```html
<figure class="ed-pullquote ed-wide">
  <blockquote><p>“Checking an answer should cost less than reading the source.”</p></blockquote>
  <figcaption>Name, role</figcaption>   <!-- omit when pulling from your own text -->
</figure>
```

**Statement** — a short centred serif line that turns the piece toward its close:
`<p class="ed-statement">Speeding up one step is not speeding up the whole.</p>`

**Finding heading** — grey kicker plus the claim, used in feature pieces:

```html
<h3 class="ed-finding"><span class="ed-finding__kicker">Finding 2: Bottlenecks</span>The rest of the time concentrates in experiments and review.</h3>
```

**Section title** (serif, centred, for feature chapters): `<h2 class="ed-section-title" id="explorer">What if the assumptions change?</h2>`

## Figures

**Image with caption**

```html
<figure class="ed-media ed-figure">
  <img src="figure.png" alt="What the figure shows, in one sentence">
  <figcaption><span class="ed-caption-label">Figure 1.</span> What to notice, and the condition it depends on.</figcaption>
</figure>
```

**Framed chart** (the signature figure)

```html
<figure class="ed-media">
  <div class="ed-frame"><div class="ed-frame__card">
    <p class="ed-chart__title">Title states the takeaway</p>
    <p class="ed-chart__sub">What is measured, unit, population</p>
    <div class="ed-chart__body"> <!-- bars, flow, SVG --> </div>
    <div class="ed-chart__foot"><span>Note: method or n</span><span>Source: …</span></div>
  </div></div>
  <figcaption><span class="ed-caption-label">Figure 2.</span> Caption outside the frame.</figcaption>
</figure>
```

Several stacked cards in one frame: repeat `.ed-frame__card`; put `<div class="ed-frame__arrow">↓</div>`
between them for a sequence. `.ed-frame--flush` removes card padding for full-bleed images. For a white
card without a frame (large charts, 960px), use `<div class="ed-wide ed-card-white">`.

**HTML bar chart** (labels stay legible on phones)

```html
<div class="ed-bars" style="--label: 160px">
  <div class="ed-bars__row" style="--v:41"><span class="ed-bars__label">Link to document</span>
    <span class="ed-bars__track"><span class="ed-bars__fill"></span><span class="ed-bars__value">41%</span></span></div>
  <div class="ed-bars__row is-key" style="--v:86"><span class="ed-bars__label">Link + quotation</span>
    <span class="ed-bars__track"><span class="ed-bars__fill"></span><span class="ed-bars__value">86%</span></span></div>
  <div class="ed-bars__axis" aria-hidden="true"><span></span><span class="ed-bars__ticks">
    <span style="left:0">0%</span><span style="left:50%">50%</span><span style="left:100%">100%</span></span></div>
</div>
```

`--v` is the bar length in percent of the axis. `is-key` colours the row with the accent; set `--c` on a
row for any other colour.

**Process diagram** (reflows to vertical under 900px)

```html
<ol class="ed-flow">
  <li style="--c: var(--ed-clay)">Question</li>
  <li style="--c: var(--ed-lavender)">Retrieve<small>top 20 passages</small></li>
  <li style="--c: var(--ed-olive)">Draft</li>
</ol>
<p class="ed-flow-note">↺ Unsupported claims return to “Draft”.</p>
```

**Legend**

```html
<ul class="ed-legend">
  <li><span class="ed-swatch" style="--c: var(--ed-lavender)"></span>Augmented</li>
  <li><span class="ed-swatch ed-swatch--line" style="--c: var(--ed-sky)"></span>Automated</li>
</ul>
```

**Chart label and caption in the Institute style** (no frame, on paper or grid paper):

```html
<p class="ed-chart-label">US GDP in 2030, by scenario (trillions of dollars)</p>
… chart …
<p class="ed-chart-caption">*Illustrative scenarios from the model described below.</p>
```

**Small multiples**

```html
<div class="ed-wide ed-panels">
  <div class="ed-panel"><p class="ed-panel__title">Modest scenario</p><svg class="ed-svg" viewBox="0 0 300 180">…</svg></div>
  …
</div>
```

**Sample marker** (remove before publishing): `<span class="ed-sample-badge">Sample data</span>` and the
`data-sample` attribute on the containing element.

## Tables and code

```html
<div class="ed-media ed-table"><table>
  <thead><tr><th scope="col">Format</th><th scope="col">Reader must</th><th scope="col" class="ed-num-cell">Verified</th></tr></thead>
  <tbody><tr><th scope="row">Passage link</th><td>Read one passage</td><td class="ed-num-cell">73%</td></tr></tbody>
</table></div>
```

```html
<pre><span class="ed-code-label">answer.json</span><code>{ <span class="tk-k">"claim"</span>: <span class="tk-s">"…"</span> }</code></pre>
```

Inline code: `<code>MODEL</code>`. Token classes for hand-marked code: `tk-k` key/keyword, `tk-s` string,
`tk-n` number, `tk-f` function, `tk-c` comment. For long listings, use a highlighter's output and keep
the frame.

## Footnotes and citation

```html
<section class="ed-footnotes" id="footnotes" aria-label="Footnotes">
  <p class="ed-footnotes__label">Footnotes</p>
  <ol><li id="fn-1">Footnote text. <a class="ed-backref" href="#fnref-1" aria-label="Back to text">↩</a></li></ol>
</section>
```

Citation block: an `h3` "Citation" followed by a `<pre><code>` BibTeX entry.

## Controls

```html
<a class="ed-btn" href="#">Secondary</a>
<a class="ed-btn ed-btn--primary" href="#">Primary</a>
<a class="ed-btn ed-btn--pill" href="#">Pill</a>

<div class="ed-segmented" role="group" aria-label="Scenario">
  <button type="button" class="ed-btn" aria-pressed="true">Modest</button>
  <button type="button" class="ed-btn" aria-pressed="false">Extreme</button>
</div>

<div class="ed-range"><label for="k"><span>Review speed-up</span> <output for="k">1.0×</output></label>
  <input id="k" type="range" min="1" max="3" step="0.1" value="1"></div>
<p class="ed-output" aria-live="polite">The result, stated in words.</p>
```

Icon arrows inside buttons: a 13px inline SVG, e.g.
`<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 11 11 5M6 5h5v5"/></svg>` (↗)
or `<path d="M8 3v10M4 9l4 4 4-4"/>` (↓).

## Scrollytelling

```html
<section class="ed-full ed-scrolly">
  <div class="ed-progress" aria-hidden="true"><div class="ed-progress__fill"></div></div>
  <div class="ed-scrolly__stage"><figure id="chart" data-state="final">…graphic…</figure></div>
  <div class="ed-scrolly__steps">
    <div class="ed-step" data-step="1"><div class="ed-step__card">
      <p class="ed-step__lead">Short sans lead</p><p>Serif body.</p><p class="ed-step__note">Source note.</p>
    </div></div>
    …
  </div>
</section>
```

Add `.is-live` from JavaScript to enable the sticky behaviour; without it the stage is a normal figure
and the cards stack below it. Wiring is described in `interaction.md` and implemented in `feature.html`.

**Timeline variant**: steps as `.ed-timeline__step` elements; add `.is-active` to the current one; year
labels use `.ed-timeline__year`.

## Backgrounds

`.ed-grid-paper` (pencil grid, 26px) and `.ed-dot-grid` (dots every 56px) for explainer stages and display
headers. Hand-drawn textures come from the SVG filters in `feature.html` (`#tex-crayon`, `#tex-pencil`);
see `figures.md`.
