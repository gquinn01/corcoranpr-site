# Corcoran Communications

The source for **[corcoranpr.com](https://corcoranpr.com/)**, and the two
AI agents that watch it.

Corcoran Communications is a veteran-owned marketing firm in Quakertown,
Pennsylvania, founded by Ruth Corcoran in January 2000 and owned since
July 2023 by her son Greg Quinn. This repo holds the website itself and
the automation around it.

The site is a static site on GitHub Pages: no database, no platform
fees, no plugins, and every character editable in a text editor. It went
live on this domain on 2026-08-27, replacing the WordPress site that had
served it before.

## What is here

```
corcoranpr-site/
├── docs/                          ← THE LIVE SITE. Pages serves this folder.
│   ├── index.html                   Homepage
│   ├── about/  free-audit/  privacy/
│   ├── services/                    Five service pages
│   │   ├── web-design/  seo/  google-ads/
│   │   └── social-media-marketing/  lead-generation/
│   ├── industries/                  Six industry pages, each earned from
│   │                                real client work
│   ├── locations/                   Three county hubs, nine town pages
│   ├── blog/                        Notes on Local Marketing: the index
│   │                                and one folder per post
│   ├── 404.html                     Branded error page
│   ├── assets/site.css              The shared stylesheet. The brand
│   │                                palette lives here and ONLY here.
│   ├── assets/site.js               Mobile menu, audit form, stat band
│   ├── llms.txt                     Guide for AI assistants (AEO)
│   ├── robots.txt                   Welcomes search and AI crawlers (AEO)
│   ├── sitemap.xml                  29 pages, the crawler's contents page
│   └── CNAME                        The custom domain. Never delete it.
├── templates/
│   ├── service-page-template.html ← The master mold. Any shared change to
│   │                                a live page lands here in the same commit.
│   ├── blog-post-template.html      The mold for a blog post. Same rule.
│   └── spa-local-business-template.html   Day-spa demo, for pitching
├── scripts/
│   ├── audit.py                   ← The SEO + AEO scanner. Scores every
│   │                                page separately. The definition of done.
│   ├── stamp-assets.py              Cache-busting stamps for the CSS and JS
│   ├── fetch_seo_news.py            Pulls Google/AI-search news for the Watcher
│   ├── cascade-analyzer.html        Checks CSS for component-vs-ancestor overrides
│   └── mobile-check.md              How to test mobile layout honestly
├── agents/
│   ├── site-auditor.md            ← Agent job descriptions, in plain English.
│   ├── google-watcher.md            That IS the programming.
│   └── content-writer.md            Drafts one post a week as a pull
│                                    request. It never publishes.
├── brand/                           Source logo art and how the live files
│                                    were derived from it
├── archive/old-site/                The WordPress site as it stood the day
│                                    before cutover, and what it was running
├── CLAUDE.md                        Standing orders: brand, voice, facts,
│                                    definition of done. Read before editing.
└── PLAYBOOK.md                      Strategy, AEO, the cutover record,
                                     the decided redirect map
```

Under `docs/` there are **45 files**: 29 real pages, 15 redirect stubs
standing at old WordPress URLs, and the 404 page. Only the 29 are in
`sitemap.xml`, which is deliberate.

## The two agents

Both run on GitHub Actions and file their work as GitHub Issues, so
every exchange is logged where a human can read it.

| Agent | Runs | Job |
|---|---|---|
| **Site Auditor** | Mondays, 8:00am ET | Runs `scripts/audit.py` against the live site, then has Claude turn the raw scan into a plain-English report with recommended fixes. |
| **Google Watcher** | Daily, 7:00am ET | Sweeps Google Search Central, the Search Status dashboard, and industry watchdogs. Files a `google-update` alert only when something warrants it. |

They coordinate through the Issues tab: the Watcher files alerts, and
the Auditor reads the open ones before writing its Monday report, so a
relevant algorithm change reorders that week's priorities.

The firm runs three more agents against client advertising accounts,
plus automated watchdog scripts checking spend pacing and conversion
tracking daily. Those live with the accounts they watch, not in this
repo. **A human reviews and approves every change. Nothing ships on a
machine's say-so.**

To run one by hand: **Actions** tab, pick the workflow, then **Run
workflow**. The report lands in **Issues** a couple of minutes later.

### Configuration

| Where | Name | Value |
|---|---|---|
| Secrets | `ANTHROPIC_API_KEY` | Anthropic API key. The agents think with it. |
| Variables | `SITE_URL` | `https://corcoranpr.com/` |

`SITE_URL` is what points the weekly audit at the live site rather than
the local files. Set, the scan takes its page list from the live
`sitemap.xml` (29 pages) and the site-wide `robots.txt` and `llms.txt`
checks run, because those have to be fetched from a real domain root.
Point it at any other domain and the same scanner audits that site,
which is how a prospect gets a free audit.

## Working on the site

Read `CLAUDE.md` first. It carries the brand palette, the voice rules,
the facts that are not negotiable, and the reasoning behind decisions
that look arbitrary until you know why.

Before committing anything:

```bash
python3 scripts/audit.py --strict     # every one of the 45 files at 100/100
python3 scripts/stamp-assets.py       # after any change to site.css or site.js
```

`--strict` exits nonzero if any file is under 100. A page is not
finished until it is in `sitemap.xml` and `llms.txt`, and the audit
enforces both, so the checklist is not something to remember. It is
something the build fails without.

## What it costs

GitHub: **$0**. The free tier includes 2,000 minutes a month of Actions
runtime and both agents together use roughly 30. Hosting on GitHub
Pages: **$0**. The Claude API: a few dollars a month.

## When a run fails

Open the failed run in the **Actions** tab, click the red step, copy the
error, and hand it to Claude with the workflow file. Action versions
drift over time and that is usually all it is.

## Built for AEO, not just SEO

SEO gets you ranked when someone searches. **AEO, answer engine
optimization**, gets you named inside the answer when someone asks
ChatGPT, Claude, Perplexity, or Google's AI a question like "best auto
body shop near me."

This repo covers both. Every page carries FAQ content mirrored in
`FAQPage` schema, `sameAs` entity links, a `robots.txt` that explicitly
welcomes AI crawlers, and an `llms.txt` guide. The auditor scores AEO
checks on every scan and fails a page whose visible FAQ has drifted from
its schema, because assistants quote the schema.

One honest note: Google has said its AI features ignore `llms.txt`,
while Anthropic and OpenAI tooling reads it. It is cheap insurance, not
magic. And the parts no script can do stay human work: a filled-out
Google Business Profile, steady reviews, and identical name, address and
phone everywhere.
