import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Data Explorer")

DATA_PATH = Path(__file__).resolve().parents[2] / 'data' / 'raw' / 'Sales_Forecasting_Time_Series_Dataset.xlsx'

@st.cache_data
def load_data(path: Path):
    if path.exists():
        return pd.read_excel(path, sheet_name='Sales_Time_Series_Data')
    return pd.DataFrame()

_df = load_data(DATA_PATH)

if _df.empty:
    st.warning("Dataset not found. Add the Excel file to data/raw to activate this page.")
else:
    st.success(f"Loaded dataset with {_df.shape[0]} rows and {_df.shape[1]} columns.")
    st.dataframe(_df.head(50), use_container_width=True)

    st.subheader("Suggested enhancements")
    st.markdown("""
    - add date-range filtering
    - add category, promotion, and holiday filters
    - plot demand by weekday / month / campaign status
    - show missingness and data quality badges
    - add downloadable filtered extracts
    """)
