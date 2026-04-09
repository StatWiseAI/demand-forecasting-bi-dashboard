import pandas as pd


def add_basic_time_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out['date'] = pd.to_datetime(out['date'])
    out['month_num'] = out['date'].dt.month
    out['day_num'] = out['date'].dt.day
    out['weekday_num'] = out['date'].dt.weekday
    return out
