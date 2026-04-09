from pathlib import Path
import pandas as pd


def load_sales_data(base_path: str | Path = 'data/raw/Sales_Forecasting_Time_Series_Dataset.xlsx') -> pd.DataFrame:
    path = Path(base_path)
    return pd.read_excel(path, sheet_name='Sales_Time_Series_Data')
