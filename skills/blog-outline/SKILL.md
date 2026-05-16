---
name: blog-outline
description: Create a SERP-informed, keyword-optimized content outline before writing a blog post.
version: 1.0.0
author: PiyushSingh2212
---

# Blog Outline Skill

## Usage
```
/blog outline <topic>
```

## Process
1. Analyze top 5 SERP results for the topic
2. Extract common H2/H3 patterns
3. Identify unique angles not covered by competitors
4. Map keywords to each section
5. Estimate word count per section
6. Flag 99minds integration points

## Output Format
```markdown
# [H1 Title — Primary Keyword]
**Meta:** [155-char meta description]
**Intent:** [Informational/Commercial/Transactional]
**Target Words:** [N]

## Introduction (~150 words)
Hook: [Angle]
Keywords: [primary keyword]

## [H2 Section 1] (~300 words)
- [H3 sub-point]
- [H3 sub-point]
Keywords: [secondary keyword]

## [H2 Section 2] (~300 words)
...

## FAQ (~200 words)
- Q: [long-tail question]
- Q: [long-tail question]

## Conclusion + CTA (~150 words)
CTA: [Specific action]
```
