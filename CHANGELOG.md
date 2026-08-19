# Changelog

Reverse-chronological. Every entry is dated `YYYY-MM-DD HH:MM IST` and summarises a change
to the site or its tooling, in enough detail that the *reason* survives — the commit log
records what moved, this records why it moved.

Not part of the deploy. Update it in the same change that touches `index.html`, `DESIGN.md`
or `tools/`; add the entry under **Unreleased** while the work sits in the working tree and
move it under a dated heading when it lands on `main`.

## Unreleased

### 2026-08-19 18:52 — copy pass on all seven sections (Ogilvy review)

Reviewed every user-facing string against positioning → promise → headline priority. The
voice was already specific and factual, so the edits are surgical, not a rewrite.

Two were factual corrections, not style:

- **offline** — the closing note claimed "the race-prep coach in artifacts exists". No such
  artifact exists (ART-01..04 are teardown, build, trace triage, writing). Claim deleted
  rather than replaced with an invented one; the section now ends on the `.hobs` grid.
- **statusline** — `#st-tab` shipped hardcoded as `01/06 about` while the JS counts sevenths.
  Now `01/07 about`.

Headline work — the `<title>` and both descriptions were category labels and keyword lists
carrying no promise:

- `<title>` → `janmeet singh makkar — ai pm, enterprise agents that survive production`,
  matching the h1's actual promise instead of restating the category.
- `meta description` → leads with the promise, then the four numbers.
- `og:description` → states the idea the four numbers belong to, rather than listing them cold.

- **artifacts** — the lead promised "things you can open and judge for yourself" directly
  above four entries reading `● in progress` with `href="#"`. Reframed to future tense, states
  plainly that nothing is finished, and offers the substitute proof (email → a real failing
  trace). This is the one place the page was asking for trust it had not earned; it stays
  reframed until an ART entry actually ships.
- **stack** — sub opened on a negative ("Not a keyword list —"). Now affirmative and it invites
  the question: "Six areas where I'd expect an engineer to push, and expect to hold."
- **systems** — SYS-05's result read as a destination ("Went into the platform roadmap").
  Now "Shipped as a per-class roadmap decision", naming the actual trade (speech-to-speech vs.
  keeping the cascade) so the result carries a fact.
- **about** — "model selection and evaluation of open-weight models" said evaluation twice.

Deliberately not written, because both would put a commitment in the owner's mouth: a
reply-time promise in contact, and a replacement closer for offline.

### 2026-08-19 — interaction polish (uncommitted at session start, author not this session)

Present in the working tree before the copy pass; recorded here for completeness, exact time
unknown.

- Every `:hover` rule on an interactive surface moved behind `@media (hover:hover) and
  (pointer:fine)`. Touch fires `:hover` on press and leaves it on the last-tapped element,
  which read as a second active state fighting `.on`.
- Shared press feedback: one `--press:scale(.985)` transform on nav, fold rules, contact rows,
  suggestion chips, the theme button and the hamburger, so every tap confirms the same way.
- Two easing tokens (`--ease-out`, `--ease-drawer`) replace inline cubic-beziers.
- Phone nav drawer wipes down via `clip-path` instead of appearing on a `display` toggle —
  a translate would show through the 90%-opaque chrome it sits above.
- Section folds close faster than they open (.22s vs .3s), on the reasoning that opening is
  the reader waiting on content and closing is the page answering.
- ASCII meter: the type-in reveal is now one-shot and gated on an `IntersectionObserver`, so a
  `?tab=contact` deep link no longer types it out offscreen; every other path into `render()`
  (modality switch, width re-fit, re-opening the about fold) paints the finished state.
  `prefers-reduced-motion` is now watched for mid-session changes instead of read once.

## 2026-08-18

- **20:28** — documented the phone folds in `DESIGN.md`; watch the breakpoint on `matchMedia`
  too, so a resize past 620px re-resolves the fold state. (`0c8f80a`)
- **20:12** — sections fold below 620px: the page opens as a listing of section rules with one
  open, ~2.7 screens instead of ~12. Section rule *is* the toggle, one DOM on every viewport.
  Added the 2px amber scroll-progress line on the top bar. (`a5154a9`)
- **20:04** — added `favicon.ico` (six pixel-exact sizes, 16–256) and `og.png` (1200×630),
  both generated from the repo and committed rather than built on deploy. The OG card renders
  through headless Chrome from `tools/og-template.html` so it uses the real Martian Mono and
  Plex faces. (`4930863`)
- **19:56** — reframed availability as curiosity, not a job hunt. No "open to work" anywhere;
  a role is one of three things worth an email, not the ask. (`f2d96cc`)
- **19:54** — default to the dark theme. (`a7333c8`)
- **19:44** — photographic greyscale backdrop, single-page scroll replacing the tabbed layout,
  contact moved into the nav. `?tab=` deep links kept, resolving to scroll positions.
  Gradients and glow permitted on interactive surfaces only; the backdrop's three
  document-scale gradients are the one decorative exception. (`dc6ba07`)
- **19:15** — gitignore the local `experiments/` scratch dir. (`b636f5c`)
- **19:10** — added `DESIGN.md` as the design contract (colour tokens, type scale, component
  states, emphasis/CTA policy) and pointed `CLAUDE.md` at it. This commit is also the frozen
  snapshot behind `legacy/index.html`. (`2118f94`)
- **15:55** — phone-only hamburger drawer for section nav. (`cffb255`)
- **15:23** — fixed cramped mobile layout; the ASCII meter now fits its bar width to narrow
  screens instead of pushing the ms column off-screen. (`1ef2e7b`)
- **14:48** — default to light theme; glow on the theme toggle. (`6c400d6`)
- **14:32** — removed the remaining fine-tuning claims from the intro, meta and spec row.
  The SYS-04 fine-tuning/distillation entry went to the gitignored `.archive/`; the matching
  clause left the stack tab's `models · inference` row. Restore both together, or neither.
  Also: the SYS-03 figure became directional phrasing and both `data-review` comments were
  deleted, so no internal Eternal Ltd. figure remains in the file or its history. (`4a9db8a`)
- **12:35** — initial commit: single-file portfolio site, seven sections, terminal-chrome +
  engineering-datasheet theme, ASCII turn-budget meter. (`21d8dec`)
