import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("kaggle_data/city_day.csv")
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Plot AQI trend for one city (Delhi)
delhi = df[df['City'] == 'Delhi']

plt.figure(figsize=(10,5))
plt.plot(delhi['Datetime'], delhi['AQI'])
plt.title("Delhi AQI Trend Over Time")
plt.xlabel("Year")
plt.ylabel("AQI")
plt.show()
