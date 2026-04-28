# Data Dictionary — Olist E-Commerce Analysis

This document provides comprehensive column-level documentation for all datasets used in this project, including the raw source files and the derived master datasets.

---

## Table of Contents

1. [Raw Datasets](#raw-datasets)
   - [olist_orders_dataset.csv](#1-olist_orders_datasetcsv)
   - [olist_order_items_dataset.csv](#2-olist_order_items_datasetcsv)
   - [olist_customers_dataset.csv](#3-olist_customers_datasetcsv)
   - [olist_order_reviews_dataset.csv](#4-olist_order_reviews_datasetcsv)
   - [olist_products_dataset.csv](#5-olist_products_datasetcsv)
   - [olist_sellers_dataset.csv](#6-olist_sellers_datasetcsv)
2. [Processed Dataset — olist_cleaned.csv](#processed-dataset--olist_cleanedcsv)
3. [Final Dataset — tableau_ready_olist.csv](#final-dataset--tableau_ready_olistcsv)
4. [Derived Column Formulas](#derived-column-formulas)
5. [Data Quality Notes](#data-quality-notes)

---

## Raw Datasets

### 1. olist_orders_dataset.csv

The core orders table. Each row represents one order placed on the Olist marketplace.

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `order_id` | `string` (UUID) | Unique identifier for each order | `e481f51cbdc54678b7cc49136f2d6af7` |
| `customer_id` | `string` (UUID) | Foreign key to `olist_customers_dataset` | `9ef432eb6251297304e76186b10a928d` |
| `order_status` | `string` | Current status of the order | `delivered`, `shipped`, `canceled` |
| `order_purchase_timestamp` | `string` → `datetime` | Timestamp when the order was placed by the customer | `2017-10-02 10:56:33` |
| `order_approved_at` | `string` → `datetime` | Timestamp when payment was approved | `2017-10-02 11:07:18` |
| `order_delivered_carrier_date` | `string` → `datetime` | Timestamp when the order was handed to the carrier | `2017-10-04 19:55:00` |
| `order_delivered_customer_date` | `string` → `datetime` | Timestamp when the order was delivered to the customer | `2017-10-10 21:25:13` |
| `order_estimated_delivery_date` | `string` → `datetime` | Estimated delivery date shown to the customer at purchase | `2017-10-18 00:00:00` |

**Primary Key:** `order_id`

---

### 2. olist_order_items_dataset.csv

Order line items. Each row represents one item within an order (orders can have multiple items).

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `order_id` | `string` (UUID) | Foreign key to `olist_orders_dataset` | `00010242fe8c5a6d1ba2dd792cb16214` |
| `order_item_id` | `int` | Sequential item number within the order (1, 2, 3…) | `1` |
| `product_id` | `string` (UUID) | Foreign key to `olist_products_dataset` | `4244733e06e7ecb4970a6e2683c13e61` |
| `seller_id` | `string` (UUID) | Foreign key to `olist_sellers_dataset` | `48436dade18ac8b2bce089ec2a041c07` |
| `shipping_limit_date` | `string` → `datetime` | Seller's shipping deadline to hand over to carrier | `2017-09-19 09:45:35` |
| `price` | `float` | Item price in Brazilian Real (BRL) | `58.90` |
| `freight_value` | `float` | Freight/shipping cost for this item in BRL | `13.29` |

**Composite Key:** `order_id` + `order_item_id`

---

### 3. olist_customers_dataset.csv

Customer demographic information, one row per customer-order pair.

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `customer_id` | `string` (UUID) | Foreign key matching `olist_orders_dataset.customer_id` | `06b8999e2fba1a1fbc88172c00ba8bc7` |
| `customer_unique_id` | `string` (UUID) | Unique customer identifier (may have multiple `customer_id`s) | `861eff4711a542e4b93843c6dd7febb0` |
| `customer_zip_code_prefix` | `int` | First 5 digits of the customer's zip code | `14409` |
| `customer_city` | `string` | Customer's city name | `franca` |
| `customer_state` | `string` | Customer's state abbreviation (2-letter code) | `SP` |

**Primary Key:** `customer_id`

---

### 4. olist_order_reviews_dataset.csv

Customer review scores and optional text feedback.

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `review_id` | `string` (UUID) | Unique review identifier | `7bc2406110b926393aa56f80a40eba40` |
| `order_id` | `string` (UUID) | Foreign key to `olist_orders_dataset` | `73fc7af87114b39712e6da79b0a377eb` |
| `review_score` | `int` | Customer satisfaction score (1–5 scale) | `4` |
| `review_comment_title` | `string` (nullable) | Short title of the review comment | `"" (empty)` |
| `review_comment_message` | `string` (nullable) | Full text body of the review | `"Recebi bem antes do prazo"` |
| `review_creation_date` | `string` → `datetime` | When the customer submitted the review | `2018-01-18 00:00:00` |
| `review_answer_timestamp` | `string` → `datetime` | When the review was responded to / registered | `2018-01-18 21:46:59` |

**Primary Key:** `review_id`  
**Note:** Some orders have duplicate reviews. During cleaning, only the latest review per order was retained.

---

### 5. olist_products_dataset.csv

Product catalog metadata.

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `product_id` | `string` (UUID) | Unique product identifier | `1e9e8ef04dbcff4541ed26657ea517e5` |
| `product_category_name` | `string` (nullable) | Product category in Portuguese | `perfumaria` |
| `product_name_lenght` | `int` (nullable) | Number of characters in the product name | `40` |
| `product_description_lenght` | `int` (nullable) | Number of characters in the description | `287` |
| `product_photos_qty` | `int` (nullable) | Number of product photos in the listing | `1` |
| `product_weight_g` | `float` (nullable) | Product weight in grams | `225.0` |
| `product_length_cm` | `float` (nullable) | Product package length in cm | `16.0` |
| `product_height_cm` | `float` (nullable) | Product package height in cm | `10.0` |
| `product_width_cm` | `float` (nullable) | Product package width in cm | `14.0` |

**Primary Key:** `product_id`  
**Note:** `product_name_lenght` is misspelled in the original dataset (Kaggle source); retained as-is.

---

### 6. olist_sellers_dataset.csv

Seller location information.

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `seller_id` | `string` (UUID) | Unique seller identifier | `3442f8959a84dea7ee197c632cb2df15` |
| `seller_zip_code_prefix` | `int` | First 5 digits of the seller's zip code | `13023` |
| `seller_city` | `string` | Seller's city name | `campinas` |
| `seller_state` | `string` | Seller's state abbreviation (2-letter code) | `SP` |

**Primary Key:** `seller_id`

---

## Processed Dataset — olist_cleaned.csv

The master analysis-ready dataset, produced by `02_cleaning.ipynb`. Contains **96,470 rows × 23 columns**.

This dataset is the result of merging all 6 raw tables, applying 15 transformation steps, and filtering to delivered orders only.

| Column | Data Type | Source | Description | Transformation Applied |
|--------|-----------|--------|-------------|----------------------|
| `order_id` | `string` | orders | Unique order identifier | None (primary key) |
| `customer_id` | `string` | orders | Customer identifier for this order | None (foreign key) |
| `order_status` | `string` | orders | Order status | Standardized to lowercase |
| `order_purchase_timestamp` | `datetime64` | orders | When the order was placed | Parsed from string to datetime |
| `order_approved_at` | `datetime64` | orders | When payment was approved | Parsed from string to datetime |
| `order_delivered_carrier_date` | `datetime64` | orders | When carrier received the package | Parsed from string to datetime |
| `order_delivered_customer_date` | `datetime64` | orders | When customer received delivery | Parsed from string to datetime; rows with null dropped |
| `order_estimated_delivery_date` | `datetime64` | orders | Estimated delivery date | Parsed from string to datetime |
| `delivery_delay_days` | `float64` | **derived** | Days between actual and estimated delivery | `(delivered_customer - estimated_delivery).dt.total_seconds() / 86400` |
| `actual_delivery_days` | `float64` | **derived** | Days between purchase and delivery | `(delivered_customer - purchase_timestamp).dt.total_seconds() / 86400` |
| `purchase_month` | `int64` | **derived** | Month the order was placed (1–12) | Extracted from `order_purchase_timestamp` |
| `purchase_year` | `int64` | **derived** | Year the order was placed | Extracted from `order_purchase_timestamp` |
| `purchase_dow` | `int64` | **derived** | Day of week (0 = Mon, 6 = Sun) | Extracted from `order_purchase_timestamp` |
| `delivery_status` | `string` | **derived** | Binary delivery classification | `"late"` if `delivery_delay_days > 0`, else `"on_time"` |
| `customer_state` | `string` | customers | Customer's state (2-letter code, e.g., SP) | Joined via `customer_id` |
| `customer_city` | `string` | customers | Customer's city name | Joined via `customer_id` |
| `total_items` | `int64` | **derived** | Number of items in the order | Aggregated count from order_items |
| `total_price` | `float64` | **derived** | Sum of item prices (BRL) | Aggregated sum from order_items.price |
| `total_freight` | `float64` | **derived** | Sum of freight costs (BRL) | Aggregated sum from order_items.freight_value |
| `avg_item_price` | `float64` | **derived** | Average item price in the order | `total_price / total_items` |
| `total_order_value` | `float64` | **derived** | Total order value including freight | `total_price + total_freight` |
| `review_score` | `int64` | reviews | Customer review score (1–5) | Deduplicated (latest review per order) |
| `review_creation_date` | `datetime64` | reviews | When the review was submitted | Parsed from string to datetime |

---

## Final Dataset — tableau_ready_olist.csv

A subset of the master dataset optimized for Tableau dashboarding. Contains **96,470 rows × 9 columns**.

| Column | Data Type | Description |
|--------|-----------|-------------|
| `order_id` | `string` | Unique order identifier |
| `customer_state` | `string` | Customer state (2-letter code) |
| `customer_city` | `string` | Customer city name |
| `delivery_delay_days` | `float64` | Delivery delay in days (positive = late) |
| `actual_delivery_days` | `float64` | Total delivery time from purchase |
| `delivery_status` | `string` | `"on_time"` or `"late"` |
| `review_score` | `int64` | Customer satisfaction (1–5) |
| `total_order_value` | `float64` | Total order value in BRL |
| `purchase_month` | `int64` | Purchase month (1–12) |

---

## Derived Column Formulas

```python
# Delivery delay (positive = late, negative = early)
delivery_delay_days = (order_delivered_customer_date - order_estimated_delivery_date).dt.total_seconds() / 86400

# Actual delivery duration
actual_delivery_days = (order_delivered_customer_date - order_purchase_timestamp).dt.total_seconds() / 86400

# Time features
purchase_month = order_purchase_timestamp.dt.month
purchase_year  = order_purchase_timestamp.dt.year
purchase_dow   = order_purchase_timestamp.dt.dayofweek  # 0 = Monday

# Delivery classification
delivery_status = "late"    if delivery_delay_days > 0
                  "on_time" if delivery_delay_days <= 0

# Order-level aggregations (from order_items table)
total_items      = COUNT(order_item_id)       per order_id
total_price      = SUM(price)                 per order_id
total_freight    = SUM(freight_value)          per order_id
avg_item_price   = MEAN(price)                per order_id
total_order_value = total_price + total_freight
```

---

## Data Quality Notes

| Issue | Affected Dataset | Count | Resolution |
|-------|-----------------|-------|------------|
| Null `order_delivered_customer_date` for delivered orders | orders | 8 rows | **Dropped** — cannot compute delivery metrics |
| Null `review_comment_title` | reviews | ~87,656 rows | **Filled with empty string** — non-analytical text field |
| Null `review_comment_message` | reviews | ~58,247 rows | **Filled with empty string** — non-analytical text field |
| Null `product_category_name` | products | 610 rows | **Filled with `"unknown"`** — preserves row integrity |
| Null product dimensions (`weight`, `length`, etc.) | products | ~2 rows each | **Filled with column median** — non-critical fields |
| Duplicate reviews per order | reviews | ~483 orders | **Deduplicated** — kept latest review per `order_id` |
| Misspelled column name `product_name_lenght` | products | — | **Retained as-is** — matches Kaggle source schema |
| Non-delivered orders in dataset | orders | ~2,971 rows | **Filtered out** — analysis focuses on completed deliveries |

---

*Last updated: April 2026*
