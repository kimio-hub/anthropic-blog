# Interaction: scrollytelling and explorers

Interaction is worth building only when a reader's action reveals a rule they would not see in a static
figure. Before building, write the loop in one line:

> The reader changes **X** → the model applies **rule R** → **Y** changes → the reader learns **L**.

If you cannot fill in R and L, make a static comparison instead (small multiples or a two-state figure).
Controls that only show and hide content are navigation, not explanation.

## Patterns

| Pattern | Good for | Source-site example |
|---|---|---|
| Sticky scrollytelling | Building a mental model step by step on one graphic | A job drawn as a bundle of tasks that recolour as AI augments or automates them |
| Timeline scrolly | A history or a sequence of stages | Five eras of AI-assisted research, the active one in ink, the rest faded |
| Scenario pills | Comparing a few meaningful, named conditions | Modest / Substantial / Extreme scenario presets |
| Slider | A continuous parameter with a defined unit and range | A speed-up factor from 1× to 3× |
| Survey or prediction | Letting readers commit to a belief before seeing results | Only when the piece really compares beliefs; always offer "skip" |

## Sticky scrollytelling

Markup is in `components.md`; a complete, working example is `feature.html`.

1. One stage (`.ed-scrolly__stage`) holds one graphic. Keep the same object on screen through every step;
   change its state, not the object.
2. Each step card (`.ed-step__card`): a short sans lead, 1–3 sentences of serif body, an optional grey note
   with the source. One idea per step, 4–8 steps in total.
3. The graphic's state is data on the element (`data-state="3"`); CSS handles colours and visibility, JS
   handles geometry. Transitions of 0.5–0.8s with `var(--ed-ease)`; move things that change meaning and
   nothing else.
4. Wire steps with an `IntersectionObserver` (`rootMargin: '-45% 0px -45% 0px'`, so a step activates when
   it crosses the middle of the viewport). Add `.is-live` to the section only when JS runs and motion is
   allowed.
5. Default markup shows the final, most informative state. With JS off or `prefers-reduced-motion:
   reduce`, the stage renders as an ordinary figure followed by the cards in order: the reader gets the
   whole story without scrolling tricks.
6. Layout: on wide screens put cards in the left gutter (416px) and the graphic in the remaining space;
   below ~1100px put the graphic at the top of the stage and cards at the bottom. Cards may overlap the
   graphic's empty areas, never its labels.
7. Optional: a sticky reading-progress bar for the section (`.ed-progress`).

```js
const section = document.querySelector('.ed-scrolly');
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (section && !reduce && 'IntersectionObserver' in window) {
  section.classList.add('is-live');
  const chart = section.querySelector('figure');
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (e.isIntersecting) chart.dataset.state = e.target.dataset.step;   // CSS reacts to data-state
  }), { rootMargin: '-45% 0px -45% 0px' });
  section.querySelectorAll('.ed-step').forEach(s => io.observe(s));
}
```

## Explorers

1. Start in a sensible default that is already worth reading (usually the middle scenario).
2. Controls: `.ed-segmented` pill buttons with `aria-pressed` for named scenarios; `<input type="range">`
   with a visible `<output>` for continuous parameters. Label units on the control.
3. Show the result three ways: the chart, a sentence in an `aria-live="polite"` region
   (`.ed-output`), and, when it matters, a big number. The sentence carries the conclusion for screen
   readers and for skimmers.
4. Compute from a model that is written down: keep parameters in one object (`MODEL` in
   `feature.html`), explain the formula in a method note, and label the output "toy model" or cite the
   source model. Never tune a toy model to produce a headline number.
5. Offer a way back (the default button or a reset) and never gate the article behind the interaction.
6. Without JS, hide the controls (`.no-js` class pattern in `feature.html`) and show the default result.

## Motion and performance

- Animate `transform`, `opacity`, `left/width` of a few elements; avoid animating layout of the whole page.
- Honour `prefers-reduced-motion` (the CSS already shortens transitions; also skip scroll-driven state).
- SVG filters are costly on large areas: apply textures to small shapes, not to full-screen layers, and
  never inside an element that animates every frame.
- Test on a phone-sized viewport: sticky stages use `100svh`, so browser toolbars do not cover content.

## Accessibility checklist

- Every control is a real `<button>`, `<input>` or link, reachable by keyboard, with a visible focus ring
  (already styled) and an accessible name.
- State is announced (`aria-pressed`, `aria-live` output) and never shown only by colour or hover.
- Information never lives only in an animation frame, a tooltip or canvas pixels.
- Touch targets are at least 44px (buttons extend their hit area with `::after`).
- The page is usable with JS disabled and with reduced motion; check both in the render script's
  screenshots or by toggling them in the browser.
