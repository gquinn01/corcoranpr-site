# The AI-First Agency Playbook

### How Lucas builds sites, what's real vs. sales talk, and your 30-day path to the cutting edge

*Prepared for Greg Quinn · Corcoran Communications · August 2026*

---

## Start here: where things stand, and your punch list

This document now travels inside your starter kit (`PLAYBOOK.md`), so everything — your rebuilt website, your two agents, the setup guide, and this playbook — lives in one folder. Once that folder is uploaded to GitHub, the repo becomes the single source of truth for your whole AI operation.

**Already done (in one working session):** You can decode any "AI agency" pitch (Part 1) and speak the vocabulary (Part 2). You own a working two-agent system — a weekly SEO/AEO site auditor and a daily Google/AI-search watcher that communicate through GitHub Issues (Part 3). Your own corcoranpr.com has been rebuilt on verified 2026 facts — solo veteran-owned firm, Ruth honored as retired founder, Quakertown address, Bucks/Montgomery/Lehigh territory, the new service lineup led by AI-built websites and automated SEO/AEO monitoring — and it scores 100/100 on your own auditor. The fictional day-spa site is your reusable client-pitch template (`templates/`). And you watched the core loop run three times: the auditor caught its own builder's mistakes, and they got fixed in minutes.

**Your punch list, in order:**

1. **Go live with the kit** (~30 min): follow `README.md` — GitHub account, upload this folder, add the API key, turn on Pages, press Run on both agents. Set the `SITE_URL` variable to `https://corcoranpr.com/` so the auditor benchmarks the old WordPress site weekly — that's your before/after story.
2. **Create the Google Business Profile** exactly matching the site's footer: Corcoran Communications, 1808 Enclave Dr, Quakertown, PA 18951, 215-259-8304. Home office: verify the address, display as a service-area business. This single step unlocks local-pack and "near me" visibility that no on-page work can substitute for.
3. **Confirm the socials** (Facebook, Instagram, X, LinkedIn) are alive and current — the site's schema now vouches for them to every AI system.
4. **Chase the testimonial**: get the "10 to 1" client's permission to attribute the quote by name, and add your headshot to the site.
5. **Cut over the domain when ready — not day one** (README's go-live section): preview on GitHub Pages first, change only web DNS records (never MX — that's your email), and 301-redirect the old blog URLs so six years of Google equity survives.
6. **Start the monthly "ask the AIs" ritual** (Part 6): log who ChatGPT, Claude, Perplexity, and Google's AI name for your five customer questions. That log is your AEO scorecard — for your own firm first, then as a billable client report.

One decision worth recording so future-you remembers the reasoning: **your site is a static page on GitHub Pages, not Wix or WordPress.** Free forever, fastest possible, nearly unhackable, and every character is directly editable by you or your agents. Wix stays in the toolbox (via its MCP) for clients who need booking or want to self-edit; WordPress-style platforms earn their fees only when a client needs what they bundle. And the triage rule that came out of the Ruth fix: **facts get corrected before anything ships — design and copy iterate forever.** The schema and llms.txt exist to be memorized and repeated by AI systems; being the wrong answer scales just as efficiently as being the right one.

---

## Part 1: What Lucas is actually doing — decoded

Let's start by taking apart the phone call, because the fastest way to catch up is to understand precisely what you heard. I looked at both sites. Here's the honest breakdown.

**"They're AI sites."** True, but less magical than it sounds. His agency site (jakeandlucas.com) and the client site (thebodyserenedayspa.com) are well-built local-business sites on Wix: clean structure, good titles and descriptions, location keywords, booking integration. "AI site" doesn't mean the site is somehow made of AI. It means AI did the labor — wrote the copy, structured the pages, generated the SEO markup — while a human directed it and approved it. The output is a normal website; the revolution is in the cost of producing it: what used to take an agency team two weeks now takes one person a day or two.

**"It's built on Wix, but he never really touches Wix."** This is the most interesting claim, and it's fully plausible. Wix ships an official [MCP server](https://www.wix.com/studio/developers/mcp-server) — MCP (Model Context Protocol) is a standard plug that lets an AI assistant operate other software. Connect the Wix MCP to an AI tool like Claude, and the AI can create Wix sites, edit content and settings, and call Wix's APIs on his behalf. So Lucas types instructions to an AI in plain English, and the AI pushes buttons in Wix for him. He genuinely never opens the Wix editor. The site *lives* on Wix; the *work* happens in his AI tools, with the project files and instructions stored in GitHub.

