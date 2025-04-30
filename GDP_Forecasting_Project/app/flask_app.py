# flask_app.py

import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend to prevent macOS crash
from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

app = Flask(__name__)

# Load cleaned dataset
data_path = "../data/worldbank_gdp_cleaned.csv"
df = pd.read_csv(data_path)

# Final, safe LSTM function using all data

def train_lstm_full_data(country_name, forecast_years=5, seq_length=3):
    country_df = df[df['country'] == country_name].sort_values('Year')
    if country_df.empty:
        raise ValueError(f"No data found for {country_name}")

    y = country_df['GDP Growth Rate (%)'].values.reshape(-1, 1)
    years = country_df['Year'].tolist()

    scaler = MinMaxScaler()
    y_scaled = scaler.fit_transform(y)

    def create_sequences(data, seq_length):
        X, y = [], []
        for i in range(len(data) - seq_length):
            X.append(data[i:i+seq_length])
            y.append(data[i+seq_length])
        return np.array(X), np.array(y)

    X, y_seq = create_sequences(y_scaled, seq_length)

    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(seq_length, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y_seq, epochs=100, verbose=0)

    last_seq = y_scaled[-seq_length:].reshape(seq_length, 1)
    forecast_scaled = []
    for _ in range(forecast_years):
        pred = model.predict(last_seq.reshape(1, seq_length, 1), verbose=0)
        forecast_scaled.append(pred[0, 0])
        pred_reshaped = pred.reshape(1, 1)
        last_seq = np.concatenate([last_seq[1:], pred_reshaped], axis=0)

    forecast = scaler.inverse_transform(np.array(forecast_scaled).reshape(-1, 1)).flatten()
    full_series = np.concatenate([scaler.inverse_transform(y).flatten(), forecast])
    last_known_year = years[-1]
    forecast_years_list = [last_known_year + i for i in range(1, forecast_years + 1)]
    full_years = years + forecast_years_list

    return forecast, full_series, full_years

@app.route('/', methods=['GET', 'POST'])
def index():
    forecast = []
    plot_url = None
    country = None
    full_years = []
    countries = sorted(df['country'].unique().tolist())

    if request.method == 'POST':
        country = request.form['country']
        try:
            forecast_years = int(request.form['forecast_years'])
            if forecast_years > 5:
                return render_template('index.html', error="⚠️ Please enter a forecast range of 5 years or less.", countries=countries, country=country)

            forecast, full_series, full_years = train_lstm_full_data(country, forecast_years)

            static_dir = os.path.join(app.root_path, 'static')
            os.makedirs(static_dir, exist_ok=True)

            plt.figure(figsize=(10, 6))
            plt.plot(full_years[:-forecast_years], full_series[:-forecast_years], label='Historical')
            plt.plot(full_years[-forecast_years:], full_series[-forecast_years:], label='Forecast', linestyle='--')
            plt.title(f"{country} GDP Growth Rate Forecast (LSTM - Full Data)")
            plt.xlabel("Year")
            plt.ylabel("GDP Growth Rate (%)")
            plt.legend()
            plt.grid(True)

            plot_path = os.path.join(static_dir, 'forecast_plot.png')
            plt.savefig(plot_path)
            plt.close()

            plot_url = 'static/forecast_plot.png'

            return render_template('index.html', country=country, forecast=forecast.tolist(), full_years=full_years, plot_url=plot_url, countries=countries)

        except Exception as e:
            return render_template('index.html', error=str(e), countries=countries, country=country)

    return render_template('index.html', countries=countries)

@app.route('/download', methods=['POST'])
def download():
    country = request.form['country']
    forecast_years = int(request.form['forecast_years'])
    forecast, _, full_years = train_lstm_full_data(country, forecast_years)

    forecast_years_list = full_years[-forecast_years:]
    forecast_data = pd.DataFrame({
        'Year': forecast_years_list,
        'Forecasted GDP Growth Rate (%)': forecast
    })

    csv_path = os.path.join("static", "forecast_download.csv")
    forecast_data.to_csv(csv_path, index=False)
    return send_file(csv_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
