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
  Midnight fill with Fresh Mint text. Darkening to #0E7A55 would put the
  mandated #062018 text at 3.2:1, under the 4.5:1 bar, and #0E7A55 is a
  text color, not a fill. Do not "fix" this back to a green hover.
- Fresh Mint #DDF7EC — light accents: card top-borders, eyebrow text
  and labels on dark panels.
- Cloud #F3F8FC — page background. Cards stay white.
- Derived neutrals — the palette names no color for body text or borders,
  so these three fill the gap. They are working neutrals, not brand
  colors, and nothing else may be added to this list without a decision:
  #4A5A6A body and secondary text on light (7.1:1 on white), #D8E4EF
  hairline borders on light, #B6C9DD secondary text on Midnight (8.6:1).
  Never substitute a warm grey — it clashes with Cloud.
- Solid colors only. No gradients, ever.
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
- No em dashes in site copy, ever, including schema text.

## Facts are sacred
- Never invent facts, numbers, years, reviews, or testimonials.
- Anything unverifiable gets flagged to Greg, not guessed.
- NAP (name/address/phone) must match everywhere exactly:
  Corcoran Communications, 1808 Enclave Dr, Quakertown, PA 18951,
  215-259-8304, greg@corcoranpr.com.

## Definition of done (every site change)
- Run: python3 scripts/audit.py docs/index.html — must score 100/100.
- Valid JSON-LD, title ≤60 chars, meta description ≤160, exactly one H1.
- Every <img> needs real alt text. The audit counts alt="" as missing
  and drops the score, so decorative-empty alt is not an option here.
- Show me the diff before committing. Commit messages in plain English.

## Repo rules
- docs/ = the live site. templates/ = client-pitch templates.
  agents/ = agent job descriptions. Never touch .github/ or scripts/
  without asking first.
- Never put API keys or secrets in any file.
