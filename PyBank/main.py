import pandas as pd

# Load the data
file_path = 'Resources/budget_data.csv'
data = pd.read_csv(file_path)

# Calculate the total number of months included in the dataset
total_months = data.shape[0]

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
data['Change'] = data['Profit/Losses'].diff()

# Calculate the average of those changes
average_change = data['Change'].mean()

# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase = data.loc[data['Change'].idxmax()]
greatest_increase_date = greatest_increase['Date']
greatest_increase_amount = greatest_increase['Change']

# Find the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = data.loc[data['Change'].idxmin()]
greatest_decrease_date = greatest_decrease['Date']
greatest_decrease_amount = greatest_decrease['Change']

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount:.0f})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount:.0f})")


# Write the results to a text file
with open("analysis/pybank_analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount:.0f})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount:.0f})\n")