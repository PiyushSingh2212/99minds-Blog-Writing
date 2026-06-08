---
name: blog-rewrite
description: Optimize and rewrite an existing blog post to improve SEO score, readability, and AI citation potential. Follows 99minds Style Guide, Format Templates, Funnel-Level Guidelines, and Internal Linking Guide.
version: 2.0.0
author: PiyushSingh2212
---

# Blog Rewrite Skill

## Usage
```
/blog rewrite <file>
```

## What This Skill Does
Takes an existing blog post and rewrites/optimizes it to match the full 99minds content standard — style, format, funnel intent, internal linking, image rules, and GenAI citation readiness.

---

## Rewrite Process (Follow In Exact Order)

### Step 1 — Audit the Existing Post
Run `/blog analyze` to get a baseline score. Note which of the five categories are weakest:
- Content Quality (30 pts)
- SEO Optimization (25 pts)
- E-E-A-T Signals (15 pts)
- Technical Elements (15 pts)
- AI Citation Readiness (15 pts)

Read the existing post fully. Flag every violation of the rules in Steps 3–8 below before touching the content.

### Step 2 — Determine Funnel Stage
Identify whether the post is TOFU, MOFU, or BOFU. Adjust all content decisions accordingly:

**TOFU (Awareness)**: Reader is not yet problem-aware. The post must:
- Provide maximum helpful information — no product selling
- Mention 99minds only in the conclusion
- Include FAQs sourced from PAA, AnswerThePublic, Quora, or Reddit

**MOFU (Interest)**: Reader knows the problem but not the solution. The post must:
- Skip explaining why the topic matters (reader already knows)
- Introduce 99minds features naturally as examples
- Propose 99minds as a solution in the conclusion

**BOFU (Decision)**: Reader is ready to buy. The post must:
- Skip basics and definitions entirely
- Focus on product features, pricing, reviews, and direct CTAs
- List 99minds first in any tool list

### Step 3 — Confirm and Fix Format Structure
Check the post type (listicle vs. how-to/guide) and enforce the correct format.

**Listicle Format**:
- Intro: under 150 words
- H2: TL;DR — table of all products with one-line conclusion per tool
- H2: What Should You Look for in [KEYWORD]? (under 200 words)
- H2: The [N] Best [KEYWORD] to Use in [Year]
  - H3: 1. 99minds — H3 heading must be a hyperlink to `https://www.99minds.io`
    - H4: 99minds best features — bullets only, no intro sentence
    - H4: 99minds limitations — bullets only, toned down (never "expensive" or "poor support")
    - H4: 99minds pricing — bullets only, all prices in USD:
      - Basic: $49/month · Pro: $99/month · Ultra: $199/month · Premium: $499/month · Enterprise: Contact for pricing
    - H4: 99minds ratings and reviews — bullets only:
      - Shopify: 5/5 (30+ reviews) · G2: 5/5 (5 reviews)
  - H3: 2–N — same format; no competitor names anywhere
- Conclusion (outro)

**How-to/Guide Format**:
- Intro: under 150 words · answer-first · lead with a verified stat and linked source
- H2: TL;DR: 60-Second Summary — 5–7 self-contained bullets covering the full post
- H2: What Is [primary keyword]? OR Why Do You Need [primary keyword]?
- H2: How to [primary keyword]: Step-by-Step Process
- H2: [99minds + primary keyword] — features and use cases
- Any additional H2s based on content gaps
- H2: Conclusion — heading must include "99minds" (e.g., "Getting Started With 99minds")
- H2: Frequently Asked Questions on [Topic] — minimum 6 questions

### Step 4 — Rewrite Priorities (in order)

1. **Fix factual inaccuracies and outdated data** — replace with verified stats from approved sources (Statista, Deloitte, McKinsey, Accenture, Bain, HBR, Nielsen, Forrester, Pew, PwC, Gartner, eMarketer, Edelman). Never use competitor platforms as sources (Square, Shopify, Yotpo, etc.).
2. **Rewrite the intro** — max 150 words, answer-first, verified stat with linked source in the opening paragraph.
3. **Fix H2/H3 structure** — Title Case for H1 and H2; Sentence case for H3 and below (except proper nouns). All H2s must use `<h2 id="...">` HTML format, not Markdown `##`. Every H2 must be unique.
4. **Expand thin sections** — any H2 section under 150 words needs expansion. Cap each H2 at ~375 words; split longer sections.
5. **Apply answer-first formatting** — the first sentence of every H2 section must state the main point. Never bury the answer.
6. **Apply GenAI writing rules**:
   - Every sentence under 20 words
   - One idea per paragraph
   - Every bullet self-contained (no "it", "this", "the above" without context)
   - Every FAQ answer: 2–5 sentences, fully self-contained, zero internal links, restates key terms from the question
