# janmeet.pm — design rules

The theme is **terminal chrome + engineering datasheet**. It was chosen specifically to
avoid the default AI-startup aesthetic: a hard-edged grid of hairline rules, monospace
labels, one accent colour, and numbers presented as data rather than as marketing.

This file is the design contract for `index.html`. It documents what is actually in the
file, not an aspiration. If you change a rule here, change the CSS in the same commit.

## Hard rules

- **No border-radius.** Everything is hard-edged. No exceptions.
- **No blur.** No `filter: blur()`, no backdrop-filter.
- **One accent colour: amber** (`--amber`). Sage (`--ok`) is reserved *exclusively* for the
  `currently` status indicator. Red (`--alert`) is unused decoration in the window chrome.
- **Never hardcode a colour.** Every colour is a variable defined in **both**
  `html[data-theme="dark"]` and `html[data-theme="light"]`. A new colour that exists in only
  one block is a bug.
- **Headings and nav are lowercase.** `text-transform:lowercase` on display type, and copy is
  written lowercase in the markup where it is a heading or a label.
- **Every content entry carries an index**: `SYS-01`, `ART-03`, `01/ about`.
- **Structure is hairline rules** (`--hair`, 1px, `--line`) forming visible column grids.
- **One file.** No build step, no framework, no `package.json`. If a change seems to need a
  build step, say so and stop.

### Gradients, shadows and glow — changed 2026-08-18

Earlier drafts of this site banned gradients, shadows and glow outright. That rule was
**lifted by the owner** and now reads:

- Gradients and glow are permitted **only on interactive surfaces**, to signal affordance.
- They are never decoration on static content: no gradient panels, no drop shadows on
  cards, no glowing headings.
- Both effects are tokenised (`--sheen-*`, `--glow*`) in both theme blocks.
- Blur and border-radius are still banned, so a "soft card" look remains impossible.

