🌍 Next-Day Air Quality Index (AQI) Forecasting

📌 Project Overview

This project predicts the Air Quality Index (AQI) for the next day using historical air pollution data and machine learning.

The goal of this project is to demonstrate:

Time-series forecasting concepts

Feature engineering on real-world data

End-to-end ML workflow

Deployment of an ML model as a web application

❓ Problem Statement

Air pollution affects health and daily life.
Being able to forecast AQI one day in advance can help individuals and authorities take preventive actions.

This project answers:

“What will be the AQI tomorrow based on today’s air quality data?”

📊 Dataset

Source: Kaggle – Air Quality Data in India (2015–2024)

File used: city_day.csv

Granularity: City-level daily data

Main features:

Pollutant concentrations (PM2.5, PM10, NO2, CO, etc.)

Date information

Historical AQI values

🧠 Machine Learning Approach

1️⃣ Data Preprocessing

Converted date column to datetime format

Sorted data by city and date

Checked and confirmed no missing values

2️⃣ Feature Engineering

Simple and explainable features were created:

Lag feature: Yesterday’s AQI

Rolling average: Last 7 days average AQI

Date features: Month and Day

These features help capture time dependency in AQI.

🤖 Models Used

The following models were trained and compared:

Linear Regression

Random Forest Regressor

XGBoost Regressor

Model Selection

Models were evaluated using Mean Absolute Error (MAE)

Linear Regression performed best for next-day AQI forecasting

The final selected model was saved and used in deployment

🔮 Next-Day AQI Forecasting

To convert the problem into a forecasting task:

The AQI column was shifted by one day

The model learns the relationship between today’s data and tomorrow’s AQI

This avoids data leakage and follows proper time-series practices.

🌐 Web Application (Flask)

A Flask-based web application was built where users can:

Enter pollutant values and historical AQI

Predict next-day AQI

See AQI category (Good, Moderate, Poor, etc.)

Key Points:

The trained model is loaded once

No retraining happens during prediction

UI supports controlled testing of inputs

🚀 Deployment

Code hosted on GitHub

Application deployed on Render

Flask app runs as a public web service

🔗 Live App Link: (Add your Render URL here)

🛠️ Tech Stack

Python

Pandas, NumPy

Scikit-learn

XGBoost

Flask

GitHub

Render

📂 Project Structure
air_quality_prediction/
├── kaggle_data/
│   └── city_day.csv
├── models/
│   └── aqi_next_day_model.pkl
├── app.py
├── train_next_day_aqi.py
├── requirements.txt
└── README.md

🎯 Key Learnings

Handling real-world time-series data

Feature engineering for forecasting

Model comparison and honest selection

Deploying ML models as web applications

Importance of clarity and reproducibility

👤 Author

Ritik (Peter)
Aspiring Machine Learning Engineer
📍 India
