#!/usr/bin/env python3
"""
SEO + AEO Site Auditor — the "scanning" half of your agent team.

This is a real, working audit script. It checks a page for the on-page
factors that matter most for local businesses — both classic SEO
(ranking in Google) and AEO / answer engine optimization (being the
answer that AI assistants like ChatGPT, Claude, Perplexity, and
Google's AI Overviews give when someone asks "best spa near me").
It then writes a markdown report. In the GitHub workflow, an AI agent
(Claude) reads this report, explains it in plain English, and files it
as a GitHub Issue with recommended fixes.

Usage:
    python3 scripts/audit.py docs/index.html           # audit a local file
    python3 scripts/audit.py https://example.com/       # audit a live URL

No external packages needed — pure Python standard library.
"""

import json
import re
import sys
import urllib.request
from html.parser import HTMLParser


class PageParser(HTMLParser):
    """Walks the HTML and collects everything the audit needs."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self._in_jsonld = False
        self.meta = {}            # name/property -> content
        self.h1s = []
        self._in_h1 = False
        self.jsonld_blocks = []
        self.images = []          # list of (src, alt-or-None)
        self.links_internal = 0
        self.links_external = 0
        self.canonical = None
        self.has_viewport = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
            self.h1s.append("")
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
            if (a.get("name") or "").lower() == "viewport":
                self.has_viewport = True
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld = True
            self.jsonld_blocks.append("")
        elif tag == "img":
            self.images.append((a.get("src", ""), a.get("alt")))
        elif tag == "a":
            href = a.get("href", "")
            if href.startswith("http"):
                self.links_external += 1
            elif href and not href.startswith(("#", "mailto:", "tel:")):
                self.links_internal += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag == "script":
            self._in_jsonld = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1 and self.h1s:
            self.h1s[-1] += data
        if self._in_jsonld and self.jsonld_blocks:
            self.jsonld_blocks[-1] += data


def load(source: str) -> str:
    if source.startswith(("http://", "https://")):
        req = urllib.request.Request(source, headers={"User-Agent": "SEO-Audit-Agent/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", errors="replace")
    with open(source, encoding="utf-8") as f:
        return f.read()


def check_ai_access(base_url: str, warns: list, passes: list, notes: list):
    """AEO checks that only make sense against a LIVE site:
    is the site letting AI assistants' crawlers in, and does it offer
    an llms.txt guide for AI agents?"""
    from urllib.parse import urlparse
    parts = urlparse(base_url)
    root = f"{parts.scheme}://{parts.netloc}"

    # --- robots.txt: are AI crawlers blocked? ---
    # If these bots are blocked, the business is invisible to the AI
    # assistants a growing share of customers ask for recommendations.
    ai_bots = ["GPTBot", "OAI-SearchBot", "ClaudeBot", "anthropic-ai",
               "PerplexityBot", "Google-Extended"]
    try:
        robots = load(root + "/robots.txt")
        blocked = []
        current_agents = []
        for line in robots.splitlines():
            line = line.split("#")[0].strip()
            if line.lower().startswith("user-agent:"):
                current_agents.append(line.split(":", 1)[1].strip())
            elif line.lower().startswith("disallow:"):
                path = line.split(":", 1)[1].strip()
                if path == "/":
                    for agent in current_agents:
                        for bot in ai_bots:
                            if bot.lower() == agent.lower():
                                blocked.append(bot)
            elif not line:
                current_agents = []
        if blocked:
            warns.append(f"**robots.txt blocks AI crawlers: {', '.join(sorted(set(blocked)))}.** "
                         "Blocked bots can't read the site, so AI assistants are less likely to "
                         "recommend this business. Unblock them unless the client explicitly wants out.")
        else:
            passes.append("AEO: robots.txt does not block the major AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.).")
    except Exception:
        notes.append("Could not fetch robots.txt — if the site truly has none, crawlers default to full access (fine), but add one to be explicit.")

    # --- llms.txt: a curated guide for AI agents ---
    # Honest status (2026): Google says it ignores llms.txt, but Anthropic
    # recommends it, OpenAI publishes them, and Perplexity has been seen
    # reading them. It costs 20 minutes — cheap insurance, not a magic bullet.
    try:
        llms = load(root + "/llms.txt")
        if llms.strip():
            passes.append("AEO: llms.txt present — AI agents get a curated guide to the business.")
    except Exception:
        notes.append("No llms.txt found. Optional (Google ignores it) but Anthropic/OpenAI agent "
                     "tooling reads it — a 20-minute add for extra AI visibility.")


def audit(source: str):
    html = load(source)
    p = PageParser()
    p.feed(html)

    passes, warns, fails, notes = [], [], [], []

    # --- Title tag ---
    t = p.title.strip()
    if not t:
        fails.append("**Missing <title> tag.** This is the strongest on-page ranking signal. Add one: `Business | Service | Town, ST`.")
    elif len(t) > 60:
        warns.append(f"**Title is {len(t)} characters** (aim for ≤60 so Google doesn't cut it off): “{t}”")
    else:
        passes.append(f"Title tag present and a good length ({len(t)} chars): “{t}”")

    # --- Meta description ---
    d = p.meta.get("description", "").strip()
    if not d:
        fails.append("**Missing meta description.** It's your free ad copy on the Google results page. Add one under 160 characters with a clear offer.")
    elif len(d) > 160:
        warns.append(f"**Meta description is {len(d)} characters** (aim for ≤160): “{d[:80]}…”")
    else:
        passes.append(f"Meta description present and a good length ({len(d)} chars).")

    # --- H1 ---
    h1s = [h.strip() for h in p.h1s if h.strip()]
    if len(h1s) == 0:
        fails.append("**No H1 heading.** Every page needs exactly one H1 containing the main service + location.")
    elif len(h1s) > 1:
        warns.append(f"**{len(h1s)} H1 headings found** — use exactly one; demote the rest to H2.")
    else:
        passes.append(f"Exactly one H1: “{h1s[0][:80]}”")

    # --- Structured data (JSON-LD) ---
    types = []
    for block in p.jsonld_blocks:
        try:
            data = json.loads(block)
            items = data if isinstance(data, list) else [data]
            for item in items:
                t2 = item.get("@type")
                if t2:
                    types.extend(t2 if isinstance(t2, list) else [t2])
        except (json.JSONDecodeError, AttributeError):
            warns.append("**A JSON-LD block failed to parse** — broken structured data is invisible to Google. Validate at validator.schema.org.")
    if types:
        passes.append(f"Structured data found: {', '.join(types)}.")
        local_types = {"LocalBusiness", "ProfessionalService", "DaySpa", "Restaurant", "Store",
                       "HomeAndConstructionBusiness", "Plumber", "Electrician", "HVACBusiness",
                       "RoofingContractor", "LegalService", "Dentist", "MedicalBusiness",
                       "AutoRepair", "BeautySalon", "HealthAndBeautyBusiness", "FinancialService",
                       "RealEstateAgent", "TravelAgency", "FoodEstablishment", "ExerciseGym"}
        if not local_types.intersection(types) and "LocalBusiness" not in " ".join(types):
            warns.append("**No LocalBusiness-type schema detected.** For a local business this is the #1 upgrade — add name, address, phone, hours, and geo as JSON-LD.")
    else:
        fails.append("**No structured data (JSON-LD) at all.** This is how you speak directly to Google's machines and AI search. Most competitors are missing it — easy win.")

    # --- AEO: is the page built to BE the answer? ---
    # AI assistants and Google's AI Overviews lift answers from pages that
    # ask the question and answer it directly. FAQPage schema + real Q&A
    # text is the closest thing to raising your hand.
    if "FAQPage" in types:
        passes.append("AEO: FAQPage schema present — the page offers ready-made Q&As for AI answers and rich results.")
    else:
        warns.append("**AEO gap: no FAQPage schema.** Add a real FAQ section (the questions customers "
                     "actually call to ask) marked up as FAQPage — it's the closest thing to raising "
                     "your hand when an AI assembles an answer.")

    # Entity clarity: sameAs links tie the business to its profiles
    # (Google Business Profile, Yelp, Instagram...), which is how AI
    # systems confirm the business is real and reviewed.
    if '"sameAs"' in " ".join(p.jsonld_blocks) or "'sameAs'" in " ".join(p.jsonld_blocks):
        passes.append("AEO: schema includes sameAs profile links — strong entity signals for AI systems.")
    else:
        warns.append("**AEO gap: no `sameAs` links in the business schema.** Add links to the Google "
                     "Business Profile, Yelp, and social profiles so AI systems can verify the entity "
                     "and its reviews.")

    # --- Social sharing ---
    if p.meta.get("og:title") and p.meta.get("og:description"):
        passes.append("Open Graph tags present — the site will look right when shared on social.")
    else:
        warns.append("**Missing Open Graph tags** (og:title / og:description) — shared links will look broken or bare on Facebook/LinkedIn.")

    # --- Technical basics ---
    if p.canonical:
        passes.append(f"Canonical URL set: {p.canonical}")
    else:
        warns.append("**No canonical URL.** Add `<link rel=\"canonical\" ...>` to avoid duplicate-content confusion.")

    if p.has_viewport:
        passes.append("Mobile viewport tag present (site is mobile-friendly at the HTML level).")
    else:
        fails.append("**No viewport meta tag** — Google indexes mobile-first; this is a must-fix.")

    robots = p.meta.get("robots", "")
    if "noindex" in robots:
        fails.append("**Page is set to NOINDEX** — it is telling Google to ignore it entirely. Fix immediately unless intentional.")

    # --- Images ---
    missing_alt = [src for src, alt in p.images if alt is None or not alt.strip()]
    if p.images and missing_alt:
        warns.append(f"**{len(missing_alt)} of {len(p.images)} images missing alt text.** Alt text helps image search and accessibility.")
    elif p.images:
        passes.append(f"All {len(p.images)} images have alt text.")

    # --- Word count (thin content check) ---
    text = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>|<[^>]+>", " ", html)
    words = len(text.split())
    if words < 300:
        warns.append(f"**Thin content: ~{words} words.** Local pages generally need 300+ words of real, useful text to rank.")
    else:
        passes.append(f"Healthy content depth: ~{words} words on the page.")

    # Live-site-only AEO checks (robots.txt AI-crawler policy, llms.txt)
    if source.startswith(("http://", "https://")):
        check_ai_access(source, warns, passes, notes)

    return passes, warns, fails, notes


def main():
    source = sys.argv[1] if len(sys.argv) > 1 else "docs/index.html"
    passes, warns, fails, notes = audit(source)

    score = round(100 * len(passes) / max(1, len(passes) + len(warns) + len(fails)))
    lines = [f"# SEO + AEO Audit Report", "", f"**Page:** `{source}`", f"**Health score: {score}/100** — {len(passes)} passing · {len(warns)} warnings · {len(fails)} critical", ""]
    if fails:
        lines += ["## 🔴 Critical — fix these first", ""] + [f"- {x}" for x in fails] + [""]
    if warns:
        lines += ["## 🟡 Warnings — worth fixing", ""] + [f"- {x}" for x in warns] + [""]
    if passes:
        lines += ["## 🟢 Passing", ""] + [f"- {x}" for x in passes] + [""]
    if notes:
        lines += ["## ℹ️ Notes (optional improvements)", ""] + [f"- {x}" for x in notes] + [""]

    report = "\n".join(lines)
    print(report)
    with open("audit-report.md", "w", encoding="utf-8") as f:
        f.write(report)
    print("\n(Report saved to audit-report.md)", file=sys.stderr)


if __name__ == "__main__":
    main()
