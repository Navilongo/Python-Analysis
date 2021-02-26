import os
import csv 


# Path to collect CSV data
current_directory = os.path.dirname(__file__)
poll_data = os.path.join(current_directory, 'Resources', 'election_data.csv')
elections_output = os.path.join(current_directory, 'Analysis', 'Analysis.txt')



# Read the CSV
with open(poll_data) as csv_file:
    poll = csv.reader(csv_file, delimiter=",")
    
    # Give start value for each variable that will be looped and added thorough loop
    votes = 0
    correy_vote = 0
    Khan_vote = 0
    otooley_vote = 0
    li_vote = 0

    # Skip header row
    next(poll)

    for row in poll:
        # Total votes per candidate
        if row[2] == "Correy":
            correy_vote = correy_vote + 1
        if row[2] == "Khan":
            Khan_vote = Khan_vote + 1
        if row[2] == "O'Tooley":
            otooley_vote = otooley_vote + 1
        if row[2] == "Li":
            li_vote = li_vote + 1
        
        # Total number of votes
        votes = votes + 1
        
        # Determine Percentages dividing number of votes counter earlier by number of votes
        correy_percent = float(correy_vote/votes)*100
        correy_percent = round(correy_percent, 3)
        Khan_percent = float(Khan_vote/votes)*100
        Khan_percent = round(Khan_percent, 3)
        otooley_percent = float(otooley_vote/votes)*100
        otooley_percent = round(otooley_percent, 3)
        li_percent = float(li_vote/votes)*100
        li_percent = round(li_percent, 3)

        # Determine highest vote
        final_votes = [correy_vote, Khan_vote, otooley_vote, li_vote]
        winner = max(final_votes)

        # Cast name of winner into Elected
        if winner == correy_vote:
            Elected = "Correy"
        elif winner == Khan_vote:
            Elected = "Khan"
        elif winner == otooley_vote:
            Elected = "O'Tooley"
        else:
            Elected = "Li"
    

# Print number of monWinner: {Elected}ths
results = f"""Election Results
------------------------------
Total Votes: {votes}
--------------------
Correy: {correy_percent}% Casted Votes: {correy_vote}
Khan: {Khan_percent}% Casted Votes: {Khan_vote}
O'Tooley: {otooley_percent}% Casted Votes: {otooley_vote}
Li: {li_percent}% Casted Votes: {li_vote}
----------------------------------------
Winner: {Elected}
--------------------
"""

print(results)



# Open the file using "write" mode. Specify the variable to hold the contents
with open(elections_output, 'w') as final_text:
    final_text.write(results)

