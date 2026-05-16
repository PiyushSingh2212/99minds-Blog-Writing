---
name: blog-calendar
description: Generate a 30/60/90-day editorial calendar for 99minds blog with topic ideas, keyword targets, and publishing schedule.
version: 1.0.0
author: PiyushSingh2212
---

# Blog Calendar Skill

## Usage
```
/blog calendar
/blog calendar --days 30
/blog calendar --days 90
```

## What This Generates
A structured editorial calendar with:
- Post titles and target keywords
- Content type (how-to, listicle, case study, etc.)
- Estimated word count
- Publishing date
- Funnel stage (TOFU/MOFU/BOFU)
- Assigned persona/author
- Status (planned/in-progress/published)

## Calendar Strategy for 99minds
- **TOFU (40%)**: Awareness content — loyalty program trends, rewards industry stats
- **MOFU (40%)**: Consideration — how-to guides, comparisons, case studies
- **BOFU (20%)**: Conversion — 99minds features, pricing guides, success stories

## Output Format
Markdown table + JSON export option

| Date | Title | Keyword | Type | Stage | Words |
|---|---|---|---|---|---|
| 2026-06-01 | How to Build a Loyalty Program | loyalty program setup | how-to | TOFU | 2000 |