**"He has agents in GitHub that talk to each other."** Real, and you now own a working copy of it (more below). GitHub isn't just for code — it's a free filing cabinet with a built-in scheduler called GitHub Actions. You can tell it: "every Monday at 8am, run this AI with these instructions." That scheduled AI-with-a-job-description is what people mean by an *agent*. The "talking to each other" part is mundane and brilliant: the agents leave each other notes in a shared inbox (GitHub Issues). Agent B files an alert; Agent A reads it before doing its own job. No science fiction — a message board with robots on both ends, and every exchange logged where you can read it.

**"One constantly scans Google's algorithm updates."** Here's where salesmanship creeps in. Nobody scans Google's algorithm — it's a trade secret inside Google's data centers. What the agent actually does is monitor the places where changes are *announced or first detected*: Google's own Search Central blog and Search Status dashboard, plus industry watchdogs like Search Engine Roundtable that spot ranking turbulence within hours. The agent reads those daily, filters the noise, and flags what matters for its sites. That's genuinely valuable — it's what a junior SEO analyst used to bill hours for — but "scanning the algorithm" is the sizzle, not the steak. Knowing that difference is your first step toward being *better* than Lucas, not just equal to him: you'll be able to sell this with claims you can defend in a room full of skeptics.

**"It is so easy."** For him, now — yes. The honest version: it's easy the way driving is easy after thirty hours of lessons. There's a two-to-four-week learning curve, and you're standing at the start of it with (as of today) a working car.

The big picture worth internalizing: **the website is no longer the product. The system around it is.** Anyone can generate a pretty site in an afternoon now — that's a commodity. What Lucas sells is a site plus a tireless monitoring-and-maintenance apparatus, delivered at near-zero marginal cost. That's the actual business model you're going to copy.

---

## Part 2: The eleven words that make you fluent

Learn these and every AI-marketing conversation stops being intimidating.

**AEO (answer engine optimization)** — getting a business named *inside the answer* when someone asks ChatGPT, Claude, Perplexity, or Google's AI a question, rather than (just) ranked in a list of links. The zero-click future of local marketing; Part 6 is devoted to it. (You'll also see "GEO," generative engine optimization — same idea, different label.)

**GitHub** — a free website where you store project folders in the cloud. Think Dropbox with superpowers: it remembers every version of every file, and it can run tasks on a schedule.

**Repo (repository)** — one project folder on GitHub. One client = one repo is a sensible habit.

**GitHub Actions** — GitHub's built-in scheduler and task-runner. "Every morning at 7, do this." The tasks run on GitHub's computers, free (2,000 minutes a month), whether your laptop is on or not. This is where the agents "live."

**Agent** — an AI given a job description, tools, and a trigger, that then works without you babysitting each step. Job description + schedule + permissions = employee. The job description is written in plain English — you, a PR man, are *more* qualified to write great ones than most engineers.

**Cron** — the scheduling syntax inside GitHub Actions (`0 12 * * 1` means "Mondays at 12:00 UTC"). You never memorize it; you ask AI to write it.

**Claude Code** — Anthropic's tool that lets an AI work directly with files, folders, GitHub, and other software — the "hands" that turn instructions into finished work. This is the tool that builds sites in an afternoon. (Cursor and GitHub Copilot are cousins.)

**MCP (Model Context Protocol)** — the standard plug that connects an AI to other software: Wix, HubSpot, Canva, Google services. When someone says "my AI manages my Wix site," MCP is how.

**Structured data / schema** — invisible labels in a webpage that tell Google's machines exactly what the business is: name, address, hours, prices, reviews. Most small-business sites are missing it, which makes it the single easiest win you can sell. It's also how sites get quoted by AI search tools — the fastest-growing way customers find local businesses.

**Static site** — a site that's just files (like the demo I built you today), no database, no monthly platform fee. Loads instantly, nearly unhackable, hosts free on GitHub Pages. For a typical local business, this plus a booking link beats a $40/month page-builder subscription.

**API key** — a password that lets your agents use an AI service, billed by usage. Guard it like a credit card number; store it in GitHub's "Secrets," never in a file.

---

## Part 3: The architecture, on one page

Everything Lucas described — and everything in your starter kit — is this picture:

