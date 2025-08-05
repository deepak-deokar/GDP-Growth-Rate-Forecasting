# GDP Growth Rate Forecasting

This project is a time series analysis of GDP growth rates for various countries. It includes data collection from the World Bank, data cleaning and exploration, modeling with ARIMA, Prophet, and LSTM, and a Flask web application to serve the final LSTM model.

## Table of Contents
- [Project Overview](#project-overview)
- [Data](#data)
- [Modeling](#modeling)
- [Application](#application)
- [Conclusion](#conclusion)

## Project Overview

The goal of this project is to forecast the GDP growth rate of any country. The project is divided into three main parts:
1.  **Data Processing**: Downloading, cleaning, and exploring the data from the World Bank.
2.  **Modeling**: Training and evaluating three different time-series models: ARIMA, Prophet, and LSTM.
3.  **Application**: A Flask web application that allows users to select a country and get a GDP growth forecast using the LSTM model.

## Data

The data used in this project is from the [World Bank Open Data](https://data.worldbank.org/). The following indicators were used:
-   GDP Growth Rate (%)
-   GDP (current US$)
-   GNI per capita (current US$)
-   Exports (% of GDP)
-   Imports (% of GDP)

The data was downloaded for all countries from 1960 to 2023. The data was then cleaned by handling missing values through interpolation and forward/backward fill on a per-country basis.

## Modeling

Three different time-series models were trained and evaluated for this project:

1.  **ARIMA**: A baseline ARIMA model was trained to get a benchmark for the forecasting task.
2.  **Prophet**: Facebook's Prophet model was used to capture trend and seasonality in the data.
3.  **LSTM**: A Long Short-Term Memory (LSTM) neural network was trained, which ultimately gave the best performance and was chosen for the final application.

The models were evaluated using Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE). The LSTM model had the lowest RMSE, making it the most accurate model for this task.

## Application

A Flask web application was built to serve the LSTM model. The application has the following features:
-   A dropdown menu to select a country.
-   An input field to specify the number of years to forecast (up to 5 years).
-   A plot of the historical and forecasted GDP growth rate.
-   A button to download the forecast as a CSV file.

To run the application locally, follow these steps:
1.  Clone the repository.
2.  Install the required packages: `pip install -r requirements.txt`
3.  Run the Flask app: `python app/flask_app.py`

## Conclusion

This project demonstrates an end-to-end time-series forecasting pipeline, from data collection and cleaning to modeling and deployment in a web application. The LSTM model proved to be the most effective for forecasting GDP growth rates in this dataset. Future improvements could include incorporating more economic indicators, hyperparameter tuning of the models, and deploying the application to a cloud service.
