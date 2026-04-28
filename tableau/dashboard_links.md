# Tableau Dashboard Links

## Dashboard Overview

The Tableau dashboard provides interactive visual analytics for the Olist E-Commerce dataset, enabling stakeholders to explore delivery performance and customer satisfaction metrics dynamically.

---

## Data Source

The dashboard is powered by `data/final/tableau_ready_olist.csv` (96,470 rows × 9 columns):

| Column | Description |
|--------|-------------|
| `order_id` | Unique order identifier |
| `customer_state` | Customer state (2-letter code) |
| `customer_city` | Customer city name |
| `delivery_delay_days` | Delivery delay in days (positive = late) |
| `actual_delivery_days` | Total delivery time from purchase |
| `delivery_status` | "on_time" or "late" |
| `review_score` | Customer satisfaction (1–5) |
| `total_order_value` | Total order value in BRL |
| `purchase_month` | Purchase month (1–12) |

---

## Recommended Dashboard Views

1. **Delivery Performance Map** — Geographic heatmap of late delivery rates by state
2. **Review Score Distribution** — Bar chart with delivery status breakdown
3. **Monthly Trends** — Line chart of order volume and average review scores over time
4. **Delay vs. Satisfaction** — Scatter plot of delivery delay against review score
5. **State Comparison** — Side-by-side comparison of top 10 states by order volume

---

## Publishing Instructions

1. Open Tableau Desktop / Tableau Public
2. Connect to `data/final/tableau_ready_olist.csv`
3. Build the recommended views above
4. Publish to Tableau Public and update this file with the live dashboard URL:

**Dashboard URL:** `[To be updated after publishing]`

---

*Last updated: April 2026*
