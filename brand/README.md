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

## Square and avatar assets

Three derived files, built 2026-08-26 for the Google Business Profile
slots. All are reconstructions under the ceiling above, and all were
made the same way: the letterforms were lifted from the wordmark's ALPHA
channel, upscaled with Lanczos-3, and re-filled with the exact brand
hex. No font was identified and none was guessed. Every shape here is
the original art's own geometry.

| File | Job |
|------|-----|
| `corcoran-gbp-avatar-720.png` | 720x720. Small circular avatar slots. A white "C", the one from Corcoran, on Midnight `#082A4A` filling the whole canvas so a circular crop has no white edge. Chosen over the Signal Blue version for contrast at 48px, which is where these are actually read. It does NOT match the site header's colors; that was the accepted trade. |
| `corcoran-gbp-logo-720.png` | 720x720. Large square slots. The stacked wordmark, "Corcoran" over "Communications", on white, sized inside a circle-safe zone. Keeps the site's colors, Signal `#0B6BD3` over Midnight `#082A4A`. Unreadable at avatar size, which is why the avatar file exists. |
| `corcoran-logo-stacked.png` | 297x94. The stacked lockup at native resolution, no upscaling at all. The source to rebuild the other two from, or to scale for any new square slot. |

The stacked lockup splits the wordmark at x 170 in cropped coordinates,
the same split point the color mapping uses, so the two words separate
where they always have.

Note the two capital C's are not the same: the one in "Corcoran" has
roughly 8px strokes at source and the one in "Communications" roughly
5px. The original logo sets the two words in different weights. The
avatar uses the heavier one.

## og-card.png

`docs/og-card.png` is 1200x630: solid Midnight, the dark wordmark at
660px wide, a Fresh Mint hairline, then two lines of Arial. Regenerate
it from `docs/logo-dark.png`, not from this source file.
