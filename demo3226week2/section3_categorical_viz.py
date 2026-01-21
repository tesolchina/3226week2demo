# Section 3: Categorical Data Visualization
# This script creates frequency tables, bar charts, and pie charts for categorical variables

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('GCAP3226_week2.csv')

# Define Likert scale labels for support_level (1-5)
likert_labels = {
    1: 'Strongly oppose',
    2: 'Oppose', 
    3: 'Neutral',
    4: 'Support',
    5: 'Strongly support'
}

# ============================================================
# 3.1 Frequency Table for support_level
# ============================================================
print("=" * 60)
print("Frequency Table for support_level:")
print("=" * 60)
freq_table = df['support_level'].value_counts().sort_index()
print(freq_table)
print("\nWith labels:")
for level, count in freq_table.items():
    print(f"  {level} ({likert_labels[level]}): {count}")

# ============================================================
# 3.2 Bar Chart for support_level
# ============================================================
plt.figure(figsize=(10, 6))

# Create bar chart ordered by Likert scale (1 to 5)
order = [1, 2, 3, 4, 5]
counts = [df['support_level'].value_counts().get(i, 0) for i in order]
labels = [f"{i}\n{likert_labels[i]}" for i in order]

plt.bar(labels, counts, color='steelblue', edgecolor='black')
plt.xlabel('Support Level', fontsize=12)
plt.ylabel('Number of Respondents', fontsize=12)
plt.title('Distribution of Support Level for MSW Charging Scheme', fontsize=14)
plt.tight_layout()
plt.savefig('plots/support_level_bar_chart.png', dpi=150)
plt.show()

# ============================================================
# 3.3 Pie Chart for support_level
# ============================================================
plt.figure(figsize=(10, 8))

# Create pie chart with labels
pie_labels = [f"{i}: {likert_labels[i]}" for i in order]
plt.pie(counts, labels=pie_labels, autopct='%1.1f%%', startangle=90,
        colors=sns.color_palette('Blues', n_colors=5))
plt.title('Distribution of Support Level for MSW Charging Scheme', fontsize=14)
plt.tight_layout()
plt.savefig('plots/support_level_pie_chart.png', dpi=150)
plt.show()

# ============================================================
# 3.4 Comparison: support_level vs support_after_info (1x2 grid)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Get the maximum count for consistent y-axis
max_count = max(
    df['support_level'].value_counts().max(),
    df['support_after_info'].value_counts().max()
) + 5

# Bar chart for support_level
counts_before = [df['support_level'].value_counts().get(i, 0) for i in order]
axes[0].bar(labels, counts_before, color='steelblue', edgecolor='black')
axes[0].set_xlabel('Support Level', fontsize=11)
axes[0].set_ylabel('Number of Respondents', fontsize=11)
axes[0].set_title('Support Level (Before Information)', fontsize=12)
axes[0].set_ylim(0, max_count)

# Bar chart for support_after_info
counts_after = [df['support_after_info'].value_counts().get(i, 0) for i in order]
axes[1].bar(labels, counts_after, color='coral', edgecolor='black')
axes[1].set_xlabel('Support Level', fontsize=11)
axes[1].set_ylabel('Number of Respondents', fontsize=11)
axes[1].set_title('Support Level (After Information)', fontsize=12)
axes[1].set_ylim(0, max_count)

plt.tight_layout()
plt.savefig('plots/support_comparison.png', dpi=150)
plt.show()

# ============================================================
# 3.5 Multiple Likert Variables (fairness, government_consideration, 
#     policy_helpfulness, waste_severity)
# ============================================================
variables = ['fairness', 'government_consideration', 'policy_helpfulness', 'waste_severity']
titles = ['Perceived Fairness', 'Government Consideration', 'Policy Helpfulness', 'Waste Severity']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

# Calculate max count for y-axis scaling
max_count = max(df[var].value_counts().max() for var in variables) + 5

for idx, (var, title) in enumerate(zip(variables, titles)):
    counts = [df[var].value_counts().get(i, 0) for i in order]
    axes[idx].bar(labels, counts, color=sns.color_palette('Set2')[idx], edgecolor='black')
    axes[idx].set_xlabel('Rating', fontsize=10)
    axes[idx].set_ylabel('Count', fontsize=10)
    axes[idx].set_title(title, fontsize=12)
    axes[idx].set_ylim(0, max_count)

plt.tight_layout()
plt.savefig('plots/likert_variables.png', dpi=150)
plt.show()

print("\nCategorical visualization completed! Check the 'plots' folder for saved images.")
