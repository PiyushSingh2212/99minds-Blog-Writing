# 99minds-Blog-Writing

> Claude Code skill ecosystem for 99minds blog content creation, SEO optimization, and brand management. Dual-optimized for Google rankings and AI citations.

[![CI](https://github.com/PiyushSingh2212/99minds-Blog-Writing/actions/workflows/ci.yml/badge.svg)](https://github.com/PiyushSingh2212/99minds-Blog-Writing/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Overview

**99minds-Blog-Writing** is a Claude Code skill plugin that gives Claude specialized capabilities for creating, optimizing, and managing blog content for [99minds](https://www.99minds.io) — the loyalty and rewards platform.

It brings 13 slash commands and 4 AI agents that work together to produce publication-ready content optimized for both Google rankings and AI citation platforms (ChatGPT, Perplexity, AI Overviews).

---

## Quick Start

### Plugin Install (Claude Code 1.0.33+)

```bash
# Clone and install
git clone https://github.com/PiyushSingh2212/99minds-Blog-Writing.git
cd 99minds-Blog-Writing
chmod +x install.sh && ./install.sh
```

**Windows (PowerShell):**
```powershell
.\install.ps1
```

Restart Claude Code after installation to activate.

---

## Commands

| Command | Description |
|---|---|
| `/blog write <topic>` | Write a complete blog post from scratch |
| `/blog rewrite <file>` | Optimize an existing blog post |
| `/blog analyze <file>` | Quality audit with 0-100 score |
| `/blog brief <topic>` | Generate a detailed content brief |
| `/blog calendar` | Create an editorial calendar |
| `/blog strategy <niche>` | Blog strategy and topic ideation |
| `/blog outline <topic>` | SERP-informed content outline |
| `/blog seo-check <file>` | Post-writing SEO validation |
| `/blog schema <file>` | Generate JSON-LD schema markup |
| `/blog repurpose <file>` | Repurpose for social, email, LinkedIn |
| `/blog audit [directory]` | Full-site blog health assessment |
| `/blog persona [cmd]` | Manage writing personas |
| `/blog factcheck <file>` | Verify statistics against sources |

---

## Features

### 5-Category Quality Scoring (100 Points)

| Category | Points | Focus |
|---|---|---|
| Content Quality | 30 | Depth, readability, structure, engagement |
| SEO Optimization | 25 | Title, headings, keywords, links, meta |
| E-E-A-T Signals | 15 | Author, citations, trust, expertise |
| Technical Elements | 15 | Schema, images, OG tags |
| AI Citation Readiness | 15 | Answer-first, FAQ, entity clarity |

Score bands: **Exceptional** (90-100) / **Strong** (80-89) / **Acceptable** (70-79) / **Below Standard** (60-69) / **Rewrite** (<60)

### AI Content Detection
Burstiness scoring, known AI phrase detection (17 phrases), vocabulary diversity analysis (TTR). Flags content as: Clean / Suspicious / Likely AI.

### Persona-Driven Writing
Three built-in writing personas for 99minds:
- **Industry Expert** — Technical, authoritative, data-driven (CTOs, engineers)
- **Practical Marketer** — Friendly, actionable, plain English (marketing teams)
- **Thought Leader** — Visionary, strategic (founders, executives)

### Dual Optimization
Every article targets both Google and AI platforms:
- **Google**: E-E-A-T compliance, schema markup, internal linking, keyword optimization
- **AI Citations**: Answer-first formatting, citation capsules, FAQ schema, passage-level citability

### Fact-Checking Pipeline
Verifies every statistic against cited source URLs with confidence scoring: Verified / Paraphrase / Unverifiable / Incorrect / Outdated.

---

## Architecture

```
99minds-Blog-Writing/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── skills/
│   ├── blog/SKILL.md            # Main orchestrator (routes 13 commands)
│   ├── blog-write/SKILL.md      # Full post generation
│   ├── blog-rewrite/SKILL.md    # Post optimization
│   ├── blog-analyze/SKILL.md    # Quality audit
│   ├── blog-brief/SKILL.md      # Content brief
│   ├── blog-calendar/SKILL.md   # Editorial calendar
│   ├── blog-strategy/SKILL.md   # Content strategy
│   ├── blog-outline/SKILL.md    # Content outline
│   ├── blog-seo-check/SKILL.md  # SEO validation
│   ├── blog-schema/SKILL.md     # JSON-LD schema
│   ├── blog-repurpose/SKILL.md  # Content repurposing
│   ├── blog-audit/SKILL.md      # Site-wide audit
│   ├── blog-persona/SKILL.md    # Persona management
│   └── blog-factcheck/SKILL.md  # Fact verification
├── agents/
│   ├── researcher.md            # Research agent
│   ├── writer.md                # Writing agent
│   ├── seo.md                   # SEO agent
│   └── reviewer.md              # Quality review agent
├── scripts/
│   └── analyze_blog.py          # Python quality scoring
├── tests/
│   ├── conftest.py              # pytest fixtures
│   └── test_analyze_blog.py     # Test suite
├── .github/workflows/ci.yml     # GitHub Actions CI
├── install.sh                   # Unix/macOS installer
├── install.ps1                  # Windows installer
├── pyproject.toml               # Python build config
├── requirements.txt             # Python dependencies
└── README.md
```

---

## Requirements

- **Claude Code CLI** installed and configured (v1.0.33+)
- **Python 3.11+** (for `analyze_blog.py` quality scoring)
- **Optional**: `pip install -r requirements.txt` for advanced analysis (readability scoring, schema detection)

---

## Platform Support

Next.js/MDX, Astro, Hugo, Jekyll, WordPress, Ghost, Shopify, 11ty, Gatsby, static HTML

---

## Content Templates

12 auto-selected templates based on topic and intent:

`how-to-guide` · `listicle` · `case-study` · `comparison` · `pillar-page` · `thought-leadership` · `product-review` · `roundup` · `tutorial` · `news-analysis` · `data-research` · `faq-knowledge-base`

---

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
python -m pytest tests/ -v

# Analyze a blog post
python scripts/analyze_blog.py path/to/post.md
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## About 99minds

[99minds](https://www.99minds.io) is a loyalty and rewards platform that enables businesses to launch and scale customer loyalty programs — including points, cashback, gift cards, and referral programs — with no-code setup and API-first architecture.

Built with Claude Code.
