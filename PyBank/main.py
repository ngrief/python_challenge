import os
import pandas as pd

# Set the exact path to the CSV file 
budget_path = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

# Verify the file exists
if not os.path.exists(budget_path):
    print(f"Error: File not found at {budget_path}")
    exit()

# Read the CSV file into a pandas DataFrame
# Assuming the first row contains headers, no changes needed for the header row
df = pd.read_csv(budget_path, header=0)  # Explicitly stating that the first row is the header

# Calculate total number of months
total_months = len(df)

# Calculate net total amount of "Profit/Losses"
net_total = df['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
df['Profit_Change'] = df['Profit/Losses'].diff()

# Calculate average change
average_change = df['Profit_Change'].mean()

# Find greatest increase in profits
greatest_increase = df.loc[df['Profit_Change'].idxmax()]

# Find greatest decrease in profits
greatest_decrease = df.loc[df['Profit_Change'].idxmin()]

# Prepare the results
results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Profit_Change']:.0f})
Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Profit_Change']:.0f})
"""

# Print results to console
print(results)

# Create output directory if it doesn't exist
output_dir = os.path.join(os.path.dirname(budget_path), "..", "Analysis")
os.makedirs(output_dir, exist_ok=True)

# Write results to text file
output_path = os.path.join(output_dir, "financial_analysis.txt")
with open(output_path, 'w') as output_file:
    output_file.write(results)

print(f"Results have been saved to {output_path}")