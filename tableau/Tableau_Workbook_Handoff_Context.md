# Tableau Workbook Handoff Context

Copy/paste this whole file into an LLM, coding agent, Tableau helper, or teammate chat to continue the Tableau workbook with full context.

## Project

Repository:

```text
https://github.com/oksaumya/SectionB_G7_BrazilianE-Commerce
```

Drive brief:

```text
https://drive.google.com/file/d/1O8yJC78FcDecg0RA3Tke1B4F09UZqLMM/view?pli=1
```

Dataset topic:

```text
Brazilian E-Commerce / Olist marketplace analytics
```

Main workbook file:

```text
tableau/Brazilian_Ecommerce_Dashboard.twbx
```

This is a Tableau packaged workbook. It should include the workbook, dashboards, worksheets, calculated fields, filters, navigation buttons, and packaged data. The next person should pull the repo and open this `.twbx` in Tableau Desktop or Tableau Public Edition.

No screenshots are included right now. The main handoff artifacts are the `.twbx` file and this markdown file.

---

## Main Data Source

Primary dataset used in Tableau:

```text
data/processed/cleaned_master.csv
```

Use this as the main source. Do not add/join other CSV files unless explicitly improving RFM/forecast views.

Common Tableau field names:

```text
Order Id
Customer Id
Order Status
Order Purchase Timestamp
Order Delivered Customer Date
Order Estimated Delivery Date
Order Item Id
Product Id
Seller Id
Price
Freight Value
Seller City
Seller State
Customer Unique Id
Customer City
Customer State
Payment Type
Payment Installments
Payment Value
Review Score
Customer Lat
Customer Lng
Product Category Name English
Order Year
Order Month
Order Month Name
Order Day Of Week
Order Quarter
Delivery Time Days
Estimated Delivery Days
Is Late
Delay Days
Total Item Value
```

Supporting files available in the repo, but not required for the current workbook:

```text
data/processed/kpi_summary.csv
data/processed/revenue_forecast.csv
data/processed/rfm_segment_summary.csv
data/processed/rfm_segments.csv
```

---

## KPI Reference Values

Use these for sanity checks. Minor differences can happen depending on the exact CSV version and active filters.

```text
Total Revenue: about R$15.9M
Total Orders: about 99,441
Total Items Sold: about 114,092
Average Order Value: about R$160.05
Delivered Orders: about 96,478
Average Delivery Time: about 12.0 days
On-Time Delivery Rate: about 90.9%
Late Delivery Rate: about 9.1%
Unique Customers: about 96,096
Repeat Customers: about 2,997
Repeat Purchase Rate: about 3.1%
Average Review Score: about 4.02 / 5
5-Star Rate: about 56.2%
1-Star Rate: about 13.1%
Top Payment Method: credit_card
Top Revenue Category: health_beauty
```

If Tableau values are off, check filters, nulls, active data source, and whether the metric is order-level or item-level.

---

## Calculated Fields

Create or verify these calculated fields.

### `M - Average Order Value`

```tableau
SUM([Total Item Value]) / COUNTD([Order Id])
```

### `M - Delivered Orders`

```tableau
COUNTD(
IF [Order Status] = "delivered" THEN [Order Id] END
)
```

### `M - Late Orders`

```tableau
COUNTD(
IF [Is Late] = 1 THEN [Order Id] END
)
```

### `M - Late Delivery Rate`

```tableau
[M - Late Orders] / [M - Delivered Orders]
```

### `M - On-Time Delivery Rate`

```tableau
1 - [M - Late Delivery Rate]
```

### `M - Orders Per Customer`

```tableau
{ FIXED [Customer Unique Id] : COUNTD([Order Id]) }
```

### `D - Customer Type`

```tableau
IF [M - Orders Per Customer] > 1 THEN "Repeat Customer"
ELSE "One-Time Customer"
END
```

### `M - Repeat Customers`

```tableau
COUNTD(
IF [M - Orders Per Customer] > 1 THEN [Customer Unique Id] END
)
```