```
                         ┌──────────────────────────────┐
                         │        GITHUB (the office)    │
                         │                              │
   Google's blogs   ┌────┤  AGENT 2: Google Watcher     │
   Status dashboard │    │  runs DAILY, 7am             │
   SEO watchdogs ───┘    │  "anything change out there?"│
                         │            │                 │
                         │            ▼  files alert    │
                         │   ┌─────────────────┐        │
                         │   │  SHARED INBOX    │        │
                         │   │  (GitHub Issues) │◄──┐    │
                         │   └─────────────────┘   │    │
                         │            ▲  reads     │    │
                         │            │  alerts    │    │
   Your client's    ┌────┤  AGENT 1: Site Auditor  │    │
   website ─────────┘    │  runs WEEKLY, Mondays ──┘    │
                         │  "how healthy is the site?"  │
                         │  writes plain-English report │
                         └──────────────┬───────────────┘
                                        ▼
                          YOU read one report over coffee,
                          approve fixes, and bill the client.
```

Three design choices here are worth stealing for everything you ever build. First, **the mechanical work and the thinking are separated**: a dumb, free script does the scanning (it can't hallucinate), and the AI only *interprets* results — cheaper and far more trustworthy. Second, **agents communicate through a logged, shared inbox**, so you can audit every "conversation" after the fact; when a client asks "how do you know about the Google update?", you show them the paper trail. Third, **each agent has minimum permissions** — the auditor can read files and write reports; it cannot touch the website itself. You approve changes. AI proposes; the human disposes. Clients will love hearing that, and it happens to be the correct engineering.

---

## Part 4: What you already own as of today

While writing this playbook I built you a working copy of the whole system — the `ai-agency-starter-kit` folder that came with it. Inside:

**Your own rebuilt website** (`docs/index.html`) — the new corcoranpr.com, rebuilt on verified 2026 facts with every SEO and AEO practice in this playbook baked in: the veteran-owned positioning, the "one senior marketer + a staff of AI agents" team story, the free-AI-audit funnel as the main call to action, and the county-level territory targeting. Open it in your browser; then open the same file in a text editor: every comment marked `WHY:` explains an SEO/AEO decision. Reading that one file *is* an on-page course. The kit also includes the fictional day-spa site (`templates/`) as your reusable template for pitching local businesses — the same genre as Lucas's client.

**A real SEO scanner** (`scripts/audit.py`) that checks a dozen ranking factors on any webpage — including any *prospect's* webpage. Remember that.

**Two hiring-ready agents** — job descriptions in plain English (`agents/`), schedules and permissions in two workflow files (`.github/workflows/`).

And a story worth retelling: when I first ran the auditor against my own demo site, **it caught me** — the page title was 67 characters, past Google's ~60-character display limit. I fixed it; the site now scores 100/100. The system criticized its own builder on the first run. That loop — build, scan, catch, fix — running unattended every week across every client, is the product.

The kit's README walks you through going live in about 30 minutes with zero coding: create a free GitHub account, upload the folder, add an API key, click twice to turn on free hosting, and press "Run workflow." Your first AI-written SEO report appears in your Issues tab minutes later.

### Adding a page to the site (the four-step checklist)

As of 2026-08-13 the site is no longer one page. It has a homepage plus five service pages under `docs/services/`, and `scripts/audit.py` now scores **every page separately** so one weak page cannot hide behind a site average.

When you add a page, all four of these happen or the page is not finished:

1. **Build it from the template.** Copy `templates/service-page-template.html` to `docs/services/<slug>/index.html` and replace every `{{TOKEN}}`. The nav, footer, palette and schema shape come with it. All internal links must stay relative (`../../` is the site root from there), because the site also serves from a project subpath where a leading `/` would 404. One token is not free copy: `{{HOW_SUB}}`, the eyebrow above **How It Works**, is always `WHAT HAPPENS WHEN YOU CALL`. All 24 pages carrying that section were standardized on it on 2026-08-21, and the audit does not check the wording, so a new page only stays consistent if you set it deliberately.
2. **Put it in the sitemap.** Add a `<url>` block to `docs/sitemap.xml` with the absolute URL, a trailing slash, and `lastmod` set to the real date you published it. A missing sitemap entry is scored as **critical**.
3. **Put it in llms.txt.** Add a line under `## Key pages` in `docs/llms.txt`, in the existing `- [Name](url): description` form. This is the file AI assistants read to learn what the business offers. A missing entry is scored as a **warning**.
4. **Link to it.** The matching homepage service card gets its "More on ..." link, and the page goes in the footer Services column, which appears on every page.

Then run `python3 scripts/audit.py`. Every page must read 100/100. Steps 2 and 3 are enforced by the scanner itself, so the sitemap, llms.txt and the actual pages cannot quietly drift apart. That is the point: the checklist is not a thing you have to remember, it is a thing the build fails without.

### The domain cutover checklist

The site is built for `corcoranpr.com` and is not served from it yet. Every absolute URL in the repo already points there: all 26 canonical tags, all 26 `<loc>` entries in `sitemap.xml`, the `Sitemap:` line in `robots.txt`, and 204 `@id`/`url` values across the schema blocks. Meanwhile `corcoranpr.com` still resolves to the old WordPress site.

That gap is not neutral, and it is the reason not to let this drag. Right now every page on the GitHub Pages address tells Google *the real version of this page lives at corcoranpr.com* — and the page that answers there is the old site. The longer both are up, the longer you are pointing crawlers at the thing you replaced.

**Before you touch DNS.**

1. **Check the MX records first.** `greg@corcoranpr.com` is a live business mailbox on this domain, and it is the only step here that can take down something you rely on today. Changing the A record does not touch mail. *Moving the nameservers* moves everything, and MX records that are not recreated on the new provider mean mail stops arriving with no error and no bounce you will see. Export the full current zone before changing one record. Today the domain answers from `dns101.register.com` / `dns102.register.com`, with the apex pointing at `162.211.81.218`.
2. **Save the old site.** It is 28 URLs: 14 pages and 14 blog posts, listed in its own `page-sitemap.xml` and `post-sitemap.xml`. Once DNS moves, that content is gone unless you have a copy. Pull the HTML and any images worth keeping.
3. **Decide the redirect map** (next section). Do this *before* cutover, not after, because the window where old URLs are dead is the window where the rankings bleed.

**The cutover itself.**

4. **Add `docs/CNAME`**, one line, `corcoranpr.com`, no protocol and no trailing slash. The repo has no CNAME file today. Without it GitHub Pages drops the custom domain on the next deploy.
5. **Set the custom domain** in Settings → Pages. The Pages API currently reports `cname: null`, serving from `main` branch, `/docs` path.
6. **Point DNS at GitHub.** Apex `corcoranpr.com` needs four A records (and the matching AAAA records) at GitHub's Pages IPs; `www` gets a CNAME to `gquinn01.github.io`. Read the current IPs off [GitHub's own docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site) on the day you do it rather than trusting any list written earlier, this one included.
7. **Wait, then enforce HTTPS.** The certificate is issued after DNS resolves, so the "Enforce HTTPS" box stays greyed out until propagation finishes. Come back for it; do not skip it.

