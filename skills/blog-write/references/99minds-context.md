# 99minds Product Context

Reference this file when you need clarity on 99minds features, pricing, integrations, or positioning. All feature details below are sourced directly from 99minds dashboard screenshots.

---

## What is 99minds?

99minds is an **all-in-one loyalty and rewards platform** for e-commerce businesses. It enables merchants to launch and scale customer loyalty programs without complex development work — no-code setup, API-first architecture.

**Website**: https://www.99minds.io  
**Blog**: https://www.99minds.io/blog  
**Logo**: https://www.99minds.io/logos/99minds-logo-b.svg

---

## Platform Overview

The 99minds dashboard left nav contains: Dashboard, Gift Cards, Store Credits, Loyalty Points, VIP Tiers, Membership, Referrals, Coupons, Workflows, Orders, Customers, Reports, Branding, Themes, Emails, SMS, Widgets, Configure, Integrations, Settings.

Top bar includes: multi-store selector, Upgrade, Web POS, B2B, Help.

The main Dashboard shows at a glance: Total Cards, Cards In Stock, Cards Sold, Cards Sold Amount, Digital vs. Physical card breakdowns, Cards Redeemed, Value Redeemed, Average Redeem Value.

---

## Core Features (Dashboard-Verified)

### 1. Gift Cards

**Platform description**: Issue new gift cards, or view and manage the already issued ones. Reload a card, extend expiry, deactivate, or block it permanently.

**Dashboard sections**: All Gift Cards, Campaigns, Manage Gift Cards, Issue Bulk Gift Cards, Batches, Transactions, Promotions, Promotion Codes.

**Key capabilities**:
- Issue Digital Gift Cards and Physical Gift Cards separately
- Group gift cards under named Campaigns (e.g., holiday campaign, co-marketing campaign)
- Multi-currency support (USD, EUR, GBP)
- 14-16 character card number formats
- Bulk gift card issuance via CSV or manual entry
- Reload card balance, extend expiry date, deactivate, or permanently block a card
- Promotions and Promotion Codes subsections for gift card-specific promo offers
- Batches: manage large groups of gift cards together

**Use cases to reference in blogs**: B2B gifting, branded digital gift cards, holiday campaigns, refund-as-gift-card, physical gift cards for retail/POS, co-marketing partner campaigns with custom card batches.

---

### 2. Store Credits

**Platform description**: Send Store Credits to customers as a reward, refund, or an upsell tool. You can also print your store credits physically on a card to share them with customers at your retail store.

**Dashboard sections**: All Store Credits, Bulk Create, Configure, Manage.

**Key capabilities**:
- Adjust Store Credit per customer: Add credits (issue to customer) or Remove credits (debit balance)
- Re-issue Store Credit (replace a card)
- Disable a store credit card
- Bulk Issue Store Credits
- Bulk Create Store Credit Cards
- Configure Store Credits (rules, expiry settings)
- Manage Store Credits (view all active credits by customer)
- Transaction types visible: CREATION, ASSIGN, RELOAD

**Per-card detail view shows**: Status (Active/Disabled), Balance, Customer, Card ID, Recent Transactions with amount, expiration date, client order ID, date, type, and source.

**Use cases**: Refunds that keep revenue in store, post-purchase rewards, return-to-store incentives, retail store credit cards, upsell credits for high-spend customers.

---

### 3. Loyalty Points

**Platform description**: Reward your repeat customers and encourage loyalty and purchase habits.

**Dashboard sections**: All Loyalty Points, Bulk Create, Configure, Manage.

**Key capabilities**:
- Issue and track points per customer via unique loyalty card numbers (format: XXXX-XXXXX)
- Adjust Points modal: Select Customer, Add points / Debit points, set Points amount, optional Point Expiry, Customer Note (shown to customer), internal Note
- Bulk Issue via manual entry or CSV
- Pass Notification: push notifications directly to the customer's mobile wallet pass
- Opt customer into loyalty program from dashboard
- Transaction types: MANUAL_DEBIT, RELOAD, ASSIGN, CREATION, EXPIRED

**Per-card detail view shows**: Status, current Balance (points), Customer name/email, Card ID, Recent Transactions (type, source, points, expiration date, client order ID, date).

