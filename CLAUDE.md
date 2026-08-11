# Corcoran Communications — standing orders

## Brand (decided 2026-08-11 — "Strategic Growth" palette; do not drift)
- Midnight #082A4A — dark panels (header, hero, bands, footer) and
  heading text on light backgrounds.
- Signal Blue #0B6BD3 — section titles, links, and hover states.
- Growth Green #15B77E — buttons/CTAs and success markers ONLY, always
  with dark text (#062018) on green fills. Use #0E7A55 for small green
  text on light backgrounds (contrast).
- Fresh Mint #DDF7EC — light accents: card top-borders, eyebrow text
  and labels on dark panels.
- Cloud #F3F8FC — page background. Cards stay white.
- Solid colors only. No gradients, ever.
- Coral is RETIRED from the site. Until new logo art exists, render the
  wordmark as text: white on dark panels, Midnight on light.
- Voice: plain English, confident, no hype. Every claim ties to leads,
  calls, or revenue.

## Facts are sacred
- Never invent facts, numbers, years, reviews, or testimonials.
- Anything unverifiable gets flagged to Greg, not guessed.
- NAP (name/address/phone) must match everywhere exactly:
  Corcoran Communications, 1808 Enclave Dr, Quakertown, PA 18951,
  850-619-5151, greg@corcoranpr.com.

## Definition of done (every site change)
- Run: python3 scripts/audit.py docs/index.html — must score 100/100.
- Valid JSON-LD, title ≤60 chars, meta description ≤160, exactly one H1.
- Show me the diff before committing. Commit messages in plain English.

## Repo rules
- docs/ = the live site. templates/ = client-pitch templates.
  agents/ = agent job descriptions. Never touch .github/ or scripts/
  without asking first.
- Never put API keys or secrets in any file.
