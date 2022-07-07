# Election Analysis (using Python)

## Project Overview
Our client is Tom, a Colorado Board of Elections employee. He wishes to conduct an election audit of the tabulated results for a US congressional precinct in colorado. Tom has asked that the following tasks be undertaken to complete the audit:  
	<ol>
	<li> Calculate the total number of votes cast in this election (for all candidates);
	<li> Extract a complete list of the candidates who received votes;
    <li> Calculate the total number of votes each candidate received;
    <li> Calculate the percentage of votes each candidate received; and
    <li> Determine the winner of the election (based on popular vote).
	</ol>

## Resources (Source Data & Analysis Software)
To accomplish these tasks, we used the following resources:
	<ol>
	<li> Data Source = 'election_results.csv'; and
	<li> Software = Python (v 3.9.7); Visual Code Studio (v 1.68,1);
	</ol>

The source data for this analysis (filename = 'election_results.csv') has the following structure:
	<ol>
	<li> It contains 369712 rows (first row contains headers);
	<li> It contains 3 columns (first column contains numeric data, and second and third columns contain strings)
	<li> The headers (Keys) are 'Ballot ID', 'County', and 'Candidate'
	</ol>
We used python to automate the election analysis and to output analysis results to a text (.csv) file, as described below.

## Results (Files Created)
The python code that we created resulted in the following outputs (files created):
	<ol>
	<li> Data Analysis Results File = 'election_analysis.txt'; and
	<li> Python Script = 'PyPoll.py';
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
	<li> There were three candidates who received votes:
    	<li> Charles Casper Stockham,
        <li> Diana DeGette, and
        <li> Raymon Anthony Doane.
    <li> There candidate results were as follows:
    	<li> Charles Casper Stockham received 23.0% of the vote (#votes = 85,213);
        <li> Diana DeGette received 73.8% of the vote (#votes = 272,892); and
        <li> Raymon Anthony Doane received 3.1% of the vote (#votes = 11,606);
    <li> The winning candidate was Diana DeGette, who received 73.8% of the vote (#votes = 272,892).
	</ol>

