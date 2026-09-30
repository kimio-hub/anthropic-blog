#!/usr/bin/env python3
"""Render-check an editorial page at desktop and phone widths.

Takes screenshots you should actually look at, then reports problems that screenshots hide:
horizontal overflow, console and network errors, fonts that fell back, leftover template samples and
placeholders, images without alt text, heading order, and whether the page survives reduced motion.

Usage
    python scripts/check_page.py page.html
    python scripts/check_page.py https://example.com/post --widths 1440,768,390 --out shots/
    python scripts/check_page.py page.html --channel msedge      # use an installed Edge/Chrome

Requires Playwright for Python:
    pip install playwright && python -m playwright install chromium
(or skip the browser download and pass --channel chrome / --channel msedge).

Exit code: 1 if there are errors (overflow, script errors, page failed to load); 0 otherwise.
Warnings (samples left, fonts not loaded, missing alt, ...) do not fail unless --strict is given.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PLACEHOLDERS = ["Your Name", "Your Site", "Field Notes", "replace with", "Replace this", "example.com",
                "你的名字", "田野笔记", "换成你的"]

PROBE_JS = r"""
(placeholders) => {
  const vw = document.documentElement.clientWidth;
  const scrollW = document.documentElement.scrollWidth;
  const clipped = el => { for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
      const o = getComputedStyle(p); if (/(auto|scroll|hidden|clip)/.test(o.overflowX)) return true; } return false; };
  const overflow = [];
  if (scrollW > vw + 1) {
    for (const el of document.querySelectorAll('body *')) {
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.right <= vw + 1 || clipped(el)) continue;
      const cls = (el.getAttribute('class') || '').split(' ')[0];
      overflow.push(`${el.tagName.toLowerCase()}${cls ? '.' + cls : ''} right=${Math.round(r.right)}px`);
      if (overflow.length >= 8) break;
    }
  }
  const samples = [...document.querySelectorAll('[data-sample], .ed-sample-badge')].length;
  const text = document.body.innerText;
  const foundPlaceholders = placeholders.filter(p => text.includes(p));
  const noAlt = [...document.images].filter(i => !i.hasAttribute('alt')).map(i => i.currentSrc || i.src).slice(0, 5);
  const unnamedSvg = [...document.querySelectorAll('svg[role="img"]')]
    .filter(s => !s.getAttribute('aria-label') && !s.getAttribute('aria-labelledby') && !s.querySelector('title')).length;
  const heads = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => +h.tagName[1]);
  const skips = []; for (let i = 1; i < heads.length; i++) if (heads[i] > heads[i - 1] + 1) skips.push(`h${heads[i - 1]}→h${heads[i]}`);
  const wanted = new Set(['Source Serif 4', 'Schibsted Grotesk', 'JetBrains Mono', 'Noto Serif SC']);
  const fonts = {};
  for (const f of document.fonts) {
    const fam = f.family.replace(/["']/g, '');
    if (!wanted.has(fam)) continue;
    fonts[fam] = fonts[fam] === 'loaded' ? 'loaded' : f.status;
  }
  const body = document.querySelector('.ed-body p') || document.querySelector('p');
  const bodyStyle = body ? getComputedStyle(body) : null;
  return {
    title: document.title, lang: document.documentElement.lang, vw, scrollW, height: document.documentElement.scrollHeight,
    overflow, samples, placeholders: foundPlaceholders, noAlt, unnamedSvg,
    h1: heads.filter(h => h === 1).length, headingSkips: [...new Set(skips)],
    fonts, bodyFont: bodyStyle ? `${bodyStyle.fontFamily.split(',')[0]} ${bodyStyle.fontSize}/${bodyStyle.lineHeight}` : null,
    scrollyLive: !!document.querySelector('.ed-scrolly.is-live'),
  };
}
"""


def launch(p, channel: str | None):
    tried = []
    for ch in ([channel] if channel else [None, "chrome", "msedge"]):
        try:
            return p.chromium.launch(channel=ch) if ch else p.chromium.launch()
        except Exception as exc:  # browser not installed for this channel
            tried.append(f"{ch or 'bundled chromium'}: {str(exc).splitlines()[0]}")
    sys.exit("Could not start a browser.\n  " + "\n  ".join(tried) +
             "\nInstall one with: python -m playwright install chromium  (or pass --channel chrome/msedge)")


def main() -> int:
    for stream in (sys.stdout, sys.stderr):   # Chinese placeholders must print on Windows consoles too
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page", help="HTML file or URL")
    ap.add_argument("--widths", default="1440,390", help="comma-separated viewport widths (default 1440,390)")
    ap.add_argument("--out", default=None, help="screenshot folder (default: <page>-check/ next to a file, ./page-check/ for URLs)")
    ap.add_argument("--shots", type=int, default=6, help="viewport screenshots per width, spread over the page (default 6)")
    ap.add_argument("--channel", default=None, help="use an installed browser: chrome or msedge")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--json", action="store_true", help="print the full report as JSON")
    args = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("Playwright for Python is not installed: pip install playwright")

    target = args.page
    if not target.startswith(("http://", "https://", "file://")):
        path = Path(target).resolve()
        if not path.exists():
            sys.exit(f"Not found: {path}")
        url = path.as_uri()
        out = Path(args.out) if args.out else path.with_name(path.stem + "-check")
    else:
        url = target
        out = Path(args.out) if args.out else Path("page-check")
    out.mkdir(parents=True, exist_ok=True)

    widths = [int(w) for w in args.widths.split(",") if w.strip()]
    report = {"url": url, "screenshots": str(out), "runs": []}
    errors, warnings = [], []

    with sync_playwright() as p:
        browser = launch(p, args.channel)
        for motion in ("no-preference", "reduce"):
            for w in (widths if motion == "no-preference" else [min(widths)]):
                h = 900 if w >= 1000 else (1024 if w >= 600 else 844)
                ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=2 if w < 600 else 1,
                                          reduced_motion=motion)
                page = ctx.new_page()
                console, failed = [], []
                page.on("console", lambda m: console.append(m.text) if m.type == "error" else None)
                page.on("pageerror", lambda e: console.append(str(e)))
                page.on("requestfailed", lambda r: failed.append(f"{r.url[:90]} ({r.failure})"))
                try:
                    page.goto(url, wait_until="networkidle", timeout=45000)
                except Exception as exc:
                    errors.append(f"[{w}px] page did not load: {exc}")
                    ctx.close()
                    continue
                page.evaluate("document.fonts.ready")
                page.wait_for_timeout(500)
                tag = f"{w}" + ("-reduced-motion" if motion == "reduce" else "")
                height = page.evaluate("document.documentElement.scrollHeight")
                n = 1 if motion == "reduce" else max(1, args.shots)
                shots = []
                for i in range(n):
                    y = 0 if n == 1 else int((height - h) * i / (n - 1))
                    page.evaluate(f"window.scrollTo(0, {max(0, y)})")
                    page.wait_for_timeout(700)
                    f = out / f"{tag}-{i + 1:02d}.png"
                    page.screenshot(path=str(f))
                    shots.append(f.name)
                page.evaluate("window.scrollTo(0, 0)")
                info = page.evaluate(PROBE_JS, PLACEHOLDERS)
                info.update(width=w, reducedMotion=motion == "reduce", consoleErrors=console, failedRequests=failed, shots=shots)
                report["runs"].append(info)
                ctx.close()

                label = f"[{tag}]"
                if info["scrollW"] > info["vw"] + 1:
                    errors.append(f"{label} horizontal overflow: page is {info['scrollW']}px wide in a {info['vw']}px viewport; "
                                  f"widest: {', '.join(info['overflow']) or 'see screenshots'}")
                for c in console:
                    errors.append(f"{label} console error: {c[:200]}")
                for r in failed:
                    warnings.append(f"{label} request failed: {r}")
                if motion == "reduce" and info["scrollyLive"]:
                    warnings.append(f"{label} scrollytelling stays live under reduced motion")
        browser.close()

    first = report["runs"][0] if report["runs"] else {}
    if first:
        if first["samples"]:
            warnings.append(f"{first['samples']} element(s) still marked data-sample / Sample data: replace or delete them")
        if first["placeholders"]:
            warnings.append("template placeholders still present: " + ", ".join(first["placeholders"]))
        if first["noAlt"]:
            warnings.append("images without alt: " + ", ".join(first["noAlt"]))
        if first["unnamedSvg"]:
            warnings.append(f"{first['unnamedSvg']} svg[role=img] without a title or aria-label")
        if first["h1"] != 1:
            warnings.append(f"page has {first['h1']} h1 elements (expected 1)")
        if first["headingSkips"]:
            warnings.append("heading levels skip: " + ", ".join(first["headingSkips"]))
        missing = [f for f, s in first["fonts"].items() if s != "loaded"]
        if missing:
            warnings.append("web fonts not loaded (fallbacks in use): " + ", ".join(missing))
        if not first.get("lang"):
            warnings.append("<html> has no lang attribute (CJK typography depends on it)")

    if args.json:
        print(json.dumps({"errors": errors, "warnings": warnings, **report}, ensure_ascii=False, indent=2))
    else:
        print(f"Checked {url}")
        for r in report["runs"]:
            mode = " reduced-motion" if r["reducedMotion"] else ""
            print(f"  {r['width']}px{mode}: {r['height']}px tall, body {r['bodyFont']}, screenshots {', '.join(r['shots'])}")
        print(f"Screenshots: {out.resolve()}")
        for e in errors:
            print("ERROR  ", e)
        for wmsg in warnings:
            print("WARN   ", wmsg)
        if not errors and not warnings:
            print("OK: no problems found. Still look at the screenshots.")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
