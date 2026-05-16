---
name: blog-rewrite
description: Optimize and rewrite an existing blog post to improve SEO score, readability, and AI citation potential.
version: 1.0.0
author: PiyushSingh2212
---

# Blog Rewrite Skill

## Usage
```
/blog rewrite <file>
```

## What This Skill Does
Takes an existing blog post and rewrites/optimizes it to improve quality score, search rankings, and brand alignment.

## Rewrite Process
1. **Audit current post** — Run blog-analyze to get baseline score
2. **Identify weak areas** — Flag low-scoring categories
3. **SERP gap analysis** — Compare with current top-ranking content
4. **Rewrite sections** — Improve weakest areas first
5. **SEO enhancement** — Optimize title, headings, meta, internal links
6. **AI citation pass** — Add answer-first formatting, FAQs, citation capsules
7. **Re-score** — Confirm improved score (must improve by 10+ pts or reach 80+)
8. **Output** — Rewritten file with change summary

## Rewrite Priorities (in order)
1. Fix factual inaccuracies or outdated data
2. Improve intro hook (grab attention in 2 sentences)
3. Add/fix H2/H3 structure with keyword-rich headings
4. Expand thin sections (under 150 words per H2)
5. Add FAQ block if missing
6. Improve meta description
7. Add internal links to 99minds product pages
8. Add JSON-LD schema if missing

## Output
- Rewritten markdown file
- Diff summary of major changes
- Before/after quality score comparison
