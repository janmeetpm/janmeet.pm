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
- One accent colour only: amber (`--amber`). Sage green (`--ok`) is reserved
  exclusively for the "open to work" status indicator. Red (`--alert`) is unused
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

Six tabs plus a contact block, switched client-side with URL state (`?tab=systems`),
so any tab can be deep-linked:

| tab | id | content |
|---|---|---|
| 01 about | `p-about` | chat-framed intro + ASCII turn-budget meter |
| 02 systems | `p-systems` | six problem/decision/result entries (SYS-01..06) |
| 03 artifacts | `p-artifacts` | four public artifacts (ART-01..04) — all still placeholders |
| 04 experience | `p-experience` | Nugget, Zomato, Blinkit, internship, IIT Ropar |
| 05 stack | `p-stack` | six capability rows |
| 06 offline | `p-offline` | running, hyrox, hiking, bouldering, music |

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

### 2. Assets not yet in the repo

- `resume.pdf` — footer links to it, currently a 404
- `favicon.ico`
- `og.png` — 1200×630, referenced by the `og:image` tag. Without it, every LinkedIn
  and Slack share renders as a blank grey box.

## Deployment

Cloudflare Pages, connected to the GitHub repo `janmeetpm/janmeet.pm`. No build command,
output directory `/`. Every push to `main` redeploys. `_headers` sets baseline security
headers — it is Cloudflare Pages config, not a build step.

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
- Never invent a metric, race time, grade, or date. Placeholder over plausible guess.
- Keep it one file. If a change seems to need a build step, say so and stop.
