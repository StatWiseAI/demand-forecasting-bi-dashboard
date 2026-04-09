import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Forecast Performance")

st.markdown("""
Use this page to present your final validated forecast versus actual demand.

### Recommended visuals
- actual vs predicted line chart
- residual over time chart
- KPI tiles for MAE / RMSE / MAPE
- peak-period error diagnostics
- model comparison summary
""")

sample = pd.DataFrame({
    'period': ['T1', 'T2', 'T3', 'T4', 'T5'],
    'actual': [70, 75, 82, 78, 88],
    'predicted': [68, 77, 80, 79, 86],
})
fig = px.line(sample, x='period', y=['actual', 'predicted'], markers=True, title='Placeholder forecast comparison')
st.plotly_chart(fig, use_container_width=True)

k1, k2, k3 = st.columns(3)
k1.metric('MAPE', 'Replace', 'with final validated value')
k2.metric('MAE', 'Replace', 'with final validated value')
k3.metric('RMSE', 'Replace', 'with final validated value')
