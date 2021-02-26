import os
import csv
import sys 

# Total number of months included in the data set

# Path to collect CSV data
current_directory = os.path.dirname(__file__)
budget_data = os.path.join(current_directory, '..', 'Resources', 'budget_data.csv')
analysis_output = os.path.join(current_directory, 'Analysis' 'Analysis.txt')

# Read the CSV
with open(budget_data) as csv_file:
    budget = csv.reader(csv_file, delimiter=",")
    total = 0
    # Skip header row
    next(budget)
    row_count = 0
    month, val = [], []
    
     
    # Loop through whole csv
    for x in budget:
        
        # Count how many rows. Each row == each month in the year 
        row_count = row_count + 1

        # Net total amount of "Profit/Losses" over the period
        total = total + int(x[1])

        # Average of total changes
        average = int(total/row_count)

        # Find the Highest Profit and Lowest Loss
        val.append(float(x[1]))
    
        month.append(x[0])



# Print number of months
results = f"""Budget Analysis
------------------------------
Number of months: {row_count}
Total profit: {total}
Average Change: {average}
Greatest Decrease in Profit: {month[val.index(min(val))]} {min(val)}
Greatest Increase in Profit: {month[val.index(max(val))]} {max(val)}
"""

print(results)



# Open the file using "write" mode. Specify the variable to hold the contents
with open(analysis_output, 'w') as final_text:
    final_text.write(results)
    
    
    


    
    

    
   

   
      
        

    

# Calculate the changes in the "Profit/Losses" over the entire period,
    # then find the average
# Greatest increase in profits (date and amount)
# Greatest decrease in losses (date and amount)


