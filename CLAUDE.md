# Corcoran Communications — standing orders

## Brand (decided 2026-08-10 — "Strategic Growth" palette; do not drift)
- Midnight #082A4A — dark panels (header, hero, bands, footer) and
  heading text on light backgrounds.
- Signal Blue #0B6BD3 — section titles, links, and hover states, on light
  backgrounds only. On Midnight panels it drops to 2.82:1 and becomes
  unreadable, so links there use Fresh Mint (footer) or white (contact
  band). Never put Signal Blue text on a dark panel.
- Growth Green #15B77E — buttons/CTAs and success markers ONLY, always
  with dark text (#062018) on green fills. Use #0E7A55 for small green
  text on light backgrounds (contrast).
- Buttons do NOT darken on hover. They leave green entirely and flip to a
  Fresh Mint fill with Midnight text, 12.91:1 (changed 2026-08-11 from the
  old Midnight fill). Darkening to #0E7A55 would put the mandated #062018
  text at 3.2:1, under the 4.5:1 bar, and #0E7A55 is a text color, not a
  fill. Do not "fix" this back to a green hover.
- The secondary (ghost) button hovers to a translucent white wash, NOT to
  a mint fill. Both buttons hovering to mint made primary and secondary
  identical on hover. Keep them distinct.
- Fresh Mint #DDF7EC — light accents: card top-borders, eyebrow text
  and labels on dark panels.
- Cloud #F3F8FC — page background. Cards stay white.
- Derived neutrals — the palette names no color for body text or borders,
  so these three fill the gap. They are working neutrals, not brand
  colors, and nothing else may be added to this list without a decision:
  #4A5A6A body and secondary text on light (7.1:1 on white), #D8E4EF
  hairline borders on light, #B6C9DD secondary text on Midnight (8.6:1).
  Never substitute a warm grey — it clashes with Cloud.
- Gradients are allowed on SECTION BACKGROUNDS ONLY (decided 2026-08-11,
  to get closer to the ServiceNow look). Everything else stays solid:
  text, buttons, cards, icon tiles, borders, logo art. Build every field
  from palette colors at low alpha over a solid palette base, so no new
  hex enters the system. Fade stops to rgba(color,0), never to
  `transparent` — some browsers interpolate that through black and smear
  grey. Always re-check contrast at the field's BRIGHTEST point, not
  against the base color: a background gradient can quietly push body
  text under 4.5:1, and #B6C9DD is the first thing to fail.
- Coral is RETIRED. The wordmark is image art (decided 2026-08-11),
  recolored from the old coral logo: docs/logo-light.png on light
  panels, docs/logo-dark.png on dark. There is no text wordmark and no
  interpunct any more — the color split between the two words IS the
  accent note. "Corcoran" carries the accent, Signal Blue on light and
  Fresh Mint on dark. "Communications" takes Midnight on light, white on
  dark. Signal Blue is 2.82:1 on Midnight, so it never carries the
  accent on a dark panel. Never render the mark in a single flat color.
- The old logo's tagline, "Public Relations • Event Coordination", is
  cropped out of both files and stays out unless those services are
  actually listed on the site. It is also illegible at wordmark size.
  The uncropped source is brand/logo-original-coral.png, and
  brand/README.md records the crop box and color mapping used to derive
  both live PNGs. Regenerate from there, never by hand.
- Voice: plain English, confident, no hype. Every claim ties to leads,
  calls, or revenue.
- Above the fold, no industry jargon: no SEO, AEO, lead gen, or funnel.
  Trade terms live in service cards, FAQ, and schema. Hero copy must make
  sense to a reader who has never bought marketing.
- SERVICE-PAGE EXCEPTION (decided 2026-08-13). The rule above governs the
  HOMEPAGE hero, where the reader has not self-selected. On a service
  page, the reader arrived by searching that exact term, so the page's
  OWN primary keyword may appear above the fold in the title and H1, and
  nothing else may. The lead paragraph explains it in plain English, no
  other trade terms (no funnel, no CTR, no top-of-funnel), and AEO is
  always spelled out as "answer engine optimization" on first use.
  One keyword per page, its own, and no jargon creep beyond it.
- Titles: all five service pages use the same suffix,
  "| Corcoran Communications". Shorten the descriptive half, never the
  brand half, to stay under 60 characters.
- When body copy describes outcomes, use the concrete triad "phone
  calls, form fills, and booked jobs" (or a page-appropriate subset),
  never "leads" or "revenue" alone. Headlines may use "phone calls" for
  punch.
- Service pages follow the template: hero with per-page graphic, plain
  English line, What You Get, differentiator band with icon tiles and
  CTA row, four-step How It Works, What It Costs with CTA row, Stronger
  Together, contact band, FAQ last. Phone CTAs are tel: links; audit
  CTAs go to #contact.
- No em dashes in site copy, ever, including schema text.

## Facts are sacred
- Never invent facts, numbers, years, reviews, or testimonials.
- Anything unverifiable gets flagged to Greg, not guessed.
- NAP (name/address/phone) must match everywhere exactly:
  Corcoran Communications, 1808 Enclave Dr, Quakertown, PA 18951,
  215-259-8304, greg@corcoranpr.com.

## Definition of done (every site change)
- Run: python3 scripts/audit.py — EVERY page must score 100/100, not just
  the one you touched. Add --strict to make the run exit nonzero when any
  page falls short. A single path still works for a quick spot check:
  python3 scripts/audit.py docs/services/seo/index.html
- Valid JSON-LD, title ≤60 chars, meta description ≤160, exactly one H1.
- Every <img> needs real alt text. The audit counts alt="" as missing
  and drops the score, so decorative-empty alt is not an option here.
- Show me the diff before committing. Commit messages in plain English.

## Adding a page (all four steps, every time)
A page does not exist until it is in sitemap.xml AND llms.txt. The audit
enforces both: a missing sitemap entry is a critical, a missing llms.txt
entry is a warning, and either one drops that page below 100/100.
1. Copy templates/service-page-template.html and replace every {{TOKEN}}.
2. Add its <url> block to docs/sitemap.xml with the real publish date.
3. Add its line to "## Key pages" in docs/llms.txt.
4. Link it from the homepage service card and the footer Services column.
Full checklist with the reasoning lives in PLAYBOOK.md.

## Links (decided 2026-08-13)
- EVERY internal link and asset path is RELATIVE and never starts with
  "/". The site also serves from a project subpath
  (gquinn01.github.io/corcoranpr-site/), where a leading slash 404s.
  From a service page the site root is ../../ , so: ../../assets/site.css,
  ../../logo-dark.png, ../../#services, ../seo/ for a sibling service.
- The only absolute URLs are the ones the spec requires to be absolute:
  canonical, og:url, og:image, sitemap <loc>, and schema @id/url values.
- Verify with: grep -rn 'href="/\|src="/' docs/ — it must print nothing.

## Repo rules
- docs/ = the live site. docs/assets/ = the shared stylesheet and script
  used by every page; the palette lives ONLY in docs/assets/site.css, so
  change it there and nowhere else. templates/ = client-pitch templates
  plus the internal service-page template. agents/ = agent job
  descriptions. Never touch .github/ or scripts/ without asking first.
- Never put API keys or secrets in any file.
