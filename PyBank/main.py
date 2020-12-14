# Your task is to create a Python script that analyzes the records to calculates each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# Print the analysis to the terminal and export a text file with the results

# Import dependencies
import os
import csv

# Define variables that will hold data
months = []
prof_loss_chgs = []

# Define variables and give them a starting value
count_months = 0
net_prof_loss = 0
prev_month_prof_loss = 0
current_month_prof_loss = 0
prof_loss_chg = 0

# Path to the csv file that I will be using
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
          
    # Read through each row of data after the header
    for row in csv_reader:

        # Count of months
        count_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_month_prof_loss = int(row[1])
        net_prof_loss += current_month_prof_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            prev_month_prof_loss = current_month_prof_loss
  
        else:

            # Compute change in profit loss 
            prof_loss_chg = current_month_prof_loss - prev_month_prof_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            prof_loss_chgs.append(prof_loss_chg)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            prev_month_prof_loss = current_month_prof_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_prof_loss = sum(prof_loss_chgs)
    avg_prof_loss = round(sum_prof_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_chg = max(prof_loss_chgs)
    lowest_chg = min(prof_loss_chgs)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = prof_loss_chgs.index(highest_chg)
    lowest_month_index = prof_loss_chgs.index(lowest_chg)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# -->>  Print the analysis to the terminal
print()
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_prof_loss}")
print(f"Average Change:  ${avg_prof_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_chg})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_chg})")


# Export a text file with the results
analysis_file = os.path.join("analysis", "budget_analysis.txt")
with open(analysis_file, "w") as outfile:

   outfile.write("\n")
   outfile.write("Financial Analysis\n")
   outfile.write("----------------------------\n")
   outfile.write(f"Total Months:  {count_months}\n")
   outfile.write(f"Total:  ${net_prof_loss}\n")
   outfile.write(f"Average Change:  ${avg_prof_loss}\n")
   outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_chg})\n")
   outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_chg})\n")
  