# 🚀 AI Agency Starter Kit

This folder is a complete, working copy of the setup Lucas described:
a professional local-business website plus **two AI agents that live in
GitHub and talk to each other** — one scans the site, one watches for
Google algorithm changes.

You do not need to know how to code. You need about 30 minutes and the
ability to follow numbered steps.

## What's in the box

```
ai-agency-starter-kit/
├── PLAYBOOK.md                     ← THE playbook: strategy, AEO, selling,
│                                     your punch list. Read this first.
├── docs/
│   ├── index.html                  ← THE NEW CORCORANPR.COM (your rebuilt site!)
│   ├── assets/
│   │   ├── site.css                ← The shared stylesheet. The brand palette
│   │   │                             lives here and ONLY here.
│   │   └── site.js                 ← Shared behaviour (the mobile menu)
│   ├── services/                   ← One page per service, all linked from
│   │   ├── web-design/               the homepage cards and the footer
│   │   ├── seo/                      (SEO also owns AEO + content marketing)
│   │   ├── google-ads/
│   │   ├── social-media-marketing/
│   │   └── lead-generation/
│   ├── llms.txt                    ← AI-agent guide to your business (AEO)
│   ├── robots.txt                  ← Welcomes search + AI crawlers (AEO)
│   └── sitemap.xml                 ← Table of contents for crawlers
├── templates/
│   ├── spa-local-business-template.html  ← The day-spa demo — your reusable
│   │                                 template for pitching local businesses
│   └── service-page-template.html  ← Start here to add a service page.
│                                     See the checklist in PLAYBOOK.md Part 4.
├── scripts/
│   ├── audit.py                    ← The SEO + AEO scanner (15+ checks).
│   │                                 Scores EVERY page of the site separately.
│   └── fetch_seo_news.py           ← Pulls Google/AI-search news from 4 trusted sources
├── agents/
│   ├── site-auditor.md             ← Agent 1's job description (plain English — edit it!)
│   └── google-watcher.md           ← Agent 2's job description
└── .github/workflows/
    ├── site-audit-agent.yml        ← Runs Agent 1 every Monday morning
    └── google-watch-agent.yml      ← Runs Agent 2 every day
```

The first thing to do: **double-click `docs/index.html`** and look at your
new site. Then open it in a text editor and read the comments marked
`WHY:` (the SEO/AEO course hiding inside the page) and `[CONFIRM]` (the
handful of facts only you can verify or decide — a named testimonial,
headshots, whether to add a street address for local-pack visibility).

## Setup (about 30 minutes, one time)

