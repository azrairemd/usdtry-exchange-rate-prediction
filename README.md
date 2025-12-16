# 📈 USD/TRY Exchange Rate Prediction (Lag-Based Linear Regression)

This project is a simple and educational introduction to machine learning model training, focusing on **time series forecasting** using a **lag-based linear regression model**.

The main goal of this project is **not financial accuracy**, but to demonstrate:

- Data preprocessing  
- Feature engineering  
- Model training  
- Recursive prediction  
- Visualization of future forecasts  

---

## 🚀 Project Overview

- **Data Source:** Yahoo Finance (`yfinance`)
- **Target Variable:** USD/TRY closing price
- **Model:** Linear Regression
- **Feature Engineering:** Lag-based features
- **Prediction Type:** Recursive multi-day forecasting

---
## 📁 Project Structure

USD/  
├── assets/                    
│  
├── data/  
│   └── data.py                 # Data retrieval and basic preprocessing  
│  
├── models/  
│   ├── linear_regression.py    # Linear Regression model definition  
│   └── random_forest.py        # Random Forest model definition  
│  
├── train/  
│   ├── linear_regression_train.py  # Train and evaluate Linear Regression model  
│   └── random_forest_train.py      # Train and evaluate Random Forest model  
│  
├── utils/  
│   ├── error.py                # RMSE function  
│   ├── plotting_regression.py  # Plot actual vs predicted values  
│   └── split.py                # Time-series aware train/test split  
│  
├── prediction_with_lr.py       # Recursive future prediction using Linear Regression  
└──  main.py                     # Main entry point of the project  


## 🧠 Feature Engineering

The model uses only **lag-based features**:

| Feature     | Description |
|------------|-------------|
| CloseLag1  | Closing price of the previous day |
| CloseLag2  | Closing price of 2 days ago |
| CloseLag3  | Closing price of 3 days ago |

These features allow the model to learn **short-term temporal dependencies** in the time series.

---

## 🤖 Model

- **Algorithm:** Linear Regression  
- **Training:** Entire historical dataset  
- **Prediction:** Recursive forecasting  

Each predicted value is reused as input for the next step.

This approach mimics **real-world forecasting scenarios**.

---

## 📊 Visualization

- Last **30 days** of actual prices are plotted  
- Future predictions are **connected smoothly** to the last real value  
- This avoids visual discontinuity in the forecast plot  

---

## 🧪 Evaluation

Model performance is evaluated using **RMSE** and compared with a naive baseline model.

**Example:**

RMSE: 0.1026
Naive RMSE: 0.1044
Improvement: ~1.7%

This shows that the model performs **slightly better than a naive approach**, which is expected for a simple baseline model.

---

## ▶️ How to Run
- Clone the repository  
- Run `main.py`

## 🌱 Future Improvements

The long-term goal of this project is to evolve it into a more robust and reusable forecasting system that can produce more consistent predictions and be applied to different financial instruments.

Planned improvements include:

- **Building a more general prediction pipeline**  
  Refactor the codebase to support multiple assets (stocks, currency pairs, indices) using a unified and configurable workflow.

- **Richer feature engineering**  
  Extend beyond simple lag features by adding longer lags, rolling statistics (moving averages, volatility), and trend-based indicators.

- **Model experimentation and comparison**  
  Evaluate different regression models (Ridge, Lasso, ElasticNet) and compare them with tree-based models to better capture non-linear patterns.

- **Rolling window and walk-forward validation**  
  Use rolling or expanding windows to simulate real-world forecasting and improve the reliability of performance evaluation.

- **Improved evaluation strategy**  
  Track performance across different assets and time periods to measure consistency rather than optimizing for a single dataset.

The aim is to transition from a simple educational model into a modular and extensible system that can be reused for multiple assets and more realistic forecasting scenarios.

## ⚠️ Disclaimer
This project is created for educational purposes only.
It is not intended for financial advice or real trading decisions.
