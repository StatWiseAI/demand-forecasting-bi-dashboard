import joblib
import pandas as pd
from pathlib import Path


def load_model(model_path: str | Path = 'models/xgboost_model.pkl'):
    return joblib.load(model_path)


def predict(model, features: pd.DataFrame):
    return model.predict(features)