**Customer detail page** (accessible from Loyalty Points) shows ALL rewards in one view:
- VIP tier status, Birthday, Anniversary
- Opted-in loyalty status
- Store Credit balance
- Loyalty Points balance and card number
- Referral code
- VIP Tier assignment
- Recent Gift Cards, Recent Orders, Recent Coupons, Recent Loyalty History
- Quick actions: Disable, Issue Giftcard, Assign VIP Tier, Issue Coupon, Adjust Loyalty Points, View Details, Create Referral Code

**Sub-features**: Manage Loyalty Cards, Configure Loyalty Points, Bulk Create Loyalty Cards.

**Use cases**: Points per purchase, bonus points on specific products or collections, points expiry management, push notifications for point milestones, punch card programs via Workflows.

---

### 4. VIP Tiers

**Platform description**: Categorize your customers on the basis of their Lifetime Value (LTV). Issue more loyalty points and higher discounts based on their LTV/CLV with your store.

**Dashboard sections**: All Tiers, Transactions.

**Key capabilities**:
- Create unlimited VIP tiers with custom names, descriptions, and ranks
- Tier Rank: numerical hierarchy (1 = lowest; higher numbers = higher tiers) - used to detect upgrades vs. downgrades
- Enable Tier Protection: prevent customers from tier downgrades for a specified period after upgrade; customers can still be upgraded to higher tiers during this protection window
- Tier Recalculation: choose when to automatically re-evaluate customer tier assignments
- Recalculation Workflow: set which workflow to use for tier recalculation
- Assign Bulk VIP Tiers to multiple customers at once
- Rank VIP Tiers: reorder tier hierarchy from the dashboard
- Tier detail shows: Default Tier flag, tier ID, full transaction history with previous tier shown

**New VIP Tier form fields**: Name, Description, Tier Rank, Enable Tier Protection toggle, Tier Recalculation setting, Recalculation Workflow selector.

**Use cases**: LTV-based segmentation, premium tier perks (more points, exclusive discounts), tier upgrade/downgrade automation, high-value customer retention, tiered discount rates by customer spend level.

---

### 5. Membership

**Platform description**: Sell memberships to your customers and allow them to receive exclusive perks and discounts on the basis of their membership level.

**Dashboard sections**: All Memberships, Members, Transactions, Bulk Assign Membership.

**Key capabilities**:
- Create paid membership tiers (e.g., Gold, Silver, Bronze) with customizable benefits
- New Membership form: Name, Description, Membership Price, Card Number Length (default 16), Character Set, Card Prefix, Add Separator toggle, Card Expiration Period
- Membership Channel Settings: configure which channels (Shopify, Dashboard) the membership is available on
- Bulk Assign Membership to multiple customers
- Member card numbers generated per membership type
- Expiration periods configurable per tier (e.g., 180 days shown)

**Membership detail view shows**: Membership ID, Card Number Length, Card Number Prefix, Expiration Period, Channel Settings ID, list of member card numbers with customer, source, expiration date, and client order ID.

**Use cases**: Paid subscription memberships, VIP access programs, annual membership passes, exclusive perks for paying members, membership-gated discounts.

---

### 6. Referrals

**Platform description**: Turn customers into your strongest brand ambassadors with Referrals. Setup referral codes and reward your customers as well as new sign ups they bring with discounts on their next purchase.

**Dashboard sections**: All Referrals, Configure.

**Key capabilities**:
- Unique referral code generated per customer (format: REF + alphanumeric, e.g., REFUDLFS)
- Block Referral option per account
- Configure referral rewards and rules
- Referral Transactions: track friend email, coupon code issued (with store prefix, e.g., PLUSH6QKVERY), transaction type (PENDING/COMPLETED), client order ID, reference ID, created date
- Coupon codes issued to referred friends use store's custom prefix for branding consistency

**Referral detail view shows**: Customer, Status (ACTIVE), Successful Referrals count, Block Referral action, full Referral Transactions log.

**Use cases**: Dual-sided referral rewards (referrer + friend both get discounts), new customer acquisition via existing customers, brand ambassador programs, referral-triggered coupon codes.

---

### 7. Coupons

**Platform description**: Issue coupon codes independent of any promotional campaigns to boost your sales. Set up promo codes for different co-marketing campaigns with partners using distinct prefixes and suffixes.

**Dashboard sections**: All Coupons, Coupon Rules, Bulk Issue Coupons, Bulk Deactivate Coupons, Batches.

