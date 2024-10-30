# GDP-Growth-Rate-Forecasting

This repository contains a project for forecasting the GDP growth rate using machine learning techniques. The project includes data preprocessing, exploratory data analysis, model development, and time series analysis for predicting future trends in GDP growth. The primary tools used include Python, machine learning libraries, and time series analysis methodologies.

## Project Structure

Global Economy Indicators.csv: This raw dataset was sourced from official databases and contains essential global economic indicators necessary for GDP growth analysis.
Cleaned Global Eco Inc.csv: This file is a cleaned and preprocessed version of the raw dataset, produced after handling missing values, outliers, and other inconsistencies. It serves as the primary dataset for model training and analysis.
MLProject.ipynb: This notebook includes the data cleaning process and various machine learning models developed to predict GDP growth. The model evaluations and comparisons are also documented in this file.
TimeSeriesMLP.ipynb: This notebook focuses on time series analysis, exploring the sequential dependencies within the GDP data and applying models specifically designed for time-dependent data to forecast future values.

## Project Workflow

Data Preprocessing: The project begins by loading and cleaning the raw data found in Global Economy Indicators.csv. The cleaned data is saved as Cleaned Global Eco Inc.csv and used for further processing and model training.
Exploratory Data Analysis: Key insights and relationships within the dataset are identified, which guide the model selection and feature engineering processes.
Machine Learning Models: Several machine learning models are implemented in MLProject.ipynb, focusing on predicting GDP growth based on selected economic indicators. The model performances are evaluated using relevant metrics.
Time Series Analysis: In TimeSeriesMLP.ipynb, we apply time series techniques to understand trends over time, using methods like moving averages, ARIMA models, and neural networks (MLP) adapted for time series forecasting.

## Requirements

Install the required packages using: pip install -r requirements.txt

## Usage

Data Cleaning: Run the MLProject.ipynb notebook to preprocess the raw dataset and create the cleaned file.
Model Training and Evaluation: Use MLProject.ipynb for experimenting with different ML models and comparing their performances for GDP growth prediction.
Time Series Forecasting: Run TimeSeriesMLP.ipynb to analyze the time series trends and generate forecasts.

## Results

The project produces:
  A cleaned and processed dataset ready for ML applications.
  Forecasting results from various machine learning and time series models, with visualizations comparing model predictions.

## Acknowledgments

Data was sourced from official economic databases. Special thanks to the creators of Python libraries such as Pandas, Scikit-Learn, and Matplotlib for facilitating analysis and visualization.


