### GOAL: Generate vote count report that will be used to certify US congressional race

# Add dependencies (import python modules)
import csv
import os

# Assign variable for source data (election results) file and path (on local machine)
file_to_load = os.path.join("resources", "election_results.csv")

# Assign variable to save analyses to file and add to path
file_to_save = os.path.join("analysis", "election_analysis.txt")


## Add vote count for each candidate
# Initialize a total vote counter
total_votes = 0

## Declare list and dict objects
candidate_options = []  #create empty list object
candidate_votes = {}    #create empty dictionary object

# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Open source data (election results) file and read file
with open(file_to_load) as election_data:

    # Read file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read header row
    headers = next(file_reader) #Use next() method to skip 1st row
    
    # Print each row in CSV file
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            # Add candidate name to candidate list
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

## Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list
for candidate_name in candidate_votes:
    
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    
    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    
###  To do: print out each candidate's name, vote count, and percentage of votes to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count
    #if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
    #     winning_count = votes
    #     winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
    #     winning_candidate = candidate_name

###  To do: print out the winning candidate, vote count and percentage to terminal

    # Print the candidate name and percentage of votes
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    
    # Print the candidate list
    #print(candidate_options)
    
    # Print the candidate vote dictionary
    #print(candidate_votes)
    
    # Print total votes
    #print(total_votes)

# Calculate total votes cast for the election

    ### CLOSE SOURCE DATA FILE
    election_data.close()