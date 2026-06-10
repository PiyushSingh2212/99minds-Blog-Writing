# 99minds Screenshot Library

All screenshots are sourced from Google Drive:
https://drive.google.com/drive/u/1/folders/1em-Y3coPYHDbd0jNq09Y2I5QrtAGysHU

Use the file IDs below with `mcp__claude_ai_Google_Drive__download_file_content` to download the image as base64, then save to `public/assets/blog/` using PowerShell:

```powershell
$base64 = "<base64 string from download tool>"
$bytes = [Convert]::FromBase64String($base64)
[IO.File]::WriteAllBytes("$env:WEBSITE_ROOT\public\assets\blog\<filename>.png", $bytes)
```

In blog HTML use:
```html
<img loading="lazy" role="img" src="/assets/blog/<filename>.png" alt="<descriptive alt text>">
```

---

## Screenshot Index by Feature

### General Dashboard
| File | Drive ID | Save as |
|---|---|---|
| 99minds Dashboard (main overview) | `14F1QgUiylSxQ_rP5iCiiaZcjs5rS_dXu` | `99minds-dashboard-overview.png` |

---

### Gift Cards
| File | Drive ID | Save as |
|---|---|---|
| Gift Card Dashboard | `1qF2cbhwXuafwaZoh1m4bw9vqgBu5j3jO` | `99minds-gift-card-dashboard.png` |

Sub-folders available (search Drive folder `1o6sF65zxxUlOY2hHK00m6LU9oUYFe9xA` for more):
- Campaigns, Issue Bulk Gift Cards, Batches, Transactions, Promotions, Promotion Codes, Manage Digital and Physical Cards, Issue E-Gift and Physical Card Manually

---

### Store Credits
| File | Drive ID | Save as |
|---|---|---|
| Store Credit Dashboard | `1hBk5qvsXuA1GpFchMUQXY4PCKeSnuuJt` | `99minds-store-credit-dashboard.png` |
| Store Credit Details (individual card) | `1t9iG9wfSE3youIU31kkrAoE0R6LIvq54` | `99minds-store-credit-details.png` |
| Adjust Store Credit (add/remove modal) | `1Kd93JKscgoMGSFZg7vis4jNm8iLUVpT-` | `99minds-adjust-store-credit.png` |
| Bulk Issue Store Credits | `15VnzTd42bbC3xYrc7z5b94h2aRtAOpeA` | `99minds-bulk-issue-store-credits.png` |
| Customer Detail (store credit view) | `1Th8-H8XRjHC4DnrIucKnUmM6JHOtkub8` | `99minds-store-credit-customer-detail.png` |

---

### Loyalty Points
| File | Drive ID | Save as |
|---|---|---|
| Loyalty Card Details | `1lYs5nUSYFlfKJybiAMrg-BO9OsFekYF6` | `99minds-loyalty-card-details.png` |
| Loyalty Card Details - Pass Notification | `1fGjk6Hnx37CqPHcO9agNZ9UeLP5j7nja` | `99minds-loyalty-pass-notification.png` |
| Loyalty Points Customer Details | `1oNlsUQzUDnj5NVcbQ9VC1fwjVGV7NYYE` | `99minds-loyalty-points-customer.png` |
| Adjust Points - Add Points | `1qUsstHqyUPw9r7Zyx_D2425qgQAIHDC2` | `99minds-adjust-loyalty-points-add.png` |
| Adjust Points - Debit Points | `1hprdoBpSv9S74s1GKrxKXYGTepv4ugIv` | `99minds-adjust-loyalty-points-debit.png` |
| Bulk Issue Loyalty - Manual | `1-RHgXlsoHc2wbcHeUZZ4qwPlMmDOZ4w7` | `99minds-bulk-issue-loyalty-manual.png` |
| Bulk Issue Loyalty - CSV | `1bp28SwjzLJ0yYByzD91skk1calYmv0Cd` | `99minds-bulk-issue-loyalty-csv.png` |

---

### VIP Tiers
| File | Drive ID | Save as |
|---|---|---|
| VIP Tiers Dashboard | `1SsdgPlMdTqIy3xCE_5N7Oniyu19oaUlx` | `99minds-vip-tiers-dashboard.png` |
| New VIP Tier (creation form) | `1FFSAab-Aa0WqPha9owfML0hVE3XQ14N2` | `99minds-new-vip-tier.png` |
| VIP Tier Details | `1NlblvQy7btKDfsqefs-JOsTgh-oBL46I` | `99minds-vip-tier-details.png` |
| Rank VIP Tiers | `1WB8kaBPY_nwTY5Z7RXtjxdFZFFRaDOhm` | `99minds-rank-vip-tiers.png` |
| Bulk Assign VIP Tiers | `1I9JUFzz3ANNbB43lN9xMn42v_gJ2cbUr` | `99minds-bulk-assign-vip-tiers.png` |

