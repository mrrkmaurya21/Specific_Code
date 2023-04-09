import glob
import pandas as pd

# Use glob to get a list of filenames in the current directory that match a pattern
filenames = glob.glob(r'S:\chart_layoff/layoff_chart_*.csv')
print(filenames)
len(filenames)
# Create an empty DataFrame
df_merged = pd.DataFrame()

# Loop through the list of filenames
for file in filenames:
    # Load each CSV file into a DataFrame, and append it to the merged DataFrame
    df_merged = df_merged.append(pd.read_csv(file))

# Save the merged DataFrame to a new CSV file
df_merged.to_csv('merged_layoff_chart.csv', index=False)