**Key capabilities**:
- Issue Coupon to specific customer: select Customer ID, Coupon Rule, add Customer Note (customer-facing), and internal Note
- Coupon Types: FREE PRODUCT, FIXED (dollar discount), PERCENT
- Coupon Rule Types: STANDARD, REFERRAL
- Coupon Rules: configure reusable rule templates with max usage, max usage per customer, min subtotal, min quantity, expiration period, coupon length, character set (LETTERS_AND_NUMBERS), custom Prefix and Suffix
- Bulk Issue Coupons and Bulk Deactivate Coupons
- Batches: group and manage sets of coupons
- Coupon detail: Resend email, Disable; shows all rule info, redemption count, last transaction type (ISSUED/REDEEMED)

**Coupon detail view shows**: Code, Status, Coupon ID, Customer, Coupon Rule title, Coupon Rule ID, Max Usage, Max Usage per Customer, Currency, Value, Expiration Period, Coupon Length, Min Quantity, Min Subtotal, Coupon Type, Coupon Rule Type, Character Set, Prefix, Suffix.

**Use cases**: One-off promotional codes, co-marketing partner campaigns (use prefix/suffix to track partner), referral friend coupons, free product coupons, bulk discount codes for events, campaign-specific coupon batches.

---

### 8. Workflows

**Platform description**: Create and manage automatic workflows. Workflows allows you to create rules for sending Store Credits, Loyalty Points, Coupons, and customer segmentation.

**Dashboard sections**: All Workflows, Cart Item Filters, Events.

**Pre-built workflow templates**:
1. Every Purchase - reward customers with store credit for every purchase
2. Average Order Value Boost - give credit based on spending amount to increase cart value
3. Punch Card - increasing rewards based on number of repeat purchases
4. VIP Loyalty Program - assign customers to VIP tiers based on lifetime spent
5. Sign Up Reward - reward customers for opening an account
6. First Purchase Reward - reward first-time buyers to become repeat customers
7. Referral Flow - reward customers for promoting the brand and sending new customers
8. Collection Promoter - gift card rewards for purchasing from a specific collection
9. Birthday Month - reward customers on their birthdays with reward points or gift cards
10. Anniversary Month - reward customers on their anniversaries with reward points or gift cards
11. Scheduled Reward - run on a recurring schedule based on a selected day
12. Create Custom Workflow - build from scratch with full control

**Workflow Triggers**: Order Paid, Anniversary Month, Account Created, Customer Loyalty Enrollment, Membership Enrolled, Membership Changed, VIP Tier Changed, Birthday Month, Order Refunded, Manual, Successful Referral, Loyalty Points Claimed.

**Event Sources**: WIDGET, SHOPIFY, DASHBOARD.

**Cart Item Filters**: filter workflow rules to apply only when specific cart items are present (product or collection-level targeting).

**Workflow Events log**: shows every triggered event with event ID, workflow ID, customer, trigger, event source, idempotent ID, and timestamp.

**Use cases**: Automated loyalty rewards, event-triggered campaigns (birthday, anniversary, sign-up), tier-change notifications, referral reward automation, order-based credit rules, punch card programs, collection-specific promotions, recurring scheduled rewards.

---

### 9. Widgets

**Platform description**: Configure the look and feel of gift card and loyalty widget.

**Available widgets**:
1. **Loyalty Widget** - customizable popup that appears on any store page (any HTML page, JavaScript CDN)
2. **Gift Card Widget** - embeddable gift card purchase/redemption widget on any HTML page (JavaScript CDN)
3. **Loyalty Page** - full dedicated loyalty program page (any HTML page, JavaScript CDN)
4. **Referral Page** - full dedicated referral program page (any HTML page, JavaScript CDN)
5. **Shopify Checkout Extensions** - embeddable at Shopify checkout; available exclusively on Shopify Plus stores
6. **Shopify POS Extensions** - check gift card balances, sell physical gift cards, redeem loyalty points directly from the POS
7. **Shopify Account Extensions** - show customers gift cards, loyalty points, store credits, referral code, and coupons inside the Shopify account section (Coming Soon)

**Sub-widget details (from screenshots)**:
- Loyalty Page Widget: dedicated page showing rewards program
- Referral Page: dedicated page with referral link sharing
- Shopify POS Extensions: specifically supports POS gift card balance check, physical card sales, and loyalty point redemption
- Shopify Checkout Extension: checkout-level widget for Shopify Plus

**Use cases**: Frontend customer-facing reward dashboards, Shopify POS loyalty, Shopify Plus checkout rewards, embedded loyalty pop-ups, gift card purchase on storefront.

---

### 10. Orders, Customers, Reports, Communications

**Orders**: View all orders associated with loyalty, gift card, and credit activity.

