# Section 5: Explore Relationships Between Variables
# This script creates a scatter plot with jitter to explore the relationship
# between Distance_artificial and recycling_effort

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('GCAP3226_week2.csv')

# ============================================================
# Scatter Plot with Jitter
# ============================================================
plt.figure(figsize=(10, 7))

# Add jitter to recycling_effort for better visualization
# (since recycling_effort is discrete: 1, 2, 3)
np.random.seed(42)  # For reproducibility
jitter = np.random.uniform(-0.2, 0.2, size=len(df))
recycling_jittered = df['recycling_effort'] + jitter

# Create scatter plot
plt.scatter(df['Distance_artificial'], recycling_jittered, 
            alpha=0.6, c='steelblue', edgecolor='white', s=60)

# Add labels and title
plt.xlabel('Distance to Nearest Recycling Facility (m)', fontsize=12)
plt.ylabel('Recycling Effort Level', fontsize=12)
plt.title('Relationship: Distance to Recycling Facility vs. Recycling Effort', fontsize=14)

# Set y-axis ticks to show discrete levels
plt.yticks([1, 2, 3], ['1\n(Low)', '2\n(Medium)', '3\n(High)'])

# Add a trend line (optional)
z = np.polyfit(df['Distance_artificial'].dropna(), df['recycling_effort'].dropna(), 1)
p = np.poly1d(z)
x_line = np.linspace(df['Distance_artificial'].min(), df['Distance_artificial'].max(), 100)
plt.plot(x_line, p(x_line), 'r--', linewidth=2, label=f'Trend line')

plt.legend()
plt.tight_layout()
plt.savefig('plots/distance_vs_recycling_scatter.png', dpi=150)
plt.show()

# ============================================================
# Additional: Seaborn regression plot
# ============================================================
plt.figure(figsize=(10, 7))
sns.regplot(x='Distance_artificial', y='recycling_effort', data=df,
            scatter_kws={'alpha': 0.5, 's': 60},
            line_kws={'color': 'red'},
            x_jitter=0, y_jitter=0.2)
plt.xlabel('Distance to Nearest Recycling Facility (m)', fontsize=12)
plt.ylabel('Recycling Effort Level', fontsize=12)
plt.title('Relationship: Distance to Recycling Facility vs. Recycling Effort\n(with Regression Line)', fontsize=14)
plt.yticks([1, 2, 3], ['1 (Low)', '2 (Medium)', '3 (High)'])
plt.tight_layout()
plt.savefig('plots/distance_vs_recycling_regplot.png', dpi=150)
plt.show()

# Print correlation coefficient
correlation = df['Distance_artificial'].corr(df['recycling_effort'])
print(f"\nCorrelation coefficient (Pearson): {correlation:.4f}")
print("Note: A weak correlation suggests little linear relationship between distance and recycling effort.")

print("\nRelationship analysis completed! Check the 'plots' folder for saved images.")
