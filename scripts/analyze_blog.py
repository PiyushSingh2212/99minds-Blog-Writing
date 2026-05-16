#!/usr/bin/env python3
"""
analyze_blog.py - 99minds Blog Quality Analysis Script
Scores blog posts 0-100 across 5 categories.

Usage:
    python scripts/analyze_blog.py <file.md>
    python scripts/analyze_blog.py ./content/blog/ --all

Requirements (optional, for advanced scoring):
    pip install textstat beautifulsoup4
"""

import re
import sys
import os
from pathlib import Path
from typing import Optional

# Optional advanced imports
try:
    import textstat
    HAS_TEXTSTAT = True
except ImportError:
    HAS_TEXTSTAT = False

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


# Known AI phrases that flag generic content
AI_PHRASES = [
    "in today's digital landscape",
    "it's important to note",
    "in conclusion",
    "it goes without saying",
    "needless to say",
    "as we move forward",
    "in the ever-evolving",
    "it is worth noting",
    "at the end of the day",
    "game-changer",
    "cutting-edge",
    "leverage",
    "synergy",
    "paradigm shift",
    "deep dive",
    "touch base",
    "circle back",
]


def load_markdown(filepath: str) -> str:
    """Load and return markdown file content."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown."""
    fm = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    key, _, val = line.partition(":")
                    fm[key.strip()] = val.strip()
    return fm


def count_words(content: str) -> int:
    """Count words in content (excluding frontmatter)."""
    # Remove frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2]
    # Remove markdown syntax
    content = re.sub(r"#{1,6}\s+", "", content)
    content = re.sub(r"\*{1,2}|_{1,2}|~~|\[|\]|\(|\)", "", content)
    return len(content.split())


def score_content_quality(content: str, word_count: int) -> tuple[int, list]:
    """Score content quality (max 30 pts)."""
    score = 0
    issues = []

    # Word count (10 pts)
    if word_count >= 2500:
        score += 10
    elif word_count >= 1500:
        score += 7
    elif word_count >= 1000:
        score += 5
    elif word_count >= 600:
        score += 3
    else:
        issues.append(f"Content too short ({word_count} words, target 1500+)")

    # Readability (10 pts)
    if HAS_TEXTSTAT:
        fre = textstat.flesch_reading_ease(content)
        if 50 <= fre <= 70:
            score += 10
        elif 40 <= fre < 50 or 70 < fre <= 80:
            score += 7
        else:
            score += 4
            issues.append(f"Readability score {fre:.0f} (target 50-70)")
    else:
        score += 7  # default if textstat unavailable

    # Structure/engagement (10 pts)
    has_intro = bool(re.search(r"^(?!#).+", content, re.MULTILINE))
    has_conclusion = bool(re.search(r"(?i)conclusion|summary|key takeaway|next step", content))
    has_lists = bool(re.search(r"^[-*]\s+", content, re.MULTILINE))
    has_bold = bool(re.search(r"\*\*[^*]+\*\*", content))

    if has_intro:
        score += 3
    if has_conclusion:
        score += 3
    else:
        issues.append("Missing conclusion or next steps section")
    if has_lists:
        score += 2
    if has_bold:
        score += 2

    return min(score, 30), issues


def score_seo(content: str, frontmatter: dict) -> tuple[int, list]:
    """Score SEO optimization (max 25 pts)."""
    score = 0
    issues = []

    # Title (5 pts)
    title = frontmatter.get("title", "")
    h1_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title or h1_match:
        title_text = title or (h1_match.group(1) if h1_match else "")
        if 40 <= len(title_text) <= 65:
            score += 5
        elif len(title_text) > 0:
            score += 3
            issues.append(f"Title length {len(title_text)} chars (target 40-65)")
    else:
        issues.append("Missing H1 title")

    # Meta description (5 pts)
    meta = frontmatter.get("meta_description", frontmatter.get("description", ""))
    if meta:
        if 120 <= len(meta) <= 160:
            score += 5
        elif len(meta) > 0:
            score += 3
            issues.append(f"Meta description {len(meta)} chars (target 120-160)")
    else:
        issues.append("Missing meta description")

    # Headings (5 pts)
    h2_count = len(re.findall(r"^## ", content, re.MULTILINE))
    if h2_count >= 3:
        score += 5
    elif h2_count >= 2:
        score += 3
    else:
        issues.append(f"Only {h2_count} H2 headings (target 3+)")

    # Internal links (5 pts)
    internal_links = len(re.findall(r"\[.+?\]\(/[^)]+\)", content))
    if internal_links >= 2:
        score += 5
    elif internal_links >= 1:
        score += 3
    else:
        issues.append("No internal links found")

    # FAQ section (5 pts)
    has_faq = bool(re.search(r"(?i)## .*faq|frequently asked", content))
    if has_faq:
        score += 5
    else:
        issues.append("Missing FAQ section")

    return min(score, 25), issues


def score_eeat(content: str, frontmatter: dict) -> tuple[int, list]:
    """Score E-E-A-T signals (max 15 pts)."""
    score = 0
    issues = []

    # Author (5 pts)
    author = frontmatter.get("author", "")
    if author:
        score += 5
    else:
        issues.append("Missing author byline")

    # Citations (5 pts)
    citation_patterns = [r"according to", r"study by", r"research from", r"source:", r"\[\d+\]"]
    has_citations = any(re.search(p, content, re.IGNORECASE) for p in citation_patterns)
    if has_citations:
        score += 5
    else:
        issues.append("No citations or external sources found")

    # Date (5 pts)
    date = frontmatter.get("date", frontmatter.get("published", ""))
    if date:
        score += 5
    else:
        issues.append("Missing publication date")

    return min(score, 15), issues