### `M - Repeat Purchase Rate`

```tableau
[M - Repeat Customers] / COUNTD([Customer Unique Id])
```

### `M - 5 Star Rate`

```tableau
SUM(IF [Review Score] = 5 THEN 1 ELSE 0 END) / COUNT([Review Score])
```

### `M - 1 Star Rate`

```tableau
SUM(IF [Review Score] = 1 THEN 1 ELSE 0 END) / COUNT([Review Score])
```

Optional simple metrics:

```tableau
M - Total Revenue = SUM([Total Item Value])
M - Total Orders = COUNTD([Order Id])
M - Avg Delivery Days = AVG([Delivery Time Days])
M - Avg Freight = AVG([Freight Value])
M - Avg Review Score = AVG([Review Score])
M - Unique Customers = COUNTD([Customer Unique Id])
```

---

## KPI Sheets

The workbook should have KPI sheets built as text marks.

### Executive KPI sheets

```text
KPI - Total Revenue
KPI - Total Orders
KPI - Average Order Value
KPI - On Time Delivery
KPI - Avg Review Score
```

Text patterns:

```text
<SUM(Total Item Value)>

Total Revenue
```

```text
<CNTD(Order Id)>

Total Orders
```

```text
<AGG(M - Average Order Value)>

Avg Order Value
```

```text
<AGG(M - On-Time Delivery Rate)>

On-Time Delivery
```

```text
<AVG(Review Score)>

Avg Review Score
```

### Operations KPI sheets

```text
KPI - Late Orders
KPI - Delivered Orders
KPI - On Time Delivery
KPI - Avg Delivery Days
KPI - Avg Freight
```

Text patterns:

```text
<AGG(M - Late Orders)>

Late Orders
```

```text
<AGG(M - Delivered Orders)>

Delivered Orders
```

```text
<AGG(M - On-Time Delivery Rate)>

On-Time Delivery
```

```text
<AVG(Delivery Time Days)>

Avg Delivery Days
```

```text
<AVG(Freight Value)>

Avg Freight
```

### Customer KPI sheets

```text
KPI - Unique Customers
KPI - Repeat Customers
KPI - Repeat Purchase Rate
KPI - Avg Review Score
KPI - 5 Star Rate
KPI - 1 Star Rate
```

Text patterns:

```text
<CNTD(Customer Unique Id)>

Unique Customers
```

```text
<AGG(M - Repeat Customers)>

Repeat Customers
```

```text
<AGG(M - Repeat Purchase Rate)>

Repeat Purchase Rate
```

```text
<AVG(Review Score)>

Avg Review Score
```

```text
<AGG(M - 5 Star Rate)>

5-Star Rate
```

```text
<AGG(M - 1 Star Rate)>

1-Star Rate
```

---

## Chart Sheets

### Executive charts

```text
CHART - Revenue Trend
CHART - Top Categories
CHART - Payment Mix
CHART - Review Distribution
```

Build details:

```text
CHART - Revenue Trend:
Columns = Order Purchase Timestamp as continuous Month timeline
Rows = SUM(Total Item Value)
Marks = Line
Title = Monthly Revenue Trend
Important: use true date timeline across years, not month numbers 1-12.

CHART - Top Categories:
Rows = Product Category Name English
Columns = SUM(Total Item Value)
Marks = Bar
Filter = Top 10 by SUM(Total Item Value)
Sort = Descending
Title = Top Revenue Categories

CHART - Payment Mix:
Rows = Payment Type
Columns = SUM(Total Item Value)
Marks = Bar
Sort = Descending
Filter out Null and not_defined
Title = Payment Mix by Revenue

CHART - Review Distribution:
Columns = Review Score as discrete dimension
Rows = CNTD(Order Id)
Marks = Bar
Filter out Null
Title = Review Score Distribution
```

### Operations charts

```text
CHART - Order Status
CHART - Late Orders by State
CHART - Delivery Days by Category
CHART - Freight by Category
CHART - Brazil State Map
```

