import os
import csv
import sys 

# Total number of months included in the data set

# Path to collect CSV data
current_directory = os.path.dirname(__file__)
budget_data = os.path.join(current_directory, '..', 'Resources', 'budget_data.csv')


# Read the CSV
with open(budget_data) as csv_file:
    budget = csv.reader(csv_file, delimiter=",")
    total = 0
    # Skip header row
    next(budget)
    row_count = 0
    minVal, maxVal = [], []
    print(f"Budget Analysis")

    print(f"-----------------------------------")
    
    # Loop through whole csv
    for x in budget:
        
        # Count how many rows. Each row == each month in the year 
        row_count = row_count + 1

        # Net total amount of "Profit/Losses" over the period
        total = total + int(x[1])

        # Average of total changes
        average = int(total/row_count)

        # Find the Highest Profit and Lowest Loss
        minVal.append(float(x[1]))
    
        maxVal.append(float(x[1]))
    
    # Print number of months
    print(f"Number of months: {row_count}")

    # Print total profit/loss
    print(f"Total profit: {total}")

    print(f"Average Change: {average}")

    print("Greatest Increase In Profit:", x[0], min(minVal))

    print("Greatest Decrease In Profit:", x[0], max(maxVal))

    original_stdout = sys.stdout 

# Open the file using "write" mode. Specify the variable to hold the contents
with open('Analysis.txt', 'w') as final_text:
    print(f"Budget Analysis", file=final_text)
    
    print(f"-----------------------------------", file=final_text)
    
    

    
    

    
   

   
      
        

    

# Calculate the changes in the "Profit/Losses" over the entire period,
    # then find the average
# Greatest increase in profits (date and amount)
# Greatest decrease in losses (date and amount)


