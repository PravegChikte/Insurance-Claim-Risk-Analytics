import streamlit as st
import pandas as pd
import numpy as np
from utils import calculate_kpis_from_sql


from plots import (
    fraud_heatmap,
    claim_velocity_chart,
    fraud_indicators_chart,
    investigator_workload_chart
)

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Insurance Claims Risk Analytics",
    layout="wide"
)

# -----------------------------
# LOAD STYLES
# -----------------------------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("../data/processed/feature_engineered_claims.csv")

import numpy as np

# -------------------------------------------------
# GEO COORDINATES (SIMULATED FOR DEMO PURPOSES)
# -------------------------------------------------
if "lat" not in df.columns or "lon" not in df.columns:
    df["lat"] = np.random.uniform(25, 49, size=len(df))   # US latitude range
    df["lon"] = np.random.uniform(-124, -66, size=len(df)) # US longitude range


# Ensure fraud_probability exists
if "fraud_probability" not in df.columns:
    df["fraud_probability"] = df["fraud_flag"].apply(
        lambda x: np.random.uniform(0.6, 0.95) if x == 1 else np.random.uniform(0.05, 0.4)
    )

# Day index for time series
df["day_index"] = range(len(df))


# KPIs
kpis = calculate_kpis_from_sql()


# -----------------------------
# HEADER
# -----------------------------
st.markdown("<h1>Insurance Claims Risk Analytics & Fraud Insight Platform</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# KPI ROW
# -----------------------------
c1, c2, c3, c4 = st.columns(4)

c1.markdown(
    f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Incurred Loss (YTD)</div>
        <div class="kpi-value kpi-green">${kpis['total_loss_m']} M</div>
    </div>
    """,
    unsafe_allow_html=True
)

c2.markdown(
    f"""
    <div class="kpi-card">
        <div class="kpi-title">Suspicious Claim Ratio</div>
        <div class="kpi-value kpi-orange">{kpis['suspicious_ratio']}%</div>
    </div>
    """,
    unsafe_allow_html=True
)

c3.markdown(
    f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Claims</div>
        <div class="kpi-value">{kpis['total_claims']}</div>
    </div>
    """,
    unsafe_allow_html=True
)

c4.markdown(
    f"""
    <div class="kpi-card">
        <div class="kpi-title">High Risk Cases</div>
        <div class="kpi-value">{kpis['high_risk_cases']}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# VISUALS
# -----------------------------
left, right = st.columns([1.3, 1])

left.plotly_chart(fraud_heatmap(df), use_container_width=True)
right.plotly_chart(claim_velocity_chart(df), use_container_width=True)

b1, b2 = st.columns(2)
b1.plotly_chart(fraud_indicators_chart(), use_container_width=True)
b2.plotly_chart(investigator_workload_chart(), use_container_width=True)
