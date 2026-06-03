---
name: blog-write
description: Write a complete, publication-ready blog post for 99minds from a brief MD file. Follows 99minds Style Guide, Format Templates, and Funnel-Level Guidelines.
version: 1.0.0
author: PiyushSingh2212
---

# Blog Write Skill

## Usage
```
/blog write <brief.md>
```

## Writing Process (Follow In Exact Order)

### Step 1 — Analyze the Brief
The blog brief (MD file) contains:
- **Primary keyword** — target this in H1, first 100 words, meta title
- **Topics/Terms to mention** — secondary keywords and semantic terms
- **Audience/Tone** — use e-commerce industry terms, audience-friendly
- **Recommended word count** — match this exactly
- **Recommended heading count** — match this exactly
- **Images** — number of images required
- **Slug** — exact URL slug to use
- **Meta title** — use as provided or optimize within 60 chars
- **SE Ranking Content Optimizer Link** — target content score from SE Ranking
- **References** — top 5 SERP competitors to analyze (not copy)
- **Internal links** — mandatory landing page + blog post links to include

### Step 2 — Determine Funnel Stage
Check the brief or keyword intent to determine TOFU / MOFU / BOFU:
- **TOFU**: Educational only — do NOT sell 99minds. Add FAQs. Mention 99minds only in conclusion.
- **MOFU**: Explain approaches + introduce 99minds features naturally. Propose as solution in conclusion.
- **BOFU**: Skip basics. Deep product info. Pricing. Reviews. Direct CTA.

### Step 3 — Select Blog Format
Auto-select based on topic type:

**Listicle Format** (e.g., "Top 10 Best [KEYWORD] Tools"):
- Intro: under 150 words
- H2: TL;DR: Top 10 Best [KEYWORD] At a Glance — table of all products with a one-line conclusion per tool
- H2: What Should You Look for in [KEYWORD]? (under 200 words)
- H2: The 10 Best [KEYWORD] to Use in [Year]
  - H3: 1. [99minds as a linked heading] — **link the H3 heading text itself to https://www.99minds.io** e.g. `<h3><a href="https://www.99minds.io" role="link" target="_blank">1. 99minds</a></h3>`
    - Intro paragraph: describe relevant 99minds features for this topic — consult `99minds-context.md` Feature-to-Blog-Topic Mapping. Use real dashboard feature names (e.g., "Workflows", "VIP Tiers", "Cart Item Filters")
    - H4: 99minds best features — **go straight into bullets, no intro sentence**
      - (bullet list of most relevant features only)
    - H4: 99minds limitations — **go straight into bullets, no intro sentence**. Tone limitations down: never say a tool is "expensive" or has "poor support" — say "some users may find the pricing higher compared to other options" or "response times may vary during peak periods"
      - (1-2 real limitations from reviews, toned down)
    - H4: 99minds pricing — **go straight into bullets, no intro sentence**. All prices in USD.
      - Basic: $49/month
      - Pro: $99/month
      - Ultra: $199/month
      - Premium: $499/month
      - Enterprise: Contact for pricing
    - H4: 99minds ratings and reviews — **go straight into bullets, no intro sentence**
      - Shopify: 5/5 (30+ reviews)
      - G2: 5/5 (5 reviews)
  - H3: 2. [Next tool] — same H4 format, same limitation tone rules, same no-intro-to-H4 rule
  - H3: 3–10. Repeat
- Conclusion at the end of the article (outro)
- **Never name 99minds competitors** (see Competitor Prohibition below)

**How-to/Guide Format** (e.g., "How to Build a Loyalty Program"):
- Intro: under 150 words · answer-first · lead with a verified stat from a reputable source
- H2: TL;DR: 60-Second Summary — 5-7 self-contained bullet points summarizing the full post
- H2: What Is [primary keyword]? or Why Do You Need [primary keyword]?
- H2: How to [primary keyword]: Step-by-Step Process
- H2: [99minds + primary keyword] — show use cases and features. **Before writing**: consult `99minds-context.md` Feature-to-Blog-Topic Mapping to identify the right features. Use real dashboard feature names and describe actual workflows and form fields.
- Any other relevant H2s based on content gap analysis
- H2: Conclusion With [99minds] — **the conclusion H2 heading must include "99minds"** e.g. "Getting Started With 99minds" or "How 99minds Helps You [Topic]". Summary + recommendation + CTA.
- H2: Frequently Asked Questions on [Topic] — minimum 6 questions from PAA/Quora/Reddit

