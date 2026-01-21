# Section 1: Load and Examine the Dataset
# This script loads the MSW Charging Scheme dataset and displays basic info

import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv('GCAP3226_week2.csv')

# Display the first five rows
print("=" * 60)
print("First 5 rows of the dataset:")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
print("=" * 60)
