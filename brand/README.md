# Brand source art

Not served to the web. `docs/` is the live site; this folder is the
archive the live files were derived from.

## logo-original-coral.png

The pre-2026 logo, 500x100 RGBA on transparency. Three tiers:

| Element                            | Color     | Region                |
|------------------------------------|-----------|-----------------------|
| "Corcoran"                         | `#ED8B70` | x 17..184, y 29..64   |
| "Communications"                   | `#D5D5D5` | x 189..481, y 30..63  |
| "Public Relations • Event Coordination" | `#FFFFFF` | x 203..473, y 75..88 |

Coral is retired and the tagline is cropped out, because Event
Coordination is not a service the site offers. See CLAUDE.md.

## Resolution ceiling

467x40 is the largest logo art that exists. `logo-original-coral.png` is
500x100, and the wordmark inside it occupies roughly 464x35, so it is no
better. There is no vector anywhere in this repo.

Anything that needs a square or large format, a Google Business Profile
logo, an app icon, a favicon at size, is therefore a RECONSTRUCTION:
upscaled from this art rather than rendered from a source. Reconstruct
from the alpha channel, not the color pixels. Each word is one flat hex
with all 53 levels of antialiasing carried in alpha, so upscaling alpha
and re-filling with the exact brand color keeps the edges clean and the
colors exact. Resampling RGB muddies both.

This ceiling lifts if the original art turns up in the old site's media
library, which is on the pre-cutover checklist in PLAYBOOK.md, step 2.
Until that is checked, treat every square-format asset as provisional.

## How the live wordmarks were derived

Both `docs/logo-light.png` and `docs/logo-dark.png` are 467x40, made
from this file by:

1. Cropping to `(16, 27, 483, 67)`, which keeps both words and drops
   the tagline band.
2. Splitting at x 170 in cropped coordinates: left of it is "Corcoran",
   right of it is "Communications".
3. Replacing RGB per side while keeping each pixel's original alpha, so
   the antialiasing survives against any background.

| File            | "Corcoran"        | "Communications"  | Used on        |
|-----------------|-------------------|-------------------|----------------|
| logo-light.png  | Signal `#0B6BD3`  | Midnight `#082A4A`| header (Cloud) |
| logo-dark.png   | Mint `#DDF7EC`    | White `#FFFFFF`   | footer (Midnight) |

## og-card.png

`docs/og-card.png` is 1200x630: solid Midnight, the dark wordmark at
660px wide, a Fresh Mint hairline, then two lines of Arial. Regenerate
it from `docs/logo-dark.png`, not from this source file.
