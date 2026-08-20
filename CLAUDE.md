# janmeet.pm — personal portfolio site

Single-file static site. Personal project, not work-related. Do not add a build step,
a framework, or a package.json. `index.html` is the entire site by design.

## Owner

Janmeet Singh Makkar — Founding PM, AI at Nugget (nugget.com), an enterprise AI agent
platform inside Eternal Ltd. (Zomato / Blinkit). The site exists to support applications
to remote AI product roles worldwide. Target audience: hiring managers and founders at
AI-native companies.

Contact on site: hello@janmeet.pm (Cloudflare Email Routing → personal Gmail).

## Stack

- One file: `index.html`. Vanilla HTML/CSS/JS, no dependencies, no bundler.
- Fonts from Google Fonts CDN: Martian Mono (display), IBM Plex Mono (data/labels),
  IBM Plex Sans (prose).
- Hosting: Cloudflare Pages, connected to this GitHub repo. No build command,
  output directory `/`. Every push to `main` redeploys.
- Domain: janmeet.pm, DNS on Cloudflare. `www` 301-redirects to apex.

## Design system — do not drift from this

The theme is deliberate: **terminal chrome + engineering datasheet**. It was chosen
specifically to avoid the default AI-startup aesthetic.

**`DESIGN.md` is the full contract** — colour tokens, type scale, component states,
emphasis/CTA policy. Read it before any visual change. The rules below are the summary.

- **No border-radius.** Everything is hard-edged.
- **No blur.**
- Gradients and glow are permitted **only on interactive surfaces** (2026-08-18, owner
  decision — they were banned outright before that). Never as decoration on static
  content. Tokenised as `--sheen-*` and `--glow*` in both theme blocks. See `DESIGN.md`.
- **The backdrop is the one exception** (also 2026-08-18, owner decision): the page sits
  over a greyscale photograph, and three document-scale gradients make it readable —
  `.bg`, `.wash`, `.frame::before`. The image is clamped to a 62–206 grey band because
  text contrast depends on it; replace it only via `tools/prepare-backdrop.py` and
  re-measure. `DESIGN.md` → Backdrop has the numbers.
- One accent colour only: amber (`--amber`). Sage green (`--ok`) is reserved
  exclusively for the `currently` status indicator. Red (`--alert`) is unused
  decoration in the window chrome.
- Structure is hairline rules (`--hair`, 1px) forming visible column grids. Every
  content entry sits in a two-column layout: a fixed-width mono label column on the
  left, separated by a vertical rule, content on the right.
- Headings and nav are lowercase.
- Every entry carries an index: `SYS-01`, `ART-03`.
- Both light and dark themes are fully tokenised under `html[data-theme="..."]`.
  Any new colour must be added as a variable in **both** blocks. Never hardcode a hex
  value in a rule.

Accessibility invariants: keep the `prefers-reduced-motion` block working, keep focus
outlines, keep the ASCII meter's `aria-live` region.

## Structure

**One page.** All seven sections are in the document at once and the nav scrolls to them;
`?tab=systems` still deep-links, resolving to a scroll position, and the URL keeps itself in
step as you scroll. The nav sits in `.topbar` together with the terminal chrome as a single
sticky unit — do not re-split them, and do not hardcode the bar's height (JS measures it into
`--stick` / `--chrome-h`).

**Below 620px the sections fold** (2026-08-18): the page opens as a listing of section rules
with one open, ~2.7 screens instead of ~12. The section rule *is* the toggle — JS swaps each
panel's first `.rule` for a `<button class="rule rule-t">` on every viewport and moves the rest
of the panel into `.pbody`, so there is one DOM; above 620px the button is disabled and renders
identically to the div it replaced. Desktop is untouched by design. The phone also gets a
2px amber scroll-progress line on the top bar. `DESIGN.md` → Responsive has the full contract,
including why load-time folds must not animate and why the two gestures (nav jump = exclusive,
rule tap = additive) differ.

| section | id | content |
|---|---|---|
| 01 about | `p-about` | chat-framed intro + ASCII turn-budget meter |
| 02 systems | `p-systems` | six problem/decision/result entries (SYS-01..06) |
| 03 artifacts | `p-artifacts` | four public artifacts (ART-01..04) — all still placeholders |
| 04 experience | `p-experience` | Nugget, Zomato, Blinkit, internship, IIT Ropar |
| 05 stack | `p-stack` | six capability rows |
| 06 offline | `p-offline` | running, hyrox, hiking, bouldering, music |
| 07 contact | `p-contact` | email, LinkedIn, résumé as label/value rows |

`/legacy/index.html` is a frozen, `noindex` snapshot of the previous solid-background tabbed
design (commit `2118f94`), kept as a one-file revert path: copy it over `index.html` and drop
`bg-grey.jpg`. Do not maintain it or port fixes into it.

