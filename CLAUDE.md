# Corcoran Communications — standing orders

## Brand (decided 2026-08-10 — "Strategic Growth" palette; do not drift)
- Midnight #082A4A — dark panels (header, hero, bands, footer) and
  heading text on light backgrounds.
- Signal Blue #0B6BD3 — section titles, links, and hover states, on light
  backgrounds only. On Midnight panels it drops to 2.82:1 and becomes
  unreadable, so links there use Fresh Mint (footer) or white (contact
  band). Never put Signal Blue text on a dark panel.
- Growth Green #15B77E — buttons/CTAs and success markers ONLY, always
  with dark text (#062018) on green fills. Use #0E7A55 for small green
  text on light backgrounds (contrast).
- Buttons do NOT darken on hover. They leave green entirely and flip to a
  Fresh Mint fill with Midnight text, 12.91:1 (changed 2026-08-11 from the
  old Midnight fill). Darkening to #0E7A55 would put the mandated #062018
  text at 3.2:1, under the 4.5:1 bar, and #0E7A55 is a text color, not a
  fill. Do not "fix" this back to a green hover.
- The secondary (ghost) button hovers to a translucent white wash, NOT to
  a mint fill. Both buttons hovering to mint made primary and secondary
  identical on hover. Keep them distinct.
- Fresh Mint #DDF7EC — light accents: card top-borders, eyebrow text
  and labels on dark panels.
- Cloud #F3F8FC — page background. Cards stay white.
- Derived neutrals — the palette names no color for body text or borders,
  so these three fill the gap. They are working neutrals, not brand
  colors, and nothing else may be added to this list without a decision:
  #4A5A6A body and secondary text on light (7.1:1 on white), #D8E4EF
  hairline borders on light, #B6C9DD secondary text on Midnight (8.6:1).
  Never substitute a warm gray — it clashes with Cloud.
- Gradients are allowed on SECTION BACKGROUNDS ONLY (decided 2026-08-11,
  to get closer to the ServiceNow look). Everything else stays solid:
  text, buttons, cards, icon tiles, borders, logo art. Build every field
  from palette colors at low alpha over a solid palette base, so no new
  hex enters the system. Fade stops to rgba(color,0), never to
  `transparent` — some browsers interpolate that through black and smear
  gray. Always re-check contrast at the field's BRIGHTEST point, not
  against the base color: a background gradient can quietly push body
  text under 4.5:1, and #B6C9DD is the first thing to fail.
- Coral is RETIRED. The wordmark is image art (decided 2026-08-11),
  recolored from the old coral logo: docs/logo-light.png on light
  panels, docs/logo-dark.png on dark. There is no text wordmark and no
  interpunct any more — the color split between the two words IS the
  accent note. "Corcoran" carries the accent, Signal Blue on light and
  Fresh Mint on dark. "Communications" takes Midnight on light, white on
  dark. Signal Blue is 2.82:1 on Midnight, so it never carries the
  accent on a dark panel. Never render the mark in a single flat color.
- The old logo's tagline, "Public Relations • Event Coordination", is
  cropped out of both files and stays out unless those services are
  actually listed on the site. It is also illegible at wordmark size.
  The uncropped source is brand/logo-original-coral.png, and
  brand/README.md records the crop box and color mapping used to derive
  both live PNGs. Regenerate from there, never by hand.
- Voice: plain English, confident, no hype. Every claim ties to leads,
  calls, or revenue.
- The page speaks to the reader, never about itself: no remarks about
  our process, no arguing with competitors the reader did not raise.
  State the fact and stop.
- Above the fold, no industry jargon: no SEO, AEO, lead gen, or funnel.
  Trade terms live in service cards, FAQ, and schema. Hero copy must make
  sense to a reader who has never bought marketing.
- SERVICE-PAGE EXCEPTION (decided 2026-08-13). The rule above governs the
  HOMEPAGE hero, where the reader has not self-selected. On a service
  page, the reader arrived by searching that exact term, so the page's
  OWN primary keyword may appear above the fold in the title and H1, and
  nothing else may. The lead paragraph explains it in plain English, no
  other trade terms (no funnel, no CTR, no top-of-funnel), and AEO is
  always spelled out as "answer engine optimization" on first use.
  One keyword per page, its own, and no jargon creep beyond it.
- Titles: all five service pages use the same suffix,
  "| Corcoran Communications". Shorten the descriptive half, never the
  brand half, to stay under 60 characters.
- When body copy describes outcomes, use the concrete triad "phone
  calls, form fills, and booked jobs" (or a page-appropriate subset),
  never "leads" or "revenue" alone. Headlines may use "phone calls" for
  punch.
- The homepage proof section is "Industries We Know" (id #industries):
  six industry cards naming real clients. Nav and footer label it
  Industries. Industry cards gain links only when an earned industry
  page exists for them.
- Every industry or location page must pass the doorway test before it
  ships: it must contain substance a competitor without our client
  history could not write, be a genuine destination rather than a funnel
  to another page, and read for a human first. Pages are built one at a
  time from Greg's own experience, never in bulk. If a page fails this
  test, it does not ship.
- Industry pages are earned: built from real client experience, one at a
  time. Industry pages carry no client-attributed numbers or results
  without the client's written permission. Client names appear on
  industry pages only where the client relationship is itself the point,
  and only for clients already named publicly on the site. Trade schools
  shipped first.
- Service pages follow the template: hero with per-page graphic, plain
  English line, What You Get, differentiator band with icon tiles and
  CTA row, four-step How It Works, What It Costs with CTA row, Stronger
  Together, contact band, FAQ last. Phone CTAs are tel: links.
- CTA arrangement (decided 2026-08-21, reversing the 2026-08-16 change
  that sent buttons to the free audit page). Every button lands on a
  form; the explainer is reached by text link, not by button.
  - Every primary "Get Your Free AI Site Audit" button links to
    #contact, its own page's form. No exceptions, including the free
    audit page, whose buttons scroll to its own form as before.
  - The nav "Free Audit" item is the route to the free audit page from
    every other page. It points at docs/free-audit/ at the correct
    relative depth. On the free audit page itself it is href="./",
    matching how About is handled on the About page.
  - The footer Get Started column's "Free AI Site Audit" item is
    #contact, the page's own form, not a link to the free audit page
    (decided 2026-08-21). Get Started is a column of ways to start, so
    all three of its items now act: the form, the phone, the email.
    That leaves the nav item as the only cross-page route to the free
    audit page, which is the accepted cost of every button and footer
    CTA landing on a form.
  - "Free Audit" replaced "How It Works" in the nav on all 27 pages and
    the template. It is plain nav text like its siblings, not a button.
    "How It Works" keeps its footer Explore link everywhere, so the
    homepage section is still linked from every page.
  - No exit links next to any form. The fine print under the form stays
    phone and email only. A reader who has reached a form should have
    nothing to click but the form, the phone, or the email.
  - The free audit page remains the ads landing destination at cutover,
    which is why it keeps its own form and its own buttons pointing at
    it.
  - Ghost phone buttons stay tel: links, and the contact band on every
    page keeps its form.
  - The film and live entertainment page is the one exception to the
    audit CTA (decided 2026-08-26). It carries no audit button, no audit
    form, and no How It Works or What It Costs section, because
    production work is project-scoped to a run rather than sold as the
    audit, flat quote, month-to-month product. Its buttons and its
    footer Get Started item point at #contact, which is direct contact
    by phone and email.
- American spelling everywhere: center not centre, neighbor not
  neighbour, skeptical not sceptical, organized not organised. Applies
  to code comments too, not just site copy. (The British words in this
  rule are the examples, not a violation of it.)
- "near me" in copy is the phrase customers type, not a description
  of distance, so it takes quotes: they search 'near me' and let
  Google decide. Bare, it reads as "close to me" and the sentence
  turns to mush. Never paste a whole search query into a sentence
  as if the reader talks that way ("if you have been searching for
  a web designer near me" was live for a while and did not parse).
  Proximity is earned by naming the real towns and counties and by
  areaServed in the schema, not by planting the string in prose.
- No em dashes in site copy, ever, including schema text.

## Facts are sacred
- Never invent facts, numbers, years, reviews, or testimonials.
- Anything unverifiable gets flagged to Greg, not guessed.
- Two tenures exist and they are not interchangeable (recorded
  2026-08-21, after the firm's 26 years was found on three pages
  described as Greg's own). The FIRM has 26 years: Ruth Corcoran founded
  it in January 2000, and that is what the "26 years / In business" stat
  band on 19 pages counts. GREG has 10 years: he joined in September
  2016 to head sales and digital, and became owner in July 2023. Never
  give the firm's 26 years to Greg personally. The dates behind both
  numbers are on the About page timeline; check there before writing any
  experience claim.
- The firm's history is not the same as its services. It did public
  relations, design, content, and events from 2000, and only added
  digital, SEO, and lead generation in 2016. So "founded in 2000" is
  true anywhere, but "doing web design since 2000" is not. Do not date
  a service earlier than the year the firm started selling it.
- The agent roster, as of 2026-08-18, is FIVE agents plus scripts.
  SIXTH AGENT ADDED 2026-08-31, and it is INTERNAL: the Content Writer
  drafts one post a week for our own blog and files it as a pull
  request. It does no client work, so it is NOT part of the five in the
  canonical description below. The site still says five agents because
  five is what a client gets. If that ever reads as a contradiction, the
  fix is Greg's decision about the copy, not a quiet edit to the number.
  THE "NO CUSTOMER-FACING COPY" HALF OF THAT RULE IS LIFTED, in one
  place only (decided 2026-09-03). The blog index FAQ, "Who writes
  these?", now says plainly that an agent drafts each note and that Greg
  edits it and verifies every fact in it. Disclosing it is the honest
  answer to a question a reader actually asks, and it costs nothing: the
  answer carries no count, so the five-agent claims on the homepage and
  the About page still stand and still describe what a CLIENT gets. This
  does not reopen the door generally. No other page mentions the sixth
  agent, and nothing anywhere calls it the Content Writer, because the
  describe-agents-by-role rule above is untouched.
  Site agents: Site Auditor (weekly), Google Watcher (daily).
  Ads agents: Industry Watcher (weekly, sweeps Google Ads announcements
  and trade press), Account Watcher (weekly, reports on client ad
  accounts: pacing, waste, anomalies, tracking health), Strategist
  (weekly, reads the other reports and produces a tagged action plan).
  Plus automated watchdog scripts inside client ad accounts checking
  spend pacing and tracking daily. A human reviews and approves every
  change; nothing ships on a machine's say-so.
- Describe agents by role in customer-facing copy, not by name. The
  names above are internal. On the site an agent is "an auditor that
  scans your site every week", never "Site Auditor".
- CANONICAL AGENT DESCRIPTION, to reuse verbatim or paraphrase:
  "Two site agents: an auditor that scans the website every week, and a
  watcher that tracks Google and AI-search changes every morning. Three
  ads agents: one follows what Google Ads is changing, one reports on
  the client's account weekly, one turns the reports into a plan.
  On top of the five, automated watchdogs check ad spend and tracking
  daily. Greg approves every change."
  The two site agents do NOT both watch the website. One audits the
  site, the other watches the search world around it. Never write "two
  watch your website"; it is the imprecision this description exists to
  prevent.
- NAP (name/address/phone) must match everywhere exactly:
  Corcoran Communications, 1808 Enclave Dr, Quakertown, PA 18951,
  215-259-8304, greg@corcoranpr.com.
- The office municipality is MILFORD TOWNSHIP (recorded 2026-08-24).
  1808 Enclave Dr carries a Quakertown 18951 mailing address but sits
  in Milford Township, not Quakertown Borough. "Our office is in
  Quakertown" and the NAP stay exactly as they are: the postal city is
  correct and has to match everywhere. Never write that the office is
  in the borough, downtown, or on Broad Street, and never add Milford
  Township to the address block. "Upper Bucks" is always safe.

## Definition of done (every site change)
- Run: python3 scripts/audit.py — EVERY page must score 100/100, not just
  the one you touched. Add --strict to make the run exit nonzero when any
  page falls short. A single path still works for a quick spot check:
  python3 scripts/audit.py docs/services/seo/index.html
- Run: python3 scripts/test-sitemap-expansion.py — it must exit 0. Ten
  offline cases guarding how a live run reads somebody else's sitemap,
  which is the one input to the audit we do not write ourselves. No
  network, about a second, so it runs before EVERY commit with no
  conditions. It is not a site check and does not care what you edited:
  our own sitemap is a plain urlset that scores 100/100 whether that
  code is right or wrong, which is precisely why a green audit is no
  reason to skip it.
- Valid JSON-LD, title ≤60 chars, meta description ≤160, exactly one H1.
- Every <img> needs real alt text. The audit counts alt="" as missing
  and drops the score, so decorative-empty alt is not an option here.
- Accessible text (aria-labels, alt text) describes what is actually
  rendered; any edit to a visible element updates its accessible
  description in the same commit.
- After any shared-CSS change, the cascade analyzer in scripts/ should
  come back clean for component-vs-ancestor overrides.
- Mobile layout checks must use a true-viewport method (the iframe
  technique documented in scripts/); a headless-Chrome window
  screenshot below ~500px is not evidence of a layout defect.
- Show me the diff before committing. Commit messages in plain English.
- COMMENTS ARE LOAD-BEARING AND ARE AUDITED LIKE COPY (decided
  2026-09-03). A comment is where the next reader, human or agent,
  learns the rules, so a wrong one is not inert: it teaches. THE
  PRE-COMMIT DIFF REVIEW COVERS EVERY COMMENT ADJACENT TO A CHANGED
  LINE, not only the changed lines themselves, and a change that
  falsifies a nearby comment IS NOT DONE until that comment moves in
  the same commit. Nothing else catches this: scripts/audit.py does not
  read comments, and a stale one costs no points and breaks no page.
  TEMPLATE COMMENTS GET THE STRICTEST READING, because their errors
  reseed. A wrong instruction in templates/ is copied into every page
  built from it afterwards, and each of those pages looks correct on
  arrival, so one bad line becomes a drift nobody can date. Two shipped
  and both were found by a sweep rather than by a check:
  templates/service-page-template.html gave the proof line's separator
  as &middot; in BOTH of its documented defaults, when 24 of the 26 live
  pages carrying that refrain used the literal, so every page built by
  following the comment inherited the wrong spelling; and
  templates/blog-post-template.html said "Hero with no decorative art"
  eighteen lines above a hero that had art, which would have taught the
  next reader, or the content writer agent, to strip the graphic.
  PRECEDENT, the four-file fix of 2026-09-03: the post template's three
  stale comments, plus the same stale hero comment still sitting in
  docs/blog/index.html and in both live posts. Rendered HTML was
  byte-identical before and after, which is exactly why only reading
  the comments would ever have found it. A stale instruction is worse
  than a stale claim, because it recruits the next reader into
  repeating it.

## Adding a page (all four steps, every time)
A page does not exist until it is in sitemap.xml AND llms.txt. The audit
enforces both: a missing sitemap entry is a critical, a missing llms.txt
entry is a warning, and either one drops that page below 100/100.
1. Copy templates/service-page-template.html and replace every {{TOKEN}}.
2. Add its <url> block to docs/sitemap.xml with the real publish date.
3. Add its line to "## Key pages" in docs/llms.txt.
4. Link it from the homepage service card and the footer Services column.
Full checklist with the reasoning lives in PLAYBOOK.md.

## Location pages
- Location pages are a three-tier tree: county hubs under
  docs/locations/<county>/, town pages nested under their county, and
  the footer. Every town in the footer links to its own page if one
  exists, otherwise to its county hub. No town link may resolve to a
  stub, a redirect, or a 404.
- County hubs are real destinations: substantive prose about the
  county's business mix and every served town named in the text.
- Town pages are anchored to web design (our strongest local keyword)
  and each must carry at least three true, checkable local facts, a
  unique FAQ (not reused from other town pages), and section order and
  phrasing varied from sibling pages. If a town cannot muster three true
  facts, it does not get a page and stays as prose on the county hub.
- Variance test before any town page ships: read it side by side with a
  sibling town page with the town names covered; if they read the same,
  it does not ship.
- Schema: one business entity in Quakertown with areaServed listing the
  counties and towns. Never a business address in any other town.
- The planned nine town pages (Quakertown, Doylestown, Newtown,
  Lansdale, Blue Bell, Collegeville, Allentown, Bethlehem, Easton) are
  built on the doorway and variance tests alone. Any town page beyond
  those nine waits for Search Console evidence from the existing pages
  before it is built. Rationale: no page can earn impressions until the
  domain cutover, and the per-page tests, not the count, are the
  doorway protection.
- Cross-linking is tree-shaped: town to county hub, county hub to
  service pages and to the towns under it. Never every town to every
  town.
- Regional names are checkable facts, not flavor. North Penn is
  Lansdale, North Wales, and Hatfield; Souderton and Harleysville are
  Indian Valley, per the county planning commission. Newtown is lower
  Bucks, Doylestown central Bucks, Quakertown upper Bucks. Quakertown's
  downtown is West Broad Street, not Main Street. Getting one of these
  wrong is what makes a local page read as written from a map.

## The blog (decided 2026-08-31)
- The blog lives at docs/blog/, index at /blog/, posts at
  /blog/<slug>/. That URL was on the old WordPress site and PLAYBOOK.md
  listed it as a deliberate 404 with one condition attached, "revisit
  only if a notes section ever launches". It has, so the URL is a real
  page again and the PLAYBOOK row moved in the same commit.
- BLOG IS IN THE FOOTER, NOT THE NAV, and that is deliberate rather
  than an oversight. It sits in the Explore column after About, on all
  29 pages, docs/404.html and BOTH templates. The link is one line per
  file at that file's own relative depth, not one identical string: the
  blog index self-links with ./ the way About and Privacy do, and
  docs/404.html uses /blog/ under its root-relative exception. Nav and
  footer cost the identical edit and give the identical crawl equity;
  the only difference is prominence, and a nav slot pointing at a
  near-empty blog advertises an empty room.
  PROMOTION TRIGGER: at roughly EIGHT published posts, move it into the
  nav after About. The nav fits a seventh item at its 1000px breakpoint
  with room to spare, measured against the 1150px step-down rule. Until
  then, a sweep that finds Blog missing from the nav has found the
  decision, not a bug.
- Post titles do NOT carry the "| Corcoran Communications" suffix. That
  rule is scoped to the five service pages. Twenty-six characters of
  brand out of sixty leaves thirty-four for a headline, which is how a
  blog ends up with titles nobody can read. Title 60 or fewer, meta 160
  or fewer, both MACHINE COUNTED, never estimated.
- EVERY POST CARRIES AN FAQ, and the reason is mechanical:
  scripts/audit.py scores a page with no FAQPage schema as a warning,
  and one warning drops it under 100/100 and fails --strict. So the FAQ
  is structural, not optional, on the index and on every post. It must
  still pass the standalone test in both senses: questions a reader
  would actually ask, and answers whose FIRST SENTENCE survives being
  lifted without its question, because that is what an assistant does
  with it. SURVIVING THE LIFT MEANS BEING TRUE ALONE, not merely
  grammatical (sharpened 2026-09-03). The blog's "Who writes these?"
  opened "Greg Quinn, the owner, writes them", which reads perfectly
  well and claims a sole authorship the very next sentence takes back.
  An assistant quoting only that sentence would have published a claim
  the full answer contradicts. Put the whole truth in sentence one and
  the reassurance after it, never the other way round.
  No bare particle openers ("No." "Yes." "Two things."), which
  comma-merge into the sentence that follows. Padding written to
  satisfy the audit is worse than no post at all. The FAQ mirror law
  applies as everywhere else: each visible question and answer
  byte-identical to its schema twin.
- A POST'S FAQ IS TOPIC-ONLY, and blog posts are the FOURTH SANCTIONED
  EXCEPTION to the contracts question that ends every other page's FAQ
  (decided 2026-08-31, after web-design, film-live-entertainment and
  privacy). Every question on a post is about that post's own subject.
  A reader who came for one answer is not being asked to think about
  an engagement model. THE BLOG INDEX IS NOT THE EXCEPTION: it is a hub
  page like any other and keeps the contracts question, byte-identical
  to every other page's. A consistency sweep that finds the question
  missing from a post has found this rule, and each post carries a
  comment in its FAQ section saying so.
- IMAGES: real photographs only, and none by default. A post ships with
  no image, and the content writer agent may never add one, because it
  does not source or generate art and invented art is a fact claim like
  any other. When Greg supplies a real photograph it goes in the
  template's .post-figure block with real alt text describing what is
  in the frame. No stock art, no generated art, ever.
- Article body runs 700 to 1200 words. Nothing enforces this but the
  writer: the audit's word count reads the whole page including nav and
  footer, so a 200-word post still clears it. That check is not the
  floor.
- Adding a post is the same four steps as any other page, plus one:
  the page from templates/blog-post-template.html, its sitemap entry,
  its llms.txt line, and its card in docs/blog/index.html AND its
  BlogPosting entry in that page's Blog schema.
- THE ARTICLE COLUMN IS TUNED FOR READING, NOT SCANNING (decided
  2026-08-31, after the first post went live and read badly). 640px at
  1.15rem, line height 1.85, which MEASURES 74 characters a line. The
  rest of the site's type is set for scanning a sales section; 900
  words is a different job. Check the measure by machine when the size
  changes: at the original 17px on a 740px column it ran to 93
  characters, well past the 60 to 75 long prose is comfortable in, and
  a wider column at a bigger size only looks generous.
- BODY TEXT IN A POST IS --midnight, NOT --slate, and this is a
  deliberate deviation from the derived-neutrals list above, which
  assigns --slate to body text on light. Recorded rather than quietly
  done: --slate is right for a card, a caption, or a paragraph you
  skim, and across 900 words on Cloud it reads washed out. Midnight is
  13.64:1 there. It applies ONLY inside .post-body. Everywhere else on
  the site body text stays --slate, and nothing new entered the
  palette.
- THE FOUR-ITEM PATTERN: when a post lists things, each one is an H3
  followed by its paragraph, never a paragraph with a bold lead-in. The
  H3 sits closer to the paragraph under it than to the one above, which
  is what makes a list read as a list. Bold lead-ins render as four
  paragraphs that happen to start bold.
- THE INDEX'S "LATEST" BAND IS LIGHT (changed 2026-09-03, reversing the
  2026-08-31 dark band). The page now runs dark hero, light posts, dark
  contact, light FAQ, the same alternation every other page keeps, and
  the posts sit on the page background with white cards like every other
  card on the site. The band carries no .dark and no field class.
  Nothing in site.css changed: it already held both variants, so the
  base light rules apply on their own, --midnight title at 14.58:1,
  --signal hover at 5.18:1, --green-text date at 5.34:1, all on white.
  The .dark .post-list rules stay in the stylesheet, unmatched here, for
  any future dark band.
- THE HARD-WON PART OF THAT OLD RULE STILL STANDS: never reuse a
  light-panel card color on a dark band without checking it. On the dark
  band a --midnight title measured 1.16:1 and --green-text measured
  2.36:1, and both shipped that way once. The colors are only safe now
  because the band under them is light.
- THE BLOG INDEX HERO CARRIES A PER-PAGE GRAPHIC like every other page:
  .hero-split wrapping .hero-copy-col and a decorative .hero-art SVG,
  aria-hidden and hidden below 1000px by the existing CSS. Palette hex
  hardcoded, because custom properties do not reach inline SVG
  attributes. This is page furniture, NOT a post image, so it is not
  touched by the real-photographs-only rule below, which governs images
  inside a post.
- EVERY POST HERO CARRIES THE SAME GRAPHIC, and the sameness is the
  point (decided 2026-09-03). It lives in
  templates/blog-post-template.html, so a post inherits it and no post
  ever needs an art decision: nothing to draw, nothing to review, one
  fewer way for a weekly post to stall. It is a marked-up page, a ruled
  margin with a bracket and a green check against a mint-washed line,
  and it is DELIBERATELY NOT the index's article card. The two heroes
  have to look different or clicking a post card reads as nothing having
  happened. Page furniture like the index's, so the
  real-photographs-only rule below does not touch it either, and the
  content writer agent may not vary it, swap it, or remove it. A sweep
  that finds all posts sharing one graphic has found this rule.
- THE INDEX HAS NO "WHAT THIS IS" SECTION (deleted 2026-09-03). The hero
  lead already says who the notes are for, and the section restated it
  at more length while the page's job is to show the posts. Nothing
  linked to its #about-these anchor.
- SKIP BEATS FILLER. The cadence is weekly to start because the blog is
  empty, and it is a ceiling, not a quota. A week with no strong topic
  files a short content-skipped issue and produces no post. The
  standard does not bend to the schedule.
- THE WRITER HAS NO `git push`. It pushes through
  scripts/push-post-branch.sh, which refuses any branch that is not the
  checked-out post/ branch. This was a permission pattern until
  2026-09-01, `Bash(git push -u origin post/:*)`, and it cost a finished
  post: the runner matches an allowlist entry TOKEN BY TOKEN, so a
  pattern ending mid-token matches nothing real. A tool-allowlist entry
  must end where a token ends. Where a rule needs to be cleverer than
  that, it goes in a script that can be tested, not in a permission
  string. Branch protection on main is the second lock and stays.
- EVERY CONTENT WRITER RUN ENDS WITH EXACTLY ONE ARTIFACT (decided
  2026-09-01, after a forced test run did ten minutes of work, produced
  nothing, and went green). The three are: a pull request from a post/
  branch, a content-skipped issue, or a content-blocked issue. Nothing
  else counts, including hitting the turn cap. The workflow's last
  step looks for one of the three and fails the job when none exists,
  because the agent's own "success" only ever meant it stopped without
  crashing. A silent stop is now a red run, not a quiet week.

## Links (decided 2026-08-13)
- EVERY internal link and asset path is RELATIVE and never starts with
  "/". From a service page the site root is ../../ , so:
  ../../assets/site.css, ../../logo-dark.png, ../../#services, ../seo/
  for a sibling service.
  THE RULE STANDS AFTER CUTOVER (2026-08-27), with a different reason.
  It was written because the site also served from a project subpath,
  gquinn01.github.io/corcoranpr-site/, where a leading slash 404s. That
  address now 301s to corcoranpr.com and keeps the path, so a leading
  slash would technically work today. It stays banned anyway: relative
  paths keep working wherever the files are served from, including a
  local checkout and any future preview, and the ban is what the whole
  repo is built on. Do not "modernize" 45 files to absolute paths.
- The only absolute URLs are the ones the spec requires to be absolute:
  canonical, og:url, og:image, sitemap <loc>, and schema @id/url values.
- ONE EXCEPTION, docs/404.html (decided 2026-08-27). GitHub Pages
  serves that file at whatever URL was missing, so the browser's address
  stays /some/deep/typo/ and every relative path on it resolves against
  a directory that does not exist. Relative paths are meaningless there,
  so the 404 page uses ROOT-RELATIVE paths throughout: stylesheet,
  script, logo, and every link. Inlining the CSS instead was rejected,
  because it would put the palette in a second file. Confirmed working
  at the domain root on 2026-08-27: a missing path returns a real 404
  status and the styled page, with /assets/site.css resolving. The
  temporary cost of it rendering unstyled on the project subpath is
  spent and gone. No other file may take this exception.
- Verify with: grep -rn 'href="/\|src="/' docs/ --exclude=404.html
  — it must print nothing. The --exclude is the 404 rule above; without
  it the check reports the exception it already knows about.

## Privacy, analytics and tracking (decided 2026-08-27)
- ONE ANALYTICS TAG, and only one: Google Analytics 4, property
  G-BNLRK8YR6Y, carried over from the old WordPress site so its history
  survives the cutover. The base gtag snippet sits in the head of every
  page and the template, above the stylesheet link. The form_submit
  event already in docs/assets/site.js reaches GA4 through it; GA4's own
  enhanced measurement cannot see that submit, because the handler calls
  preventDefault() to keep the no-reload thank you.
- THE OLD SITE'S OTHER FIVE TAGS DID NOT COME ACROSS, deliberately: the
  GTM-MFPHPDK container, a Meta pixel (214048892700199), a dead
  Universal Analytics property (UA-62592023-10, stopped processing in
  July 2023), Jetpack Stats, and reCAPTCHA. Do not restore any of them
  by default.
- NO GOOGLE ADS CONVERSION TAG. Corcoran has no Google Ads account of
  its own; Greg manages client accounts, and the firm has never run its
  own ads. There is no AW- ID and none may be invented. When the firm
  does run its own ads, see the two lines in PLAYBOOK.md.
- Redirect stubs carry no analytics. They are machine-facing files that
  a browser leaves in under a second.
- docs/privacy/ IS THE DISCLOSURE. There is no consent banner, and the
  privacy page is what stands in its place, so it has to stay true. Any
  change to what the form collects, to who processes it, or to what
  tracking runs, updates docs/privacy/ IN THE SAME COMMIT and moves the
  "Last updated" date in its hero. No invented legal boilerplate ever
  goes on it, and it claims compliance with no framework we have not
  verified.
- The privacy page is the THIRD sanctioned exception to the contracts
  question that ends every other page's FAQ, after web-design and
  film-live-entertainment. (Blog POSTS became the fourth on 2026-08-31;
  see The blog. The blog INDEX keeps the question.) A privacy policy has no product to contract
  for. It also carries no audit form: its contact band is direct phone
  and email, following the film page, because phone and email are how a
  reader asks to have their information deleted.
- Every page's footer bottom line ends with a Privacy Policy link, at
  the correct relative depth, or ./ on the privacy page itself, the same
  way About and Free Audit handle their own.

## Redirect stubs and the 404 page (decided 2026-08-27)
- The old WordPress site's 28 URLs were mapped before cutover. 15 have a
  page here that genuinely answers what they answered, and each of those
  is a stub at docs/<old-slug>/index.html: a rel=canonical at the target,
  a meta refresh, a location.replace, and a real visible link. The other
  13, plus the 167 tag, 139 attachment, 2 category and 2 author URLs,
  404 on purpose. A redirect that lies about relevance is worse than an
  honest 404, and Google treats a mass redirect of unrelated pages to
  one page as a soft 404 anyway.
- A stub's canonical carries NO FRAGMENT even when its refresh target
  does. Google strips fragments from canonicals, so the reader lands on
  the anchor and the crawler is told the page.
- STUBS AND THE 404 PAGE STAY OUT OF sitemap.xml AND llms.txt. That is
  the point of them, not an oversight.
- Both declare themselves in the head so the audit can tell:
  <meta name="corcoran-page" content="redirect-stub"> and
  content="error-404". scripts/audit.py scores each against a short
  rubric of its own, and they still have to reach 100/100.
- The full decided map lives in PLAYBOOK.md. Building a new stub means
  adding a row there in the same commit.

## Asset cache-busting (decided 2026-08-27)
- docs/assets/site.css and site.js are referenced everywhere as
  assets/site.css?v=<first 8 hex of that file's SHA-256>.
- After changing either file, run in the same commit:
  python3 scripts/stamp-assets.py
  It rewrites every reference under docs/ and in templates/, and it is
  idempotent. Add --check to report stale stamps without writing.
- WHY: GitHub Pages serves both files with cache-control: max-age=600,
  so a browser holds either for up to ten minutes without revalidating.
  Twice during the build that looked exactly like a CSS bug and got
  chased as one. A hash, not a date: two edits on one day share a date,
  and the second would serve stale.
- Forgetting is not possible. scripts/audit.py records a stale or
  missing stamp as a CRITICAL against that page, which drops it under
  100/100 and fails --strict, the same way a missing sitemap entry does.

## Agents and their permissions (decided 2026-09-03)
- NO INSTRUCTION SHIPS IN ANY agents/*.md UNLESS THAT WORKFLOW'S TOOL
  LIST CAN EXECUTE IT. Cross-check the two files on every edit to
  either: agents/<name>.md against the `--allowedTools` line in
  .github/workflows/<name>-agent.yml. Writing a step is not the same as
  checking the agent can perform it, and nothing else in the repo
  catches the gap: the audit does not read agent files, and the runner
  reports a refused command as a normal stop, so the job still goes
  green.
- This has now cost two runs. On 2026-09-01 the permission pattern
  `Bash(git push -u origin post/:*)` matched nothing real, because the
  runner matches an allowlist entry TOKEN BY TOKEN and that entry ends
  mid-token; a finished post could not be pushed. On 2026-09-03 a new
  Site Auditor step told the agent to run four shell greps, two of them
  piped into `wc -l`, when its Bash grant is only `gh issue`, `gh label`
  and `date`. The second was caught before it ran only because the
  workflow was read. Read the workflow.
- A TOOL-ALLOWLIST ENTRY MUST END WHERE A TOKEN ENDS. Where a rule needs
  to be cleverer than that, it goes in a script that can be tested, not
  in a permission string. That is why scripts/push-post-branch.sh exists.
- FILE PERMISSIONS ARE `Edit(path)`, NEVER `Write(path)`. Claude Code
  checks file rules against Edit and Read only. A `Write(path)` rule is
  accepted and then never consulted, so it reads as correct and does
  nothing, which is the worst failure shape there is. Verified three
  ways on 2026-09-03: `Write(./.audit-issue-body.md)` refused the write,
  `Edit(./.audit-issue-body.md)` allowed it, and that same rule refused
  a different filename. Scope the rule to one exact filename; never
  grant a general Write to a reporting agent.
- A BASH COMMAND OVER ROUGHLY 5KB IS REFUSED for length, and a heredoc
  is part of the same command string, so `--body-file -` does not escape
  it. A long issue body is written to the agent's one granted scratch
  file and passed with `--body-file <name>`. Measured on 2026-09-03:
  12,871 characters refused, 4,727 accepted.
- VERIFY A PERMISSION RULE, DO NOT ASSUME IT. `claude -p "<task>"
  --allowedTools "<rule>"` in a scratch directory proves a rule in
  seconds, including the negative case, and costs nothing next to a
  wasted agent run.

## Repo rules
- docs/ = the live site. docs/assets/ = the shared stylesheet and script
  used by every page; the palette lives ONLY in docs/assets/site.css, so
  change it there and nowhere else. templates/ = client-pitch templates
  plus the internal service-page template. agents/ = agent job
  descriptions. Never touch .github/ or scripts/ without asking first.
- The service page template is the master mold. When a shared structural
  element changes on any live page, templates/service-page-template.html
  changes in the same commit, so the template never falls behind the
  site.
- Contact form: audit request form on every page, posting to a hosted
  Formspree endpoint; no server code. Two pages carry a direct contact
  band instead, phone and email with no form: film-live-entertainment
  and privacy. Redirect stubs and the 404 page carry neither.
- SITE_URL, the repo variable the weekly Site Auditor reads, is SET to
  https://corcoranpr.com/ as of 2026-08-27, the day the domain cutover
  happened. The weekly scan therefore audits the live site, and the
  site-wide AEO checks (robots.txt and llms.txt, which have to be
  fetched from a domain root) run again for the first time since
  2026-08-20. Between 2026-08-20 and the cutover it was deliberately
  unset, because the domain still served the old WordPress site and a
  live scan would have scored somebody else's pages.
- THE LIVE SCAN AND THE LOCAL SCAN COVER DIFFERENT SETS, and this is the
  one thing to keep straight now that SITE_URL is set. A live run takes
  its page list FROM sitemap.xml, which is 29 pages. The 15 redirect
  stubs and the 404 page are deliberately not in the sitemap, so the
  weekly report will never mention them. Only a local run,
  python3 scripts/audit.py, covers all 45 files. Run the local one
  before committing; that is what the definition of done means by
  "EVERY page".
- Never put API keys or secrets in any file.