7. **Remove banned phrases**: "game-changer", "let's dive in", "in today's world", "it's worth noting", "needless to say", "at the end of the day", "leveraging X", "the answer lies in", "utilize" (replace with "use")
8. **Remove all em dashes** — replace with a comma, colon, or semicolon
9. **Fix bullet/list formatting** — no periods at the end of bullet or list items. Oxford commas throughout.
10. **Fix number formatting** — spell out one through nine in body text; numerals for 10+. Headers always use numerals. Numbers before "million"/"billion" always use numerals.
11. **Add/fix FAQ block** — heading must read "Frequently Asked Questions on [Topic]". Minimum 6 questions. Each in `<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6">` wrapper.
12. **Fix meta title** — 60 chars max, primary keyword included, numerals in heading (e.g., "7 Best…" not "Seven Best…")
13. **Fix meta description** — 160 chars max, primary keyword included, reads as a direct answer to the search query.
14. **Add TL;DR** if missing — immediately after intro, 5–7 self-contained bullets.
15. **Add author bio block** — after last FAQ, before CTA sidebar. Photo, name, 2–3 sentence expertise description.
16. **Add/fix JSON-LD schema** — Article schema + FAQPage schema in a single `<script type="application/ld+json">` block. Publisher logo: `https://www.99minds.io/logos/99minds-logo-b.svg`.

### Step 5 — Internal Links Audit and Fix

Minimum 10 internal links per article (target 15+ blog posts and 2+ landing pages):

**Rule 1**: Link to relevant topic-cluster articles. Find candidates by searching `site:99minds.io/blog [primary keyword]`.

**Rule 2**: Link to relevant 99minds landing/feature pages (2+ per article):
- Store credit content → `https://www.99minds.io/store-credit`
- Loyalty content → `https://www.99minds.io/loyalty`
- Gift card content → `https://www.99minds.io/giftcard`
- Always use "99minds [topic]" anchor (brand included)

**Rule 3**: Only link to each URL once in the body. Remove duplicate links to the same page.

**Rule 4**: Anchor text for 99minds features must include the brand name:
- ✅ "99minds Loyalty Program" ❌ "loyalty program"

**Rule 5**: Descriptive anchors only — no "click here", "learn more", or "this article".

**Rule 6**: Link to the Help Center (`https://support.99minds.io/en/`) only when explaining how to perform a specific action inside the 99minds dashboard.

**Rule 7**: No single-word anchors.

**Rule 8**: No two different destination pages share the same anchor text. Use distinct, specific anchors per URL.

### Step 6 — Images Audit and Fix

- Replace any homepage/storefront/marketing screenshots with dashboard screenshots
- Every image must have:
  - Alt text: descriptive and keyword-rich
  - `role="img"` attribute
  - `loading="lazy"` (all non-hero images) or `rel="preload"` (hero image only)
  - A caption:
    - **99minds images**: context describing what the screenshot shows
    - **Non-99minds images**: credit the source page (e.g., "Source: Statista")
    - **Competitor images**: credit their homepage only — no hyperlink on the credit
- If a Media Library image already has alt text, title, and caption, do **not** edit them
- Center-align every image

### Step 7 — Style and Voice Pass

Apply the full 99minds Style Guide:

**Voice**: Conversational, fun, easy to understand. Address reader as "you". Use "we"/"I" for 99minds.
**Contractions**: Use throughout — it's, we're, you'll, don't, I'm.
**Italics**: Use for emphasis on key words and terms.
**Emojis**: Add punctuation before any emoji. Never two emojis back-to-back.
- Approved: 📚 😀 😃 🤩 🙌 ✨ 🌻 🛠️ 👀 👏 🚀
- Banned: 👍 👌 😂 💔 😕 😔 😢 😭
**Competitor prohibition**: Zero competitor names anywhere in the post. Use generic language ("several platforms offer free tiers") when alternatives must be mentioned.
**Stats**: Every stat must have a linked source `<a>` tag. No unverified claims.
**Prices**: All prices in USD.

