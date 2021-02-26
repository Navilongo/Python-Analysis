import os
import csv 

# Total number of months included in the data set

# Path to collect CSV data
current_directory = os.path.dirname(__file__)
poll_data = os.path.join(current_directory, 'Resources', 'election_data.csv')


# Read the CSV
with open(poll_data) as csv_file:
    poll = csv.reader(csv_file, delimiter=",")
    
    votes = 0
    correy_vote = 0
    Khan_vote = 0

    # Skip header row
    next(poll)

    for row in poll:
        # Total votes per candidate
        if row[2] == "Correy":
            correy_vote = correy_vote + 1
        if row[2] == "Khan":
            Khan_vote = Khan_vote + 1
        votes = votes + 1
        
        #Percentages
        correy_percent = float(correy_vote/votes)*100
        correy_percent = round(correy_percent, 3)
    print(f"Correy: {correy_percent}% Total: {correy_vote}")
    #print(f"Khan: {Khan_vote}")
    #print(votes)


#Total number of votes
#List of candidates who received votes
# percentage of votes each candidate won
# winner of election based on popular vote