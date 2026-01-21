# Section 3 (Extended): District Distribution and Cross-Table Analysis
# This script analyzes district distribution and food waste behavior by district

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('GCAP3226_week2.csv')

# ============================================================
# Step 1: Identify and count district columns
# ============================================================
# Find all columns containing "HongKongDistrict"
district_cols = [col for col in df.columns if 'HongKongDistrict' in col]
print(f"Number of district columns: {len(district_cols)}")
print("District columns:", district_cols)

# ============================================================
# Step 2: Combine all district columns and count frequencies
# ============================================================
district_counts = {}
for col in district_cols:
    # Extract district name after the underscore
    district_name = col.replace('HongKongDistrict_', '')
    # Sum the values (number of participants for this district)
    district_counts[district_name] = df[col].sum()

# Convert to Series for easier plotting
district_series = pd.Series(district_counts)
print("\n" + "=" * 60)
print("District Distribution of Respondents:")
print("=" * 60)
print(district_series.sort_values(ascending=False))

# ============================================================
# Step 3: Generate a bar chart sorted by frequency (descending)
# ============================================================
plt.figure(figsize=(12, 6))
district_sorted = district_series.sort_values(ascending=True)  # ascending for horizontal bar
plt.barh(district_sorted.index, district_sorted.values, color='steelblue', edgecolor='black')
plt.xlabel('Number of Respondents', fontsize=12)
plt.ylabel('District', fontsize=12)
plt.title('Living District Distribution of Respondents', fontsize=14)
plt.tight_layout()
plt.savefig('plots/district_distribution.png', dpi=150)
plt.show()

# ============================================================
# Cross Table: Food Waste Behavior by District
# ============================================================
print("\n" + "=" * 60)
print("Cross Table: Food Waste Behavior by District")
print("=" * 60)

# Step 1: Create a DataFrame to hold district and food waste behavior
cross_data = []
for col in district_cols:
    district_name = col.replace('HongKongDistrict_', '')
    # Filter respondents living in this district
    district_respondents = df[df[col] == 1]
    if len(district_respondents) > 0:
        # Count food waste behavior
        behavior_counts = district_respondents['food_waste_behavior'].value_counts()
        for behavior, count in behavior_counts.items():
            cross_data.append({
                'District': district_name,
                'Behavior': behavior,
                'Count': count,
                'Percentage': count / len(district_respondents) * 100
            })

cross_df = pd.DataFrame(cross_data)

# Step 2: Create a pivot table for better visualization
pivot_table = cross_df.pivot_table(
    index='District', 
    columns='Behavior', 
    values='Percentage', 
    fill_value=0
)
print(pivot_table.round(1))

# Step 3: Visualize the pivot table using a grouped bar chart
plt.figure(figsize=(14, 8))
pivot_table.plot(kind='bar', figsize=(14, 8), colormap='Set2', edgecolor='black')
plt.xlabel('District', fontsize=12)
plt.ylabel('Percentage of Respondents (%)', fontsize=12)
plt.title('Food Waste Behavior by District', fontsize=14)
plt.legend(title='Behavior', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('plots/food_waste_by_district.png', dpi=150)
plt.show()

print("\nDistrict analysis completed! Check the 'plots' folder for saved images.")
