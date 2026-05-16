---
name: blog-factcheck
description: Verify all statistics, data points, and claims in a blog post against their cited sources.
version: 1.0.0
author: PiyushSingh2212
---

# Blog Factcheck Skill

## Usage
```
/blog factcheck <file>
```

## What Gets Checked
- All numerical statistics (percentages, dollar figures, user counts)
- Research study citations
- Market data and industry reports
- Product claims about 99minds
- Year of data (flags stats older than 3 years)
- Source URL validity

## Verification Process
1. Extract all claims with citation markers
2. For each claim, check:
   - Source URL resolves (HTTP 200)
   - Claim matches source content
   - Data is within acceptable date range (< 3 years)
3. Score each claim:
   - **Verified**: Exact match in source
   - **Paraphrase**: Meaning matches, wording differs
   - **Unverifiable**: Source not accessible
   - **Incorrect**: Claim contradicts source
   - **Outdated**: Data is older than 3 years

## Output
```
FACTCHECK REPORT: filename.md
Claims checked: 12
Verified: 8 (67%)
Paraphrase: 2 (17%)
Unverifiable: 1 (8%)
Incorrect: 1 (8%)

ISSUES:
[Line 45] "73% of consumers prefer brands with loyalty programs"
  Status: INCORRECT - Source says 68%, not 73%
  Source: Nielsen 2023 Loyalty Report
  Fix: Change to "68%"

[Line 78] "Source URL broken"
  Status: UNVERIFIABLE - URL returns 404
  Fix: Find alternative source or remove claim
```
