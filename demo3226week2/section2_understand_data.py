# Section 2: Understand the Dataset Structure and Variables
# This script displays dataset information and summary statistics

import pandas as pd

# Load the dataset
df = pd.read_csv('GCAP3226_week2.csv')

# Display the structure and information of the dataset
print("=" * 60)
print("Dataset Information:")
print("=" * 60)
# df.info() shows column names, non-null counts, and data types
df.info()

print("\n" + "=" * 60)
print("Summary Statistics (Numerical Variables):")
print("=" * 60)
# df.describe() provides count, mean, std, min, 25%, 50%, 75%, max for numerical columns
print(df.describe())

print("\n" + "=" * 60)
print("Summary Statistics (All Variables including Categorical):")
print("=" * 60)
# include='all' also shows stats for non-numeric columns
print(df.describe(include='all'))

print("\n" + "=" * 60)
print("Column Names:")
print("=" * 60)
# List all column names for reference
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")
