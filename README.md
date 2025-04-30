# GDP-Growth-Rate-Forecasting
Time Series Analysis Project

# 🌍 GDP Growth Rate Forecasting App

This web application allows users to forecast the GDP growth rate of any country using a fine-tuned LSTM model. Built with Flask, the app uses World Bank economic indicators and provides a smooth, interactive user experience.

---

## 📈 Features

- 🔮 **LSTM-based Time Series Forecasting** (up to 5 years)
- 🔽 **Auto-populated Country Dropdown**
- 🌓 **Light/Dark Mode Toggle**
- 📥 **Download Forecast as CSV**
- 📊 **Interactive GDP Growth Plot**

---

## 🧠 Models Used

| Model    | Framework   | Purpose                   |
|----------|-------------|---------------------------|
| ARIMA    | statsmodels | Baseline time series      |
| Prophet  | Facebook    | Trend + seasonality model |
| LSTM     | TensorFlow  | Final selected model      |

> Only the **LSTM model** is used in the deployed version for real-time forecasting.

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Flask Templates)
- **Backend:** Python (Flask)
- **ML Libraries:** TensorFlow, scikit-learn, pandas, matplotlib
- **Data Source:** [World Bank Indicators](https://data.worldbank.org)

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/gdp-forecast-app.git
   cd gdp-forecast-

2. Install requirements:
   ```bash
   pip install -r requirements.txt

3. Run the app:
   ```bash
   cd app
   python flask_app.py
