# Section 6: Save Visualizations to a Designated Directory
# This script checks if the 'plots' directory exists, creates it if not,
# and lists all saved plot files

import os

# ============================================================
# Check if 'plots' directory exists, create if not
# ============================================================
plots_dir = 'plots'

if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)
    print(f"Created directory: '{plots_dir}'")
else:
    print(f"Directory '{plots_dir}' already exists")

# ============================================================
# List all files in the plots directory
# ============================================================
print("\n" + "=" * 60)
print("Files in the 'plots' directory:")
print("=" * 60)

if os.path.exists(plots_dir):
    files = os.listdir(plots_dir)
    if files:
        for i, file in enumerate(files, 1):
            file_path = os.path.join(plots_dir, file)
            file_size = os.path.getsize(file_path) / 1024  # Size in KB
            print(f"{i}. {file} ({file_size:.1f} KB)")
    else:
        print("No files found. Run the visualization scripts to generate plots.")
else:
    print(f"Directory '{plots_dir}' does not exist.")

print("\n" + "=" * 60)
print("To save plots, use plt.savefig() in your visualization code:")
print("  Example: plt.savefig('plots/my_plot.png', dpi=150)")
print("=" * 60)
