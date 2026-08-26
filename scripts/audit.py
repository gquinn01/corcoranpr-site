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

The site is no longer one page, so this audits EVERY page and scores
each one separately. A single page dragging the site down is visible by
name in the summary table instead of being averaged away.

Usage:
    python3 scripts/audit.py                           # every page under docs/
    python3 scripts/audit.py docs/index.html           # one local file
    python3 scripts/audit.py docs/services/seo/        # a folder
    python3 scripts/audit.py https://example.com/      # a live site, expanded
                                                       # via its sitemap.xml
    python3 scripts/audit.py --strict                  # exit 1 if any page < 100

No external packages needed — pure Python standard library.
"""

import argparse
import glob
import json
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urlparse

# The live site's page list comes from its own sitemap. Locally we glob
# the folder that IS the live site.
SITE_DIR = "docs"
SITEMAP_PATH = os.path.join(SITE_DIR, "sitemap.xml")
LLMS_PATH = os.path.join(SITE_DIR, "llms.txt")

# The NAP phone and email, in the formats they could plausibly be typed.
# Every visible mention of either is meant to be tappable: a reader on a
# phone should never have to memorize a number and retype it in the
# dialer. Mentions inside JSON-LD are data, not copy, and are skipped.
NAP_PHONE_RE = re.compile(r"\(?215\)?[\s.\-]?259[\s.\-]?8304")
NAP_EMAIL_RE = re.compile(r"greg@corcoranpr\.com")


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
        self.contacts_linked = 0  # phone/email mentions inside tel:/mailto:
        self.contacts_bare = []   # (line, kind) for the ones that are not
        self._href_stack = []     # open <a> hrefs, innermost last
        self._skip_depth = 0      # inside <script>/<style>
        # Visible FAQ items, as (question, answer) of rendered text. The
        # house rule is that each one is byte-identical to its schema
        # twin, so this collects what a reader sees and the FAQ mirror
        # check compares it against the FAQPage node.
        self.faq_visible = []
        self._details_depth = 0
        self._in_summary = False
        self._in_faq_answer = False
        self._faq_q = None
        self._faq_a = None
        self._skip_faq_ico = 0    # the chevron <span>, art with no words

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self._skip_depth += 1
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
        elif tag == "details":
            self._details_depth += 1
            self._faq_q, self._faq_a = None, None
        elif tag == "summary" and self._details_depth:
            self._in_summary = True
            self._faq_q = ""
        elif tag == "span" and self._in_summary and "faq-ico" in (a.get("class") or ""):
            self._skip_faq_ico += 1
        elif tag == "p" and self._details_depth and self._faq_a is None:
            self._in_faq_answer = True
            self._faq_a = ""
        elif tag == "a":
            href = a.get("href", "")
            self._href_stack.append(href)
            if href.startswith("http"):
                self.links_external += 1
            elif href and not href.startswith(("#", "mailto:", "tel:")):
                self.links_internal += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag == "summary":
            self._in_summary = False
        elif tag == "span" and self._skip_faq_ico:
            self._skip_faq_ico -= 1
        elif tag == "p" and self._in_faq_answer:
            self._in_faq_answer = False
        elif tag == "details":
            if self._details_depth:
                self._details_depth -= 1
            if self._faq_q is not None:
                self.faq_visible.append((self._faq_q.strip(), (self._faq_a or "").strip()))
            self._faq_q, self._faq_a = None, None
        elif tag == "a":
            if self._href_stack:
                self._href_stack.pop()
        elif tag == "script":
            self._in_jsonld = False
        if tag in ("script", "style") and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1 and self.h1s:
            self.h1s[-1] += data
        if self._in_jsonld and self.jsonld_blocks:
            self.jsonld_blocks[-1] += data
        if self._in_summary and not self._skip_faq_ico and self._faq_q is not None:
            self._faq_q += data
        if self._in_faq_answer and self._faq_a is not None:
            self._faq_a += data
        if self._skip_depth:
            return
        linked = any(h.startswith(("tel:", "mailto:")) for h in self._href_stack)
        for kind, rx in (("phone", NAP_PHONE_RE), ("email", NAP_EMAIL_RE)):
            for _ in rx.finditer(data):
                if linked:
                    self.contacts_linked += 1
                else:
                    self.contacts_bare.append((self.getpos()[0], kind))


def load(source: str) -> str:
    if source.startswith(("http://", "https://")):
        req = urllib.request.Request(source, headers={"User-Agent": "SEO-Audit-Agent/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", errors="replace")
    with open(source, encoding="utf-8") as f:
        return f.read()


def is_url(source: str) -> bool:
    return source.startswith(("http://", "https://"))


def check_ai_access(base_url: str, warns: list, passes: list, notes: list):
    """AEO checks that only make sense against a LIVE site:
    is the site letting AI assistants' crawlers in, and does it offer
    an llms.txt guide for AI agents?

    These are properties of the SITE, not of any one page, so they run
    once per run and are reported in their own section. Running them per
    page would just refetch the same two files five more times."""
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


def audit(source: str, coverage: dict = None):
    """Scores one page. `coverage` carries the parsed sitemap.xml and
    llms.txt for local runs, so a page that was built but never published
    into either file gets caught here rather than by a customer."""
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
    faq_nodes = []            # every FAQPage node found, for the mirror check
    for block in p.jsonld_blocks:
        try:
            data = json.loads(block)
            items = data if isinstance(data, list) else [data]
            # A page that describes several things at once (a business, a
            # service, a breadcrumb, an FAQ) puts them in an @graph so they
            # can reference each other by @id. Unwrap it, or every node
            # inside is invisible and the page looks like it has no schema
            # at all. Most modern CMS sites emit one, so this matters when
            # auditing a prospect's site too.
            unwrapped = []
            for item in items:
                graph = item.get("@graph") if isinstance(item, dict) else None
                if graph:
                    unwrapped.extend(graph if isinstance(graph, list) else [graph])
                else:
                    unwrapped.append(item)
            for item in unwrapped:
                t2 = item.get("@type")
                if t2:
                    types.extend(t2 if isinstance(t2, list) else [t2])
                    if "FAQPage" in (t2 if isinstance(t2, list) else [t2]):
                        faq_nodes.append(item)
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

    # --- FAQ mirror: does the schema say what the page says? ---
    # Assistants and rich results quote acceptedAnswer, not the visible
    # copy, so the two drifting apart means the machines are handing out a
    # sentence the reader never sees. The house rule is that each visible
    # question and answer is byte-identical to its schema twin: edit one,
    # edit both. Runs on parsed page text, so it works the same against a
    # local file or a fetched live URL.
    schema_faq = []
    for node in faq_nodes:
        entities = node.get("mainEntity") or []
        for q in entities if isinstance(entities, list) else [entities]:
            if not isinstance(q, dict):
                continue
            ans = q.get("acceptedAnswer") or {}
            schema_faq.append((str(q.get("name", "")).strip(),
                               str(ans.get("text", "")).strip() if isinstance(ans, dict) else ""))
    if schema_faq and not p.faq_visible:
        # Schema but nothing this check can read. On our pages that means
        # the FAQ section is gone; on a prospect's it usually means their
        # FAQ is built from divs we do not recognize. Not worth scoring a
        # stranger's site down for markup we simply cannot see, so it says
        # so and stops.
        notes.append(f"{len(schema_faq)} FAQ question(s) in FAQPage schema, but no visible "
                     f"<details>/<summary> FAQ was found to compare them against. Either the "
                     f"page's FAQ is missing, or it is built with markup this check does not read.")
    elif p.faq_visible and not schema_faq:
        # The AEO check above already warns that FAQPage schema is absent,
        # and that warning is itself a scoring defect. Saying it again per
        # question would punish one mistake several times over.
        pass
    elif schema_faq or p.faq_visible:
        by_schema = dict(schema_faq)
        by_page = dict(p.faq_visible)
        only_schema = [q for q in by_schema if q not in by_page]
        only_page = [q for q in by_page if q not in by_schema]
        mismatched = [q for q in by_schema if q in by_page and by_schema[q] != by_page[q]]

        # One on each side is almost always the same item with its
        # question edited in one place only. Say that, rather than
        # reporting it twice as two unrelated absences.
        if len(only_schema) == 1 and len(only_page) == 1:
            fails.append(
                f"**FAQ question text differs between the page and its schema.** "
                f"Schema asks “{only_schema[0][:90]}”, the page asks “{only_page[0][:90]}”. "
                f"Each question must be byte-identical in both: edit one, edit both.")
            only_schema, only_page = [], []
        for q in only_schema:
            fails.append(f"**FAQ in schema but not on the page: “{q[:90]}”.** "
                         f"Schema promising an answer the reader never sees is the kind of thing "
                         f"Google penalizes as mismatched structured data. Add it or drop it.")
        for q in only_page:
            fails.append(f"**FAQ on the page but not in schema: “{q[:90]}”.** "
                         f"It cannot be quoted by AI answers or rich results until it is in the "
                         f"FAQPage node.")
        for q in mismatched:
            fails.append(f"**FAQ answer does not match its schema: “{q[:70]}”.** "
                         f"The page says “{by_page[q][:80]}…” and the schema says "
                         f"“{by_schema[q][:80]}…”. Assistants quote the schema, so this is the "
                         f"sentence being handed out instead of yours. Edit one, edit both.")
        if not (only_schema or only_page or mismatched) and schema_faq:
            passes.append(f"All {len(schema_faq)} FAQ questions and answers are byte-identical "
                          f"between the visible page and the FAQPage schema.")

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
    # The 160-character ceiling on og:description is a HOUSE RULE, not a
    # standard. Open Graph itself sets no limit, and the networks all cut
    # at different points (and move the goalposts), so nobody can tell you
    # the "correct" length. What we can do is keep one number in the head
    # of every page: the meta description is capped at 160 above, and the
    # two descriptions are usually near-copies of each other, so letting
    # og: run longer just means the pair drifts apart. A NOTE, not a
    # warning and never a critical: notes are the one bucket score_of()
    # does not count, which is right for a rule we invented. An over-long
    # og:description still shares fine, so it should never be the reason
    # a page drops off 100. The missing-tags case below stays a warning,
    # because that one is a real defect.
    og_d = p.meta.get("og:description", "").strip()
    if not (p.meta.get("og:title") and og_d):
        warns.append("**Missing Open Graph tags** (og:title / og:description) — shared links will look broken or bare on Facebook/LinkedIn.")
    else:
        passes.append(f"Open Graph tags present ({len(og_d)}-char og:description) — the site will look right when shared on social.")
        if len(og_d) > 160:
            notes.append(f"og:description is {len(og_d)} characters, past the 160 the meta description keeps. House consistency rule, not a spec: trim it when convenient, preserving the promises over the connectives. “{og_d[:80]}…”")

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

    # --- Tappable phone and email ---
    # A bare number in body copy is a number the reader has to memorize
    # and retype. Every visible mention should be a tel:/mailto: link, so
    # a phone reader taps once. Silent regression is the real risk here:
    # this is the kind of thing that gets missed when a new FAQ answer or
    # card is written, which is exactly why it is checked on every page.
    if p.contacts_bare:
        where = ", ".join(f"line {ln} ({kind})" for ln, kind in p.contacts_bare[:5])
        warns.append(f"**{len(p.contacts_bare)} phone/email mention(s) not linked** ({where}). "
                     "Wrap each one so it is tappable on a phone: "
                     "`<a href=\"tel:+12152598304\">215-259-8304</a>` or "
                     "`<a href=\"mailto:greg@corcoranpr.com\">greg@corcoranpr.com</a>`.")
    elif p.contacts_linked:
        passes.append(f"All {p.contacts_linked} phone/email mentions are tappable tel:/mailto: links.")

    # --- Word count (thin content check) ---
    text = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>|<[^>]+>", " ", html)
    words = len(text.split())
    if words < 300:
        warns.append(f"**Thin content: ~{words} words.** Local pages generally need 300+ words of real, useful text to rank.")
    else:
        passes.append(f"Healthy content depth: ~{words} words on the page.")

    # --- Published where crawlers can find it ---
    # A page that exists but is in neither sitemap.xml nor llms.txt is a
    # page Google and the AI assistants may never discover. On a live run
    # this is moot: the page list came FROM the sitemap.
    if coverage is not None and p.canonical:
        canon = p.canonical.strip()
        if canon in coverage["sitemap_locs"]:
            passes.append(f"Listed in sitemap.xml, so crawlers get pointed at it: {canon}")
        else:
            fails.append(f"**Not listed in `docs/sitemap.xml`.** The page is live at {canon} but "
                         "the sitemap never mentions it, so Google has to stumble on it. Add a "
                         "`<url>` block with today's date.")
        # Word-boundary match: without it, the homepage's canonical would
        # match any deeper URL that starts with it and always "pass".
        if re.search(re.escape(canon) + r"(?![\w/.\-])", coverage["llms_text"]):
            passes.append("AEO: listed in llms.txt, so AI agents get a guided route to the page.")
        else:
            warns.append(f"**Not listed in `docs/llms.txt`.** Add {canon} under `## Key pages` so "
                         "AI assistants reading the guide know this page exists.")

    return passes, warns, fails, notes


def score_of(n_pass: int, n_warn: int, n_fail: int) -> int:
    """Unchanged formula: the share of checks that passed. Notes are free."""
    return round(100 * n_pass / max(1, n_pass + n_warn + n_fail))


def expand_sitemap(url: str):
    """A live site's page list comes from its own sitemap. If that can't
    be read we still audit the URL we were given, and say why."""
    parts = urlparse(url)
    root = f"{parts.scheme}://{parts.netloc}"
    try:
        xml = load(root + "/sitemap.xml")
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
        if locs:
            return sorted(set(locs)), None
        return [url], (f"{root}/sitemap.xml has no <loc> entries, so only the page you named "
                       "was audited.")
    except Exception:
        return [url], (f"Could not read {root}/sitemap.xml, so only the page you named was "
                       "audited. Add a sitemap so every page gets scanned.")


def resolve_targets(args):
    """No arguments audits the whole site. Paths, folders and URLs all work."""
    if not args:
        return sorted(glob.glob(os.path.join(SITE_DIR, "**", "*.html"), recursive=True)), None
    if len(args) == 1 and is_url(args[0]):
        return expand_sitemap(args[0])
    targets = []
    for a in args:
        if is_url(a) or os.path.isfile(a):
            targets.append(a)
        elif os.path.isdir(a):
            targets.extend(sorted(glob.glob(os.path.join(a, "**", "*.html"), recursive=True)))
        else:
            targets.append(a)   # let it fail loudly with a real filename
    return targets, None


def local_coverage():
    """Reads sitemap.xml and llms.txt once, for the two publish checks."""
    try:
        with open(SITEMAP_PATH, encoding="utf-8") as f:
            sitemap = f.read()
        with open(LLMS_PATH, encoding="utf-8") as f:
            llms = f.read()
    except OSError:
        return None
    return {
        "sitemap_locs": set(re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", sitemap)),
        "llms_text": llms,
    }


def section(title: str, items: list, level: str = "###") -> list:
    return [f"{level} {title}", ""] + [f"- {x}" for x in items] + [""] if items else []


def main():
    ap = argparse.ArgumentParser(
        description="Audit every page of the site for SEO and AEO, scoring each one.")
    ap.add_argument("targets", nargs="*",
                    help="Files, folders or a live URL. Default: every .html under docs/")
    ap.add_argument("--strict", action="store_true",
                    help="Exit 1 if any page scores under 100. Use it in a build gate.")
    opts = ap.parse_args()

    targets, expand_note = resolve_targets(opts.targets)
    if not targets:
        print(f"No HTML pages found under {SITE_DIR}/.", file=sys.stderr)
        return 1

    live = [t for t in targets if is_url(t)]
    coverage = None if live else local_coverage()

    results = []
    for t in targets:
        # One unreadable page must never take the whole run down with it.
        # load() reaches the network for a live URL, and every network
        # error is an exception: DNS, TLS, timeout, 500, a redirect loop.
        # Uncaught, that ends the process with a traceback, no report file
        # is written, and the weekly agent has nothing to read — which is
        # exactly how the 2026-08-17 scheduled run died on a transient DNS
        # failure at the runner. A page we cannot read is a finding, so
        # record it as a critical against that page and keep going.
        try:
            passes, warns, fails, notes = audit(t, coverage=None if is_url(t) else coverage)
        except Exception as e:
            passes, warns, notes = [], [], []
            fails = [f"**Could not read this page** ({type(e).__name__}: {e}). "
                     "For a live URL that usually means the site or the network was "
                     "unreachable when the scan ran, not that the page is broken. "
                     "Re-run before acting on it."]
        results.append({"source": t, "passes": passes, "warns": warns,
                        "fails": fails, "notes": notes,
                        "score": score_of(len(passes), len(warns), len(fails))})

    # Site-wide AEO checks run once, against the live site only.
    site_passes, site_warns, site_notes = [], [], []
    if live:
        check_ai_access(live[0], site_warns, site_passes, site_notes)
    if expand_note:
        site_notes.append(expand_note)

    total_pass = sum(len(r["passes"]) for r in results) + len(site_passes)
    total_warn = sum(len(r["warns"]) for r in results) + len(site_warns)
    total_fail = sum(len(r["fails"]) for r in results)
    site_score = score_of(total_pass, total_warn, total_fail)
    perfect = [r for r in results if r["score"] == 100]

    lines = [
        "# SEO + AEO Audit Report", "",
        f"**Site score: {site_score}/100** — {len(perfect)} of {len(results)} "
        f"{'page' if len(results) == 1 else 'pages'} at 100/100",
        f"**{total_pass} passing · {total_warn} warnings · {total_fail} critical** across the site",
        "",
        "| Page | Score | Passing | Warnings | Critical |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        flag = "" if r["score"] == 100 else " ⚠️"
        lines.append(f"| `{r['source']}` | {r['score']}/100{flag} | {len(r['passes'])} | "
                     f"{len(r['warns'])} | {len(r['fails'])} |")
    lines.append("")

    if site_passes or site_warns or site_notes:
        lines += ["## Site-wide", ""]
        lines += section("🟡 Warnings — worth fixing", site_warns)
        lines += section("🟢 Passing", site_passes)
        lines += section("ℹ️ Notes (optional improvements)", site_notes)

    for r in results:
        lines += [f"## Page: `{r['source']}` — {r['score']}/100", ""]
        lines += section("🔴 Critical — fix these first", r["fails"])
        lines += section("🟡 Warnings — worth fixing", r["warns"])
        lines += section("🟢 Passing", r["passes"])
        lines += section("ℹ️ Notes (optional improvements)", r["notes"])

    report = "\n".join(lines)
    print(report)
    with open("audit-report.md", "w", encoding="utf-8") as f:
        f.write(report)
    print("\n(Report saved to audit-report.md)", file=sys.stderr)

    below = [r for r in results if r["score"] < 100]
    if below:
        print(f"{len(below)} page(s) under 100/100: "
              + ", ".join(r["source"] for r in below), file=sys.stderr)
    return 1 if (opts.strict and below) else 0


if __name__ == "__main__":
    sys.exit(main())