**After it is live.**

8. **Restore `SITE_URL`**: `gh variable set SITE_URL --body "https://corcoranpr.com/"`. See the rule in `CLAUDE.md`. This is what puts the weekly audit back on the live site, and it is what turns the site-wide AEO checks back on — `robots.txt` and `llms.txt` are fetched from a domain root, so while the scan runs on local files those two checks do not run at all.
9. **Confirm `robots.txt` is finally real.** The file says so itself in its own header comment: on a project subpath it is decorative. At a domain root it starts working, and the AI-crawler `Allow` rules that are the whole point of it take effect.
10. **Search Console.** Add `corcoranpr.com` as a property, verify it, submit `sitemap.xml`. Do not use Change of Address — that tool is for moving between different domains, and this is the same domain changing what it serves.
11. **Re-run the audit against the live site** once, by hand: `python3 scripts/audit.py https://corcoranpr.com/`. The page list comes from the live sitemap, so this is also the check that the sitemap deployed correctly.
12. **Update the profiles that carry the URL** — Google Business Profile first, then the four social accounts in the schema `sameAs` array.
13. **Clean up the pre-cutover language.** The `SITE_URL` rule in `CLAUDE.md` and the site-wide AEO instruction in `agents/site-auditor.md` are both written "until the domain cutover." Once it has happened they are stale.

#### The redirect map: decide it, don't default it

`.nojekyll` is in `docs/`, which turns Jekyll off, so `jekyll-redirect-from` is not available. GitHub Pages serves static files and cannot issue a real 301. A redirect here is an HTML file at the old path with a `meta refresh` and a `rel="canonical"` at the new one. Google follows those and passes most of the signal, but it is a weaker instrument than a server redirect, so spend it where it counts.

