# GenAI-Friendly Content Guidelines

These rules ensure 99minds blog posts are correctly retrieved, summarized, and cited by AI systems (ChatGPT, Gemini, Perplexity, Claude, AI Overviews, etc.). Apply every rule on every post.

Source: Document360 — How to Write GenAI-Friendly Content

---

## Why This Matters

AI models chunk, index, and retrieve content differently from humans. A page that ranks well in Google can still be invisible to AI if it's structured poorly. GenAI-friendly content is structured so that:
- Each section is independently understandable without surrounding context
- AI can extract a complete, accurate answer from any single section or paragraph
- The full article is machine-scannable without ambiguity

---

## Rule 1 — Sentence Length

**Keep sentences under 20 words.** Long, compound sentences confuse AI parsers and produce garbled citations.

- ✅ "Promotional codes with no usage limit erode perceived value."
- ❌ "While promotional codes can be effective tools for acquisition and retention, those that are deployed without appropriate usage limits or expiry windows tend to erode perceived value over time."

Split any sentence over 20 words into two.

---

## Rule 2 — One Idea Per Paragraph

Each paragraph covers exactly one idea. Do not bundle two concepts in one paragraph even if they're related. AI summarizes paragraph by paragraph — a bundled paragraph produces an incomplete or blended summary.

- ✅ Write a paragraph on what a promotional code is. Write a separate paragraph on how it differs from a coupon code.
- ❌ "A promotional code is X. It differs from a coupon code in Y. Some merchants also confuse it with Z."

---

## Rule 3 — Section Length Cap

**Keep each H2 section under ~375 words** (roughly 500 tokens). Sections longer than this are harder for AI to summarize accurately. If a section runs longer, split it into two H2 sections or move supporting detail into a sub-section under an H3.

---

## Rule 4 — Self-Contained List Items

Every bullet point must function as a standalone statement. AI extracts lists item by item — if an item relies on the surrounding text for meaning, it becomes unintelligible when cited in isolation.

- ✅ "Set a maximum per-customer usage limit of one to prevent code-stacking."
- ❌ "Set it to one." (relies on previous sentence to explain what "it" refers to)
- ✅ "Use an expiry window of 24-72 hours to create urgency without frustrating customers."
- ❌ "Use a short window." (vague - AI cannot infer the appropriate timeframe)

Lists should have 3-7 items. Use parallel structure across all items in the same list.

---

## Rule 5 — Self-Contained FAQ Answers

FAQ answers are the highest-value content for AI citation - they're extracted verbatim as direct answers to user queries. Every FAQ answer must:
- Be fully self-contained: answerable without reading the surrounding article
- Restate the key terms from the question (don't start with "Yes" or "It depends" without context)
- Be 2-5 sentences: long enough to be complete, short enough to be cited
- Contain no internal links (links break the citation and confuse AI extraction)

- ✅ "A promotional code is an alphanumeric string customers enter at checkout to receive a discount, free shipping, or a free product. Unlike automatic discounts, promotional codes require active entry, which lets merchants control who receives the offer and how many times it can be used."
- ❌ "Yes, they work great. See the section above for more details."

---

## Rule 6 — Answer-First at Every H2

The first sentence of every H2 section must state the main point directly. AI retrieves the opening sentence of a section as the primary answer to a query matching that heading. Burying the answer in the third sentence loses the citation.

- ✅ "Percentage discount codes work best for cart abandonment and seasonal campaigns."
- ❌ "There are many ways to think about discount code types. Some merchants prefer percentage-based while others use fixed amounts. Let's explore the differences."

---

## Rule 7 — Descriptive Anchor Text

Anchor text must describe the destination article's specific topic. AI uses anchor text to infer the relationship between articles and build its knowledge graph of the site.

- ✅ `<a href="...">how to build a loyalty program for small businesses</a>`
- ✅ `<a href="...">BOGO vs. volume discounts</a>`
- ❌ `<a href="...">click here</a>`
- ❌ `<a href="...">learn more</a>`
- ❌ `<a href="...">this article</a>`

---

## Rule 8 — Functional Alt Text on Images

Alt text for dashboard screenshots must describe what the image functionally shows, not just label it. AI uses alt text to understand image content when it cannot render the image.

- ✅ `alt="99minds coupons dashboard showing coupon codes, rules, and redemption status"`
- ✅ `alt="99minds VIP Tiers dashboard with tier names, customer counts, and tier rank controls"`
- ❌ `alt="screenshot"`
- ❌ `alt="99minds dashboard"`

---

## Rule 9 — No Duplicate H2 Headings

Every H2 in an article must be unique. AI indexes headings as topic identifiers - duplicate headings create ambiguity about which section answers a given query.

---

## Rule 10 — Keyword Consistency

Use the primary keyword exactly as it appears in the target keyword list. Do not vary spelling, capitalization, or phrasing arbitrarily. AI citation accuracy drops when the same concept appears under multiple surface forms.

- Primary keyword appears in: H1 title, first paragraph, at least two H2s, meta description
- Secondary keywords appear in H2s and H3s where natural

---

## Rule 11 — Meta Description

Write the meta description as a direct answer to the implied question behind the primary keyword. It should read as a self-contained summary the reader (and AI) can act on immediately.

- ✅ "Learn what a promotional code is, the 7 types that drive conversions, how to set usage rules that protect margins, and how 99minds automates coupon distribution."
- ❌ "In this article we discuss promotional codes and how to use them for your business."

---

## GenAI Checklist (Run Before Publishing)

- [ ] Every sentence is under 20 words (or split into two)
- [ ] Every paragraph contains exactly one idea
- [ ] Every H2 section is under 375 words
- [ ] Every bullet point is self-contained (no "it", "this", "the above")
- [ ] Every FAQ answer is self-contained, 2-5 sentences, no internal links
- [ ] Every H2 opens with the answer in the first sentence
- [ ] All anchor text describes the destination article's topic
- [ ] All image alt text is functional and descriptive
- [ ] No duplicate H2 headings in the article
- [ ] Primary keyword appears in H1, first paragraph, meta description
