"""
test_analyze_blog.py - Tests for the blog quality analysis script
"""
import pytest
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from analyze_blog import (
    load_markdown,
    extract_frontmatter,
    count_words,
    score_content_quality,
    score_seo,
    score_eeat,
    score_technical,
    score_ai_readiness,
    detect_ai_content,
    get_rating,
    analyze,
)


class TestExtractFrontmatter:
    def test_extracts_title(self):
        content = "---\ntitle: Test Post\n---\nBody"
        fm = extract_frontmatter(content)
        assert fm.get("title") == "Test Post"

    def test_extracts_author(self):
        content = "---\nauthor: 99minds Team\n---\nBody"
        fm = extract_frontmatter(content)
        assert fm.get("author") == "99minds Team"

    def test_no_frontmatter(self):
        content = "# Just a heading\nSome content"
        fm = extract_frontmatter(content)
        assert fm == {}


class TestCountWords:
    def test_basic_count(self):
        content = "# Title\nThis is a sentence with seven words total."
        wc = count_words(content)
        assert wc >= 7

    def test_excludes_frontmatter(self):
        content = "---\ntitle: Post\nauthor: Name\n---\nHello world"
        wc = count_words(content)
        assert wc == 2


class TestScoreContentQuality:
    def test_high_score_long_content(self, sample_good_post):
        wc = count_words(sample_good_post)
        score, issues = score_content_quality(sample_good_post, wc)
        assert score >= 20, f"Expected 20+, got {score}. Issues: {issues}"

    def test_low_score_short_content(self, sample_poor_post):
        wc = count_words(sample_poor_post)
        score, issues = score_content_quality(sample_poor_post, wc)
        assert score < 20
        assert any("short" in i.lower() for i in issues)


class TestScoreSEO:
    def test_good_post_seo_score(self, sample_good_post):
        fm = extract_frontmatter(sample_good_post)
        score, issues = score_seo(sample_good_post, fm)
        assert score >= 15, f"Expected 15+, got {score}. Issues: {issues}"

    def test_missing_meta_description(self):
        content = "---\ntitle: Test\n---\n# Test\n\n" + "Word " * 500
        fm = extract_frontmatter(content)
        score, issues = score_seo(content, fm)
        assert any("meta" in i.lower() for i in issues)


class TestScoreEEAT:
    def test_has_author_and_date(self, sample_good_post):
        fm = extract_frontmatter(sample_good_post)
        score, issues = score_eeat(sample_good_post, fm)
        assert score >= 10

    def test_missing_author(self):
        content = "---\ndate: 2026-01-01\n---\nContent"
        fm = extract_frontmatter(content)
        score, issues = score_eeat(content, fm)
        assert any("author" in i.lower() for i in issues)


class TestDetectAIContent:
    def test_clean_content(self, sample_good_post):
        result = detect_ai_content(sample_good_post)
        assert result["status"] in ["Clean", "Suspicious"]

    def test_detects_ai_phrases(self):
        ai_content = "In today's digital landscape, it's important to note that synergy is a game-changer. Needless to say, cutting-edge leverage is key."
        result = detect_ai_content(ai_content)
        assert result["phrases_found"] >= 3
        assert result["status"] in ["Suspicious", "Likely AI"]


class TestGetRating:
    def test_rating_bands(self):
        assert get_rating(95) == "Exceptional"
        assert get_rating(85) == "Strong"
        assert get_rating(75) == "Acceptable"
        assert get_rating(65) == "Below Standard"
        assert get_rating(50) == "Rewrite Required"


class TestAnalyze:
    def test_good_post_passes(self, tmp_post_file):
        result = analyze(tmp_post_file)
        assert result["total"] >= 70, f"Good post scored {result['total']}, expected 70+"
        assert result["rating"] in ["Acceptable", "Strong", "Exceptional"]

    def test_poor_post_fails(self, tmp_poor_file):
        result = analyze(tmp_poor_file)
        assert result["total"] < 70

    def test_result_structure(self, tmp_post_file):
        result = analyze(tmp_post_file)
        assert "total" in result
        assert "rating" in result
        assert "word_count" in result
        assert "scores" in result
        assert "ai_detection" in result
        assert "issues" in result

    def test_scores_sum_to_total(self, tmp_post_file):
        result = analyze(tmp_post_file)
        scores_sum = sum(result["scores"].values())
        assert scores_sum == result["total"]
