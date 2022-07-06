### GOAL: Generate vote count report that will be used to certify US congressional race

# Import python modules
import csv
import os

### Step 1: OPEN SOURCE DATA FILE

# Assign variable for source data (election results) file and path (on local machine)
#file_to_load = '/Users/GwenF/Documents/GitHub/election_analysis/resources/election_results.csv'

# Open source data (election results) file and read file
#election_data = open(file_to_load, 'r')

# Assign variable for source data (election results) file and path (on local machine)
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign variable to save analyses to file and add to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open source data (election results) file and read file
with open(file_to_load) as election_data:

    # Read file object with the reader function
    file_reader = csv.reader(election_data)

    ### Step 2: RETRIEVE LIST OF CANDIDATE NAMES (KEYS)

    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)

    # Print 1st item from each row in the CSV file.
    #for row in file_reader:
    #    for i in range(len(row)):
    #        print([i])
    
    # Print 1st item from each row in the CSV file.
    for row in file_reader:
        for i in range(len(row)):
            print([i])
        
### Step 3: PERFORM DATA ANALYSES

# Add vote count for each candidate

# Calculate  total votes for each candidate

# Calculate total votes cast for the election

    ### Step 4: CLOSE SOURCE DATA FILE
    election_data.close()