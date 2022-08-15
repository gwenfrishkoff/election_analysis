# Election Analysis (using Python)

## Project Overview
Our client is Tom, a Colorado Board of Elections employee. He wishes to conduct an election audit of the tabulated results for a US congressional precinct in Colorado. Tom has asked that the following tasks be undertaken to complete the audit:  
	<ol>
	<li> Determine election results (total #votes & %votes) for each candidate;
	<li> Determine election results (total #votes & %votes) for each county;
	<li> Find the county with the largest turnout; and
	<li> Determine the winner of the election (based on popular vote).
	</ol>

We have been asked to write a python script that determines election results, prints findings to the terminal, and saves them to a text file.

## Resources (Source Data & Analysis Software)
To accomplish these tasks, we used the following resources:
	<ol>
	<li> Data Source = 'election_results.csv'; and
	<li> Software = Python (v 3.9.7); Visual Code Studio (v 1.68.1);
	</ol>

The source data for this analysis (filename = 'election_results.csv') has the following structure:
	<ol>
	<li> It contains 369712 rows (first row contains headers);
	<li> It contains 3 columns (first column contains numeric data, and second and third columns contain strings)
	<li> The headers (Keys) are 'Ballot ID', 'County', and 'Candidate'
	</ol>
We used python 3 to automate the election analysis and to output analysis results to a text (.csv) file, as described below.

## Results (Files Created)
The python code that we created resulted in the following outputs (files created):
	<ol>
	<li> Data Analysis Results File = 'election_analysis.txt'; and
	<li> Python Script = 'PyPoll_Challenge.py';
	</ol>

The analysis results file (filename = 'election_analysis.txt') has the following structure:
	<ol>
	<li> It contains 13 rows (including a title row and 7 rows with tabulated results);
	<li> The first row of tabulated results shows the total number of votes cast in this election;
	<li> The next three rows of tabulated results show the number and percentage of votes cast for each of the three candidates; and
	<li> The final three rows of tabulated results show the winning candidate, winning vote count, and winning percentage.
	</ol>

The analysis python script (filename = 'PyPoll.py') has the following structure:
	<ol>
	<li> It contains 91 rows (including rows with code comments and annotations);
	<li> The first chunk of code imports dependencies (python modules);
	<li> The next chunk of code declares and initializes key variables (including empty lists and dictionary objects);
	<li> The subsequent chunk of code opens and reads the source (.csv) data using python; 
	<li> The next several chunks of code determine the percentage of voates cast for each candidate, the winning vote count, winning percentage, and winning candidate; and
	<li> The final chunk of code prints the candidates' results to the terminal and saves results to a text file.
	</ol>

## Summary
Analysis results suggest the following conclusions:
	<ol>
	<li> There were 369,711 total votes cast in the election.
	<li> The winning candidate was Diana DeGette, who received 73.8% of the vote (#votes = 272,892).
	<li> The county with the largest turnout (#votes = 306,055, 82% of the vote) was in Denver, CO.
	</ol>

