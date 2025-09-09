<img width="600" height="182" alt="0625cbe3-4e88-4381-892e-c048a70cb083_removalai_preview" src="https://github.com/user-attachments/assets/56ecc3b8-2c75-412c-baea-7913bfa45a01" />

# 📊PhonePe Transaction Insights
Domain:Finance / Payment Systems  
Author: Sagheer Ahmed  
## Introduction

The PhonePe Transaction Insights Project is a data-driven analytics and visualization platform built using the PhonePe Pulse dataset. The project extracts, transforms, and analyzes nationwide digital transaction data to uncover meaningful insights into India’s evolving digital payments ecosystem.

The dataset, made available by PhonePe, includes structured and anonymized records of transactions, users, insurance penetration, and geographical distributions across states, districts, and pin codes from 2018 to 2024.

This project provides:

ETL pipeline to clean, transform, and store data into structured formats (MySQL/CSV/SQL).

Interactive dashboard (Streamlit) to visualize transaction trends, user behavior, and insurance penetration.

```Case study analysis covering six business perspectives:
  -Transaction Dynamics
  -Device Dominance
  -Insurance Penetration
  -Market Expansion
  -User Engagement & Growth Strategy
  -Insurance Engagement
```

The aim is to enable businesses, policymakers, and researchers to explore how digital transactions are shaping the economy, identify growth opportunities, detect anomalies, and understand user behavior at scale.
This repository contains a two-part analytics project on **PhonePe Pulse data**:

- ETL (ETL.py) — Extracts PhonePe Pulse JSON files, transforms them into structured tabular form, and loads them into a MySQL database.  
- Dashboard (Dashboard.py) — A **Streamlit application** that connects to MySQL and provides interactive analyses & visualizations across multiple business cases:
  - Transaction Trends  
  - Device Dominance & Engagement  
  - Insurance Penetration  
  - Market Expansion  
  - User Engagement & Growth Strategy  

The project helps **business users, product managers, and growth teams** identify hotspots, measure penetration, and prioritize campaigns & investments.

---

## 📂 Project Structure
```phonepe-pulse-project
├─ src/
├─ ETL.py
├─ dashboard.py
├─ Docs/
│ ├─ Documentation.md
│ └─ presentation.pptx
├─ Pulse/
│ ├─ data/
│ │ ├─ aggregated/
│ │ ├─ map/
│ │ └─ top/
├─ Sql/
│ └─ create_tables.sql
├─ README.md
└─ requirements.txt
```


---

## ⚙️ Setup & Requirements
### Install dependencies
```bash
pip install -r requirements.txt
```


**Core Libraries**
  json
  pandas
  os
  streamlit  
  plotly.express
  requests
  pymysql
  streamlit-option-menu

**Database**
  MySQL (database: phonepe)
Data Sources & Database Schema

  The ETL script ingests raw JSON files from the PhonePe Pulse dataset and creates MySQL tables:
  
    agg_transaction → State-level transaction metrics
    
    agg_insurance → State-level insurance metrics
    
    agg_user → State-level user (device/brand) metrics
    
    map_transaction, map_insurance, map_user → District-level hover data
    
    top_transaction, top_insurance, top_user, top_district → Pincode/District top lists
    
  Common Columns: States, Years, Quarter, transaction/user/insurance metrics, District, Pincode.

ETL (ETL.py)

  ```Connects to MySQL
  
  Creates schema (create_tables.sql)
  
  Reads JSON recursively from /Pulse folders (aggregated, map, top)
  
  Normalizes state names
  
  Loads into MySQL tables via Pandas
```

Dashboard (Dashboard.py)

  ```A Streamlit + Plotly dashboard that:
  
  Connects to MySQL and fetches DataFrames
  
  Provides Business Case modules (ques1–ques5)
  
  Includes Map Explorer & Home Page KPIs
  
  Visualizes transactions, users, insurance, devices, and engagement trends
```

Helper Functions

  ```safe_groupby() → Robust groupby aggregation
  
  plot_bar(), plot_line(), plot_scatter() → Standardized Plotly visuals
  
  calc_penetration() → Computes penetration metrics
  
  calculate_year_growth() → Year-on-year growth functions
```

Business Cases
📌 Case 1 — Transaction Type Trends

```P2P payments dominate 77.1% of volume

Merchant payments growing (18.9%)

Q4 consistently has highest transactions

Maharashtra & Karnataka lead in value; West Bengal leads in count
```

📌 Case 2 — Device Dominance & User Engagement

```Xiaomi dominates 32 states (869M+ transactions)

Engagement scores: Xiaomi 227M > Samsung 129M > Vivo 104M

Top engagement states: Meghalaya (174), Arunachal (139)

Bottom: Chandigarh (13), Delhi (15)
```

📌 Case 3 — Insurance Penetration & Trends

```Leaders: Karnataka (₹2,743M), Maharashtra (₹2,363M)

Q4 > Q3 in insurance demand

District hotspots: Bengaluru Urban, Pune, Thane

High penetration: Andaman (11.53), Kerala (7.11)

Explosive growth in Lakshadweep (+23,871%)
```

📌 Case 4 — Market Expansion

```Transaction leaders: Telangana (₹41.6T), Karnataka (₹40.7T)

User leaders: Maharashtra (1.14B), UP (942M)

Growth: Andaman (+16,158%), Ladakh (+14,111%)

High average usage: Meghalaya (174), Arunachal (139)

```

📌 Case 5 — User Engagement & Growth Strategy

```Engagement Ratio (India): 45.38 (402B app opens / 8.86B users)

Top states: Meghalaya (174), Arunachal (139), Mizoram (137)

Registered Users grew 12.7× (46M → 587M, 2018–2024)

Loyalty Index: Rajasthan (87.28), Maharashtra (43.52)

Brand share: Xiaomi (25.1%), Samsung (19.4%), Vivo (18.1%)
```

Maps & Visualizations

  ```Choropleth maps: State/District transactions, insurance, users
  
  KPIs & Bar charts: Top/Bottom rankings
  
  Line charts: Year/Quarter trends
  
  Scatter plots: Correlations
  
  Pie charts: Brand share & transaction splits
```

Streamlit UI / Navigation

  Sidebar Navigation:
  
    Home
    
    Data Exploration
    
    Business Cases (Case1–Case5)
    
    Map
  
  Features:
  
    India GeoJSON for choropleths
    
    State/District/Pincode filters
    
    Tabs for charts vs raw data

How to Run

  Create a Python virtual environment
  
    Install dependencies
  
    ```pip install -r requirements.txt```


  Ensure MySQL is running and accessible

  Run ETL to populate database

    python ETL.py


  Launch dashboard

    streamlit run Dashboard.py


Use sidebar to explore Home, Cases, Map

Deliverables

ETL.py — ETL script

  ```Dashboard.py — Streamlit dashboard
  
  Docs/Documentation.md — Detailed project report
  
  Docs/presentation.pptx — Slide deck
  
  Sql/create_tables.sql — Database schema
  
  README.md — GitHub documentation
```

Recommended Improvements

  ```Add caching for DB & GeoJSON
  
  CSV/Excel/PDF export options
  
  Optimize MySQL (indexes, batch inserts)
  
  District/Pincode-level choropleths
  
  Deploy on Streamlit Cloud / Docker
```
<img width="707" height="353" alt="Guvi-removebg-preview" src="https://github.com/user-attachments/assets/3552cc26-f9b7-4f73-94db-e44cec6358e9" />

License

This project is for educational and analytical purposes only.
Dataset: PhonePe Pulse: https://github.com/PhonePe/pulse
