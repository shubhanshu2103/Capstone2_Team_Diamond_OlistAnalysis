# Brazilian E-Commerce Delivery & Satisfaction Analysis

## Olist Dataset — Capstone Project

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Dataset Description](#dataset-description)
4. [Project Structure](#project-structure)
5. [ETL Pipeline](#etl-pipeline)
6. [Exploratory Data Analysis](#exploratory-data-analysis)
7. [Statistical Analysis](#statistical-analysis)
8. [Key Findings](#key-findings)
9. [Visualizations & Dashboard](#visualizations--dashboard)
10. [Technologies Used](#technologies-used)
11. [Team Members & Roles](#team-members--roles)
12. [How to Run](#how-to-run)
13. [References](#references)

---

## 🎯 Project Overview

This capstone project analyzes the **Olist Brazilian E-Commerce** public dataset (sourced from Kaggle) to investigate the relationship between **delivery performance** and **customer satisfaction** in the Brazilian e-commerce ecosystem. The project follows a complete data analytics lifecycle: data extraction, cleaning, exploratory data analysis (EDA), statistical analysis, visualization, and reporting.

The analysis covers approximately **99,000+ orders** placed between 2016 and 2018 on the Olist marketplace, encompassing 6 core datasets with over 40 attributes.

---

## ❓ Problem Statement

**How does delivery performance (on-time vs. late deliveries) impact customer satisfaction (review scores) in Brazilian e-commerce?**

### Sub-questions:
- What is the distribution of customer review scores across the platform?
- How are delivery delays distributed? What percentage of orders arrive late?
- Is there a statistically significant correlation between delivery delay and review score?
- Do late deliveries receive significantly lower review scores compared to on-time deliveries?
- Can delivery delay predict review scores using a linear regression model?
- Which states/regions experience the most delivery delays?
- What are the monthly order trends over the analysis period?

---

## 📊 Dataset Description

| Dataset | Rows | Columns | Description |
|---------|------|---------|-------------|
| `olist_orders_dataset.csv` | 99,441 | 8 | Core orders table with timestamps and status |
| `olist_order_items_dataset.csv` | 112,650 | 7 | Order line items with price and freight |
| `olist_customers_dataset.csv` | 99,441 | 5 | Customer demographics (city, state) |
| `olist_order_reviews_dataset.csv` | 99,224 | 7 | Customer review scores and comments |
| `olist_products_dataset.csv` | 32,951 | 9 | Product catalog information |
| `olist_sellers_dataset.csv` | 3,095 | 4 | Seller location data |

**Source:** [Kaggle — Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

> For detailed column-level documentation, see the [Data Dictionary](docs/data_dictionary.md).

---

## 📂 Project Structure

```
SectionName_TeamID_OlistAnalysis/
├── README.md                          # This file — project overview & documentation
├── data/
│   ├── raw/                           # Original unmodified CSV files from Kaggle
│   │   ├── olist_orders_dataset.csv
│   │   ├── olist_order_items_dataset.csv
│   │   ├── olist_customers_dataset.csv
│   │   ├── olist_order_reviews_dataset.csv
│   │   ├── olist_products_dataset.csv
│   │   └── olist_sellers_dataset.csv
│   ├── processed/                     # Cleaned & merged master dataset
│   │   └── olist_cleaned.csv
│   └── final/                         # Tableau-optimized final dataset
│       └── tableau_ready_olist.csv
├── notebooks/
│   ├── 01_extraction.ipynb            # Data loading, schema inspection, null audit
│   ├── 02_cleaning.ipynb              # Full ETL pipeline with 15 transformations
│   ├── 03_eda.ipynb                   # Exploratory data analysis with 7 charts
│   ├── 04_statistical_analysis.ipynb  # Correlation, hypothesis testing, regression
│   └── 05_final_load_prep.ipynb       # Tableau-ready dataset preparation
├── scripts/
│   └── etl_pipeline.py               # Reproducible Python ETL script
├── docs/
│   └── data_dictionary.md            # Comprehensive data dictionary
├── reports/
│   ├── plots/                         # All analysis charts (PNG)
│   │   ├── chart1_review_scores.png
│   │   ├── chart2_delivery_delay.png
│   │   ├── chart3_delay_vs_score.png
│   │   ├── chart4_monthly_orders.png
│   │   ├── chart5_top_categories.png
│   │   ├── chart6_late_by_state.png
│   │   ├── chart7_payment_types.png
│   │   ├── correlation_plot.png
│   │   ├── hypothesis_test_plot.png
│   │   └── regression_plot.png
│   └── .gitkeep
└── tableau/
    ├── dashboard_links.md             # Links to Tableau dashboards
    └── screenshots/
        └── .gitkeep
```

---

## 🔧 ETL Pipeline

The ETL (Extract, Transform, Load) pipeline is documented in `notebooks/02_cleaning.ipynb` and automated in `scripts/etl_pipeline.py`. It consists of **15 transformation steps**:

| # | Transformation | Reason |
|---|---|---|
| 01 | Parsed 5 datetime columns | Enable time arithmetic |
| 02 | Computed `delivery_delay_days` | Core KPI — positive = late, negative = early |
| 03 | Computed `actual_delivery_days` | Logistics performance metric |
| 04 | Extracted `purchase_month`, `purchase_year`, `purchase_dow` | Time-series grouping |
| 05 | Dropped delivered orders with null delivery date | Data quality error rows (8 rows) |
| 06 | Filled review comment nulls with empty string | Non-analytical text column |
| 07 | Filled product category nulls with 'unknown' | Preserve row, flag missing (610 rows) |
| 08 | Filled product dimension nulls with median | Non-critical, preserve row |
| 09 | Standardized `order_status` to lowercase | Consistent categorical values |
| 10 | Standardized `product_category_name` | Remove underscores, uniform case |
| 11 | Created `delivery_status` (on_time / late / unknown) | Binary classification column |
| 12 | Aggregated `order_items` to order level | One row per order (98,666 unique orders) |
| 13 | Deduplicated reviews (keep latest) | Prevent duplicate join inflation |
| 14 | Merged all tables into master DataFrame | Single analysis-ready dataset |
| 15 | Filtered to delivered orders only | Focus analysis on completed orders |

**Final master dataset:** 96,470 rows × 23 columns → exported to `data/processed/olist_cleaned.csv`

---

## 📈 Exploratory Data Analysis

The EDA (notebook `03_eda.ipynb`) produced 7 key visualizations:

1. **Review Score Distribution** — Majority of reviews are 5-star; distribution is heavily right-skewed
2. **Delivery Delay Distribution** — Most orders arrive early (mean delay: −12 days); ~6.8% arrive late
3. **Average Delay by Review Score** — Clear inverse relationship: late deliveries → low scores
4. **Monthly Order Trends** — Order volume grew significantly from 2017 to 2018
5. **Top Product Categories** — "cama mesa banho" (bed/bath) leads with 3,029 products
6. **Late Deliveries by State** — Geographic variation in delivery performance across Brazilian states
7. **Payment Type Distribution** — Credit card is the dominant payment method

---

## 📊 Statistical Analysis

The statistical analysis (notebook `04_statistical_analysis.ipynb`) includes three rigorous analyses:

### 1. Pearson Correlation Analysis
| Metric | Value |
|--------|-------|
| Correlation (r) | **−0.2668** |
| P-value | 0.00e+00 |
| Interpretation | Statistically significant negative correlation |

> Delivery delay and review score have a **moderate negative correlation** — as delays increase, satisfaction decreases.

### 2. Independent Samples T-Test (Late vs. On-Time)
| Group | Count | Mean Review Score |
|-------|-------|-------------------|
| On-Time Orders | 89,949 | **4.29** |
| Late Orders | 6,410 | **2.27** |
| T-statistic | | −132.0470 |
| P-value | | 0.00e+00 |
| Result | | **REJECT H₀ — significant difference** |

> Late deliveries receive dramatically lower review scores (2.27 vs 4.29, p < 0.001).

### 3. Linear Regression
| Metric | Value |
|--------|-------|
| Coefficient | **−0.0339** |
| Intercept | 3.7516 |
| R² Score | 0.0712 |

> For every additional day of delay, the predicted review score decreases by **0.034 points**. The low R² (7.12%) indicates that while delivery delay is a significant predictor, other factors also influence customer satisfaction.

---

## 🔑 Key Findings

1. **Delivery performance is a critical driver of customer satisfaction.** Late deliveries receive review scores approximately 2 points lower than on-time deliveries.
2. **The relationship is statistically significant** (p < 0.001) with a Pearson correlation of −0.27.
3. **93.2% of orders arrive on time or early**, with an average of 12 days ahead of the estimated delivery date.
4. **Only 6.8% of orders are late**, but these drive a disproportionate share of negative reviews.
5. **Order volume showed strong growth** throughout 2017–2018, indicating a healthy marketplace.
6. **Geographic disparities exist** — some states experience significantly higher late delivery rates.
7. **Delivery delay alone explains ~7% of review score variance**, suggesting that product quality, seller communication, and other factors also play important roles.

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| **Programming** | Python 3.12 |
| **Data Manipulation** | Pandas, NumPy |
| **Statistical Analysis** | SciPy (Pearson, T-test), Scikit-learn (Linear Regression) |
| **Visualization** | Matplotlib, Seaborn |
| **Dashboarding** | Tableau |
| **Notebooks** | Jupyter Notebook, Google Colab |
| **Version Control** | Git, GitHub |

---

## 👥 Team Members & Roles

| Role | Responsibility |
|------|---------------|
| **Member 1** — ETL Lead | Data extraction, cleaning pipeline, schema design |
| **Member 2** — EDA Lead | Exploratory data analysis, chart generation |
| **Member 3** — Statistical Analysis Lead | Correlation, hypothesis testing, regression |
| **Member 4** — Dashboard Lead | Tableau dashboard design and implementation |
| **Member 5** — Documentation Lead | Project report (PDF), presentation deck, README, data dictionary |

---

## 🚀 How to Run

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```

### Step-by-step
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd SectionName_TeamID_OlistAnalysis
   ```

2. **Download the dataset** from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and place CSV files in `data/raw/`.

3. **Run the ETL pipeline:**
   ```bash
   python scripts/etl_pipeline.py
   ```
   Or execute notebooks sequentially:
   - `01_extraction.ipynb` — Inspect and validate raw data
   - `02_cleaning.ipynb` — Clean, transform, and merge into master dataset
   - `03_eda.ipynb` — Generate exploratory visualizations
   - `04_statistical_analysis.ipynb` — Perform statistical analyses
   - `05_final_load_prep.ipynb` — Prepare Tableau-ready dataset

4. **View outputs:**
   - Cleaned data: `data/processed/olist_cleaned.csv`
   - Tableau data: `data/final/tableau_ready_olist.csv`
   - Charts: `reports/plots/`

---

## 📚 References

- [Olist Brazilian E-Commerce Dataset (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SciPy Statistics](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Scikit-learn Linear Regression](https://scikit-learn.org/stable/modules/linear_model.html)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

---

*This project was completed as part of the capstone requirement. All analysis is based on publicly available data from the Olist Brazilian E-Commerce dataset.*
