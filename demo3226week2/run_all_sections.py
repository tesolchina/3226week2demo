#!/usr/bin/env python3
"""
Run All Sections - MSW Charging Scheme Data Visualization
==========================================================
This script runs all sections of the data visualization workflow.
It creates the plots directory and generates all visualizations.

Run this file to execute all tasks from the notebook.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Change to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ============================================================
# Section 0: Import Libraries (already done above)
# ============================================================
print("=" * 70)
print("SECTION 0: Libraries imported successfully!")
print("=" * 70)

# ============================================================
# Section 6 (Pre-run): Create plots directory
# ============================================================
if not os.path.exists('plots'):
    os.makedirs('plots')
    print("Created 'plots' directory")

# ============================================================
# Section 1: Load and Examine the Dataset
# ============================================================
print("\n" + "=" * 70)
print("SECTION 1: Load and Examine the Dataset")
print("=" * 70)
df = pd.read_csv('GCAP3226_week2.csv')
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nFirst 5 rows:")
print(df.head())

# ============================================================
# Section 2: Understand Dataset Structure
# ============================================================
print("\n" + "=" * 70)
print("SECTION 2: Dataset Structure and Summary Statistics")
print("=" * 70)
print("\nDataset Info:")
df.info()
print("\nSummary Statistics:")
print(df.describe())

# ============================================================
# Section 3: Categorical Data Visualization
# ============================================================
print("\n" + "=" * 70)
print("SECTION 3: Categorical Data Visualization")
print("=" * 70)

# Likert scale labels
likert_labels = {1: 'Strongly oppose', 2: 'Oppose', 3: 'Neutral', 
                 4: 'Support', 5: 'Strongly support'}
order = [1, 2, 3, 4, 5]
labels = [f"{i}\n{likert_labels[i]}" for i in order]

# 3.1 Frequency Table
print("\nFrequency Table - support_level:")
freq_table = df['support_level'].value_counts().sort_index()
for level, count in freq_table.items():
    print(f"  {level} ({likert_labels[level]}): {count}")

# 3.2 Bar Chart for support_level
plt.figure(figsize=(10, 6))
counts = [df['support_level'].value_counts().get(i, 0) for i in order]
plt.bar(labels, counts, color='steelblue', edgecolor='black')
plt.xlabel('Support Level', fontsize=12)
plt.ylabel('Number of Respondents', fontsize=12)
plt.title('Distribution of Support Level for MSW Charging Scheme', fontsize=14)
plt.tight_layout()
plt.savefig('plots/support_level_bar_chart.png', dpi=150)
plt.close()
print("Saved: plots/support_level_bar_chart.png")

# 3.3 Pie Chart
plt.figure(figsize=(10, 8))
pie_labels = [f"{i}: {likert_labels[i]}" for i in order]
plt.pie(counts, labels=pie_labels, autopct='%1.1f%%', startangle=90,
        colors=sns.color_palette('Blues', n_colors=5))
plt.title('Distribution of Support Level', fontsize=14)
plt.tight_layout()
plt.savefig('plots/support_level_pie_chart.png', dpi=150)
plt.close()
print("Saved: plots/support_level_pie_chart.png")

# 3.4 Comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
max_count = max(df['support_level'].value_counts().max(), 
                df['support_after_info'].value_counts().max()) + 5

counts_before = [df['support_level'].value_counts().get(i, 0) for i in order]
counts_after = [df['support_after_info'].value_counts().get(i, 0) for i in order]

axes[0].bar(labels, counts_before, color='steelblue', edgecolor='black')
axes[0].set_title('Support Level (Before Information)', fontsize=12)
axes[0].set_ylim(0, max_count)

axes[1].bar(labels, counts_after, color='coral', edgecolor='black')
axes[1].set_title('Support Level (After Information)', fontsize=12)
axes[1].set_ylim(0, max_count)

plt.tight_layout()
plt.savefig('plots/support_comparison.png', dpi=150)
plt.close()
print("Saved: plots/support_comparison.png")

# 3.5 District Distribution
district_cols = [col for col in df.columns if 'HongKongDistrict' in col]
district_counts = {}
for col in district_cols:
    district_name = col.replace('HongKongDistrict_', '')
    district_counts[district_name] = df[col].sum()

district_series = pd.Series(district_counts).sort_values(ascending=True)

plt.figure(figsize=(12, 6))
plt.barh(district_series.index, district_series.values, color='steelblue', edgecolor='black')
plt.xlabel('Number of Respondents', fontsize=12)
plt.title('Living District Distribution of Respondents', fontsize=14)
plt.tight_layout()
plt.savefig('plots/district_distribution.png', dpi=150)
plt.close()
print("Saved: plots/district_distribution.png")

# ============================================================
# Section 4: Continuous Data Analysis
# ============================================================
print("\n" + "=" * 70)
print("SECTION 4: Continuous Data Analysis")
print("=" * 70)

print("\nFive-Number Summary for Distance_artificial:")
print(f"  Minimum: {df['Distance_artificial'].min():.2f}")
print(f"  Q1:      {df['Distance_artificial'].quantile(0.25):.2f}")
print(f"  Median:  {df['Distance_artificial'].median():.2f}")
print(f"  Q3:      {df['Distance_artificial'].quantile(0.75):.2f}")
print(f"  Maximum: {df['Distance_artificial'].max():.2f}")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot
axes[0].boxplot(df['Distance_artificial'].dropna(), vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue'))
axes[0].set_ylabel('Distance (m)', fontsize=11)
axes[0].set_title('Box-Whisker Plot of Distance_artificial', fontsize=12)

# Histogram
axes[1].hist(df['Distance_artificial'].dropna(), bins=15, color='steelblue', edgecolor='black')
axes[1].set_xlabel('Distance (m)', fontsize=11)
axes[1].set_ylabel('Frequency', fontsize=11)
axes[1].set_title('Histogram of Distance_artificial', fontsize=12)
axes[1].axvline(df['Distance_artificial'].mean(), color='red', linestyle='--', 
                label=f'Mean: {df["Distance_artificial"].mean():.1f}m')
axes[1].legend()

plt.tight_layout()
plt.savefig('plots/distance_analysis.png', dpi=150)
plt.close()
print("Saved: plots/distance_analysis.png")

# ============================================================
# Section 5: Relationship Analysis
# ============================================================
print("\n" + "=" * 70)
print("SECTION 5: Relationship Analysis")
print("=" * 70)

plt.figure(figsize=(10, 7))
np.random.seed(42)
jitter = np.random.uniform(-0.2, 0.2, size=len(df))
plt.scatter(df['Distance_artificial'], df['recycling_effort'] + jitter, 
            alpha=0.6, c='steelblue', edgecolor='white', s=60)
plt.xlabel('Distance to Nearest Recycling Facility (m)', fontsize=12)
plt.ylabel('Recycling Effort Level', fontsize=12)
plt.title('Distance vs. Recycling Effort', fontsize=14)
plt.yticks([1, 2, 3], ['1 (Low)', '2 (Medium)', '3 (High)'])
plt.tight_layout()
plt.savefig('plots/distance_vs_recycling.png', dpi=150)
plt.close()

correlation = df['Distance_artificial'].corr(df['recycling_effort'])
print(f"Correlation coefficient: {correlation:.4f}")
print("Saved: plots/distance_vs_recycling.png")

# ============================================================
# Section 6: Summary of saved files
# ============================================================
print("\n" + "=" * 70)
print("SECTION 6: Saved Visualizations")
print("=" * 70)
files = os.listdir('plots')
for i, f in enumerate(sorted(files), 1):
    file_size = os.path.getsize(os.path.join('plots', f)) / 1024
    print(f"  {i}. {f} ({file_size:.1f} KB)")

print("\n" + "=" * 70)
print("ALL SECTIONS COMPLETED SUCCESSFULLY!")
print("=" * 70)
