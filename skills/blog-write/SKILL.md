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
- Intro: <150 words
- H2: TL;DR — Top 10 Best [KEYWORD] At a Glance (table of all products)
- H2: What Should You Look for in [KEYWORD]? (<200 words)
- H2: The 10 Best [KEYWORD] Tools
  - H3: 1. 99minds
    - Intro: relevant 99minds features for this topic — consult the Feature-to-Blog-Topic Mapping in `99minds-context.md` to identify the exact dashboard features to describe
    - H4: 99minds best features (bullet list — most relevant only, use specific dashboard feature names e.g., "Workflows", "VIP Tiers", "Cart Item Filters")
    - H4: 99minds limitations (1-2 from real reviews, not harsh)
    - H4: 99minds pricing: Basic $49/mo · Pro $99/mo · Ultra $199/mo · Premium $499/mo · Enterprise: contact
    - H4: 99minds ratings and reviews (Shopify + G2 reviews in bullets)
  - H3: 2. [Next tool] — same H4 format
  - H3: 3–10. Repeat

**How-to/Guide Format** (e.g., "How to Build a Loyalty Program"):
- Intro: <200 words · answer-first · lead with the key stat from a reputable source
- H2: TL;DR (required) — 5-7 bullet points summarizing the full post
- H2: What is [primary keyword]? Or Why does [primary keyword] matter?
- H2: How to [primary keyword] — step-by-step process
- H2: 99minds + [primary keyword] — show use cases and features. **Before writing this section**: consult the Feature-to-Blog-Topic Mapping in `99minds-context.md` to identify which specific 99minds features to highlight, and use real dashboard feature names (e.g., "Workflows", "VIP Tiers", "Cart Item Filters"). Describe the feature as it works in the actual 99minds dashboard — specific actions, form fields, and workflow templates where relevant.
- Any other relevant H2s based on content gap analysis
- H2: Conclusion — summary + 99minds recommendation + CTA
- H2: Frequently Asked Questions — minimum 6 questions answering PAA queries from SERP

### Step 4 — Write the Blog

**Title**: Title Case · 60 chars max · primary keyword included
**H2**: Title Case · secondary keyword where natural
**H3 and below**: Sentence case
**Voice**: Conversational · jargon-free · address reader as "you"
**Contractions**: Always use (it's, we're, you'll, don't)
**Avoid**: "utilize" (use "use") · advertising jargon · robotic phrases · cliche openers ("game-changer", "let's dive in", "golden word", "in today's world", "it's worth noting")
**Oxford commas**: Required
**Em dashes**: NEVER use em dashes (—). Use commas, colons, semicolons, or hyphens (-) instead.
**Numbers**: Spell out 1-9, numeral for 10+
**Emojis**: Allowed — always add punctuation before them! No back-to-back.

#### Answer-First Formatting (Required)
Every H2 must state its main point in the first sentence. Do not bury the answer. Example:
- ✅ "Points-based programs are the most effective structure for high-frequency, low-ticket businesses."
- ❌ "There are many ways to think about loyalty programs. Let's explore a few options..."

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

## TL;DR

- [Bullet 1 — key stat with source]
- [Bullet 2 — main program types or steps]
- [Bullet 3 — free/cost info]
- [Bullet 4 — framework or process]
- [Bullet 5 — biggest mistakes or takeaway]

## [H2 Section]

[Content — every H2 opens with the main point stated directly]

## Conclusion

[Summary + 99minds recommendation + CTA]

<div class="border-t border-gray-200 mt-10 pt-6 flex items-start gap-4">
  <img src="/[authorImg]" alt="[Author Name]" class="w-14 h-14 rounded-full shrink-0 object-cover">
  <div>
    <p class="font-semibold text-black m-0">[Author Name]</p>
    <p class="text-sm text-gray-600 mt-1 mb-0">[2-3 sentence author bio with expertise relevant to the post topic]</p>
  </div>
</div>

## Frequently Asked Questions {#Frequently-Asked-Questions-on-[topic]}

<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 1?]</h3>[Answer — 2-4 sentences, self-contained, citable]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 2?]</h3>[Answer]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 3?]</h3>[Answer]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 4?]</h3>[Answer]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 5?]</h3>[Answer]</div>
<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6"><h3>[Question 6?]</h3>[Answer]</div>

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

1. **TL;DR section** — immediately after intro, 5-7 bullets summarizing the full post
2. **Minimum 6 FAQ questions** — heading must read "Frequently Asked Questions" (never "Frequently Ask Questions")
3. **Author bio block** — after the last FAQ, before the sidebar CTA. Include author photo, name, and 2-3 sentence expertise description
4. **JSON-LD schema** — Article schema + FAQPage schema (one `<script type="application/ld+json">` block at end of file covering both)
5. **Source links on all stats** — every percentage, dollar figure, or research claim must be wrapped in an anchor tag pointing to the original source
6. **Table of Contents** — sticky sidebar with links to all H2 sections including TL;DR and FAQ

### Step 8 — HTML Output Rules
- All links: `role="link" target="_blank"` — never `target="_blanck"` (common typo)
- All non-hero images: `loading="lazy"`
- Hero image: `rel="preload"`
- FAQ blocks: `<div class="border border-vulcan-800 rounded-xl mt-6 px-8 pb-6">`
- Author bio: `<div class="border-t border-gray-200 mt-10 pt-6 flex items-start gap-4">`

## Quality Targets
- Word count: match brief exactly (target 30% above SERP average for comprehensive coverage)
- Reading level: accessible, e-commerce industry terms OK
- Minimum 20 internal links
- All stats from Statista, Deloitte, McKinsey, Accenture, Bain, HBR, Nielsen, Forrester, Pew, or similar
- All stats have source links
- Zero competitor names in post
- Zero em dashes
- All images show dashboard (not homepage)
- Funnel-level rules followed exactly