The temptation is to point all 28 old URLs at the homepage. Don't. Google treats a mass redirect of unrelated pages to one page as a soft 404 and drops them anyway, so it buys nothing and costs you a pile of files to maintain. Redirect only where the new page genuinely answers what the old page answered. Let the rest 404 honestly.

| Old URL | Where it should go | Why |
|---|---|---|
| `/` | `/` | Same URL. Nothing to do. |
| `/about/` | `/about/` | Same URL, and the new page is better. Free win. |
| `/social-media-marketing/` | `/services/social-media-marketing/` | Clean one-to-one match. |
| `/portfolio/` | `/#industries` | Industries We Know is the closest thing we now have to a portfolio. |
| `/contact/` | `/free-audit/` | The new site has no contact page; the free audit is the front door. |
| `/digital-marketing-services/` | `/#services` | Broad old page, no single new equivalent. |
| `/content-marketing/` | **Decide** | `llms.txt` lists content marketing as a service, but no page exists for it yet. Either build the page or let this 404. |
| `/public-relations/` | **Decide** | No equivalent. PR is not a service the new site sells. |
| `/graphic-design-services/` | **Decide** | No equivalent. |
| `/branding-agency/` | **Decide** | No equivalent. |
| `/blog/`, `/blog/weekly-podcast/`, 14 posts | **Decide** | There is no blog on the new site. These 16 URLs are the real question: they are the only pages on the old domain with any age on them. Porting the two or three that still read well is worth more than redirecting all 16 to nothing. |
| `/landing-page-template/`, `/thanks/` | Let them 404 | Leftovers. Nobody links to them. |

A 404 is not a failure state. It is the correct, honest answer for a page that no longer exists, and it is what Google prefers to a redirect that lies about relevance. Which is also the argument for **adding `docs/404.html`** while you are in here: there is none today, so a wrong URL currently lands on GitHub's default page with none of your branding, no nav, and no way back into the site.

---

## Part 5: The 30-day path to the cutting edge

**Week 1 — Ship something real (this week).** Follow the kit README start to finish, until the demo site is live at your own GitHub Pages address and both agents have run. Don't study first — ship first; the understanding follows the doing. Then spend one hour reading the `WHY:` comments in the site and the two agent job descriptions. By Sunday you can say, truthfully, "I run AI agents in GitHub that monitor sites and Google's algorithm changes." Day one to Lucas-parity-in-vocabulary: seven days.

