# PhonePe Dashboard — Master Documentation

## Table of Contents
1. Overview
2. Project Structure
3. Setup & Requirements
4. Data Sources & Database Schema
5. ETL (etl.py) — Summary
6. Dashboard (Dashboard.py) — Overview
7. Helper Functions
8. Business Cases (Modules)
   - Case 1: Transaction Type Trends (ques1)
   - Case 2: Device Dominance & User Engagement (ques2)
   - Case 3: Insurance Penetration & Trends (ques3)
   - Case 4: Transaction Analysis for Market Expansion (ques4)
   - Case 5: User Engagement & Growth Strategy (ques5)
9. Map & Home Page Visualizations
10. Streamlit UI / Navigation
11. Visualizations & Charts
12. Recommended Improvements
13. How to run
14. Deliverables
15. Contribution & License

---

## 1. Overview
This repository contains a two-part PhonePe analytics project:

- **ETL (`etl.py`)** — extracts PhonePe Pulse JSON files, transforms them into clean tabular form, and loads them into a MySQL database.
- **Dashboard (`Dashboard.py`)** — a Streamlit application that reads the MySQL tables and provides interactive analyses and visualizations across multiple business cases: transactions, insurance, user engagement, and geographic insights.

The dashboard targets business users, product managers, marketing, and growth teams to identify hotspots, measure penetration, and prioritize campaigns and product investments.

---

## 2. Project Structure (recommended)
```
phonepe-pulse-project/
├─ etl.py
├─ dashboard.py
├─ requirements.txt
├─ README.md
├─ sql/ (optional - schema & sample queries)
├─ assets/ (images, logos)
└─ docs/ (this documentation)
```

---

## 3. Setup & Requirements
**Core libraries**
- Python 3.8+
- pandas
- pymysql
- streamlit
- plotly
- requests
- streamlit-option-menu

**Database**
- MySQL (or compatible RDBMS)

**Environment & credentials**
- Create a MySQL user and database for `phonepe`.
- Store DB credentials securely (avoid plaintext in production). For local testing the code uses hardcoded credentials — update before pushing to prod.

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Run dashboard**
```bash
streamlit run Dashboard.py
```

---

## 4. Data Sources & Database Schema
The ETL script ingests raw JSON files from PhonePe Pulse Pulse dataset and creates the following MySQL tables (each table schema is created by `etl.py`):

- `agg_transaction` — state-level aggregated transaction type metrics
- `agg_insurance` — state-level aggregated insurance metrics
- `agg_user` — state-level aggregated user (device/brand) metrics
- `map_transaction` — district-level transaction hover data
- `map_insurance` — district-level insurance hover data
- `map_user` — district-level user metrics (registered users, app opens)
- `top_transaction` — top pincodes for transactions
- `top_insurance` — top pincodes for insurance
- `top_user` — top pincodes for registered users
- `top_district` — district-level transaction top lists

Each table stores: States, Years, Quarter and relevant metric columns (counts, amounts, registered users, app opens, pincodes, etc.).

---

## 5. ETL (`etl.py`) — Summary
**Purpose:** Traverse the provided file tree of JSON Pulse data and materialize consistent tables in MySQL.

**High-level steps:**
1. Connect to MySQL via `pymysql`.
2. Create database `phonepe` if not exists.
3. For each dataset path (aggregated, map, top folders), read JSON files recursively.
4. Parse JSON to collect rows into dictionaries then convert to Pandas DataFrames.
5. Normalize state names and create/insert into MySQL tables.
6. Commit bulk inserts using parameterized queries.

**Notes:**
- File paths are currently absolute — update them to relative or configurable paths.
- Ensure JSON schema stability; guard for missing keys.

---

## 6. Dashboard (`Dashboard.py`) — Overview
**Purpose:** Provide an interactive analytics interface using Streamlit and Plotly for the aggregated tables loaded into MySQL.

**Main responsibilities:**
- Connect to MySQL, read tables into Pandas DataFrames.
- Expose multiple business-case-driven visualization modules (ques1–ques5).
- Provide map visualizations and a home page for quick KPIs.

The app fetches nine primary DataFrames and uses helper functions to build charts, maps, and ranked lists.

---

## 7. Helper Functions
Key helpers centralized in the script:

- `safe_groupby(df, group_cols, agg_dict)` — safe grouping & aggregation that returns empty DataFrame when input invalid.
- `plot_bar(df, x, y, ...)` — standardized Plotly bar chart wrapper.
- `plot_line(...)`, `plot_scatter(...)` — wrappers for consistent Plotly line/scatter visuals.
- `calc_penetration(df, group_cols, value_col, user_col)` — computes penetration metric.
- `calculate_year_growth(...)` and `calculate_year_growth1(...)` — compute growth percentages (numeric and string-formatted `%`).

