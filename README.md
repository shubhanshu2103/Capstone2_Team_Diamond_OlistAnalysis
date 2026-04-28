# Brazilian E-Commerce Delivery & Satisfaction Analysis

> **Newton School of Technology | Data Visualization & Analytics**
> A 2-week industry simulation capstone using Python, GitHub, and Tableau to convert raw data into actionable business intelligence.

---

| Field | Details |
|---|---|
| **Project Title** | Brazilian E-Commerce Delivery & Satisfaction Analysis |
| **Sector** | E-Commerce |
| **Team ID** | Team_Diamond |
| **Section** | _To be filled by team_ |
| **Faculty Mentor** | _To be filled by team_ |
| **Institute** | Newton School of Technology |
| **Submission Date** | 28 April 2026 |

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead / ETL Lead | Shubhanshu dubey | `shubhanshu2103` |
| Data Lead / EDA Lead | Om mishra | `Om-Mishra09` |
| Analysis Lead | Karan rawat | `Karan301205` |
| Visualization Lead | Mridul | `Mridul012` |
| PPT and Quality Lead | ansh sharma | `AnshS-GIT` |

---

## Business Problem
The project analyzes the **Olist Brazilian E-Commerce** public dataset to investigate the relationship between **delivery performance** and **customer satisfaction** in the Brazilian e-commerce ecosystem.

**Core Business Question**

> How does delivery performance (on-time vs. late deliveries) impact customer satisfaction (review scores) in Brazilian e-commerce?

**Decision Supported**

> Enable targeted logistics improvements in specific regions and implement proactive communication strategies for delayed orders to mitigate negative customer reviews.

---

