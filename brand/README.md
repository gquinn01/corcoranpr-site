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

## logo-original-white-reverse.png

The same pre-2026 logo, 500x100 RGBA, same alpha bounding box
(16, 29, 483, 90), but with "Corcoran" set in WHITE rather than coral.
An all-white reverse variant that was sitting in the old site's media
library alongside the coral one. Salvaged 2026-08-27, on the last pass
before cutover. It is not a resolution gain and nothing on the live site
is derived from it; it is archived because it is a second original of
the same art and there will be no second chance to take it.

## Resolution ceiling

**SETTLED 2026-08-27. Checked against the old site's live media library,
and no vector exists.** The evidence, so this is not re-litigated: the
logo the old header actually rendered is
`wp-content/uploads/Corcoran-Communications-Logo-Reverse-1.png`, and it
is byte-identical (SHA-256) to `logo-original-coral.png` in this folder.
The full media library, 140 items read through the WordPress REST API,
contains no SVG, EPS, AI or PDF. The uploads directory listing returns
403 and eight likely vector filenames returned 404. The theme's
customizer favicon turned out to be the previous web vendor's own squid
logo, not Corcoran art at all. The ceiling is permanent, and every
square-format asset below is a reconstruction for good.

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

The media library was checked before cutover, per PLAYBOOK.md step 2,
and it held nothing better. Do not treat the square assets as
provisional any more, and do not go looking again: the domain is the
only place that art could have been, and it has been read.

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

## Favicon

Three files at the site root, built 2026-10-12. All three are a CROP of
`corcoran-gbp-avatar-720.png`, scaled DOWN, so nothing here is a new
reconstruction and no letterform was redrawn.

The avatar cannot be used as it stands. It was sized for Google's
circular profile slot, so the "C" is 374px of a 720px canvas, 52% of the
height, and at 16px in a browser tab that leaves a letter about eight
pixels tall that reads as a smudge. Three crops were rendered side by
side at 16, 32 and 48px (letter at 52%, 62% and 70% of the height) and
Greg picked 70%, the only one that holds at tab size.

**The recipe.** Crop box `(93, 93, 627, 627)` in the avatar's own
coordinates: a 534px square centered on the letter's bounding box
`(251, 173, 469, 547)`, which sits dead center at `(360, 360)`. Then
Lanczos to each size. The canvas is solid Midnight `#082A4A` edge to
edge, so the crop needs no fill.

| File | Job |
|------|-----|
| `docs/favicon.ico` | 16, 32 and 48px in one file. Browser tabs, and the default path a browser asks for when a page names no icon. |
| `docs/favicon-192.png` | 192x192. The one Google and high-density screens take. |
| `docs/apple-touch-icon.png` | 180x180. iPhone home screen. iOS rounds the corners itself, so the file stays square and full bleed. |

Circle-safe by measurement, which matters because Google shows the icon
in a circle: the letter's diagonal is 0.81 of the cropped square, so it
sits inside the inscribed circle with room on every side.

Regenerate all three from the avatar with that crop box, never by hand
and never from each other. If the avatar is ever rebuilt, re-measure the
letter's bounding box first; the crop box follows from it.

## og-card.png

`docs/og-card.png` is 1200x630: solid Midnight, the dark wordmark at
660px wide, a Fresh Mint hairline, then two lines of Arial. Regenerate
it from `docs/logo-dark.png`, not from this source file.