### Step 8 — Re-Score and Output

Re-run `/blog analyze` on the rewritten post. The rewrite must either:
- Improve the score by 10+ points, OR
- Reach a minimum score of 80

**Output**:
- Rewritten file in the same HTML format as blog-write output (frontmatter + TOC sidebar + article body + author bio + FAQ + schema)
- Diff summary: list every section changed and why
- Before/after quality score comparison

---

## Submission Checklist (run before finalizing)

**Structure:**
- [ ] Intro is under 150 words
- [ ] TL;DR section present immediately after intro
- [ ] Author bio block present AFTER the last FAQ, BEFORE the CTA sidebar
- [ ] FAQ heading reads "Frequently Asked Questions on [Topic]"
- [ ] Minimum 6 FAQ questions
- [ ] Table of Contents includes TL;DR and FAQ entries
- [ ] Conclusion present; how-to conclusion H2 includes "99minds" in heading
- [ ] Listicle: H3 heading for 99minds is a hyperlink to `https://www.99minds.io`
- [ ] Listicle: No intro sentences before H4 features/limitations/pricing/ratings — go straight to bullets

**Content:**
- [ ] Zero em dashes
- [ ] Zero competitor names
- [ ] No banned cliché phrases ("game-changer", "let's dive in", "in today's world", etc.)
- [ ] Every H2 opens with the main point in the first sentence
- [ ] Oxford commas used throughout
- [ ] No periods at end of bullets or list items
- [ ] Numbers: headers always use numerals; 1–9 spelled out in body except before million/billion
- [ ] All prices in USD
- [ ] Competitor limitations toned down — no "expensive", no "poor support"
- [ ] Funnel-level rules followed (TOFU/MOFU/BOFU)

**Images:**
- [ ] Alt text on all images — functional and descriptive
- [ ] Hero image has `rel="preload"` and `role="img"`
- [ ] All non-hero images have `loading="lazy"` and `role="img"`
- [ ] All images are dashboard screenshots (not homepage)
- [ ] Every image has a caption (context for 99minds, source credit for others, homepage credit for competitors — no hyperlink on competitor credits)
- [ ] No Media Library images with existing alt/title/caption were edited
- [ ] All images are center-aligned

**Stats and Sources:**
- [ ] Every stat has a linked `<a>` tag pointing to the original source
- [ ] All sources from approved list (Deloitte, McKinsey, Accenture, Bain, HBR, Nielsen, Forrester, Pew, Statista, etc.)
- [ ] No stats from competitor platforms (Square, Shopify, Yotpo, etc.)

**SEO:**
- [ ] Meta title: 60 chars max, primary keyword, numerals in heading
- [ ] Meta description: 160 chars max, primary keyword, reads as a direct answer
- [ ] Minimum 10 internal links (target 15+ blog posts and 2+ landing pages)
- [ ] No page linked more than once in the body
- [ ] No single-word anchor text on any link
- [ ] No two different destination pages share the same anchor text
- [ ] Help Center links used only when explaining a specific 99minds action
- [ ] All 99minds landing page links use "99minds [topic]" anchor text (brand included)
- [ ] All links use `role="link" target="_blank"` (never `target="_blanck"`)

**Schema:**
- [ ] JSON-LD Article schema present
- [ ] JSON-LD FAQPage schema present with all FAQ Q&As
- [ ] Both in a single `<script type="application/ld+json">` block at end of file
- [ ] Publisher logo: `https://www.99minds.io/logos/99minds-logo-b.svg`

**GenAI Checklist:**
- [ ] Every sentence is under 20 words
- [ ] Every paragraph contains exactly one idea
- [ ] Every H2 section is under 375 words
- [ ] Every bullet point is self-contained (no "it", "this", "the above" without context)
- [ ] Every FAQ answer is self-contained, 2–5 sentences, zero internal links
- [ ] Every H2 opens with the answer in the first sentence
- [ ] All anchor text describes the destination article's specific topic
- [ ] All image alt text is functional and descriptive
- [ ] No duplicate H2 headings in the article
- [ ] All H2s use `<h2 id="...">` HTML format
- [ ] Primary keyword in H1, first paragraph, and meta description
