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
      "url": "https://www.99minds.io/logos/99minds-logo-b.svg"
    }
  },
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "image": "https://www.99minds.io/blog/images/post-hero.jpg",
  "url": "https://www.99minds.io/blog/post-slug"
}
```

## FAQPage Schema Template
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question text here?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Answer text here."
      }
    }
  ]
}
```

## HowTo Schema Template
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to [Topic]",
  "description": "Meta description text.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Step 1 heading",
      "text": "Step 1 description."
    },
    {
      "@type": "HowToStep",
      "name": "Step 2 heading",
      "text": "Step 2 description."
    }
  ]
}
```

## BreadcrumbList Schema Template
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Blog",
      "item": "https://www.99minds.io/blog"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Post Title",
      "item": "https://www.99minds.io/blog/post-slug"
    }
  ]
}
```

## Output
Combine all applicable schema types into a **single** `<script type="application/ld+json">` block placed at the **end of the post file**, before the closing tag. Do not split schemas across multiple script blocks and do not place them in the `<head>`.
