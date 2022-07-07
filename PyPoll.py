### GOAL: Generate vote count report that will be used to certify US congressional race

## Add dependencies (import python modules)
import csv
import os

## Initialize variables
# Assign variable for source data (election results) file and path (on local machine)
file_to_load = os.path.join("resources", "election_results.csv")
# Assign variable to save analyses to file and add to path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize total vote counter
total_votes = 0
# Declare list and dict objects
candidate_options = []  #create empty list object
candidate_votes = {}    #create empty dictionary object
# Initialize winning candidate, vote count, and percentage variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

## Open source data (election results) file and read file
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

# Open text file & save analysis results to file
with open(file_to_save, "w") as txt_file:
    
    # After opening the file, print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # After printing the final vote count to the terminal, save the final vote count to the text file
    txt_file.write(election_results)
    
## Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Save each candidate's name, vote count, and percentage of votes to file
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage to terminal
        print(candidate_results)
        #  Save the candidate results to our text file
        txt_file.write(candidate_results)

## Determine winning vote count, winning percentage, and winning candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true, then set winning_count = votes & winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            
    # Print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
