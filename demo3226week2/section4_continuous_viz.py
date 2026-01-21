# Section 4: Analyze Continuous Data
# This script creates summary statistics, box-whisker plots, and histograms
# for the Distance_artificial variable

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('GCAP3226_week2.csv')

# ============================================================
# Summary Statistics for Distance_artificial
# ============================================================
print("=" * 60)
print("Summary Statistics for Distance_artificial (meters):")
print("=" * 60)

# The five-number summary plus additional statistics
stats = df['Distance_artificial'].describe()
print(stats)

print("\n" + "-" * 40)
print("Five-Number Summary:")
print(f"  Minimum:   {df['Distance_artificial'].min():.2f}")
print(f"  Q1 (25%):  {df['Distance_artificial'].quantile(0.25):.2f}")
print(f"  Median:    {df['Distance_artificial'].median():.2f}")
print(f"  Q3 (75%):  {df['Distance_artificial'].quantile(0.75):.2f}")
print(f"  Maximum:   {df['Distance_artificial'].max():.2f}")

# ============================================================
# Box-Whisker Plot and Histogram (1x2 layout)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box-whisker plot
axes[0].boxplot(df['Distance_artificial'].dropna(), vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='black'),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', markerfacecolor='gray', markersize=6))
axes[0].set_ylabel('Distance to Nearest Recycling Facility (m)', fontsize=11)
axes[0].set_title('Box-Whisker Plot of Distance_artificial', fontsize=12)
axes[0].set_xticklabels(['Distance'])

# Histogram
axes[1].hist(df['Distance_artificial'].dropna(), bins=15, color='steelblue', 
             edgecolor='black', alpha=0.7)
axes[1].set_xlabel('Distance to Nearest Recycling Facility (m)', fontsize=11)
axes[1].set_ylabel('Frequency', fontsize=11)
axes[1].set_title('Histogram of Distance_artificial', fontsize=12)

# Add mean and median lines to histogram
mean_val = df['Distance_artificial'].mean()
median_val = df['Distance_artificial'].median()
axes[1].axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.1f}m')
axes[1].axvline(median_val, color='green', linestyle='-', linewidth=2, label=f'Median: {median_val:.1f}m')
axes[1].legend()

plt.tight_layout()
plt.savefig('plots/distance_analysis.png', dpi=150)
plt.show()

print("\nContinuous data visualization completed! Check the 'plots' folder for saved images.")