### 1. Create a free GitHub account
Go to [github.com](https://github.com) → Sign up. GitHub is where your
sites and agents will live. Free plan is all you need.

### 2. Create a repository (a "repo" = a project folder in the cloud)
Click the **+** in the top-right → **New repository** → name it
`my-first-ai-site` → set it to **Public** → **Create repository**.

### 3. Upload this kit
On your new repo's page: **Add file → Upload files**, then drag the
*contents* of this folder (not the folder itself) into the box and click
**Commit changes**.

> **Mac tip:** the `.github` folder is hidden by default. In Finder, press
> **Cmd + Shift + .** (period) to reveal hidden folders so it gets dragged
> along with everything else. On Windows it's visible normally.
>
> **The pro move:** once you install [Claude Code](https://code.claude.com)
> later, you'll just say *"push this folder to a new GitHub repo"* and it
> does all of this for you. That's the actual workflow Lucas uses.

### 4. Give your agents a brain (API key)
The agents think using Claude, which needs an API key (like a prepaid
phone card for AI):

1. Go to [console.anthropic.com](https://console.anthropic.com) → sign up
   → **API Keys** → **Create key**. Copy it. Add $5–10 of credit.
2. In your GitHub repo: **Settings → Secrets and variables → Actions →
   New repository secret**.
3. Name: `ANTHROPIC_API_KEY` · Value: paste the key → **Add secret**.

### 5. Turn on your live website (free hosting!)
In the repo: **Settings → Pages** → under "Build and deployment" choose
**Deploy from a branch** → branch `main`, folder `/docs` → **Save**.
Two minutes later your site is live at
`https://YOUR-USERNAME.github.io/my-first-ai-site/`.

### 6. Wake up the agents
Go to the **Actions** tab → click **"Agent: Site Auditor (weekly)"** →
**Run workflow** → **Run workflow** (green button). Wait ~2 minutes,
then open the **Issues** tab. Your first AI-written SEO report is
sitting there. Do the same for the Google Watcher.

From now on they run themselves: the Watcher every morning, the Auditor
every Monday — even while you sleep. **The Issues tab is where you watch
your agents talk to each other**: the Watcher files `google-update`
alerts; the Auditor reads them and folds them into its Monday report.

## Pointing the auditor at a real (live) site

**Settings → Secrets and variables → Actions → Variables tab → New
repository variable**: Name `SITE_URL`, value `https://corcoranpr.com/`.
The Monday audit will scan your LIVE site instead of the copy in this
repo — set this on day one so the auditor benchmarks the old WordPress
site, and you get a before/after story once the new site goes live.
This works on ANY site — including a prospect's site. (Audit a prospect,
send them the report, close the deal.)

## Going live on corcoranpr.com (when you're ready — not day one)

The new site previews free at your GitHub Pages address first. Live it
with, tweak it, and only then cut over. When you're ready:

1. **Don't touch anything else yet.** Your old WordPress site stays up
   and untouched throughout; there is no downtime moment.
2. In the repo: **Settings → Pages → Custom domain** → enter
   `corcoranpr.com` → Save. GitHub shows you the DNS records it needs.
3. At your domain registrar (wherever corcoranpr.com is registered),
   update ONLY the web records (A / CNAME) as GitHub instructs.
   **Do not change MX records — those are your email.** greg@corcoranpr.com
   keeps working untouched.
4. Check "Enforce HTTPS" once GitHub offers it (minutes to an hour).
5. **Redirects matter:** your old blog posts and pages have Google
   equity. Before cutover, list the old URLs that get traffic and either
   keep them (export the posts into the new site as pages) or 301-redirect
   them. Paste the old URL list into Claude and ask it to generate the
   redirect setup — this is a 20-minute AI job, not a weekend.

If any of this feels hairy, it's a perfect first Claude Code task:
"Here's my repo and my registrar — walk me through the cutover."

## What this costs

GitHub: **$0** (free tier includes 2,000 minutes/month of agent runtime;
this kit uses roughly 30). Claude API: **pennies per run** — a few
dollars a month for both agents. Hosting: **$0** on GitHub Pages.

## When something breaks

Open the failed run in the **Actions** tab, click the red step, copy the
error text, and paste it into Claude with: *"This GitHub Action failed
with this error. Fix my workflow file."* That is the entire skill of
debugging in 2026 — knowing what to paste and what to ask. (Versions of
actions change over time; Claude will update the YAML for you.)

## Built for AEO, not just SEO

SEO gets you ranked when someone *searches*. **AEO (answer engine
optimization)** gets you *recommended* when someone asks ChatGPT, Claude,
Perplexity, or Google's AI a question like "best day spa near Ridgewood."
This kit covers both. The demo site carries the AEO signals (FAQ content
with FAQPage schema, `sameAs` entity links, `robots.txt` that welcomes AI
crawlers, an `llms.txt` guide for AI agents), the auditor scores AEO
checks on every scan, and the Google Watcher tracks answer-engine changes
— not just Google's. One honest note: Google has said its AI features
ignore `llms.txt`, while Anthropic and OpenAI tooling uses it — it's
20-minute insurance, not magic. The parts no script can do for a client:
a fully filled-out Google Business Profile, steady reviews, and identical
name/address/phone everywhere. That's human work — bill for it.

## Make it yours

- Edit `agents/site-auditor.md` and `agents/google-watcher.md` — they're
  plain English. That IS the programming.
- Replace `docs/index.html` with a real client's site.
- Ask Claude to add a third agent — a content writer that drafts a
  monthly blog post as a pull request for your review. Same pattern:
  a schedule, a script, a job description, an Issue.
  
