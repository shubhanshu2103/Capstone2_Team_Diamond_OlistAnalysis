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
| Data Lead / EDA Lead | Om mishra | `github-handle` |
| Analysis Lead | Karan rawat | `github-handle` |
| Visualization Lead | Mridul | `github-handle` |
| PPT and Quality Lead | ansh sharma | `github-handle` |

---

## Business Problem
The project serves e-commerce logistics and operations managers aiming to improve customer satisfaction. By analyzing the relationship between delivery delays and customer review scores, the business can identify key areas for logistics optimization and customer communication.

**Core Business Question**

> How does delivery performance (on-time vs. late deliveries) impact customer satisfaction (review scores) in Brazilian e-commerce?

**Decision Supported**

> Enable targeted logistics improvements in specific regions and implement proactive communication strategies for delayed orders to mitigate negative customer reviews.

---

## Dataset
| Attribute | Details |
|---|---|
| **Source Name** | Kaggle - Brazilian E-Commerce Public Dataset by Olist |
| **Direct Access Link** | [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| **Row Count** | 99,441 (Orders) |
| **Column Count** | > 40 across 6 datasets |
| **Time Period Covered** | 2016 to 2018 |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| `order_status` | Status of the order (e.g., delivered) | Used to filter completed orders |
| `order_purchase_timestamp` | Date and time the order was placed | Used for time-series and monthly trends |
| `order_delivered_customer_date` | Date the order reached the customer | Used to compute delivery delay |
| `order_estimated_delivery_date` | Promised delivery date | Used to compute delivery delay |
| `review_score` | Customer rating from 1 to 5 | Target variable for customer satisfaction |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework
| KPI | Definition | Formula / Computation |
|---|---|---|
| Delivery Delay Days | Difference between estimated and actual delivery | `actual_delivery_date - estimated_delivery_date` |
| On-Time Delivery Rate % | Percentage of orders delivered on or before the estimated date | `(Orders with delay <= 0 / Total Orders) * 100` |
| Average Review Score | Mean customer satisfaction rating | `sum(review_score) / count(reviews)` |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

---

## Tableau Dashboard
| Item | Details |
|---|---|
| **Dashboard URL** | _Paste Tableau Public link here_ |
| **Executive View** | High-level summary of total orders, average review scores, and overall on-time delivery rates. |
| **Operational View** | Detailed breakdown of delivery delays by state, review score distribution, and correlation between delay days and scores. |
| **Main Filters** | Year/Month of purchase, Product Category, Delivery Status (On-Time / Late) |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and document the public links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights

1. **Late Deliveries Plunge Satisfaction**: Delivery performance is a critical driver of customer satisfaction. Late deliveries receive review scores approximately 2 points lower than on-time deliveries (2.27 vs 4.29).
2. **Statistically Significant Relationship**: The relationship between delivery delay and review score is statistically significant (p < 0.001) with a Pearson correlation of −0.27.
3. **High On-Time Rate**: 93.2% of orders arrive on time or early, with an average of 12 days ahead of the estimated delivery date.
4. **Disproportionate Impact of Delays**: Only 6.8% of orders are late, but these drive a disproportionate share of negative reviews.
5. **Growth in Order Volume**: Order volume showed strong growth throughout 2017–2018, indicating a healthy marketplace.
6. **Geographic Disparities**: Certain states experience significantly higher late delivery rates, indicating regional logistics challenges.
7. **Multifaceted Satisfaction**: Delivery delay alone explains ~7% of review score variance, suggesting that product quality, seller communication, and other factors also play important roles.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Geographic Disparities in late deliveries | Investigate and partner with better regional logistics providers in underperforming states. | Reduction in late delivery rate and improved review scores in targeted states. |
| 2 | Late deliveries drastically reduce satisfaction | Implement proactive customer communication when an order is flagged as delayed before the customer notices. | Mitigation of the negative impact on review scores for late deliveries. |
| 3 | Delivery delay explains only 7% of score variance | Establish quality control mechanisms and seller performance metrics beyond just logistics. | Holistic improvement in customer satisfaction driven by product and seller quality. |

---

## Repository Structure
```text
SectionName_TeamID_OlistAnalysis/
|
|-- README.md
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output from ETL pipeline
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   `-- dashboard_links.md
|
|-- reports/
|   |-- README.md
|   |-- project_report_template.md
|   `-- presentation_outline.md
|
|-- docs/
|   `-- data_dictionary.md
|
|-- DVA-oriented-Resume/
`-- DVA-focused-Portfolio/
```

---

## Analytical Pipeline
The project follows a structured 7-step workflow:

1. **Define** - Sector selected, problem statement scoped, mentor approval obtained.
2. **Extract** - Raw dataset sourced and committed to `data/raw/`; data dictionary drafted.
3. **Clean and Transform** - Cleaning pipeline built in `notebooks/02_cleaning.ipynb` and optionally `scripts/etl_pipeline.py`.
4. **Analyze** - EDA and statistical analysis performed in notebooks `03` and `04`.
5. **Visualize** - Interactive Tableau dashboard built and published on Tableau Public.
6. **Recommend** - 3-5 data-backed business recommendations delivered.
7. **Report** - Final project report and presentation deck completed and exported to PDF in `reports/`.

---

## Tech Stack
| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, analysis, and KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, contribution audit |
| SQL | Optional | Initial data extraction only, if documented |

**Recommended Python libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`, `scikit-learn`

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

> Marks are awarded for analytical thinking and decision relevance, not chart quantity, visual decoration, or code length.

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

**Project Report**

- [ ] Final report exported as PDF into `reports/`
- [ ] Cover page, executive summary, sector context, problem statement
- [ ] Data description, cleaning methodology, KPI framework
- [ ] EDA with written insights, statistical analysis results
- [ ] Dashboard screenshots and explanation
- [ ] 8-12 key insights in decision language
- [ ] 3-5 actionable recommendations with impact estimates
- [ ] Contribution matrix matches GitHub history

**Presentation Deck**

- [ ] Final presentation exported as PDF into `reports/`
- [ ] Title slide through recommendations, impact, limitations, and next steps

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

*Newton School of Technology - Data Visualization & Analytics | Capstone 2*