**Week 2 — Learn to direct the builder.** Your own site is already rebuilt (it ships in the kit), so this week you *iterate* on it and then build one from scratch. Install [Claude Code](https://code.claude.com), open your repo, and direct it like you'd direct a junior team: "warmer," "more white space," "rewrite the hero for CFOs," "add a portfolio page for the Disney on Ice work." Then prove you can do it cold: pick a real local business you'd love as a client and build their site from the spa template — "Rebuild templates/spa-local-business-template.html for [business], keep all the schema patterns, title under 60 characters." The skill you're building is *creative direction of machines*, and it transfers straight from your PR instincts. This week ends when you've built a site you'd be proud to invoice for.

**Week 3 — Add the agent layer everywhere.** Point the auditor at real, live sites (the README shows the one-line change). Ask Claude to add a third agent to your repo — a content writer that drafts a monthly, locally-relevant blog post and files it as a *draft for your approval* rather than publishing (that approval step is your quality moat). If a client is on Wix, connect the [Wix MCP](https://www.wix.com/studio/developers/mcp-server) to Claude and experience "never touching Wix" firsthand. This is also the week to skim what the industry is doing — [agentic SEO workflows](https://www.lyzr.ai/blog/ai-agents-for-seo/) and [current AI SEO agents](https://nightwatch.io/blog/best-ai-seo-agents/) — not to buy anything, but so you can name-drop and compare honestly.

**Week 4 — Productize and sell.** Package what you now do into three tiers you can quote from memory. The audit funnel: run `audit.py` on a prospect's site, have Claude turn the findings into a two-page plain-English report with your branding, and send it free — it's a lead magnet that costs you four minutes. The build: AI-built site, flat fee — market rate for local-business sites is $2,000–5,000, and your cost is now mostly your taste and a weekend. The retainer (this is the business): "AI-monitored SEO care" at $300–750/month, where the agents do the watching and you deliver a monthly summary in person, by phone, with your PR polish. Ten care-plan clients is real recurring revenue that runs while you sleep — that's what "it is so easy" actually meant.

**After day 30** — compounding. Every new client repo is a copy-paste of the last. Add agents as you find repeatable chores: a review-watcher for Google Business Profile, a competitor-watcher, a monthly report-writer. Your agency's org chart becomes: Greg, plus a growing staff of agents, each with a job description you wrote in English.

---

## Part 6: AEO — being the answer, not just ranking for it

SEO wins when someone *searches* and clicks. **AEO — answer engine optimization — wins when someone asks a question and an AI answers it.** "Best day spa near Ridgewood?" typed into ChatGPT, asked of Claude, spoken to a phone, or answered by Google's AI Overviews at the top of the results page. Most of those interactions end without a click — roughly [two-thirds of searches already end zero-click](https://cxl.com/blog/answer-engine-optimization-aeo-the-comprehensive-guide/) — so the businesses named *inside the answer* win, and everyone else is invisible. For local businesses this is not a future concern; it's where a growing share of "who should I call?" decisions already happen. It's also a genuine differentiator for you: most local agencies still sell 2020-era SEO.

The encouraging news: AEO is not a separate dark art. It's built from parts you now own, aimed at a second audience. Five moves cover the local-business version of it.

**Structure content as questions with direct answers.** AI systems assemble answers from pages that ask the customer's actual question and answer it completely in the first sentence or two. That's why the demo site's FAQ uses the questions people phone in ("Where do I park?") with plain, complete answers, marked up with FAQPage schema. When you build for clients, mine their inbox and front desk for the ten questions they answer every week — that's the highest-value content on the internet for them, and no competitor bothers to publish it.

**Make the entity verifiable.** Before an AI recommends a business, it wants evidence the business is real, open, and liked: consistent name/address/phone everywhere, a fully filled-out [Google Business Profile](https://brandify.io/blog/aeo-for-local-businesses/), review volume and recency, and `sameAs` schema links tying the website to its Instagram, Yelp, and directory profiles. The demo site now carries those links, and the auditor checks for them. Note that most of this is *off*-site work — profiles, citations, review cadence — which no script fully automates. That's human work. It's also exactly the kind of thing a PR firm is better at than any dev shop, so bill for it.

**Let the AI crawlers in.** AI assistants can only recommend what their crawlers can read. A surprising number of sites block GPTBot, ClaudeBot, and PerplexityBot with copy-pasted "block AI" robots.txt templates — self-inflicted invisibility. The kit now ships a robots.txt that explicitly welcomes them, and the auditor checks any live site for accidental blocking. (Prospecting angle: run the audit on a prospect and discover they've been invisible to ChatGPT for a year. That's a phone call that closes.)

**llms.txt — with an honest label.** This is a plain-text "guide to the business" written for AI agents, and it's the most hyped and most oversold item in AEO. The truth, as of mid-2026: [Google has said its AI Search features ignore it](https://www.getpassionfruit.com/blog/should-i-create-an-llms.txt-file-google-s-2026-guidance-explained), while Anthropic recommends it for agents, OpenAI publishes them for its own products, and Perplexity has been seen reading them. Twenty minutes of work, some upside, zero downside — the kit includes one for the demo spa. When a competitor pitches llms.txt as an AI-ranking miracle to one of your clients, you'll be the one in the room who knows both halves of that story.

**Measure it by asking.** There's no "rank tracker" for AI answers yet that's worth trusting, so do the direct thing: once a month, ask ChatGPT, Claude, Perplexity, and Google (AI mode) the five questions a customer would ask — "best spa in Ridgewood," "spa near me open Sunday," and so on — and log who gets named. That log is your AEO scorecard, it costs nothing, and handing a client a before/after version of it is the most persuasive marketing report they will ever receive. (This is also a chore an agent can do — ask Claude to add a monthly "ask the AIs" agent to your repo once you're comfortable.)

Your kit already reflects all of this: the demo site carries FAQPage schema, entity links, a welcome-mat robots.txt, a sitemap, and an llms.txt; the auditor scores AEO checks on every scan; and the Google Watcher's job description now explicitly covers answer-engine news — AI Overviews changes, crawler policy shifts, and how assistants pick local businesses — not just classic algorithm updates.

---

## Part 7: Your unfair advantage (and the honest hype filter)

Here's what Lucas didn't tell you: the technology is the *easy* half, and it's rapidly becoming the same for everyone. Within a year, every competitor will generate decent sites. What won't be commoditized: knowing what a business should *say*, earning trust in a room, media instincts, and the judgment to catch an AI when it's confidently wrong. You've spent a career on exactly those. AI doesn't replace your PR skills — it gives them hands, working around the clock.

To stay at the cutting edge, you also need a filter for the next Lucas call — and there will be many. When anyone pitches you AI capabilities, ask three questions. *"What exactly triggers it, and what exactly does it output?"* — real systems have concrete answers (mine: "a Monday 8am timer; a written report in the Issues tab"); hype has vibes. *"Where can I see the log?"* — real agent work leaves an auditable trail; if you can't inspect it, be skeptical. *"What does the human still approve?"* — anyone claiming full autonomy with no human checkpoint is either reckless or exaggerating. You'll notice "scanning Google's algorithm" fails question one — and now you know to translate it, not to be intimidated by it.

One last calibration: Lucas is real, current, and ahead of most local agencies — give him that. But nothing he described is beyond you, and after today, most of it is sitting in your GitHub-ready folder. The gap was never coding ability. It was vocabulary and a working example. Now you have both.

---

## Sources and further reading

**AEO / answer engines**

- [AEO: the comprehensive guide (CXL)](https://cxl.com/blog/answer-engine-optimization-aeo-the-comprehensive-guide/) — answer-first structure, schema, measurement
- [AEO for local businesses (Brandify)](https://brandify.io/blog/aeo-for-local-businesses/) — entity clarity, profiles, reviews, schema types
- [AEO best practices for 2026 (Position Digital)](https://www.position.digital/blog/answer-engine-optimization-best-practices/) and [HubSpot's AEO trends](https://blog.hubspot.com/marketing/answer-engine-optimization-trends)
- [Should you create llms.txt? Google's 2026 guidance explained](https://www.getpassionfruit.com/blog/should-i-create-an-llms.txt-file-google-s-2026-guidance-explained) — the honest verdict
- [AI crawlers explained: GPTBot, ClaudeBot, PerplexityBot](https://www.anagram.ai/blog/ai-crawlers-explained-gptbot-claudebot-perplexitybot-and-how-to-let-them-in-2026) and [robots.txt for AI crawlers](https://pixis.ai/blog/robots-txt-for-ai-crawlers-gptbot-perplexitybot-geo-audit/)

**Building and agents**

- [The Official Wix MCP Server](https://www.wix.com/studio/developers/mcp-server) and [About the Wix MCP](https://dev.wix.com/docs/sdk/articles/use-the-wix-mcp/about-the-wix-mcp) — how AI manages Wix sites without touching the editor
- [Introducing the Wix MCP Server](https://www.wix.com/press-room/home/post/introducing-the-wix-model-context-protocol-mcp-server-for-seamless-ai-driven-web-app-development) — Wix's announcement
- [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions) — official docs for AI agents in GitHub
- [Scheduled Claude Code automation with GitHub Actions](https://smartscope.blog/en/ai-development/claude-code-scheduled-automation-guide/) — the cron-agent pattern
- [AI Agents for SEO: agentic SEO workflows](https://www.lyzr.ai/blog/ai-agents-for-seo/) — the industry playbook
- [The 8 Best AI SEO Agents in 2026](https://nightwatch.io/blog/best-ai-seo-agents/) and [what they actually automate](https://fixaeo.com/blogs/best-ai-seo-agents/) — the competitive landscape
- [How to build an SEO AI agent, with 7 workflows](https://www.tryanalyze.ai/blog/how-to-build-an-seo-ai-agent) — more agent recipes
- [How to make a website with Claude](https://www.wix.com/blog/how-to-make-a-website-with-claude) — Wix's own guide
- [Building websites with Claude Code](https://leonfurze.com/2026/02/14/building-websites-with-claude-code/) and [Claude Code workflows in 2026](https://medium.com/data-science-collective/effective-claude-code-workflows-in-2026-what-changed-and-what-works-now-c93ebc6f8f50) — practitioner walkthroughs
- [How an agency runs on Claude Code](https://rsla.io/blog/claude-code-marketing-agency-workflow) — an agency's own account