def score_technical(content: str) -> tuple[int, list]:
    """Score technical elements (max 15 pts)."""
    score = 0
    issues = []

    # Schema markup (5 pts)
    has_schema = bool(re.search(r"application/ld\+json|@context.*schema\.org", content))
    if has_schema:
        score += 5
    else:
        issues.append("Missing JSON-LD schema markup")

    # Images (5 pts)
    img_count = len(re.findall(r"!\[", content))
    if img_count >= 2:
        score += 5
    elif img_count >= 1:
        score += 3
    else:
        issues.append("No images found (target 2+)")

    # Open Graph (5 pts)
    has_og = bool(re.search(r"og:title|og:description|open.graph", content, re.IGNORECASE))
    if has_og:
        score += 5
    else:
        issues.append("Missing Open Graph meta tags")

    return min(score, 15), issues


def score_ai_readiness(content: str) -> tuple[int, list]:
    """Score AI citation readiness (max 15 pts)."""
    score = 0
    issues = []

    # Answer-first (5 pts)
    first_para = re.search(r"^(?!#|\[|!).+", content.split("\n\n")[1] if "\n\n" in content else content, re.MULTILINE)
    if first_para and len(first_para.group(0)) > 50:
        score += 5

    # FAQ (5 pts)
    faq_questions = len(re.findall(r"\*\*Q:|^#+.*\?|^\?", content, re.MULTILINE))
    if faq_questions >= 3:
        score += 5
    elif faq_questions >= 1:
        score += 3
    else:
        issues.append("Add FAQ questions for AI citability (target 3+)")

    # Entity clarity (5 pts)
    # Check for clear entity definitions
    entity_patterns = [r"is a ", r"refers to", r"defined as", r"which means"]
    has_definitions = any(re.search(p, content, re.IGNORECASE) for p in entity_patterns)
    if has_definitions:
        score += 5

    return min(score, 15), issues


def detect_ai_content(content: str) -> dict:
    """Detect AI-generated content patterns."""
    found_phrases = [p for p in AI_PHRASES if p.lower() in content.lower()]
    words = content.lower().split()
    unique_ratio = len(set(words)) / len(words) if words else 0

    status = "Clean"
    if len(found_phrases) >= 5 or unique_ratio < 0.35:
        status = "Likely AI"
    elif len(found_phrases) >= 2 or unique_ratio < 0.45:
        status = "Suspicious"

    return {
        "status": status,
        "phrases_found": len(found_phrases),
        "ttr": round(unique_ratio, 3),
        "flagged_phrases": found_phrases[:5],
    }


def get_rating(score: int) -> str:
    if score >= 90:
        return "Exceptional"
    elif score >= 80:
        return "Strong"
    elif score >= 70:
        return "Acceptable"
    elif score >= 60:
        return "Below Standard"
    else:
        return "Rewrite Required"


def analyze(filepath: str) -> dict:
    """Run full analysis on a blog post file."""
    content = load_markdown(filepath)
    frontmatter = extract_frontmatter(content)
    word_count = count_words(content)

    cq_score, cq_issues = score_content_quality(content, word_count)
    seo_score, seo_issues = score_seo(content, frontmatter)
    eeat_score, eeat_issues = score_eeat(content, frontmatter)
    tech_score, tech_issues = score_technical(content)
    ai_score, ai_issues = score_ai_readiness(content)
    ai_detection = detect_ai_content(content)

    total = cq_score + seo_score + eeat_score + tech_score + ai_score
    all_issues = cq_issues + seo_issues + eeat_issues + tech_issues + ai_issues

    return {
        "file": filepath,
        "total": total,
        "rating": get_rating(total),
        "word_count": word_count,
        "scores": {
            "content_quality": cq_score,
            "seo_optimization": seo_score,
            "eeat_signals": eeat_score,
            "technical": tech_score,
            "ai_citation_readiness": ai_score,
        },
        "ai_detection": ai_detection,
        "issues": all_issues,
    }


def print_report(result: dict) -> None:
    """Print a formatted quality report."""
    print(f"\n{'='*60}")
    print(f"QUALITY REPORT: {os.path.basename(result['file'])}")
    print(f"{'='*60}")
    print(f"Overall Score:  {result['total']}/100 — {result['rating']}")
    print(f"Word Count:     {result['word_count']} words")
    print()
    print(f"Content Quality:      {result['scores']['content_quality']}/30")
    print(f"SEO Optimization:     {result['scores']['seo_optimization']}/25")
    print(f"E-E-A-T Signals:      {result['scores']['eeat_signals']}/15")
    print(f"Technical Elements:   {result['scores']['technical']}/15")
    print(f"AI Citation Ready:    {result['scores']['ai_citation_readiness']}/15")
    print()
    ai = result["ai_detection"]
    print(f"AI Detection: {ai['status']} (TTR: {ai['ttr']}, Phrases: {ai['phrases_found']})")
    if result["issues"]:
        print(f"\nTop Issues ({len(result['issues'])}):")
        for i, issue in enumerate(result["issues"][:5], 1):
            print(f"  {i}. {issue}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/analyze_blog.py <file.md>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    result = analyze(filepath)
    print_report(result)
    sys.exit(0 if result["total"] >= 70 else 1)
