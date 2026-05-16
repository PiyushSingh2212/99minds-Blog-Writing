---
name: blog-write
description: Write a complete, SEO-optimized blog post for 99minds from scratch based on a given topic.
version: 1.0.0
author: PiyushSingh2212
---

# Blog Write Skill

## Usage
```
/blog write <topic>
```

## What This Skill Does
Generates a complete, publication-ready blog post optimized for Google rankings and AI citations, aligned with 99minds brand voice.

## Process
1. **Clarify intent** — Identify search intent (informational, commercial, transactional)
2. **Select template** — Auto-select content type: how-to, listicle, case study, comparison, pillar page, thought leadership, or FAQ
3. **Research phase** — Identify top SERP competitors and content gaps
4. **Structure** — Create H1/H2/H3 outline with keyword placement plan
5. **Write** — Draft full article following brand voice guidelines
6. **SEO pass** — Validate title, meta, headings, keyword density, internal links
7. **Quality check** — Score with blog-analyze rubric (must reach 70+)
8. **Schema** — Auto-generate JSON-LD Article schema
9. **Output** — Final markdown file ready for CMS

## Output Format
```markdown
---
title: "SEO Title (60 chars max)"
meta_description: "Meta description (155 chars max)"
slug: "url-slug"
author: "Author Name"
date: "YYYY-MM-DD"
tags: [tag1, tag2]
---

# H1 Title

[Full article content...]

## FAQ

**Q: Question?**
A: Answer.

```

## Content Templates Available
- how-to-guide
- listicle
- case-study
- comparison
- pillar-page
- thought-leadership
- product-review
- roundup
- tutorial
- news-analysis
- data-research
- faq-knowledge-base

## Quality Targets
- Minimum 1,200 words for standard posts
- Minimum 2,500 words for pillar pages
- Flesch Reading Ease: 50-70
- Quality score: 70+ to pass
