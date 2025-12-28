import pandas as pd

# Load data
df = pd.read_csv("kaggle_data/city_day.csv")

# Convert Datetime to proper datetime type
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Sort data by city and date (VERY IMPORTANT for time series)
df = df.sort_values(by=['City', 'Datetime'])

# Set datetime as index (optional but good practice)
df.set_index('Datetime', inplace=True)

print(df.head())
print("\nData types:\n")
print(df.dtypes)
