import os
import csv 

# Total number of months included in the data set

# Path to collect CSV data
current_directory = os.path.dirname(__file__)
budget_data = os.path.join(current_directory, 'Resources', 'budget_data.csv')


# Read the CSV
with open(budget_data) as csv_file:
    budget = csv.reader(csv_file, delimiter=",")

    # Skip header row
    next(budget)

    print(f"Budget Analysis")

    print(f"-----------------------------------")
    
    # Loop through whole csv
    for row in budget:
        
    
    # Net total amount of "Profit/Losses" over the period
        total = 0
        total += int(row[1])
        print(f"Total profit {total}")

    # Count how many rows. Each row == each month in the year 
        row_count = sum(1 for row in budget)     
     
    # Print number of months
        print(f"Number of months: {row_count}")

    
    

    
   

   
      
        

    

# Calculate the changes in the "Profit/Losses" over the entire period,
    # then find the average
# Greatest increase in profits (date and amount)
# Greatest decrease in losses (date and amount)