## Dataset
| Attribute | Details |
|---|---|
| **Source Name** | Kaggle — Brazilian E-Commerce Public Dataset by Olist |
| **Direct Access Link** | [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| **Row Count** | 99,441 (Orders) |
| **Column Count** | > 40 across 6 datasets |
| **Time Period Covered** | 2016 to 2018 |
| **Format** | CSV |

**Key Datasets Used**

| Dataset | Rows | Columns | Description |
|---------|------|---------|-------------|
| `olist_orders_dataset.csv` | 99,441 | 8 | Core orders table with timestamps and status |
| `olist_order_items_dataset.csv` | 112,650 | 7 | Order line items with price and freight |
| `olist_customers_dataset.csv` | 99,441 | 5 | Customer demographics (city, state) |
| `olist_order_reviews_dataset.csv` | 99,224 | 7 | Customer review scores and comments |
| `olist_products_dataset.csv` | 32,951 | 9 | Product catalog information |
| `olist_sellers_dataset.csv` | 3,095 | 4 | Seller location data |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework
| KPI | Definition | Formula / Computation |
|---|---|---|
| Delivery Delay Days | Core KPI — Difference between estimated and actual delivery | `order_delivered_customer_date - order_estimated_delivery_date` |
| Actual Delivery Days | Logistics performance metric | `order_delivered_customer_date - order_purchase_timestamp` |
| Average Review Score | Mean customer satisfaction rating | `sum(review_score) / count(reviews)` |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

---

## Tableau Dashboard
| Item | Details |
|---|---|
| **Dashboard URL** | _Paste Tableau Public link here_ |
| **Executive View** | High-level summary of total orders, average review scores, and overall delivery performance. |
| **Operational View** | Detailed breakdown of delivery delays by state, review score distribution, and correlation analysis. |
| **Main Filters** | Year/Month of purchase, Delivery Status, Product Category |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and document the public links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights
1. **Delivery performance is a critical driver of customer satisfaction.** Late deliveries receive review scores approximately 2 points lower than on-time deliveries (2.27 vs 4.29).
2. **The relationship is statistically significant** (p < 0.001) with a Pearson correlation of −0.27.
3. **93.2% of orders arrive on time or early**, with an average of 12 days ahead of the estimated delivery date.
4. **Only 6.8% of orders are late**, but these drive a disproportionate share of negative reviews.
5. **Order volume showed strong growth** throughout 2017–2018, indicating a healthy marketplace.
6. **Geographic disparities exist** — some states experience significantly higher late delivery rates.
7. **Delivery delay alone explains ~7% of review score variance**, suggesting that product quality, seller communication, and other factors also play important roles.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Geographic disparities exist in late delivery rates | Target underperforming states with enhanced logistics partnerships or localized distribution centers. | Lower delivery delays in specific regions and corresponding rise in review scores. |
| 2 | Late deliveries drastically lower review scores (2.27 vs 4.29) | Implement automated, proactive customer communication for orders that are predicted to be late. | Mitigation of customer frustration, potentially raising the review scores of late orders. |
| 3 | Delivery delay explains 7% of review score variance | Expand analysis and quality control to product quality and seller performance. | Address the remaining 93% of variance to achieve holistically high customer satisfaction. |

---

## Repository Structure
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

## Analytical Pipeline
The project follows a structured workflow:

1. **Extraction**: Inspected 6 datasets with 99,000+ orders, validating schemas and performing null audits (`01_extraction.ipynb`).
2. **ETL & Cleaning**: Executed a 15-step transformation pipeline, merging tables, handling nulls, parsing dates, and computing key metrics like `delivery_delay_days`. Exported single master dataset (`02_cleaning.ipynb` & `scripts/etl_pipeline.py`).
3. **Exploratory Data Analysis**: Generated 7 key visualizations uncovering delivery distributions, monthly trends, top categories, and state-wise delays (`03_eda.ipynb`).
4. **Statistical Analysis**: Conducted Pearson Correlation, Independent Samples T-Test, and Linear Regression to quantify the impact of delays on satisfaction (`04_statistical_analysis.ipynb`).
5. **Dashboard Prep**: Formatted the final optimized dataset for Tableau (`05_final_load_prep.ipynb`).
6. **Visualization**: Interactive Tableau dashboard built to support logistics optimization decisions.
7. **Report**: Final project report and presentation deck.

---

## Tech Stack
| Tool | Status | Purpose |
|---|---|---|
| Python 3.12 | Mandatory | Core programming language |
| Pandas, NumPy | Mandatory | Data manipulation and processing |
| SciPy, Scikit-learn | Mandatory | Statistical analysis (Pearson, T-test, Regression) |
| Matplotlib, Seaborn | Mandatory | Data visualization and plotting |
| Jupyter Notebook | Mandatory | Interactive analysis environment |
| Tableau | Mandatory | Interactive dashboard design |
| Git, GitHub | Mandatory | Version control and collaboration |

---

## Evaluation Rubric
| Area | Marks | Focus |
|---|---|---|
| Problem Framing | 10 | Is the business question clear and well-scoped? |
| Data Quality and ETL | 15 | Is the cleaning pipeline thorough and documented? |
| Analysis Depth | 25 | Are statistical methods applied correctly with insight? |
| Dashboard and Visualization | 20 | Is the Tableau dashboard interactive and decision-relevant? |
| Business Recommendations | 20 | Are insights actionable and well-reasoned? |
| Storytelling and Clarity | 10 | Is the presentation professional and coherent? |
| **Total** | **100** | |

---

## Submission Checklist
**GitHub Repository**
- [ ] Public repository created with the correct naming convention (`SectionName_TeamID_ProjectName`)
- [ ] All notebooks committed in `.ipynb` format
- [ ] `data/raw/` contains the original, unedited dataset
- [ ] `data/processed/` contains the cleaned pipeline output
- [ ] `tableau/screenshots/` contains dashboard screenshots
- [ ] `tableau/dashboard_links.md` contains the Tableau Public URL
- [ ] `docs/data_dictionary.md` is complete
- [ ] `README.md` explains the project, dataset, and team
- [ ] All members have visible commits and pull requests

**Tableau Dashboard**
- [ ] Published on Tableau Public and accessible via public URL
- [ ] At least one interactive filter included
- [ ] Dashboard directly addresses the business problem

**Project Report & Presentation**
- [ ] Final report exported as PDF into `reports/`
- [ ] Final presentation exported as PDF into `reports/`
- [ ] Contribution matrix matches GitHub history

**Individual Assets**
- [ ] DVA-oriented resume updated to include this capstone
- [ ] Portfolio link or project case study added

---

## Contribution Matrix
This table must match evidence in GitHub Insights, PR history, and committed files.

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
|---|---|---|---|---|---|---|---|
| Shubhanshu dubey | Owner | Owner | Support | Support | Support | Owner | Support |
| Om mishra | Support | Support | Owner | Support | Support | Support | Support |
| Karan rawat | Support | Support | Support | Owner | Support | Support | Support |
| Mridul | Support | Support | Support | Support | Owner | Support | Support |
| ansh sharma | Support | Support | Support | Support | Support | Support | Owner |

_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._

**Team Lead Name:** Shubhanshu dubey

**Date:** 28 April 2026

---

## Academic Integrity
All analysis, code, and recommendations in this repository must be the original work of the team listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.

---

## How to Run

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```

### Step-by-step
1. **Clone the repository:**
   ```bash
   git clone https://github.com/shubhanshu2103/Capstone2_Team_Diamond_OlistAnalysis.git
   cd SectionName_TeamID_OlistAnalysis
   ```

2. **Download the dataset** from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and place CSV files in `data/raw/`.

3. **Run the ETL pipeline:**
   ```bash
   python scripts/etl_pipeline.py
   ```
   Or execute notebooks sequentially in `notebooks/`.

4. **View outputs:**
   - Cleaned data: `data/processed/olist_cleaned.csv`
   - Tableau data: `data/final/tableau_ready_olist.csv`
   - Charts: `reports/plots/`

---

*Newton School of Technology - Data Visualization & Analytics | Capstone 2*
