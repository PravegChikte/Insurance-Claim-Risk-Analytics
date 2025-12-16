import sqlite3
import pandas as pd

DB_PATH = "../insurance.db"

def get_connection():
    return sqlite3.connect(DB_PATH)


def calculate_kpis_from_sql():
    conn = get_connection()

    total_loss = pd.read_sql(
        "SELECT SUM(total_claim_amount) AS total FROM claims",
        conn
    )["total"][0] / 1_000_000

    suspicious_ratio = pd.read_sql(
        """
        SELECT COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims) AS ratio
        FROM claims
        WHERE fraud_probability > 0.7
        """,
        conn
    )["ratio"][0]

    high_risk = pd.read_sql(
        "SELECT COUNT(*) AS cnt FROM claims WHERE fraud_probability > 0.85",
        conn
    )["cnt"][0]

    total_claims = pd.read_sql(
        "SELECT COUNT(*) AS cnt FROM claims",
        conn
    )["cnt"][0]

    conn.close()

    return {
        "total_loss_m": round(total_loss, 2),
        "suspicious_ratio": round(suspicious_ratio, 2),
        "high_risk_cases": int(high_risk),
        "total_claims": int(total_claims)
    }