Build details:

```text
CHART - Order Status:
Rows = Order Status
Columns = CNTD(Order Id)
Marks = Bar
Sort = Descending
Title = Order Status Distribution

CHART - Late Orders by State:
Rows = Customer State
Columns = AGG(M - Late Orders)
Marks = Bar
Sort = Descending
Title = Late Orders by Customer State

CHART - Delivery Days by Category:
Rows = Product Category Name English
Columns = AVG(Delivery Time Days)
Marks = Bar
Filter = Top 10 if needed
Sort = Descending
Title = Average Delivery Days by Category

CHART - Freight by Category:
Rows = Product Category Name English
Columns = AVG(Freight Value)
Marks = Bar
Filter = Top 10 by AVG(Freight Value)
Sort = Descending
Title = Average Freight by Category
```

Map note:

A Brazil state map was attempted. If it works, place it in the Operations dashboard. If it does not work, keep the reliable state bar chart.

For a geographic state map:

```text
1. Right-click Customer State → Geographic Role → State/Province.
2. Map → Edit Locations → Country/Region = Brazil.
3. Double-click Customer State to create a map.
4. Drag M - Late Orders to Color and Size.
5. If Tableau shows 27 unknown, the Brazilian state codes are not being recognized. Use the bar chart instead.
```

Alternative lat/lng map:

```text
Customer Lng → Columns
Customer Lat → Rows
Customer State → Detail
M - Late Orders → Color and Size
Marks → Circle
```

### Customer charts

```text
CHART - Customer Type Mix
CHART - Revenue by Customer Type
CHART - Review Distribution
CHART - Review by Category
```

Build details:

```text
CHART - Customer Type Mix:
Rows = D - Customer Type
Columns = CNTD(Customer Unique Id)
Marks = Bar
Sort = Descending
Title = Repeat vs One-Time Customers

CHART - Revenue by Customer Type:
Rows = D - Customer Type
Columns = SUM(Total Item Value)
Marks = Bar
Sort = Descending
Title = Revenue by Customer Type

CHART - Review by Category:
Rows = Product Category Name English
Columns = AVG(Review Score)
Marks = Bar
Sort = Ascending or descending depending on story
Filter Top/Bottom 10 if needed
Title = Average Review Score by Category
```

---

## Final Dashboards

### `FINAL - Executive Cockpit`

Purpose:

```text
How is the marketplace performing overall?
```

KPI cards:

```text
KPI - Total Revenue
KPI - Total Orders
KPI - Average Order Value
KPI - On Time Delivery
KPI - Avg Review Score
```

Charts:

```text
CHART - Revenue Trend
CHART - Top Categories
CHART - Payment Mix
CHART - Review Distribution
```

Filters:

```text
Order Purchase Timestamp
Customer State
Product Category Name English
Payment Type
```

Business story:

```text
Executive overview of revenue, orders, order value, delivery reliability, satisfaction, top categories, payment mix, and reviews.
```

### `FINAL - Operations Command Center`

Purpose:

```text
Where are delivery and operational risks happening?
```

KPI cards:

```text
KPI - Late Orders
KPI - Delivered Orders
KPI - On Time Delivery
KPI - Avg Delivery Days
KPI - Avg Freight
```

Charts:

```text
CHART - Order Status
CHART - Late Orders by State OR CHART - Brazil State Map
CHART - Delivery Days by Category
CHART - Freight by Category
```

Filters:

```text
Order Purchase Timestamp
Customer State
Product Category Name English
Order Status
```

Business story:

```text
Operations view of delivery/order risk by status, state, category, freight, and delivery days.
```

### `FINAL - Customer Retention`

Purpose:

```text
Which customers and satisfaction areas should the business focus on?
```

KPI cards:

```text
KPI - Unique Customers
KPI - Repeat Customers
KPI - Repeat Purchase Rate
KPI - Avg Review Score
KPI - 5 Star Rate
KPI - 1 Star Rate
```

Charts:

