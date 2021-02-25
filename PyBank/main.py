import os
import csv 

# Total number of months included in the data set

# Path to collect CSV data
current_directory = os.path.dirname(__file__)
budget_data = os.path.join(current_directory, 'Resources', 'budget_data.csv')


# Read the CSV
with open(budget_data) as csv_file:
    budget = csv.reader(csv_file, delimiter=",")
    total = 0
    # Skip header row
    next(budget)
    row_count = 0
    print(f"Budget Analysis")

    print(f"-----------------------------------")
    
    # Loop through whole csv
    for x in budget:
        # Count how many rows. Each row == each month in the year 
        row_count = row_count + 1

        # Net total amount of "Profit/Losses" over the period
        total = total + int(x[1])

        # Average of total changes
        average = total/row_count
        

    

     # Average of total changes
       # average = total/row_count
            
     
    # Print number of months
    print(f"Number of months: {row_count}")

    # Print total profit/loss
    print(f"Total profit {total}")

    print(f"Average Change {average}")

    
    

    
   

   
      
        

    

# Calculate the changes in the "Profit/Losses" over the entire period,
    # then find the average
# Greatest increase in profits (date and amount)
# Greatest decrease in losses (date and amount)


