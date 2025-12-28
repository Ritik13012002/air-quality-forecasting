import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pickle

# Load data
df = pd.read_csv("kaggle_data/city_day.csv")
df['Datetime'] = pd.to_datetime(df['Datetime'])
df = df.sort_values(by=['City', 'Datetime'])

# -----------------------------
# Feature Engineering
# -----------------------------
df['month'] = df['Datetime'].dt.month
df['day'] = df['Datetime'].dt.day

df['AQI_lag_1'] = df.groupby('City')['AQI'].shift(1)
df['AQI_roll_7'] = (
    df.groupby('City')['AQI']
    .rolling(7)
    .mean()
    .reset_index(0, drop=True)
)

# -----------------------------
# NEXT-DAY TARGET
# -----------------------------
df['AQI_next_day'] = df.groupby('City')['AQI'].shift(-1)

df = df.dropna()

# -----------------------------
# Features & Target
# -----------------------------
features = [
    'PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3',
    'Benzene','Toluene','Xylene',
    'month','day','AQI_lag_1','AQI_roll_7'
]

X = df[features]
y = df['AQI_next_day']

# -----------------------------
# Time-aware split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# -----------------------------
# Train model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Evaluate
# -----------------------------
pred = model.predict(X_test)
mae = mean_absolute_error(y_test, pred)

print("Next-Day AQI MAE:", mae)

# -----------------------------
# Save model
# -----------------------------
pickle.dump(model, open("models/aqi_next_day_model.pkl", "wb"))
print("Next-day AQI model saved successfully")