```text
CHART - Customer Type Mix
CHART - Revenue by Customer Type
CHART - Review Distribution
CHART - Review by Category
```

Filters:

```text
Order Purchase Timestamp
Customer State
Product Category Name English
Review Score
```

Business story:

```text
Retention and satisfaction view. Main message: repeat purchase is low, most customers are one-time buyers, and review/category patterns show where to improve retention.
```

---

## Sidebar and Navigation

Each dashboard should have a sidebar.

In Tableau Desktop edit mode, test navigation buttons with:

```text
Option + Click on Mac
Alt + Click on Windows
```

In published/view mode, normal click should work.

### Executive sidebar

```text
Brazilian
E-Commerce

Analytics Cockpit

● Executive
Operations  ← navigation button to FINAL - Operations Command Center
Customers   ← navigation button to FINAL - Customer Retention
```

### Operations sidebar

```text
Brazilian
E-Commerce

Analytics Cockpit

Executive   ← navigation button to FINAL - Executive Cockpit
● Operations
Customers   ← navigation button to FINAL - Customer Retention
```

### Customer sidebar

```text
Brazilian
E-Commerce

Analytics Cockpit

Executive   ← navigation button to FINAL - Executive Cockpit
Operations  ← navigation button to FINAL - Operations Command Center
● Customers
```

---

## Filters / Slicers

Each dashboard should show useful filters in the sidebar.

For every filter:

```text
Filter card dropdown → Apply to Worksheets → All Using This Data Source
```

Recommended display styles:

```text
Order Purchase Timestamp → Range Slider
Customer State → Multiple Values Dropdown
Product Category Name English → Multiple Values Dropdown
Payment Type → Multiple Values Dropdown
Order Status → Multiple Values Dropdown
Review Score → Multiple Values Dropdown or list
```

Avoid long checkbox lists in the sidebar.

Remove duplicate date filters such as:

```text
Month of Order Purchase Timestamp
```

Keep:

```text
Order Purchase Timestamp
```

---

## Design Polish Still Needed

The workbook may be structurally complete but still needs polish.

Recommended visual theme:

```text
Sidebar background: #1F2A30
Main background: #F5F7FA
Card background: #FFFFFF
Primary green: #0B6E4F
Secondary green: #2FA866
Gold highlight: #F2B705
Risk coral/red: #E85D4F
Neutral/geography blue: #1B7FBD
Text: #1F2A30
Muted text: #6D7B73
Border/light gray: #E2E8E4
```

Formatting improvements:

```text
Revenue: R$15.9M
AOV: R$160.1
On-Time Delivery: 90.9%
Late Delivery Rate: 9.1%
Review Score: 4.02 / 5
Repeat Purchase Rate: 3.1%
Delivery Days: 12.0 days
```

Polish checklist:

```text
[ ] Dark sidebar with light text
[ ] Larger KPI values, smaller labels
[ ] Revenue and AOV formatted as R$
[ ] Percentage KPIs formatted as %
[ ] Review score formatted cleanly
[ ] Gridlines reduced/hidden
[ ] Raw worksheet titles cleaned or hidden
[ ] Filters converted to dropdowns
[ ] Null/not_defined removed where appropriate
[ ] Consistent green/gold/blue/coral theme
[ ] White card-like chart areas
[ ] Spacing/padding improved
```

---

## Save and GitHub Handoff Steps

After any edits:

1. In Tableau Desktop:

```text
File → Save As
```

2. Save as packaged workbook:

```text
tableau/Brazilian_Ecommerce_Dashboard.twbx
```

Use `.twbx`, not `.twb`.

3. Verify by closing Tableau and reopening the `.twbx`.

4. Add to GitHub:

```bash
git add tableau/Brazilian_Ecommerce_Dashboard.twbx
git add tableau/Tableau_Workbook_Handoff_Context.md
git commit -m "Add Tableau workbook and handoff context"
git push
```

If the `.twbx` is larger than GitHub’s normal limit, use Git LFS:

