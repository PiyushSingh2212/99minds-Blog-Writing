---
name: blog-audit
description: Full-site blog health assessment — scans all posts in a directory and generates a prioritized fix list.
version: 1.0.0
author: PiyushSingh2212
---

# Blog Audit Skill

## Usage
```
/blog audit
/blog audit ./content/blog
/blog audit ./posts --format csv
```

## What Gets Audited
For each blog post in the directory:
- Quality score (using blog-analyze rubric)
- SEO completeness
- Missing schema markup
- Broken or missing internal links
- Outdated content (last modified > 12 months)
- Missing meta descriptions
- Title length violations
- Duplicate topic coverage
- Low word count (<800 words)
- Missing FAQ sections
- AI content flags

## Output Report

### Summary Dashboard
- Total posts scanned
- Average quality score
- Posts needing immediate attention (score < 60)
- Posts needing optimization (score 60–79)
- Posts in good shape (score 80+)

### Prioritized Fix List
Sorted by impact potential:
1. Quick wins (easy fix, high impact)
2. Major rewrites needed
3. Posts to consolidate (keyword cannibalization)
4. Posts to delete (outdated, low quality)

### Export Formats
- Markdown report
- CSV spreadsheet
- JSON data file
