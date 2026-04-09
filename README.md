# Demand Forecasting & Supply Chain Optimization

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](#)
[![XGBoost](https://img.shields.io/badge/XGBoost-Forecasting-2c7be5.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end supply chain analytics project that transforms **reactive inventory management** into **proactive, data-driven operations** using time-series forecasting, business intelligence, and scenario-based decision support.

## Executive Summary

This project uses two years of daily retail operations data to forecast sales demand, explain the operational drivers behind volatility, and translate forecast quality into business actions for inventory planning, staffing, promotions, and working-capital optimization.

The final solution combines:
- rigorous time-series preprocessing
- business-aware feature engineering
- walk-forward validation for realistic forecasting
- gradient-boosted machine learning for demand prediction
- a Streamlit dashboard for executive communication

## Business Problem

Many retail and supply chain teams still plan inventory and staffing reactively. This creates avoidable stockouts, inefficient safety-stock buffers, misaligned staffing, and idle working capital.

This project addresses that problem by building a forecasting and decision-support layer that helps answer:
- How much demand should we expect next?
- Which factors are amplifying demand?
- When should inventory and staffing be increased?
- How much uncertainty should be absorbed by safety stock?

## Dataset

The project is based on a structured daily retail time-series dataset covering **731 observations** across **2024-01-01 to 2025-12-31**.

### Core data domains
- calendar and seasonality variables
- sales outcome (`sales_amount`)
- product category context
- promotion and discount activity
- email and paid media signals
- weather and temperature context
- holiday effects
- competitor promotion signals
- lagged and rolling sales features

## Methodology

### 1) Data preparation
- validated schema and date granularity
- preserved chronological integrity
- handled missing environmental features
- standardized categorical and numerical inputs

### 2) Exploratory analysis
- quantified weekend uplift
- identified promotion effects
- isolated holiday and Black Friday spikes
- mapped business patterns into forecasting assumptions

### 3) Feature engineering
- lag features and rolling windows
- cyclical calendar encoding
- interaction terms for promotions and peak periods
- demand-driver enrichment for business interpretation

### 4) Forecast modeling
- baseline comparison across multiple models
- walk-forward validation instead of random split
- final production-oriented gradient-boosted forecasting setup

### 5) Business translation
- residual review and model diagnostics
- forecast-versus-actual performance assessment
- conversion of forecast error into operational actions
- estimation of working-capital implications

## Repository Structure

```text
sales-forecasting-supply-chain-optimization/
├── app/                         # Streamlit application
│   ├── app.py
│   ├── assets/
│   └── pages/
├── src/                         # Reusable business and ML logic
├── data/
│   ├── raw/
│   └── processed/
├── models/                      # Serialized model artifacts
├── notebooks/                   # Clean research notebooks
├── reports/                     # PDF report and presentation exports
├── docs/                        # GitHub Pages landing page assets
├── requirements.txt
├── README.md
└── LICENSE
```

## Streamlit Application

The Streamlit app is designed as an executive-facing showcase with the following sections:
- **Overview** — project value proposition and KPI summary
- **Data Explorer** — interactive exploration of the raw business signals
- **Forecast Performance** — actual vs predicted demand review
- **Scenario Simulator** — promotion, weekend, and peak-period what-if analysis
- **Business Impact** — inventory, staffing, and working-capital interpretation

## Recommended Deployment Strategy

### Best professional setup
1. **GitHub** for source control and credibility
2. **Streamlit Community Cloud** for the live interactive dashboard
3. **GitHub Pages** for the portfolio-grade landing page

### Good alternative
- **Hugging Face Spaces** if you want a stronger ML-demo positioning
- **Render** if you prefer a generic Python web deployment path

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
streamlit run app/app.py
```

## Suggested GitHub Topics

`time-series` `forecasting` `supply-chain` `streamlit` `xgboost` `business-intelligence` `operations-analytics` `demand-planning`

## Future Improvements

- introduce probabilistic forecasting intervals
- add model registry and experiment tracking
- externalize scenario assumptions to configuration files
- connect to a live database or data warehouse
- extend from daily forecasting to SKU-category planning

## Author

**Dany Djeudeu**  
Supply Chain Management | Business Intelligence | Forecasting | Decision Support

If you want this repository to function as a strong public portfolio piece, prioritize:
1. clean reproducible code
2. a polished live demo
3. a sharp business narrative
4. screenshots and evidence of outcomes
