import streamlit as st

st.set_page_config(
    page_title="Demand Forecasting & Supply Chain Optimization",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📦 Demand Forecasting & Supply Chain Optimization")
st.caption("From reactive inventory management to proactive, data-driven operations")

st.markdown("""
Welcome to the executive demo environment for the SCM forecasting project.

Use the navigation in the sidebar to explore:
- the business problem and KPI summary
- the dataset and its operational drivers
- forecast performance and model interpretation
- scenario-based planning decisions
- business impact for inventory, staffing, and working capital
""")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Forecast Horizon", "Daily", "731-day history")
col2.metric("Primary Use Case", "Demand Planning", "Inventory + Staffing")
col3.metric("Model Family", "XGBoost", "Walk-forward ready")
col4.metric("Showcase Mode", "Executive Demo", "Portfolio-grade")

st.info(
    "This skeleton is intentionally deployment-ready but data-safe. Replace placeholder metrics and charts with your final validated model outputs and saved artifacts."
)

st.subheader("Recommended user journey")
st.markdown(
    "1. Read the strategic summary → 2. Inspect demand drivers → 3. Review forecast quality → 4. Run scenarios → 5. Translate outputs into operations and finance decisions."
)
