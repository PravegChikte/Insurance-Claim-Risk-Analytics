import plotly.express as px

def fraud_heatmap(df):
    fig = px.density_mapbox(
        df,
        lat="lat",
        lon="lon",
        z="fraud_probability",
        radius=20,
        center=dict(lat=37.09, lon=-95.71),
        zoom=3,
        mapbox_style="carto-darkmatter",
        color_continuous_scale="Turbo",
        title="Geospatial Fraud Risk Heatmap"
    )
    return fig


def claim_velocity_chart(df):
    fig = px.line(
        df,
        x="day_index",
        y="fraud_probability",
        title="Claim Velocity & Spike Detection"
    )

    spikes = df[df["fraud_probability"] > 0.85]

    fig.add_scatter(
        x=spikes["day_index"],
        y=spikes["fraud_probability"],
        mode="markers",
        marker=dict(color="orange", size=8),
        name="Fraud Spikes"
    )

    fig.update_layout(template="plotly_dark")
    return fig


def fraud_indicators_chart():
    data = {
        "Feature": [
            "Incident Severity",
            "Claim-Premium Ratio",
            "Policy Age",
            "Customer Tenure",
            "Authorities Contacted"
        ],
        "Importance": [0.28, 0.22, 0.19, 0.17, 0.14]
    }

    fig = px.bar(
        data,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top 5 Fraud Indicators",
        color_discrete_sequence=["#00cec9"]
    )
    return fig


def investigator_workload_chart():
    data = {
        "Status": ["New", "In Progress", "Escalated"],
        "Count": [45, 28, 12]
    }

    fig = px.bar(
        data,
        x="Count",
        y="Status",
        orientation="h",
        color="Status",
        color_discrete_map={
            "New": "#3498db",
            "In Progress": "#f1c40f",
            "Escalated": "#e74c3c"
        },
        title="Investigator Workload"
    )
    return fig
