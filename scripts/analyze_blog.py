#!/usr/bin/env python3
"""
analyze_blog.py - 99minds Blog Quality Analysis Script
Scores blog posts 0-100 across 5 categories.

Usage:
    python scripts/analyze_blog.py <file.md>
    python scripts/analyze_blog.py ./content/blog/ --all
    python scripts/analyze_blog.py ./content/blog/ --all --format csv
    python scripts/analyze_blog.py ./content/blog/ --all --format json

Requirements (optional, for advanced scoring):
    pip install textstat beautifulsoup4
"""

import re
import sys
import os
import argparse
from pathlib import Path
from typing import Optional
from datetime import datetime

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
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2]
    content = re.sub(r"#{1,6}\s+", "", content)
    content = re.sub(r"\*{1,2}|_{1,2}|~~|\[|\]|\(|\)", "", content)
    return len(content.split())


def score_content_quality(content: str, word_count: int) -> tuple[int, list]:
    """Score content quality (max 30 pts)."""
    score = 0
    issues = []

    # Word count (10 pts) — flag below 800 per audit standard
    if word_count >= 2500:
        score += 10
    elif word_count >= 1500:
        score += 7
    elif word_count >= 1000:
        score += 5
    elif word_count >= 600:
        score += 3
        if word_count < 800:
            issues.append(f"Low word count ({word_count} words, minimum 800 recommended)")
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
    # Intro: require 40+ non-heading words before first H2 (not a trivial always-true check)
    first_section = content.split("\n## ")[0] if "\n## " in content else content[:1000]
    intro_text = re.sub(r"^\s*#{1,6}\s*.+", "", first_section, flags=re.MULTILINE)
    if len(intro_text.split()) >= 40:
        score += 3
    else:
        issues.append("Weak or missing intro paragraph (target 40+ words before first section)")

    has_conclusion = bool(re.search(r"(?i)conclusion|summary|key takeaway|next step", content))
    has_lists = bool(re.search(r"^[-*]\s+", content, re.MULTILINE))
    has_bold = bool(re.search(r"\*\*[^*]+\*\*", content))

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

    # Internal links — match both markdown [text](/path) and HTML <a href="/path"> (5 pts)
    # Standard requires 20 minimum (2+ landing pages + 15+ blog posts)
    md_links = len(re.findall(r"\[.+?\]\(/[^)]+\)", content))
    html_links = len(re.findall(r'href="(/[^"]+)"', content)) + len(re.findall(r"href='(/[^']+)'", content))
    internal_links = md_links + html_links
    if internal_links >= 20:
        score += 5
    elif internal_links >= 10:
        score += 3
    elif internal_links >= 2:
        score += 1
    else:
        issues.append(
            f"Only {internal_links} internal links (target 20+: 2+ landing pages + 15+ blog posts)"
        )

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

    # Images — match both markdown ![alt](src) and HTML <img (5 pts)
    img_count = len(re.findall(r"!\[|<img\s", content))
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
    first_para = re.search(
        r"^(?!#|\[|!).+",
        content.split("\n\n")[1] if "\n\n" in content else content,
        re.MULTILINE,
    )
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


def check_outdated(filepath: str, frontmatter: dict) -> bool:
    """Return True if post is older than 12 months."""
    date_str = frontmatter.get(
        "date", frontmatter.get("published", frontmatter.get("pubDate", ""))
    )
    if date_str:
        date_str = date_str.strip("\"'")
        for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%B %d, %Y"):
            try:
                post_date = datetime.strptime(date_str[:10], fmt[:10])
                return (datetime.now() - post_date).days > 365
            except ValueError:
                continue
    # Fall back to file modification time
    mtime = os.path.getmtime(filepath)
    return (datetime.now().timestamp() - mtime) > (365 * 24 * 3600)


def find_duplicates(results: list) -> list:
    """Find post pairs with overlapping filenames/topics (keyword cannibalization)."""
    STOPWORDS = {
        "a", "an", "the", "is", "are", "how", "to", "for", "of", "in",
        "and", "or", "with", "your", "what", "why", "when", "that", "this",
    }

    def sig_words(text: str) -> set:
        return {
            w.lower().strip("\"':,-")
            for w in text.split()
            if len(w) > 3 and w.lower() not in STOPWORDS
        }

    duplicates = []
    entries = [
        (r["file"], sig_words(os.path.splitext(os.path.basename(r["file"]))[0].replace("-", " ")))
        for r in results
    ]

    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            overlap = entries[i][1] & entries[j][1]
            if len(overlap) >= 3:
                duplicates.append({
                    "file_a": entries[i][0],
                    "file_b": entries[j][0],
                    "shared_keywords": sorted(overlap),
                })
    return duplicates


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
        "outdated": check_outdated(filepath, frontmatter),
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


def scan_directory(dirpath: str) -> list:
    """Analyze all markdown and HTML blog posts in a directory."""
    results = []
    path = Path(dirpath)
    for ext in ("*.md", "*.mdx", "*.html"):
        for f in sorted(path.rglob(ext)):
            try:
                results.append(analyze(str(f)))
            except Exception as e:
                print(f"Warning: Could not analyze {f}: {e}", file=sys.stderr)
    return results


