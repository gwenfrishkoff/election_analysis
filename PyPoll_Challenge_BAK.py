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
candidate_options = []  #create empty list of candidates
candidate_votes = {}  #create empty dict (key:value = candidate:#votes)

county_list = []  ##create empty list of counties
county_votes = {}  #create empty dict (key:value = county:#votes)

# Initialize variables
winning_candidate = "" #create empty string (for winning candidate name)
winning_count = 0 #create variable (to hold vote count for winning candidate)
winning_percentage = 0 #create variable (to hold %votes cast for winning candidate)

largest_county = "" #create empty string (for name of county w/largest turnout)
largest_county_count = 0 #create variable (to hold vote count for county w/largest turnout)
largest_percentage = 0 #create variable (to hold %votes cast for largest county)


## Open source data (election results) file and read file
with open(file_to_load) as election_data:
    # Read file object with the reader function
    file_reader = csv.reader(election_data)
    # Read header row
    headers = next(file_reader) #Use next() method to skip 1st row 
    # Get each row in CSV file
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1
        
        # Get the county name from each row
        county_name = row[1] 
        # Get the candidate name from each row
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add candidate name to candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1      
        
        # If the county name is not in county list...
        if county_name not in county_list:
            # Add county name to county list
            county_list.append(county_name)
            # Begin tracking that county's vote count
            county_votes[county_name] = 0
        # Add a vote to that county's count
        county_votes[county_name] += 1

## Loop through to get County Results
## Determine the votes count for each county by looping through the counts
    county_results = "" #Initialize string to hold county results (concatenated below)
    # Iterate through the county list
    for county_name in county_votes:
        # Retrieve vote count of a candidate
        votes_per_county = county_votes[county_name]
        # Calculate the percentage of votes per county
        county_vote_perc = int(votes_per_county) / int(total_votes) * 100
        # Save each county name, vote count, and percentage of votes to file
        county_results += (f"{county_name}: {county_vote_perc:.1f}% ({votes_per_county:,})\n")   

## Loop through to get Candidate Results
## Determine the percentage of votes for each candidate by looping through the counts
    candidate_results = "" #Initialize string to hold candidate results (concatenated below)
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes_per_candidate = candidate_votes[candidate_name]
        # Calculate the percentage of votes per candidate
        candidate_vote_perc = int(votes_per_candidate) / int(total_votes) * 100
        # Save each candidate's name, vote count, and percentage of votes to file
        candidate_results += (f"{candidate_name}: {candidate_vote_perc:.1f}% ({votes_per_candidate:,})\n")

## Determine winning candidate & winning candidate votes (count, %total)
        # Determine if the votes is greater than the winning count
        if (votes_per_candidate > winning_count) and (candidate_vote_perc > winning_percentage):
            # If true, then set winning_count = votes & winning_percent = vote_percentage
            winning_count = votes_per_candidate
            winning_percentage = candidate_vote_perc
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            
## Determine county with largest vote count & compute county stats (vote count, %total vote)            
## Calculate county results by looping through the counts
    # Iterate through the county list
    for county_name in county_votes:
        # Retrieve vote count for each county in county_votes dict
        votes_per_county = county_votes[county_name]
        # Calculate the percentage of votes per county
        county_vote_perc = int(votes_per_county) / int(total_votes) * 100
        # Find county with largest vote count
        if votes_per_county == max(county_votes.values()):        
            # If true, then set largest_county_count = #votes for theat county
            largest_county_count = votes_per_county
            largest_percentage = county_vote_perc
            # And, set the winning_candidate equal to the candidate's name.
            largest_county =  county_name          

##Print & save final (total & winning) election results
# Open text file & save analysis results to file
with open(file_to_save, "w") as txt_file:

    # Print the summary (total & winning) outcomes
    election_results = (
        f"\nElection Results\n"
        f"\n-------------------------\n"
        f"Total Votes: {total_votes:,}"
        f"\n-------------------------\n"      
        f"\nCounty Results:\n" 
        f"{county_results}" 
        f"\n-------------------------\n"     
        f"Largest County: {largest_county}\n"
        f"Largest County Turnout: {largest_county_count:,}\n"
        f"Largest County %Total Votes: {largest_percentage:.1f}%\n"   
        f"\n-------------------------\n"    
        f"\nCandidate Results:\n" 
        f"{candidate_results}" 
        f"\n-------------------------\n"  
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
        f"-------------------------\n")
    print(election_results, end="")           
    
    # Save the final outcomes to a text file
    txt_file.write(election_results)
  