# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# Print the analysis to the terminal and export a text file with the results

import os
import csv

# Read in csv file
election_data_csv = os.path.join('Resources','election_data.csv')

# Create variables
total_votes = 0
candidates_unique = []
candidate_vote_count = []

#read the csv file
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #This is the total votes cast, just count rows
        total_votes += 1
        #read in the candidate from column 3 of csv
        candidate_in = (row[2])
        #if candidate alreaady in list then locate the candidate by index # and increment the vote count by 1
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            #if candidate was not found in candidates_unique list then append to list and add 1 to vote count
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)

pct = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
    #calculation to get the percentage, x is the looper value
    vote_pct = round(candidate_vote_count[x]/total_votes*100)
    pct.append(vote_pct)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index] 

# Print to Screen
print('\n')
print('Election Results')
print('--------------------------')
print(f'Total Votes: {total_votes}')
print('--------------------------')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pct[x]}.000% ({candidate_vote_count[x]})')
print('--------------------------')
print(f'Winner: {election_winner}')
print('--------------------------')

# Create a text file
analysis_file = os.path.join("analysis", "election_analysis.txt")
with open(analysis_file, "w") as outfile:
    
    outfile.write('\n')
    outfile.write('--------------------------\n')
    outfile.write('Election Results\n')
    outfile.write('--------------------------\n')
    outfile.write(f'Total Votes: {total_votes}\n')
    outfile.write('--------------------------\n')
    for x in range(len(candidates_unique)):
        outfile.write(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    outfile.write('--------------------------\n')
    outfile.write(f'Election winner: {election_winner.upper()}\n')
    outfile.write('--------------------------\n')