def export_csv(results: list) -> str:
    import csv
    import io
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow([
        "file", "total", "rating", "word_count", "outdated",
        "content_quality", "seo_optimization", "eeat_signals",
        "technical", "ai_citation_readiness", "ai_status", "top_issues",
    ])
    for r in results:
        writer.writerow([
            r["file"], r["total"], r["rating"], r["word_count"], r["outdated"],
            r["scores"]["content_quality"], r["scores"]["seo_optimization"],
            r["scores"]["eeat_signals"], r["scores"]["technical"],
            r["scores"]["ai_citation_readiness"],
            r["ai_detection"]["status"],
            "; ".join(r["issues"][:3]),
        ])
    return out.getvalue()


def export_json(results: list) -> str:
    import json
    return json.dumps(results, indent=2)


def print_report(result: dict) -> None:
    """Print a formatted quality report for a single post."""
    print(f"\n{'='*60}")
    print(f"QUALITY REPORT: {os.path.basename(result['file'])}")
    print(f"{'='*60}")
    print(f"Overall Score:  {result['total']}/100 — {result['rating']}")
    print(f"Word Count:     {result['word_count']} words")
    if result.get("outdated"):
        print(f"Status:         OUTDATED (last updated >12 months ago)")
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


def print_audit_report(results: list) -> None:
    """Print a summary dashboard for a directory scan."""
    if not results:
        print("No blog posts found.")
        return

    total_posts = len(results)
    avg_score = sum(r["total"] for r in results) / total_posts
    immediate = [r for r in results if r["total"] < 60]
    optimize = [r for r in results if 60 <= r["total"] < 80]
    good = [r for r in results if r["total"] >= 80]
    outdated = [r for r in results if r.get("outdated")]

    print(f"\n{'='*60}")
    print(f"BLOG AUDIT REPORT — {total_posts} posts scanned")
    print(f"{'='*60}")
    print(f"Average Score:              {avg_score:.1f}/100")
    print(f"Immediate attention  (<60): {len(immediate)} posts")
    print(f"Needs optimization (60-79): {len(optimize)} posts")
    print(f"Good shape           (80+): {len(good)} posts")
    if outdated:
        print(f"Outdated (>12 months):      {len(outdated)} posts")

    print(f"\n{'--- PRIORITIZED FIX LIST ':=<60}")

    if immediate:
        print("\n[CRITICAL] Rewrite Required (<60):")
        for r in sorted(immediate, key=lambda x: x["total"]):
            print(f"  {r['total']:3d}/100  {os.path.basename(r['file'])}")
            if r["issues"]:
                print(f"          └─ {r['issues'][0]}")

    if optimize:
        print("\n[OPTIMIZE] Below 80:")
        for r in sorted(optimize, key=lambda x: x["total"]):
            print(f"  {r['total']:3d}/100  {os.path.basename(r['file'])}")
            if r["issues"]:
                print(f"          └─ {r['issues'][0]}")

    if outdated:
        print("\n[OUTDATED] Content >12 months old:")
        for r in outdated:
            print(f"          {os.path.basename(r['file'])}")

    duplicates = find_duplicates(results)
    if duplicates:
        print(f"\n[DUPLICATES] Potential keyword cannibalization ({len(duplicates)} pairs):")
        for d in duplicates[:5]:
            print(f"  {os.path.basename(d['file_a'])} <-> {os.path.basename(d['file_b'])}")
            print(f"    Shared: {', '.join(d['shared_keywords'][:5])}")

    print(f"{'='*60}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="99minds Blog Quality Analysis Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python scripts/analyze_blog.py post.md\n"
            "  python scripts/analyze_blog.py ./content/blog/ --all\n"
            "  python scripts/analyze_blog.py ./content/blog/ --all --format csv\n"
            "  python scripts/analyze_blog.py ./content/blog/ --all --format json"
        ),
    )
    parser.add_argument("path", help="Blog post file or directory (use --all for directories)")
    parser.add_argument("--all", action="store_true", help="Scan all posts in a directory")
    parser.add_argument(
        "--format",
        choices=["markdown", "csv", "json"],
        default="markdown",
        help="Output format (default: markdown)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Path not found: {args.path}", file=sys.stderr)
        sys.exit(1)

    if args.all or os.path.isdir(args.path):
        results = scan_directory(args.path)
        if args.format == "csv":
            print(export_csv(results))
        elif args.format == "json":
            print(export_json(results))
        else:
            print_audit_report(results)
        sys.exit(0 if all(r["total"] >= 70 for r in results) else 1)
    else:
        result = analyze(args.path)
        if args.format == "csv":
            print(export_csv([result]))
        elif args.format == "json":
            print(export_json([result]))
        else:
            print_report(result)
        sys.exit(0 if result["total"] >= 70 else 1)
