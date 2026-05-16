---
name: blog-seo-check
description: Post-writing SEO validation checklist to confirm a blog post is fully optimized before publishing.
version: 1.0.0
author: PiyushSingh2212
---

# Blog SEO Check Skill

## Usage
```
/blog seo-check <file>
```

## Validation Checks

### Title & Meta
- [ ] H1 title contains primary keyword (within first 60 chars)
- [ ] Title length: 50-60 characters
- [ ] Meta description: 140-155 characters
- [ ] Meta description includes keyword + action phrase

### URL & Structure
- [ ] Slug is lowercase, hyphenated, keyword-rich
- [ ] Slug is under 75 characters
- [ ] No stop words in slug (a, the, in, of, etc.)

### Content
- [ ] Primary keyword in first 100 words
- [ ] Keyword density: 1-2% (not stuffed)
- [ ] H2 headings include secondary keywords
- [ ] Content length meets target (1200+ standard, 2500+ pillar)
- [ ] No duplicate H1s on the site
- [ ] External links open in new tab (rel="noopener")

### Technical
- [ ] JSON-LD Article schema present
- [ ] Open Graph title and description set
- [ ] Canonical URL defined
- [ ] Images have descriptive alt text
- [ ] No broken internal links

### Linking
- [ ] 2-3 internal links to related posts
- [ ] 1-2 external links to authoritative sources
- [ ] No orphaned page (has at least 1 page linking to it)

## Output
Pass/Fail per item + overall SEO readiness score (0-100) + top 3 fixes.
