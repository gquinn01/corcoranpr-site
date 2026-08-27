# The old corcoranpr.com, as it stood before the cutover

Crawled 2026-08-27, while the WordPress site was still live and serving
from `162.211.81.218`. This is the last copy. When DNS moves, the
original is gone, along with its media library.

Nothing in here is served. `docs/` is the live site; this folder is
evidence and raw material.

## What is here

| Folder | What it holds |
|---|---|
| `pages/` | All 28 indexable URLs, exactly as the server returned them: 14 pages and 14 blog posts. Filenames are the URL path with slashes turned into underscores; the homepage is `home.html`. |
| `media/` | 73 originals from the media library, at full size. |
| `sitemaps/` | The Yoast sitemap index and all six child sitemaps, which are the inventory this crawl was built from. |

## The inventory it was built from

The old sitemap exposed **338 URLs**: 14 pages, 14 posts, 167 tags, 139
attachments, 2 categories, 2 authors. The redirect map in `PLAYBOOK.md`
decides what happens to each of the 28 real ones; everything else 404s
on purpose.

## What was left behind, and why

`media/` is 73 of the 140 library items, not all of them. Skipped:
licensed stock (the `Depositphotos_*` files, `hipster-on-mobile`,
`girl-on-phone-in-coffee-shop`, `FB-Like-Share`), the Beaver Builder
plugin's generated CSS and JS cache, blog post headers that only
illustrate posts we are not porting, and the theme's parallax and
placeholder decoration. What was kept is the material that is
irreplaceable because it is *ours*: Ruth's portrait, Greg's photos,
twelve portfolio print pieces, and the client logos.

## The logo hunt, settled

The whole reason for going in was to find larger or vector logo art. It
is not there. The header logo the old site rendered is byte-identical to
`brand/logo-original-coral.png`, the library holds no SVG, EPS, AI or
PDF, and the uploads directory listing is closed. One new variant came
back, the all-white reverse, and it is now
`brand/logo-original-white-reverse.png`. The reasoning and the evidence
are written up in `brand/README.md` under "Resolution ceiling", which is
now settled rather than open.

One incidental finding worth keeping: the old site's favicon was the
previous web vendor's own logo, a purple squid reading "DigiSquid.com".
It had been the browser-tab icon on corcoranpr.com for years.

## What the old site was running

Five tracking scripts on every one of the 28 pages, and no consent
banner anywhere:

| What | ID |
|---|---|
| Google Tag Manager | `GTM-MFPHPDK` |
| Google tag (gtag.js), fanning out to GA4 | `GT-KVN7J44` -> `G-BNLRK8YR6Y` |
| Meta / Facebook Pixel | `214048892700199` |
| Jetpack / WordPress.com Stats | blog id `152788815` |
| Google reCAPTCHA v3 | (no id in page source) |

The GTM container's only configured tag was Universal Analytics
`UA-62592023-10`, which stopped processing data in July 2023 and had
been firing into nothing for about three years. There was no Google Ads
conversion tag anywhere.

Of those, only GA4 `G-BNLRK8YR6Y` came across to the new site. See
`CLAUDE.md` under "Privacy, analytics and tracking".
