import streamlit as st

st.title("Executive Overview")

st.markdown("""
## Strategic framing
This project demonstrates how a retail organization can improve planning maturity by replacing reactive decisions with forecast-led operations.

### What this showcase should communicate
- the business problem is operational, not purely academic
- the modeling workflow is disciplined and production-aware
- the outputs are interpretable by operations, finance, and leadership stakeholders
- the solution is suitable for portfolio presentation, interviews, and client-style demos
""")

c1, c2, c3 = st.columns(3)
c1.metric("Core Outcome", "Forecast-led planning")
c2.metric("Decision Layer", "Inventory / Staffing / Promotions")
c3.metric("Audience", "Ops leaders, recruiters, stakeholders")

st.subheader("Senior-level narrative")
st.write(
    "The value of this work is not only model accuracy. The real value is the ability to convert forecast quality into better operational timing, lower inventory friction, and stronger financial discipline."
)

st.subheader("What to finalize before publishing")
st.markdown("""
- confirm one final set of KPI values
- add screenshots from final charts
- export and store a production model artifact
- include a concise architecture diagram in the repository README
- align all numbers across report, slides, notebook, and dashboard
""")
