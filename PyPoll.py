### GOAL: Generate vote count report that will be used to certify US congressional race

# Add dependencies (import python modules)
import csv
import os

### Step 1: OPEN SOURCE DATA FILE

# Assign variable for source data (election results) file and path (on local machine)
file_to_load = os.path.join("resources", "election_results.csv")

# Assign variable to save analyses to file and add to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

### Step 2: RETRIEVE LIST OF CANDIDATE NAMES (KEYS)
        
### Step 3: PERFORM DATA ANALYSES

## Add vote count for each candidate

# 1. Initialize a total vote counter.
total_votes = 0

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
        # 2. Add to the total vote count
        total_votes += 1

    # 3. Print the total votes.
    print(total_votes)

# Calculate  total votes for each candidate

# Calculate total votes cast for the election

    ### Step 4: CLOSE SOURCE DATA FILE
    election_data.close()