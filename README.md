# RiceYieldWeatherAdvisor

*Predicting Rice Production Suitability Using Weather Data*

## Overview
This repository contains code and resources for predicting daily weather suitability for rice cultivation in Bangladesh using machine learning. The system classifies conditions as "suitable" or "not suitable" based on temperature, sunshine, and rainfall data, and provides actionable recommendations for farmers.

## Features
- **Dataset**: Synthetic data (10,000 samples) with 5 features:
  - `Season`
  - `average_day_temp` (°C)
  - `average_night_temp` (°C)
  - `daily_sunshine_hours`
  - `daily_rainfall` (mm)
- **Models**: SVM, Random Forest, XGBoost, LightGBM, KNN, Logistic Regression.
- **API Integration**: Fetch real-time weather data via OpenWeather API.
- **Recommendations**: Mitigation steps for unfavorable conditions.
