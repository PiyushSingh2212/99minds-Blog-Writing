"""
conftest.py - pytest configuration and shared fixtures for 99minds blog tests
"""
import pytest
import os
import tempfile


@pytest.fixture
def sample_good_post():
    """A well-structured blog post that should score 70+."""
    return """---
title: "How to Build a Customer Loyalty Program: Complete Guide"
meta_description: "Learn how to build a customer loyalty program that drives repeat purchases. Step-by-step guide with examples from top brands."
slug: "how-to-build-customer-loyalty-program"
author: "99minds Team"
date: "2026-05-01"
tags: [loyalty, rewards, customer-retention]
---

# How to Build a Customer Loyalty Program: Complete Guide

Building a customer loyalty program is one of the most effective strategies for increasing customer lifetime value and reducing churn. According to a 2024 study by Bain & Company, increasing customer retention by just 5% can boost profits by 25-95%.

## What Is a Customer Loyalty Program?

A customer loyalty program is a structured marketing strategy that rewards repeat customers with points, discounts, or exclusive perks. The goal is to incentivize continued purchases and deepen brand relationships.

## Types of Loyalty Programs

### Points-Based Programs

Points-based programs reward customers for every dollar spent. Customers accumulate points and redeem them for discounts or free products.

### Tiered Programs

Tiered programs like Gold, Silver, and Platinum create aspirational goals for customers to unlock better benefits.

### Cashback Programs

Cashback programs return a percentage of purchases as credit, offering straightforward value with high perceived benefit.

## How to Set Up a Loyalty Program

Follow these steps to launch your loyalty program:

- Define your reward structure
- Choose your platform (like 99minds)
- Set up tiers and point values
- Integrate with your e-commerce store
- Launch and promote to existing customers

## Common Mistakes to Avoid

Many businesses make the mistake of offering rewards that are too hard to redeem. According to research from Merkle, 54% of loyalty program members are inactive because rewards feel unattainable.

## FAQ

**Q: How much does it cost to build a loyalty program?**
A: Costs vary by platform. 99minds offers flexible pricing starting at no cost for small programs.

**Q: How long does setup take?**
A: With a modern platform like 99minds, you can launch in under a day.

**Q: What rewards work best?**
A: Research shows cashback and points-for-dollars are the most popular reward types among consumers.

## Conclusion

Building a customer loyalty program doesn't have to be complex. Start with a clear reward structure, pick the right platform, and iterate based on customer feedback.

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "Article", "headline": "How to Build a Customer Loyalty Program"}
</script>
"""


@pytest.fixture
def sample_poor_post():
    """A minimal blog post that should score below 70."""
    return """# Short Post

This is a short post about loyalty programs. They are good for business.
Customers like rewards.
"""


@pytest.fixture
def tmp_post_file(tmp_path, sample_good_post):
    """Create a temporary markdown file with good content."""
    post_file = tmp_path / "test_post.md"
    post_file.write_text(sample_good_post, encoding="utf-8")
    return str(post_file)


@pytest.fixture
def tmp_poor_file(tmp_path, sample_poor_post):
    """Create a temporary markdown file with poor content."""
    post_file = tmp_path / "poor_post.md"
    post_file.write_text(sample_poor_post, encoding="utf-8")
    return str(post_file)