### Step 4 — Write the Blog

**Title / H1 / H2**: Title Case · H1/meta title 60 chars max · primary keyword included
**H3, H4, H5, H6**: Sentence case only (proper nouns are the only exception)
**Voice**: Conversational, fun, easy to understand · address reader as "you" · use "we"/"I" for 99minds
**Contractions**: Always use (it's, we're, you'll, don't, I'm)
**Avoid**: "utilize" (use "use") · advertising jargon · robotic phrases · cliche openers ("game-changer", "let's dive in", "in today's world", "it's worth noting", "needless to say", "at the end of the day", "leveraging X", "the answer lies in")
**Oxford commas**: Required for lists of three or more items
**Em dashes**: NEVER use em dashes (—). Replace with a comma, colon, or semicolon.
**Bullet / list points**: No full stops (periods) at the end of bullet points or list items. If a bullet has multiple sentences, end the final sentence without a period.
**Numbers**: Spell out one through nine; use numerals for 10 and above
  - Exception: headers and meta descriptions always use numerals (e.g., "7 Types of..." not "Seven Types of...")
  - Exception: write 1-9 numerically when they appear before "million" or "billion" (e.g., "3 million customers")
**Emojis**: Always add punctuation before an emoji! Never use two emojis back-to-back.
  - Go-to: 📚 😀 😃 🤩 🙌 ✨ 🌻 🛠️ 👀 👏 🚀
  - Restricted (do not use): 👍 👌 😂 💔 😕 😔 😢 😭
**Italics**: Use for emphasis on key words and terms - matches the conversational 99minds tone
**Prices**: All prices in USD. Use other currencies only if USD is not supported.
**Competitor cons**: Never say a tool is "expensive" or "has poor support". Say "some users may find the pricing higher compared to other options" or "response times may vary during peak periods".

#### Answer-First Formatting (Required)
Every H2 must state its main point in the first sentence. Do not bury the answer. Example:
- ✅ "Points-based programs are the most effective structure for high-frequency, low-ticket businesses."
- ❌ "There are many ways to think about loyalty programs. Let's explore a few options..."

#### GenAI-Friendly Writing Rules (Required)
These rules ensure the post is correctly retrieved and cited by AI systems (ChatGPT, Perplexity, AI Overviews, Claude). See `genai-content-guidelines.md` for full detail.

**Sentence length**: Keep sentences under 20 words. Split anything longer into two sentences.

**One idea per paragraph**: Each paragraph covers exactly one concept. AI summarizes paragraph by paragraph — bundled paragraphs produce blended, inaccurate citations.

**Section length cap**: Keep each H2 section under ~375 words. Split longer sections into two H2s or use H3 sub-sections.

**Self-contained list items**: Every bullet must function as a standalone statement without relying on surrounding text for meaning. Never start a bullet with "it", "this", or "the above".
- ✅ "Set a maximum per-customer usage limit of one to prevent code-stacking."
- ❌ "Set it to one."

**Anchor text**: Must describe the destination article's topic. Never use "click here", "learn more", or "this article".
- ✅ `how to build a loyalty program for small businesses`
- ❌ `learn more`

**No duplicate H2 headings**: Every H2 in the article must be unique.

**Heading format**: All H2 headings use raw HTML with explicit IDs - `<h2 id="Heading-Text">Heading Text</h2>`. Never use `## Heading {#id}` Markdown syntax — this blog does not support it.

**FAQ answers**: Must be fully self-contained, 2-5 sentences, no internal links. AI extracts FAQ answers verbatim as direct responses to user queries — they must make complete sense without any surrounding context. Restate key terms from the question inside the answer.
- ✅ "A promotional code is an alphanumeric string customers enter at checkout to receive a discount. Unlike automatic discounts, it requires active entry, giving merchants control over who receives the offer."
- ❌ "Yes, they work. See the section above."

#### Stats and Sources (MANDATORY)
- **Only use stats from reputable research organizations**: Statista, Deloitte, McKinsey, Accenture, Bain & Company, Harvard Business Review, Nielsen, Forrester Research, Pew Research Center, World Bank, PwC, Gartner, eMarketer, Edelman
- **Never use stats from competitor platforms** (Square, Shopify, Yotpo, Smile.io, etc.) as research sources
- **Every stat must include a linked source** — wrap the stat or source name in an `<a>` tag pointing to the original report/article
- **Never cite a stat without verifying it** — check the source URL resolves and the number matches

#### Competitor Prohibition (MANDATORY)
- **Never name 99minds competitors** anywhere in the blog post — not in comparisons, examples, tool lists, or FAQs
- Competitors include but are not limited to: Loopy Loyalty, Smile.io, Square Loyalty, Stamp Me, Yotpo, LoyaltyLion, Loyalty Lion, Fivestars, Marsello, Zinrelo, Antavo, Loyalzoo, Kangaroo Rewards
- When describing free or alternative tool options, use generic language: "several platforms offer free tiers" — never name them
- **99minds is always the only named platform recommendation**

### Step 5 — Internal Linking (MANDATORY)
Minimum 20 internal links per article:
- **Landing/feature pages** (2+): Always anchor text as "99minds [topic]" (e.g., "99minds Loyalty Program Software")
- **Blog posts** (15+): Related 99minds blog posts, distributed naturally throughout the article — not dumped in one section
- Weave links into sentences naturally; do not create a standalone "related posts" list

### Step 6 — Images

Use **dashboard screenshots** from the 99minds Google Drive library — NOT homepage, storefront, or marketing page screenshots.

**Number of images** = as specified in brief. For process/flow content: use graphics or flowcharts.

#### How to embed a dashboard screenshot (required workflow):

1. **Pick the right screenshot** — consult `99minds-screenshot-library.md` for the Feature-to-Screenshot Quick Reference. Choose screenshots that directly show the feature being discussed in that section of the post.

2. **Check if already saved locally** — look in `public/assets/blog/` for a file matching the `Save as` name from the library. If it exists, skip to step 4.

3. **Download and save** — if not already local:
   - Call `mcp__claude_ai_Google_Drive__download_file_content` with the Drive ID from the library
   - The tool returns a base64 string — save it to disk with PowerShell:
   ```powershell
   $base64 = "<base64 from download tool>"
   $bytes = [Convert]::FromBase64String($base64)
   [IO.File]::WriteAllBytes("C:\Users\Piyush Singh\Desktop\99minds-website\www.99minds.io-astro\public\assets\blog\<filename>.png", $bytes)
   ```

4. **Embed in blog HTML**:
   ```html
   <img loading="lazy" role="img" src="/assets/blog/<filename>.png" alt="<descriptive, keyword-rich alt text>">
   ```
   - Hero image uses `rel="preload"` instead of `loading="lazy"`
   - Alt text must be descriptive and include the primary keyword where natural
   - For full-width dashboard shots add `class="w-full h-auto"`
   - **Image source goes in the caption text, NOT as a hyperlink on the image itself**. If the image needs attribution, add a text caption below it.

5. **If you need a screenshot not in the library** — search the Drive folder directly:
   - Root folder ID: `1em-Y3coPYHDbd0jNq09Y2I5QrtAGysHU`
   - Use `mcp__claude_ai_Google_Drive__search_files` with `parentId = '<subfolder-id>'` to list available images in a specific feature folder (subfolder IDs are listed in `99minds-screenshot-library.md`)

### Step 7 — Finalize Output

```markdown
---
pubDate: YYYY-MM-DD
author: x
authorImg: "x.webp"
title: ""
description: ""
image:
  url: "/assets/blog/image.webp"
  alt: "xyx"
tags: ["tagq", "tag2"]
url: "https://www.99minds.io/blog/loyalty-program-apps"
keywords: ["Keyword"]
--- 
<div class="lg:flex lg:gap-6">
  <div class="lg:w-[250px] lg:sticky top-40 self-start shrink-0 p-[0.060rem] lg:mt-2 h-full text-black pb-4 overflow-y-auto max-h-[80vh]">
    <p class="text-black font-semibold text-nowrap pl-0">Table of Contents:</p>
<ul class="pl-0 text-base list-none">
  <li class="hover:bg-gray-100 lg:mt-4">
  <a role="link" href="#What-is-a-Loyalty-Program-App?" rel="noreferrer">What is a Loyalty Program App?</a>
  </li>
  <li class="hover:bg-gray-100 lg:mt-4">
<a rolw="link" href="#Why-eCommerce-Merchants-Need-Loyalty-Apps?" rel="noreferrer">Why eCommerce Merchants Need Loyalty Apps?</a>
</li>
  <li class="hover:bg-gray-100 lg:mt-4">
  <a role="link" href="#what-is-x" rel="noreferrer">What is x?</a>
  </li>
  <li class="hover:bg-gray-100 lg:mt-4">
  <a role="link" href="#Conclusion" rel="noreferrer">Conclusion</a>
  </li>
 <li class="hover:bg-gray-100 lg:mt-4">
  <a role="link" href="#tldr" rel="noreferrer">TL;DR</a></li>
  <li class="hover:bg-gray-100 lg:mt-4">
  <a role="link" href="#Frequently-Asked-Questions-on-[topic]" rel="noreferrer">Frequently Asked Questions</a></li>
</ul>
</div>

<div class="w-full">
<img rel="preload" role="img" src="/assets/blog/image.webp" alt="x">

[Intro — answer-first, lead with verified stat + source link, max 200 words]

<h2 id="tldr">TL;DR</h2>

- [Bullet 1 — key stat with source, self-contained]
- [Bullet 2 — main program types or steps, self-contained]
- [Bullet 3 — free/cost info, self-contained]
- [Bullet 4 — framework or process, self-contained]
- [Bullet 5 — biggest mistakes or takeaway, self-contained]

<h2 id="[Section-Slug]">[H2 Section Title]</h2>

[Content — first sentence states the main point. Each paragraph = one idea. Sentences under 20 words. Section under 375 words.]

<h2 id="Conclusion">Conclusion</h2>

[Summary + 99minds recommendation + CTA]

<div class="border-t border-gray-200 mt-10 pt-6 flex items-start gap-4">
  <img src="/[authorImg]" alt="[Author Name]" class="w-14 h-14 rounded-full shrink-0 object-cover">
  <div>
    <p class="font-semibold text-black m-0">[Author Name]</p>
    <p class="text-sm text-gray-600 mt-1 mb-0">[2-3 sentence author bio with expertise relevant to the post topic]</p>
  </div>
</div>

<h2 id="Frequently-Asked-Questions-on-[topic]">Frequently Asked Questions on [Topic]</h2>

<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 1?]</h3>[Answer — 2-5 sentences, fully self-contained, no internal links, restates key terms from the question]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 2?]</h3>[Answer — self-contained, no links]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 3?]</h3>[Answer — self-contained, no links]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 4?]</h3>[Answer — self-contained, no links]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 5?]</h3>[Answer — self-contained, no links]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 6?]</h3>[Answer — self-contained, no links]</div>

</div>
<!-- CTA sidebar -->
<div class="lg:w-[270px] lg:sticky top-40 self-start shrink-0 ...">
  ...
</div>

</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "[title]",
      "description": "[description]",
      "image": "https://www.99minds.io/assets/blog/[image]",
      "author": { "@type": "Person", "name": "[author]", "url": "https://www.99minds.io" },
      "publisher": { "@type": "Organization", "name": "99minds", "logo": { "@type": "ImageObject", "url": "https://www.99minds.io/logo.png" } },
      "datePublished": "[pubDate]",
      "dateModified": "[pubDate]",
      "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.99minds.io/blog/[slug]" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "[Q1]", "acceptedAnswer": { "@type": "Answer", "text": "[A1]" } },
        { "@type": "Question", "name": "[Q2]", "acceptedAnswer": { "@type": "Answer", "text": "[A2]" } }
      ]
    }
  ]
}
</script>
```

### Step 7 — Required Structural Elements

Every blog post must include ALL of the following before submission:

1. **TL;DR section** — immediately after intro, 5-7 self-contained bullets summarizing the full post
2. **Minimum 6 FAQ questions** — heading must read "Frequently Asked Questions on [Topic]" (never "Frequently Ask Questions"). FAQs sourced from PAA, AnswerThePublic, Quora, or Reddit
3. **Author bio block** — placed AFTER the last FAQ, BEFORE the CTA sidebar. Include author photo, name, and 2-3 sentence expertise description
4. **JSON-LD schema** — Article schema + FAQPage schema in a single `<script type="application/ld+json">` block at end of file. Publisher logo must use: `https://www.99minds.io/logos/99minds-logo-b.svg`
5. **Source links on all stats** — every percentage, dollar figure, or research claim wrapped in an `<a>` tag pointing to the original source
6. **Table of Contents** — sticky sidebar with links to all H2 sections including TL;DR and FAQ
7. **Meta title** — 60 chars max, primary keyword included, always use numerals in the title (e.g., "7 Best..." not "Seven Best...")
8. **Meta description** — 160 chars max, primary keyword included, reads as a direct answer to the implied search query
9. **Conclusion / outro** — every article ends with a conclusion section. How-to posts: the conclusion H2 must include "99minds" in the heading

### Step 8 — HTML Output Rules
- All links: `role="link" target="_blank"` — never `target="_blanck"` (common typo)
- All non-hero images: `loading="lazy"`
- Hero image: `rel="preload"`
- FAQ blocks: `<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6">`
- Author bio: `<div class="border-t border-gray-200 mt-10 pt-6 flex items-start gap-4">`

## Quality Targets

**Content:**
- Word count: match brief exactly (target 30% above SERP average for comprehensive coverage)
- Reading level: accessible, e-commerce industry terms OK
- All stats from Statista, Deloitte, McKinsey, Accenture, Bain, HBR, Nielsen, Forrester, Pew, or similar
- All stats have source links
- Zero competitor names in post
- Zero em dashes
- Zero periods at end of bullet/list items
- All images show dashboard (not homepage)
- All prices in USD
- Funnel-level rules followed exactly

**Submission Checklist (run before finalizing):**

Structure:
- [ ] Intro is under 150 words
- [ ] TL;DR section present immediately after intro
- [ ] Author bio block present AFTER the last FAQ, BEFORE the CTA sidebar
- [ ] FAQ heading reads "Frequently Asked Questions on [Topic]"
- [ ] Minimum 6 FAQ questions
- [ ] Table of Contents includes TL;DR and FAQ entries
- [ ] Conclusion present; how-to conclusion H2 includes "99minds" in heading
- [ ] Listicle: H3 heading for 99minds is a hyperlink to https://www.99minds.io
- [ ] Listicle: No intro sentences before H4 pros/cons/pricing/ratings — go straight to bullets

Content:
- [ ] Zero em dashes
- [ ] Zero competitor names
- [ ] No banned cliche phrases ("game-changer", "let's dive in", "in today's world", etc.)
- [ ] Every H2 opens with the main point in the first sentence
- [ ] Oxford commas used throughout
- [ ] No periods at end of bullets or list items
- [ ] Numbers: headers always use numerals; 1-9 spelled out in body except before million/billion
- [ ] All prices in USD
- [ ] Competitor limitations toned down (no "expensive", no "poor support" — use softened language)

Images:
- [ ] Alt text on all images — functional and descriptive
- [ ] Hero image has `rel="preload"` and `role="img"`
- [ ] All non-hero images have `loading="lazy"` and `role="img"`
- [ ] All images are dashboard screenshots (not homepage)
- [ ] Image source in caption text, NOT linked from the image itself

Stats and Sources:
- [ ] Every stat has a linked source anchor tag
- [ ] All sources from approved list (Deloitte, McKinsey, Accenture, Bain, HBR, Nielsen, Forrester, Pew, Statista, etc.)
- [ ] No stats from competitor platforms (Square, Shopify, Yotpo, etc.)

SEO:
- [ ] Meta title: 60 chars max, primary keyword, numerals in heading (not spelled out)
- [ ] Meta description: 160 chars max, primary keyword, reads as a direct answer
- [ ] Minimum 10 internal links (15+ blog posts and 2+ landing pages is ideal)
- [ ] All 99minds landing page links use "99minds [topic]" anchor text
- [ ] All links use `role="link" target="_blank"` (never `target="_blanck"`)

Schema:
- [ ] JSON-LD Article schema present
- [ ] JSON-LD FAQPage schema present with all FAQ Q&As
- [ ] Both in a single `<script type="application/ld+json">` block at end of file
- [ ] Publisher logo: `https://www.99minds.io/logos/99minds-logo-b.svg`

**GenAI Checklist:**
- [ ] Every sentence is under 20 words
- [ ] Every paragraph contains exactly one idea
- [ ] Every H2 section is under 375 words
- [ ] Every bullet point is self-contained (no "it", "this", "the above" without context)
- [ ] Every FAQ answer is self-contained, 2-5 sentences, zero internal links
- [ ] Every H2 opens with the answer in the first sentence
- [ ] All anchor text describes the destination article's specific topic
- [ ] All image alt text is functional and descriptive
- [ ] No duplicate H2 headings in the article
- [ ] All H2s use `<h2 id="...">` HTML format
- [ ] Primary keyword in H1, first paragraph, and meta description
