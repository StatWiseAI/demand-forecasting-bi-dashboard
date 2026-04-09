import streamlit as st

st.title("Scenario Simulator")

st.markdown("""
This page is where the app becomes decision support instead of a static report.

Use sliders, toggles, and select boxes to let a user test how different commercial and calendar conditions affect expected demand.
""")

promotion = st.toggle('Promotion active', value=False)
weekend = st.toggle('Weekend', value=False)
discount = st.slider('Discount percentage', 0, 40, 10)
holiday = st.selectbox('Holiday status', ['None', 'Public Holiday', 'Black Friday', 'Seasonal Event'])

base_sales = 70000
adjustment = 1.0
if promotion:
    adjustment *= 1.18
if weekend:
    adjustment *= 1.10
adjustment *= 1 + (discount / 1000)
if holiday == 'Black Friday':
    adjustment *= 1.65
elif holiday == 'Public Holiday':
    adjustment *= 1.08

forecast = base_sales * adjustment
st.metric('Illustrative scenario forecast', f'€{forecast:,.0f}')

st.caption('Replace this simple rule-based placeholder with your fitted model inference pipeline.')
