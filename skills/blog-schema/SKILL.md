---
name: blog-schema
description: Generate JSON-LD schema markup for a blog post (Article, FAQPage, HowTo, BreadcrumbList).
version: 1.0.0
author: PiyushSingh2212
---

# Blog Schema Skill

## Usage
```
/blog schema <file>
```

## Schema Types Generated
- **Article** — Always generated for all posts
- **FAQPage** — Generated when FAQ section is detected
- **HowTo** — Generated for how-to guide content types
- **BreadcrumbList** — Generated for site navigation context

## Article Schema Template
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Post Title",
  "description": "Meta description",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://www.99minds.io/team/author"
  },
  "publisher": {
    "@type": "Organization",
    "name": "99minds",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.99minds.io/logo.png"
    }
  },
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "image": "https://www.99minds.io/blog/images/post-hero.jpg",
  "url": "https://www.99minds.io/blog/post-slug"
}
```

## Output
Generates `<script type="application/ld+json">` blocks to paste into post head or CMS custom fields.