---

### Membership
| File | Drive ID | Save as |
|---|---|---|
| Membership Dashboard | `1wAX9Zi2nitSeQf3cx2ov-uScMDKm7VkF` | `99minds-membership-dashboard.png` |
| Add New Membership (creation form) | `1W9EFtTNkXWa803XgwlJjO9u_2TpyCDXW` | `99minds-add-new-membership.png` |
| Membership Tier Details | `1sVxfhlMbEd4L1sJ0b1TbD67fDzPEKPeD` | `99minds-membership-tier-details.png` |

---

### Referral Program
| File | Drive ID | Save as |
|---|---|---|
| Referrals List | `12dXEKG2iofk5_Wo_SgCPWXZ5WLL_In0A` | `99minds-referrals-dashboard.png` |
| Referral Details | `1BGBeK6mvXxi0PAtNh0ktuSzpj615B2kX` | `99minds-referral-details.png` |

---

### Coupons
| File | Drive ID | Save as |
|---|---|---|
| Coupons Dashboard | `1vqSbbrfk_A-0NHarSdcYNjtlzdlznjQA` | `99minds-coupons-dashboard.png` |
| Issue Coupon (modal) | `10QwfGJukzKReZpH1wJ0LmkqwJOgJ4aKl` | `99minds-issue-coupon.png` |
| Coupon Code Detail | `1SkeKfDXOdhruD67CKmwPw2IsBSCZxawK` | `99minds-coupon-code-detail.png` |

---

### Workflows
| File | Drive ID | Save as |
|---|---|---|
| Workflows List | `1RGQ0NbeBxPN-ENDPsaZYG0Htqwj0Lef8` | `99minds-workflows-dashboard.png` |
| Create Workflow (template gallery) | `1ujl5HNI0zvB9aOQTdGwFfg5yniiy4mdH` | `99minds-create-workflow.png` |
| Workflow Events Log | `1cjqh5RqV5mLfp4zYcSAilTZ4QPS-d3QQ` | `99minds-workflow-events.png` |

---

### Widgets
| File | Drive ID | Save as |
|---|---|---|
| Widget Settings (all widget types) | `1sF8RYTwTTlDdYGRT3-UYSppq1mpcKU0_` | `99minds-widget-settings.png` |

Sub-folders for detailed widget screenshots (search Drive for more):
- Loyalty Widget folder: `1NYA_IMs_ipn7YcWSl-lT_4vvyOL8CiYB`
- Gift Card Widget folder: `1ii__fzhjaPVNGtgqorgxztcuGRbt3k6q`
- Loyalty Page Widget folder: `1N9KZKYymTdXhsYUypDwv9gz_8pQfCT9P`
- Referral Page folder: `1syjBjs7Q0PLH-_qZpFef4cKiWXOW8tE5`
- Shopify Checkout Extension folder: `1nxaHTUqRqmQq1xj-RHlIxFVkc_zjRX2y`
- Shopify POS Extensions folder: `10Z1xf9bDuA1Fr6u0gADtSHqAIMy7ugqF`

---

## Feature-to-Screenshot Quick Reference

| Blog topic | Best screenshots to use |
|---|---|
| Loyalty programs, points, repeat purchase | `99minds-loyalty-card-details.png`, `99minds-adjust-loyalty-points-add.png`, `99minds-loyalty-points-customer.png` |
| VIP tiers, premium customers, LTV segmentation | `99minds-vip-tiers-dashboard.png`, `99minds-new-vip-tier.png`, `99minds-vip-tier-details.png` |
| Gift card marketing, B2B gifting | `99minds-gift-card-dashboard.png` |
| Store credit, refund alternatives | `99minds-store-credit-dashboard.png`, `99minds-adjust-store-credit.png` |
| Referral programs, word of mouth | `99minds-referrals-dashboard.png`, `99minds-referral-details.png` |
| Membership, subscription programs | `99minds-membership-dashboard.png`, `99minds-membership-tier-details.png` |
| Coupons, promo codes, co-marketing | `99minds-coupons-dashboard.png`, `99minds-coupon-code-detail.png` |
| Automation, workflows, triggered rewards | `99minds-workflows-dashboard.png`, `99minds-create-workflow.png` |
| Shopify loyalty, POS, checkout | `99minds-widget-settings.png` (shows Shopify extensions) |
| General 99minds platform overview | `99minds-dashboard-overview.png` |