```bash
git lfs install
git lfs track "*.twbx"
git add .gitattributes
git add tableau/Brazilian_Ecommerce_Dashboard.twbx
git commit -m "Track Tableau workbook with Git LFS"
git push
```

---

## Copy/Paste Prompt for an LLM or Agent

```text
You are helping me continue a Tableau dashboard project.

Repo:
https://github.com/oksaumya/SectionB_G7_BrazilianE-Commerce

Drive brief:
https://drive.google.com/file/d/1O8yJC78FcDecg0RA3Tke1B4F09UZqLMM/view?pli=1

Main workbook:
tableau/Brazilian_Ecommerce_Dashboard.twbx

Main data source:
data/processed/cleaned_master.csv

Dataset topic:
Brazilian E-Commerce / Olist marketplace analytics.

I already built a Tableau packaged workbook with three dashboards:
1. FINAL - Executive Cockpit
2. FINAL - Operations Command Center
3. FINAL - Customer Retention

The workbook should contain KPI sheets, chart sheets, sidebar navigation buttons, and filters/slicers. I need help polishing, fixing, or completing it without rebuilding from scratch.

Dashboard 1: Executive Cockpit
Purpose: overall marketplace performance.
KPIs:
- Total Revenue
- Total Orders
- Average Order Value
- On-Time Delivery
- Avg Review Score
Charts:
- Monthly Revenue Trend
- Top Revenue Categories
- Payment Mix
- Review Score Distribution
Filters:
- Order Purchase Timestamp
- Customer State
- Product Category Name English
- Payment Type

Dashboard 2: Operations Command Center
Purpose: delivery and operations risk.
KPIs:
- Late Orders
- Delivered Orders
- On-Time Delivery
- Avg Delivery Days
- Avg Freight
Charts:
- Order Status Distribution
- Late Orders by State or Brazil State Map
- Average Delivery Days by Category
- Average Freight by Category
Filters:
- Order Purchase Timestamp
- Customer State
- Product Category Name English
- Order Status

Dashboard 3: Customer Retention
Purpose: customer behavior, repeat purchase, and satisfaction.
KPIs:
- Unique Customers
- Repeat Customers
- Repeat Purchase Rate
- Avg Review Score
- 5-Star Rate
- 1-Star Rate
Charts:
- Repeat vs One-Time Customers
- Revenue by Customer Type
- Review Score Distribution
- Average Review Score by Category
Filters:
- Order Purchase Timestamp
- Customer State
- Product Category Name English
- Review Score

Important calculated fields:
M - Average Order Value =
SUM([Total Item Value]) / COUNTD([Order Id])

M - Delivered Orders =
COUNTD(IF [Order Status] = "delivered" THEN [Order Id] END)

M - Late Orders =
COUNTD(IF [Is Late] = 1 THEN [Order Id] END)

M - Late Delivery Rate =
[M - Late Orders] / [M - Delivered Orders]

M - On-Time Delivery Rate =
1 - [M - Late Delivery Rate]

M - Orders Per Customer =
{ FIXED [Customer Unique Id] : COUNTD([Order Id]) }

D - Customer Type =
IF [M - Orders Per Customer] > 1 THEN "Repeat Customer"
ELSE "One-Time Customer"
END

M - Repeat Customers =
COUNTD(IF [M - Orders Per Customer] > 1 THEN [Customer Unique Id] END)

M - Repeat Purchase Rate =
[M - Repeat Customers] / COUNTD([Customer Unique Id])

M - 5 Star Rate =
SUM(IF [Review Score] = 5 THEN 1 ELSE 0 END) / COUNT([Review Score])

M - 1 Star Rate =
SUM(IF [Review Score] = 1 THEN 1 ELSE 0 END) / COUNT([Review Score])

Please help me continue from the packaged workbook. Do not assume screenshots exist. Focus on improving the `.twbx` workbook. Check dashboard logic, filters, calculated fields, navigation, and formatting. The final dashboard should look like a polished BI cockpit, not default Tableau sheets.
```