**Customers**: Unified customer detail page showing all reward activity across: VIP tier, Birthday, Anniversary, opted-in status, Store Credit, Loyalty Points, Referral Code, Recent Gift Cards, Recent Orders, Recent Coupons, Recent Loyalty History. Quick actions: Issue Giftcard, Assign VIP Tier, Issue Coupon, Adjust Loyalty Points, Create Referral Code.

**Reports**: Analytics and reporting on all program performance.

**Emails + SMS**: Built-in communication channels for customer notifications (reward earned, coupon issued, tier changed, birthday reward, etc.).

**Branding + Themes**: Visual customization of all customer-facing widgets and pages.

**Web POS**: Web-based point of sale for in-store redemption.

**B2B**: B2B-specific features for wholesale/business gifting.

---

## Pricing

| Plan | Price |
|---|---|
| Basic | $49/month |
| Pro | $99/month |
| Ultra | $199/month |
| Premium | $499/month |
| Enterprise | Contact for pricing |

---

## Integrations (100+)

**E-commerce platforms**: Shopify, WooCommerce, BigCommerce, Magento, Wix, Squarespace  
**Email marketing**: Klaviyo, Mailchimp, Omnisend  
**CRM**: HubSpot, Salesforce  
**POS systems**: Square, Lightspeed  
**Review platforms**: Yotpo, Okendo, Stamped  
**And 90+ more**

---

## Key Differentiators vs Competitors

- No-code setup (launch in under a day)
- API-first for developers who need custom integrations
- 100+ native integrations
- Supports multiple reward types in one platform: points + gift cards + store credit + referrals + memberships + VIP tiers + coupons + workflows
- Shopify Plus Checkout Extensions (exclusive Shopify Plus feature)
- Shopify POS Extensions (in-store loyalty and gift card redemption)
- Workflow automation with 12 pre-built templates and custom builder
- Affordable pricing starting at $49/month

---

## Ratings & Reviews

**Shopify App Store**: 5/5 (30+ reviews)  
**G2**: 5/5 (5 reviews)

Common praise: easy to set up, responsive customer support, flexible reward rules, good value for money.  
Common limitations (real, from reviews - don't be harsh): smaller review count vs. larger competitors, some advanced customization requires developer help.

---

## Feature-to-Blog-Topic Mapping

Use this to match blog topics to the right 99minds feature to highlight:

| Blog topic | Primary 99minds feature to highlight |
|---|---|
| Loyalty programs, repeat purchase, customer retention | Loyalty Points, Workflows (Every Purchase, Punch Card), VIP Tiers |
| Gift card marketing, gifting, B2B gifting | Gift Cards, Campaigns, Bulk Issue, Promotions |
| Refund alternatives, store credit | Store Credits (refund-as-credit positioning) |
| Referral programs, word of mouth | Referrals, Workflows (Referral Flow) |
| Tiered programs, VIP, premium customers | VIP Tiers, Membership |
| Subscription / paid membership | Membership |
| Birthday and anniversary marketing | Workflows (Birthday Month, Anniversary Month triggers) |
| Coupon marketing, promo codes, co-marketing | Coupons, Coupon Rules (prefix/suffix for partner campaigns) |
| Shopify loyalty, Shopify rewards | Widgets (Shopify Checkout Extension, POS Extension, Account Extension) |
| Customer segmentation | VIP Tiers, Workflows (customer segmentation rules) |
| Email/SMS loyalty marketing | Emails, SMS, Workflows (automated triggers) |
| Punch card programs | Workflows (Punch Card template) |
| First purchase, new customer conversion | Workflows (First Purchase Reward, Sign Up Reward) |
| AOV optimization, upsell | Workflows (Average Order Value Boost), Store Credits (upsell tool) |
| Collection-specific promotions | Workflows (Collection Promoter), Cart Item Filters |

---

## Brand Voice Reminder

- Conversational, jargon-free, easy to understand
- Address reader as "you"; use "we" for 99minds
- Use contractions (it's, we're, you'll)
- Oxford commas required
- NEVER use em dashes (-). Use commas, colons, semicolons, or hyphens instead
- Screenshots: always use dashboard view, never homepage

---

## CTA Options by Funnel Stage

**TOFU**: "Learn more about 99minds" or brief mention in conclusion  
**MOFU**: "See how 99minds can help" or "Try 99minds for your store"  
**BOFU**: "Start your free trial" or "Get started with 99minds today"