**One further exception, also the owner's call (2026-08-18): the backdrop.** The page now
sits over a photograph, and three document-scale gradients are what make that readable —
see [Backdrop](#backdrop). They are the page's ground, not decoration applied to a
component, and they are the only gradients allowed to touch static content. A gradient on
a card, a heading or a panel is still wrong.

## Colour tokens

Same token names in both themes. Dark is the default (`<html data-theme="dark">`); the
choice persists in `localStorage` (`STORE = true`).

| token | role | dark | light |
|---|---|---|---|
| `--bg` | page background | `#111010` | `#EFEBE1` |
| `--bg-2` | recessed / hover fill | `#181615` | `#E7E2D6` |
| `--panel` | panel fill | `#1B1918` | `#F6F3EB` |
| `--ink` | primary text | `#EDE7DC` | `#181510` |
| `--mid` | body / secondary text | `#9A9287` | `#5A544A` |
| `--dim` | labels, captions | `#6A635A` | `#8A8377` |
| `--line` | hairline rules | `#2E2A27` | `#D2CCBD` |
| `--line-2` | stronger edges, borders | `#3D3833` | `#BFB8A6` |
| `--amber` | the one accent | `#F0A93B` | `#7E4A04` |
| `--amber-dim` | muted accent | `#8A6425` | `#C79B57` |
| `--alert` | chrome dot only | `#E4633C` | `#B33A17` |
| `--ok` | **`currently` status indicator only** | `#8FA76B` | `#5C7238` |
| `--inv-ink` | text on an amber fill | `#141210` | `#F6F3EB` |
| `--glow` | 1px glow ring | `rgba(240,169,59,.30)` | `rgba(154,93,6,.30)` |
| `--glow-strong` | glow bloom | `rgba(240,169,59,.55)` | `rgba(154,93,6,.52)` |
| `--sheen-1` / `--sheen-2` | resting gradient stops | `rgba(255,255,255,.045)` → transparent | `rgba(0,0,0,.035)` → transparent |
| `--sheen-h1` / `--sheen-h2` | hover gradient stops | `rgba(240,169,59,.16)` → `.02` | `rgba(154,93,6,.13)` → `.015` |

**Light `--amber` was `#9A5D06` until the backdrop landed.** It is now `#7E4A04`, two steps
deeper. The reading pane darkens as you scroll, and a mid-tone accent on a darkening
surface loses contrast: at `#9A5D06` the pane can vary ~0 levels before amber breaks
4.5:1 on small mono labels; at `#8A5205`, ~7 levels, which is invisible; at `#7E4A04`,
~18 levels with amber still at 4.5:1. `--dim` moved two steps in both themes for the same
reason. Restoring either without flattening `--pane-top`/`--pane-bot` first puts the site
under AA.

Light-theme glow carries a **higher alpha than dark** (.30/.52 vs .30/.55 is deliberate, and
light was raised from .22/.42). The same alpha over a pale background reads much weaker than
over near-black; matching the numbers makes light look broken.

### Backdrop tokens

| token | role | dark | light |
|---|---|---|---|
| `--img-a` | the photograph's opacity | `.40` | `.70` |
| `--pane-top` | reading pane at the masthead | `rgba(17,16,16,.68)` | `rgba(239,235,225,.90)` |
| `--pane-bot` | reading pane at the contact block | `rgba(17,16,16,.62)` | `rgba(239,235,225,.80)` |
| `--bar-a` | sticky top bar / statusline | `rgba(17,16,16,.90)` | `rgba(239,235,225,.92)` |
| `--bg-2-a` | translucent `--bg-2`, for fills over the backdrop | `rgba(24,22,21,.42)` | `rgba(231,226,214,.55)` |
| `--wash-top` / `--wash-bot` | the scroll wash's ends | `rgba(255,255,255,.04)` → `rgba(0,0,0,.60)` | `rgba(255,255,255,.12)` → `rgba(0,0,0,.30)` |
| `--grain` | grain layer opacity | `.055` | `.05` |
| `--stick` / `--chrome-h` | set by JS: top bar height, chrome height | measured | measured |

### Layout tokens

| token | value | role |
|---|---|---|
| `--col` | `860px` | max content measure |
| `--pad` | `clamp(16px,4vw,26px)` | horizontal page padding |
| `--hair` | `1px` | every rule on the page |

## Typography

Three families, each with a job. Do not use a family outside its job.

| token | family | job |
|---|---|---|
| `--disp` | Martian Mono (500/600/700) | display: `h1`, `.lead`, entry headings |
| `--mono` | IBM Plex Mono (400/500) | data, labels, indices, chrome, the meter |
| `--sans` | IBM Plex Sans (300/400/500) | prose only: body copy, list items, descriptions |

The distinction that matters: **anything that is a value, a label, a path, a filename, an
address or a measurement is `--mono`.** Anything that is a sentence is `--sans`. Display
type is `--disp` and is always lowercase with negative tracking.

### Scale

| use | size / line-height | tracking | family |
|---|---|---|---|
| `body` | 15.5px / 1.6, weight 300 | — | sans |
| `h1` | `clamp(19px,3.6vw,29px)` / 1.14 | `-.05em` | disp 700 |
| `.lead` | `clamp(14px,1.9vw,17px)` / 1.5 | `-.035em` | disp 500 |
| entry heading `.item h3` | 14.5px / 1.35 | `-.04em` | disp 600 |
| job heading `.job h3` | 13px | `-.035em` | disp 600 |
| prose `.sub`, `.kv dd`, `.job li` | 15px / 14.5px, 1.55–1.6 | — | sans |
| chat prose `.turn .msg` | 15px / 1.6 | — | sans |
| chat user turn | 12.5px | — | mono |
| section rule `.rule` | 10px uppercase | `.19em` | mono |
| datasheet label `.spec .k`, `.kit .k`, `.hob .k` | 10px uppercase | `.13–.15em` | mono |
| datasheet value `.spec .v` | 12px | — | mono |
| entry index `.item .idx` | 10px uppercase | `.13em` | mono |
| `.kv dt` | 9.5px uppercase | `.14em` | mono |
| inline metric `.kv dd b` | 13px, weight 500, amber | — | mono |
| nav tab | 11px (12px in drawer) | `.02em` | mono |
| chrome bar | 11px | — | mono |
| statusline | 10px uppercase | `.09em` | mono |
| meter row `.lrow` | 12px (10px ≤620px) | — | mono |
| contact label `.links .k` | 11px **lowercase** | `.04em` | mono |
| contact value `.links .v` | 13.5px (14.5px for the email) | `-.01em` | mono |

### Two typographic rules that get broken by accident

1. **Align baselines, not padding.** A 10px label and a 14px value given the same
   `padding-top` sit ~1.5px apart, which reads as a mistake rather than a decision. Where two
   different sizes share a row, use `align-items:baseline`. When you do, grid cells stop
   stretching — so draw the column rule on the row (absolutely positioned 1px line) instead
   of as `border-right` on the cell, or the rule collapses to a stub.
2. **Inset text from a filled edge.** Text may sit flush at the page margin when the row has
   no fill (see `.spec`), because there is no visible box for it to collide with. As soon as a
   row carries a `--sheen` gradient it reads as a box and needs a real inset (14px+) on every
   side. Flush text inside a filled box looks broken.

## Emphasis and CTAs

The site has **one** action worth emphasising: the email address. Everything else is
navigation or data.

- **At most one amber-filled block per view.** Two filled blocks read as two competing CTAs
  and the page starts to look like a landing page.
- **A status is not a CTA.** The statusline status is sage `--ok` text with a `●` marker —
  matching the `● building` treatment in the spec table — *not* a
  filled slab. It was a filled amber slab once; it read as a button and was wrong.
- **Emphasise with colour and weight, not with a fill.** The email is amber `--amber` text at
  weight 500 and one step up in size. That is enough.
- **Contact details are data, not buttons.** They use the standard label/value row, and the
  value shows the real destination (`/in/janmeet-s-makkar`, `resume.pdf`), not a button label.
- A filled amber background is legitimate for the **selected state of a real control** — the
  `text` / `voice` segment in the meter — where it means "this one is active".

## Structure: the entry row

Every content entry is a two-column grid: a fixed-width mono label column, a vertical
hairline, content on the right.

```
grid-template-columns: 132px 1fr;   /* 106px for the narrower contact rows */
```

Used by `.spec .r`, `.item`, `.job`, `.kit .r`, `.hob`, `.links a`. Rows are separated by a
single `--line` hairline. Below 620px the grid collapses to one column and the label becomes
a caption above its content — **with no rule between label and value**, so an entry reads as
one block and the page doesn't become a dense ladder of lines.

Short content should not span the full measure: the contact block is capped at `34em` so
three short facts don't render as three wide, mostly-empty boxes.

## Backdrop

Three layers under the chrome, the way a translucent terminal sits over a desktop picture:

| layer | position | role |
|---|---|---|
| `.bg` | `fixed`, viewport | the photograph, `bg-grey.jpg`, at `--img-a` |
| `.wash` | `absolute`, document height | black-to-clear: light at the masthead, dark at the contact block |
| `.frame::before` | `absolute`, document height | the reading pane, `--pane-top` → `--pane-bot` |

`.bg` is **fixed**, so the page scrolls past it. That parallax is what makes translucency
read as depth rather than as a flat tint — and it means the photograph's own composition is
a *viewport* effect: its horizon sits at the same screen height at every scroll position.
The scroll-driven darkening is `.wash`'s job, not the picture's.

**The pane ramp runs the same direction as the wash** — the pane gets *clearer* toward the
bottom, so the darkening reads through the centre column and not only in the margins either
side of the 860px frame. The reading surface shifts 15–18 levels between the masthead and
the contact block; the margins shift 60–99. Reverse the ramp and the centre column goes
static; flatten it and the accent can go back to `#9A5D06`. Those are the same decision.

**The image is constrained, not decorative.** `bg-grey.jpg` is greyscale — one accent colour
on this site, and a colour cast would be a second — and flattened into a **62–206 grey band**
(53–219 after JPEG). The pane composites over whatever the picture does, so a real black or a
real white behind it takes text contrast with it. Worst case over the band, measured:

| | ink | body | micro-labels | accent |
|---|---|---|---|---|
| light | 11.2:1 | 4.6:1 | 3.4:1 | 4.5:1 |
| dark | 11.3:1 | 4.5:1 | 3.4:1 | 6.9:1 |

Replace the image only through `tools/prepare-backdrop.py`, which enforces greyscale, the
band, the resize and EXIF stripping — then re-measure. Dropping a camera-original JPEG in
place will look fine at the masthead and fail at the bottom of the page.

## Structure: one page, seven sections

The six section panels and the contact block are **all in the document at once**, stacked, in
`?tab=` order. There are no tabs any more:

- The nav lives in `.topbar` **with the chrome**, one sticky unit, one `top:0`. They used to
  stick separately, which meant guessing the chrome's height for the nav's `top` — the guess
  (37px) was 8px short of what Plex Mono actually renders (45px) and the nav slid underneath.
  Do not re-split them.
- Nav items scroll to their section. A `rAF`-throttled scroll listener owns the active item,
  the chrome path and the statusline counter, so those are right whether you clicked or
  scrolled.
- `?tab=systems` still deep-links; it resolves to a scroll position, and `replaceState` keeps
  the URL in step as you scroll. Existing links keep working.
- `--stick` (top bar height) and `--chrome-h` are **measured by JS** on load, on
  `document.fonts.ready` and on resize, then used for `scroll-margin-top` and the scrollspy
  line. Hardcoding them back means section rules land behind the bar.
- Contact is the seventh nav item and a `.panel` like the rest (`#p-contact`).

`/legacy/index.html` is a verbatim snapshot of the previous solid-background, tabbed design
(commit `2118f94`), `noindex`, kept so the old design can be reverted to at any time. It is a
frozen artefact — do not maintain it, do not port fixes into it.

## Interactive surfaces

Applies to `.links a`, `a.item`, `.sugg button`, `nav.cmds button`, `.seg button`.

| state | treatment |
|---|---|
| rest | `linear-gradient(180deg, var(--sheen-1), var(--sheen-2))`, no shadow |
| hover / `:focus-visible` | amber sheen (`--sheen-h1/h2`) + `0 0 0 1px var(--glow), 0 0 16px var(--glow-strong)` |
| active tab / segment | `0 0 14px var(--glow)` — persistent, so the current section is findable without hovering |

Chrome buttons (`.themebtn`, `.hamb`) carry a resting `0 0 8px var(--glow)` and tighten to a
1px ring plus a 12px bloom on hover/focus.

Transitions are `box-shadow .15s, background-image .15s` and are killed wholesale by the
`prefers-reduced-motion` block.

Note that hover effects are pointer-only: on a phone, interactive rows show the resting
sheen and the active-tab glow, nothing more. Do not make an affordance *depend* on hover.

## Responsive

| breakpoint | change |
|---|---|
| ≤900px | frame loses its left/right border |
| ≤620px | entry grids collapse to one column; nav becomes a hamburger drawer; contact rows go full width; the redundant statusline cell is hidden |
| ≤340px | (nothing — the former two-column nav grid was replaced by the drawer) |

**The hamburger drawer** reuses `nav.cmds` itself — it is not a second nav. On mobile that
element becomes `position:fixed` under the chrome, one full-width row per section. There is
no duplicate list to fall out of sync with `show()`. It closes on selection, on `Escape`
(returning focus to the button), on outside tap, and on the button.

**The ASCII meter** row is `LBL + W + 2 + MSW` monospace cells. `W` is not a constant:
`fitW()` measures real character width with a hidden probe and clamps the bar to 12–34 cells
so the `ms` column never falls off a narrow screen. Never hardcode `W` back to 34 — at 375px
that pushes the numbers behind a horizontal scrollbar, which silently hides the only data on
the panel.

## Accessibility invariants

Do not break these:

- The `prefers-reduced-motion: reduce` block must keep killing all animation and transition.
- `:focus-visible{outline:1px solid var(--amber);outline-offset:2px}` stays. Glow is **added
  alongside** focus outlines, never as a replacement — colour bloom alone is not a focus
  indicator.
- The meter's `aria-live="polite"` region stays.
- The drawer keeps `aria-expanded` / `aria-controls` and moves focus into itself on open.
- Text colours must clear 4.5:1 against their background in both themes.

## Copy conventions

- **Verb precision.** "Built" is reserved for work done hands-on. "Led", "Designed", "Owned",
  "Shipped" are distinct and deliberate. Do not upgrade a verb.
- **Never invent a metric, race time, grade or date.** Placeholder over plausible guess.
- The meter's numbers are **illustrative, not benchmarks**, and the caption says so. Do not
  relabel them as measured results.
- No internal Eternal Ltd. figures. Directional phrasing instead.
