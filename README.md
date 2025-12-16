# 🛡️ Insurance Claims Risk Analytics & Fraud Insight Platform

An end-to-end **insurance risk analytics and fraud detection system** that transforms raw claims data into actionable business insights using **machine learning, SQL pipelines, and an executive decision dashboard**.

---

## 📌 Project Overview

Insurance organizations process thousands of claims daily, where identifying fraudulent or high-risk claims early is critical to minimizing losses and optimizing investigation efforts.

This project simulates a **real-world Property & Casualty (P&C) insurance analytics pipeline**, focusing on:

* Fraud risk identification
* Claims severity analysis
* Executive-level insight delivery

The final output is a **C-suite–ready dashboard** backed by a robust data and analytics pipeline.

---

## 🎯 Business Objectives

* Identify potentially fraudulent insurance claims using data-driven techniques
* Prioritize high-risk claims for investigation teams
* Provide leadership with visibility into loss exposure and fraud trends
* Demonstrate a scalable analytics pipeline suitable for enterprise environments

---

## 🏗️ System Architecture

```
Raw Claims Data (CSV)
        ↓
Data Cleaning & Preprocessing (Python)
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature Engineering (Risk Indicators)
        ↓
Fraud Risk Modeling (ML)
        ↓
SQL Persistence (SQLite)
        ↓
Executive Analytics Dashboard (Streamlit + Plotly)
```

---

## 🔍 Key Features

### ✔ Data Engineering

* Cleaned and standardized raw insurance claims data
* Removed leakage-prone identifiers and irrelevant fields
* Engineered temporal, financial, and behavioral risk features

### ✔ Exploratory Data Analysis

* Fraud vs non-fraud pattern discovery
* Incident-level and customer-level risk analysis
* Financial outlier identification

### ✔ Machine Learning & Risk Modeling

* Fraud probability prediction using supervised ML
* Addressed class imbalance using weighted models
* Evaluated models using **ROC-AUC, Precision, and Recall**
* Translated predictions into business-friendly risk levels (Low / Medium / High)

### ✔ SQL-Based Analytics Pipeline

* Persisted processed data into a relational database
* Retrieved KPIs directly from SQL queries
* Simulated production-style analytics workflows

### ✔ Executive Dashboard

* Dark-mode, high-tech analytics interface
* KPI cards for loss exposure and fraud risk
* Geospatial fraud risk heatmap
* Claim velocity and anomaly detection
* Investigator workload visualization
* Actionable fraud indicators

---

## 🧰 Tech Stack

| Category         | Technologies                  |
| ---------------- | ----------------------------- |
| Language         | Python                        |
| Data Analysis    | Pandas, NumPy                 |
| Visualization    | Plotly, Streamlit             |
| Machine Learning | Scikit-learn                  |
| Database         | SQLite                        |
| Styling          | Custom CSS                    |
| Domain           | P&C Insurance, Risk Analytics |

---

## 📊 Key KPIs Tracked

* Total Incurred Loss (YTD)
* Suspicious Claim Ratio
* High-Risk Fraud Cases
* Claim Velocity & Anomaly Spikes
* Investigator Workload Distribution

---

## 🧠 Design Philosophy

* **Explainability first** – models chosen to balance performance and transparency
* **Business-aligned metrics** – KPIs reflect real insurance decision-making
* **Separation of concerns** – analytics, persistence, and visualization layers are decoupled
* **Scalability-ready** – architecture can be extended to cloud platforms and big data tools

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Build SQL database

```bash
cd sql
python db_setup.py
```

### 3️⃣ Launch dashboard

```bash
cd ../dashboard
streamlit run app.py
```

---

## 📈 Sample Use Cases

* Claims investigation prioritization
* Fraud risk monitoring for insurance operations
* Loss exposure analysis for leadership
* Analytics proof-of-concept for insurance data platforms

---

## 🔮 Future Enhancements

* Integration with cloud databases (AWS RDS / Azure SQL)
* Real-time data ingestion pipelines
* Role-based access control for investigators
* Power BI / Tableau integration
* Advanced explainability using SHAP values

---

## 🏆 Learning Outcomes

* Built an end-to-end analytics pipeline from raw data to executive insights
* Gained hands-on experience in insurance domain risk analytics
* Applied machine learning with real business constraints
* Designed production-style dashboards for decision-makers

---

## 👤 Author

**Praveg Chikte**
*Aspiring Insurance Analytics & Risk Analytics Professional*

---

## 📜 Disclaimer

This project uses **anonymized and publicly available datasets**.
Any resemblance to real insurance data is purely coincidental.

---

### ⭐ If you find this project useful, feel free to star the repository!

---