### The ASCII meter

The one animated element on the page. Renders a monospace block-character bar chart of
a single agent turn's latency budget, typing in cell by cell. Toggles between `text`
and `voice` modality. Data lives in the `DATA` object in the script; `W` is the bar
width in characters.

The numbers are **illustrative, not benchmarks**, and the caption says so. Do not
relabel them as measured results.

## Outstanding work

### Resolved 2026-08-18 (first commit)

- Confidentiality: the SYS-03 76% figure is now directional phrasing; both `data-review`
  comments deleted. No internal Eternal Ltd. figure remains in the file or its history.
- SYS-04 (fine-tuning / distillation) archived to `.archive/sys-04-fine-tuning.html`,
  which is gitignored so it never enters public history. The fine-tune work started
  recently; restore the entry (and renumber) once it is defensible end to end. The
  matching clause was also removed from the stack tab's `models · inference` row —
  put both back together, not one without the other.
- Offline tab: the three empty stat lines were deleted; `FILL:` comments are gone.
  Half-marathon and hyrox PBs are real and remain.
- `STORE` is now `true`, so the light/dark choice persists.

### 1. Placeholder content — the highest-value remaining change

All four ART entries read `● in progress` with `href="#"`. Filling at least one is the
most valuable change possible to this site. Until then it argues for the owner's
thinking but every claim terminates at "trust me".

### 2. Assets — done 2026-08-18

`favicon.ico` (the masthead's amber block cursor on the dark surface, six pixel-exact
sizes, 16–256) and `og.png` (1200×630) are both in the repo now, with `og:image:width`,
`:height` and `:alt` declared so unfurls do not have to guess.

Both are generated, and both regenerate from the repo — `python3 tools/make-favicon.py`
and `sh tools/make-og.sh`. The OG card is rendered by **headless Chrome** from
`tools/og-template.html` rather than drawn with PIL, so it uses the site's real Martian
Mono and IBM Plex faces instead of a system mono standing in for them; the template
duplicates the dark theme tokens, so update it when those change. Neither script runs on
deploy — the outputs are committed.

## Deployment

Cloudflare Pages, connected to the GitHub repo `janmeetpm/janmeet.pm`. No build command,
output directory `/`. Every push to `main` redeploys. `_headers` sets baseline security
headers — it is Cloudflare Pages config, not a build step.

Files served besides `index.html`: `bg-grey.jpg` (the backdrop), `og.png`,
`favicon.ico`, `resume.pdf`, `legacy/index.html`. `tools/` and `experiments/` are not part of the deploy — `experiments/`
is gitignored entirely.

## Git identity

This repo uses a personal GitHub account (`janmeetpm`), separate from the work account.
It has a repo-local identity override and an SSH host alias — the remote is
`git@github-personal:...`, not `git@github.com:...`.

Before any commit, verify the author is not a work address:

```
git log -1 --format='%an <%ae>'
```

## Conventions

- Verb precision in all copy: "Built" is reserved for work done hands-on; "Led",
  "Designed", "Owned", "Shipped" are distinct and deliberate. Do not upgrade a verb.
- **Reading level is layered** (owner call, 2026-08-20). Everything above `02 systems` — the
  h1, the `.spec` rows, the about turns, the meter, and the `<title>`/`meta`/`og` strings — is
  written for a reader with no deep AI background: a recruiter or a non-AI founder. No
  *adherence*, *orchestration*, *eval coverage*, *inference economics* or *latency* on page
  one; the four numbers appear there as four plain questions. From `02 systems` down, the
  technical vocabulary is correct and expected. Page one sells, the rest proves — do not
  "restore" the jargon upward, and do not strip the terminology below.
- Never invent a metric, race time, grade, or date. Placeholder over plausible guess.
- **Availability is framed as curiosity, not as a job hunt** (owner call, 2026-08-18).
  No "open to work", "available for hire", or "seeking opportunities" anywhere. Keep the door
  open, keep the tone level.
  **Refined 2026-08-19:** the point of the site is still to produce an email, so the contact
  section must carry a *promise* — what the reader gets for writing — not a list of what the
  owner enjoys receiving. Full-time ownership is named there as a possible outcome, but
  conditional and reader-initiated ("if what you're building needs…"). Do not revert that to
  the older "one of three things worth an email" phrasing as though it were drift, and do not
  push it the other way into an ask.
- Keep it one file. If a change seems to need a build step, say so and stop.
- **Log every change in `CHANGELOG.md`.** Reverse-chronological, `YYYY-MM-DD HH:MM IST`.
  Record the *reason*, not just what moved — the commit log already has the diff. Add the
  entry under **Unreleased** while the work is in the working tree; move it under a dated
  heading when it lands on `main`. It is a repo doc, not a deploy asset.
