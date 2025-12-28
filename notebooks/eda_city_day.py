import pandas as pd

# load dataset
df = pd.read_csv("kaggle_data/city_day.csv")

# basic inspection
print("Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nFirst 5 rows:\n")
print(df.head())

print("\nMissing values:\n")
print(df.isnull().sum())
