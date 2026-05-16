---
name: blog-analyze
description: Run a comprehensive quality audit on a blog post and return a 0-100 score with actionable feedback.
version: 1.0.0
author: PiyushSingh2212
---

# Blog Analyze Skill

## Usage
```
/blog analyze <file>
```

## Scoring Rubric (100 Points Total)

### 1. Content Quality (30 pts)
- Depth and comprehensiveness (10 pts)
- Readability and clarity (10 pts)
- Originality and engagement (10 pts)

### 2. SEO Optimization (25 pts)
- Title and H1 optimization (5 pts)
- Heading structure (H2/H3) (5 pts)
- Keyword usage and density (5 pts)
- Meta description quality (5 pts)
- Internal/external linking (5 pts)

### 3. E-E-A-T Signals (15 pts)
- Author expertise signals (5 pts)
- Citations and sources (5 pts)
- Trust indicators (5 pts)

### 4. Technical Elements (15 pts)
- Schema markup present (5 pts)
- Image optimization (5 pts)
- Mobile/performance considerations (5 pts)

### 5. AI Citation Readiness (15 pts)
- Answer-first formatting (5 pts)
- FAQ/Q&A sections (5 pts)
- Entity clarity and passage citability (5 pts)

## Score Bands
| Score | Rating |
|---|---|
| 90-100 | Exceptional |
| 80-89 | Strong |
| 70-79 | Acceptable |
| 60-69 | Below Standard |
| <60 | Rewrite Required |

## AI Content Detection
- Checks for 17 common AI phrases
- Vocabulary diversity (TTR score)
- Sentence burstiness analysis
- Flags: Clean / Suspicious / Likely AI

## Output Format
```
QUALITY REPORT: filename.md
Overall Score: 82/100 — Strong

Content Quality:    26/30
SEO Optimization:   21/25
E-E-A-T Signals:   11/15
Technical Elements: 12/15
AI Citation Ready:  12/15

AI Detection: Clean (TTR: 0.68)

TOP ISSUES:
1. Missing JSON-LD schema (-5)
2. No author byline (-4)
3. Meta description too long (-3)

RECOMMENDATIONS:
...
```
