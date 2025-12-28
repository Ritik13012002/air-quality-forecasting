import pandas as pd

df = pd.read_csv("kaggle_data/city_day.csv")
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Sort data
df = df.sort_values(by=['City', 'Datetime'])

# Simple time features
df['month'] = df['Datetime'].dt.month
df['day'] = df['Datetime'].dt.day

# Lag feature (previous day AQI)
df['AQI_lag_1'] = df.groupby('City')['AQI'].shift(1)

# Rolling average (7-day)
df['AQI_roll_7'] = df.groupby('City')['AQI'].rolling(7).mean().reset_index(0, drop=True)

# Drop rows created with NaN due to lag/rolling
df = df.dropna()

print(df.head())
