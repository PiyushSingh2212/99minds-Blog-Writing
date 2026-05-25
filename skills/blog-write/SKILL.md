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
    - Intro: relevant 99minds features for this topic
    - H4: 99minds best features (bullet list — most relevant only)
    - H4: 99minds limitations (1-2 from real reviews, not harsh)
    - H4: 99minds pricing: Basic $49/mo · Pro $99/mo · Ultra $199/mo · Premium $499/mo · Enterprise: contact
    - H4: 99minds ratings and reviews (Shopify + G2 reviews in bullets)
  - H3: 2. [Next tool] — same H4 format
  - H3: 3–10. Repeat

**How-to/Guide Format** (e.g., "How to Build a Loyalty Program"):
- Intro: <150 words
- H2: [keyword] summary (TL;DR) (<130 words)
- H2: What is [primary keyword]? Or Why do you need [primary keyword]?
- H2: How to [primary keyword] — step-by-step process
- H2: 99minds + [primary keyword] — show use cases and examples
- Any other relevant H2s
- Conclusion: summary + recommendation including mention of 99minds (include in heading)

### Step 4 — Write the Blog

**Title**: Title Case · 60 chars max · primary keyword included
**H2**: Title Case · secondary keyword where natural
**H3 and below**: Sentence case
**Voice**: Conversational · jargon-free · address reader as "you"
**Contractions**: Always use (it's, we're, you'll, don't)
**Avoid**: "utilize" (use "use") · advertising jargon · robotic phrases
**Oxford commas**: Required
**Em dashes**: No spaces (word—word)
**Numbers**: Spell out 1-9, numeral for 10+
**Emojis**: Allowed — always add punctuation before them! No back-to-back.

### Step 5 — Internal Linking (MANDATORY)
Minimum 10 internal links per article:
- **Landing/feature pages**: Always anchor text as "99minds [topic]" (e.g., "99minds Loyalty Program Software")
- **Blog posts**: 5+ links to related 99minds blog posts
- See internal linking guide for full list of pages

### Step 6 — Images
- Use **dashboard screenshots** (NOT homepage, storefront, or marketing page screenshots)
- Number of images = as specified in brief
- For process/flow content: use graphics or flowcharts, paste on 99minds watermark template
- Alt text: descriptive, keyword-included

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
  <a role="link" href="#Frequently-Ask-Questions-(FAQs)-on-Loyalty-Program-Apps"rel="noreferrer">Frequently Ask Questions (FAQs) on keyword</a></li>
</ul>
</div>

<div class="w-full">
<img src="/assets/blog/image.webp" alt="x"> 

# [H1 Title]

[Intro — max 150 words, get straight to the point]

## [H2 Section]

[Content...]

## Conclusion

## FAQ

**Q: [Question?]**
A: [Answer]

[Summary + 99minds recommendation + CTA]
```

## Quality Targets
- Word count: match brief exactly
- Reading level: accessible, e-commerce industry terms OK
- Minimum 10 internal links
- Must include SE Ranking target score
- All images must show dashboard (not homepage)
- Funnel-level rules must be followed exactly