These help maintain consistent visuals and avoid duplicated code across business-case modules.

---

## 8. Business Cases (Modules)
Each `quesN` function implements a business case and renders interactive charts & tables.

### Case 1 — Transaction Type Trends (`ques1`)
- Maps: Most used transaction type by amount and count (choropleth).
- State / Year / Quarter trends, distribution, and Top/Bottom 5 states.
- Useful for payment performance and category popularity insights.

### Case 2 — Device Dominance & User Engagement (`ques2`)
- Engagement scoring per brand and state (Transaction_count × Transaction_percentage).
- Brand popularity, trends, and best brand per state (choropleth).
- User engagement metrics (Registered Users & App Opens) and engagement ratio maps.

### Case 3 — Insurance Penetration & Trends (`ques3`)
- Insurance penetration choropleths (amount & count), hotspots, district/pincode rankings.
- Insurance vs user growth scatter plots (state/district/pincode).
- Penetration and growth analysis with year comparisons.

### Case 4 — Market Expansion (`ques4`)
- State-level transaction & user maps for expansion analysis.
- Penetration, growth%, and average usage (AppOpens / RegisteredUser) calculations.
- Top/bottom states for transactions, users and app opens.

### Case 5 — User Engagement & Growth Strategy (`ques5`)
- Engagement Ratio (App Opens per Registered User) maps and trends.
- Loyalty index (App Opens vs Registered Users) for states and districts.
- Brand share pie chart and top registered-pincodes/districts analysis.

---

## 9. Map & Home Page Visualizations
`map()` provides a flexible map explorer that allows the user to:
- Choose from multiple DataFrames (agg, map, top).
- Select a column (e.g., Transaction_amount, Transaction_type, Brand).
- Apply Year/Quarter filters and render state-level choropleths and top/bottom rankings.

The Home page provides hierarchical filters (State → District → Pincode) and quick KPI cards, with tabbed bar charts at the selected granularity.

---

## 10. Streamlit UI / Navigation
- Sidebar contains a logo and main menu (`Home`, `Data Exploration`, `Business Cases`, `Map`).
- Each page uses Streamlit widgets (selectbox, tabs, columns) for interactive filters.
- Several modules use GeoJSON for India states to render choropleth maps.

---

## 11. Visualizations & Charts
Primary chart types used:
- Choropleth (Plotly) — state-level geographical views.
- Bar charts (Plotly) — ranking/top/bottom views.
- Line charts — time series for trends.
- Scatter — correlation analyses (e.g., insurance vs users).
- Pie/Donut — distribution (transaction type, brand share).

Design principles: consistent color scales, use of tabs for side-by-side raw data & charts, and protective empty-data handling with warnings.

---

## 12. Recommended Improvements (prioritized)
1. **Config & Secrets**: Move DB credentials to environment variables or Streamlit secrets.
2. **Path Config**: Make ETL file paths configurable (YAML/ENV) rather than hard-coded.
3. **Caching**: Cache GeoJSON and DB reads to speed up UI.
4. **Validation**: Add robust JSON parsing guards, unit tests for ETL and SQL queries.
5. **Normalization**: Provide per-user or per-capita normalization for fair comparisons.
6. **Exports**: Add CSV/Excel/PDF download for filtered views.
7. **Performance**: Batch inserts and index commonly filtered columns in MySQL.
8. **Visualization**: Add district/pincode choropleths (if geo-shapes available).

---

## 13. How to run (developer quickstart)
1. Create a Python virtual environment.
2. Install packages from `requirements.txt`.
3. Ensure MySQL is running and `etl.py` can connect.
4. Run `etl.py` to populate the database (or load sample CSVs).
5. Run the dashboard:
```bash
streamlit run Dashboard.py
```
6. Use sidebar to explore pages: Home, Data Exploration, Business Cases, Map.

---

## 14. Deliverables
- `etl.py` — ETL script that loads PhonePe JSON files into MySQL.
- `Dashboard.py` — Streamlit application for visualization.
- This master documentation file.
- Recommended additional deliverables: a `README.md`, sample SQL queries folder, and slide deck.

---

## 15. Contribution & License
- Add a `CONTRIBUTING.md` for coding standards and PR workflow.
- Use an OSI-compatible license (MIT/Apache) and add `LICENSE` file.

---

### Next steps I can help with
- Generate a `README.md` ready for GitHub (project summary, installation, run instructions).
- Convert this documentation to PDF or a slide deck.
- Add a curated list of SQL queries used in the analysis.



