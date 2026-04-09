import streamlit as st

st.title("Business Impact")

st.markdown("""
## Why this matters
A forecasting project becomes senior-level when it informs real decisions.

Translate technical outputs into business language:
- lower forecast error -> tighter safety stock
- tighter safety stock -> less idle capital
- better anticipation of peaks -> fewer stockouts and better staffing
- better visibility into drivers -> smarter promotion planning
""")

st.subheader("Recommended KPI blocks")
st.markdown("""
- expected daily planning error
- estimated safety-stock implication
- working-capital released versus baseline
- peak-period readiness level
- category or campaign sensitivity
""")

st.subheader("Executive takeaway")
st.write(
    "The strongest portfolio message is not just that the model predicts demand well, but that it gives the business a more disciplined operating rhythm."
)
