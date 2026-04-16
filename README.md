# NST DVA Capstone 2 - Project Repository

> **Newton School of Technology | Data Visualization & Analytics**
> A 2-week industry simulation capstone using Python, GitHub, and Tableau to convert raw data into actionable business intelligence.

---

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | Brazilian E-Commerce |
| **Sector** | E-commerce / Retail |
| **Team ID** | G7 |
| **Section** | B |
| **Faculty Mentor** | Satyaki Das |
| **Institute** | Newton School of Technology |

### Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead | Saumya Kumar | `oksaumya` |
| Data Lead | _Name_ | `github-handle` |
| ETL Lead | _Name_ | `github-handle` |
| Analysis Lead | _Name_ | `github-handle` |
| Visualization Lead | _Name_ | `github-handle` |
| Strategy Lead | _Name_ | `github-handle` |
| PPT and Quality Lead | _Name_ | `github-handle` |

---

## Business Problem

A large online marketplace wants to improve delivery reliability, customer satisfaction, and seller performance by analyzing order status, payment behavior, product attributes, delivery times, and review scores. The company needs to identify the main operational factors that cause delays, complaints, and revenue loss so it can make better decisions about fulfillment, seller management, and customer experience.

**Core Business Question**

> Which products, sellers, regions, and delivery patterns should management focus on to reduce service issues and improve revenue and repeat business?

**Decision Supported**

> This analysis will help the stakeholder decide where to improve operations first, such as which sellers to monitor, which regions face delivery issues, and which product categories need better fulfillment or customer support. It will also support decisions on how to reduce late deliveries, cancellations, and poor reviews to improve customer retention and repeat purchases.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Kaggle (raw) |
| **Direct Access Link** | https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce |
| **Row Count** | 100,000+ rows |
| **Column Count** | 37 columns after merging the key tables for analysis |
| **Time Period Covered** | 2016 to 2018 |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| `order_id` | Unique identifier for each order | Join key across tables |
| `customer_id` | Unique identifier for each order customer | Customer-level analysis |
| `order_purchase_timestamp` | Date and time the order was placed | Time trend and monthly KPI analysis |
| `order_delivered_customer_date` | Date and time the order was delivered | Delivery delay analysis |
| `order_estimated_delivery_date` | Estimated delivery date shown to customer | Delivery gap and service quality analysis |
| `order_status` | Current status of the order | Cancellation / fulfillment analysis |
| `review_score` | Customer satisfaction rating | Customer experience KPI |
| `payment_value` | Total payment amount for the order | Revenue analysis |
| `product_category_name` | Product category | Category performance analysis |
| `seller_id` | Unique seller identifier | Seller performance analysis |

For full column definitions, see `docs/data_dictionary.md`.

---

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| Monthly Revenue Growth % | Tracks how revenue changes month over month | `(Current Month Revenue - Previous Month Revenue) / Previous Month Revenue * 100` |
| Average Customer Review Score | Measures customer satisfaction | `Average of review_score` |
| Late Delivery Rate | Tracks delivery performance issues | `Late deliveries / Total delivered orders * 100` |
| Cancellation Rate | Measures order failure or business leakage | `Canceled orders / Total orders * 100` |
| Repeat Purchase Rate | Measures customer retention behavior | `Customers with more than 1 order / Total customers * 100` |

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard URL** | _Paste Tableau Public link here_ |
| **Executive View** | High-level view of revenue, delivery performance, review scores, and cancellations |
| **Operational View** | Seller, category, region, and delivery drill-down analysis |
| **Main Filters** | Date, state, product category, seller, order status |

Store dashboard screenshots in `tableau/screenshots/` and document the public links in `tableau/dashboard_links.md`.

---

## Key Insights

1. Late deliveries are expected to reduce customer review scores and repeat business.
2. Some sellers are likely to contribute disproportionately to delays and complaints.
3. A small number of product categories may drive most of the revenue and service issues.
4. Certain regions or states may show weaker delivery performance than others.
5. Canceled orders are expected to create measurable revenue leakage.
6. Faster delivery is likely to be associated with higher satisfaction scores.
7. Order volume may be seasonal, with visible peaks in certain months.
8. Repeat customers are likely to contribute more stable revenue than one-time buyers.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Late deliveries affect satisfaction | Improve logistics monitoring for high-delay regions and sellers | Lower delay rate and better reviews |
| 2 | Some sellers underperform | Create seller scorecards and corrective actions for weak performers | Better marketplace consistency |
| 3 | Certain categories drive issues | Prioritize fulfillment planning for high-volume, high-complaint categories | Reduced complaints and cancellations |
| 4 | Cancellations create revenue leakage | Track cancellation reasons and trigger alerts for risky orders | Lower revenue loss |
| 5 | Repeat customers matter | Build retention campaigns for valuable customer groups | Higher repeat purchase rate |

---

## Repository Structure

```text
SectionName_TeamID_ProjectName/
|
|-- README.md
|
|-- data/
|   |-- raw/
|   `-- processed/
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

**Recommended Python libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`

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

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
|---|---|---|---|---|---|---|---|
| _Member 1_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ |
| _Member 2_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ |
| _Member 3_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ |
| _Member 4_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ |
| _Member 5_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ |
| _Member 6_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ | _Owner / support_ |

_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._

**Team Lead Name:** _____________________________

**Date:** _______________

---

## Academic Integrity

All analysis, code, and recommendations in this repository must be the original work of the team listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.

---