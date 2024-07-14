# Import modules
import os
import csv

# set file paths for data and output files
dataPath = os.path.join('Resources', 'election_data.csv')
outputPath = os.path.join('analysis', 'results.txt')

# target recording variables
totalVotes = 0
ballot = []
'''
Each candidate will be defined as a dictionary in this
ballot list with a name (string), votes, and percentage
'''

# open the file and parse it
with open(dataPath) as votesFile:
    readable = csv.reader(votesFile, delimiter=",")
    
    # read over the header
    next(readable)

    # loop through each line to get each candidate
    for row in readable:
        # if the candidate name on the ballot hasn't been recorded...
        
            # create a new dictionary in the ballot with the candidate's name
            ballot.append({"Name": row[2], "Votes": 0, "Percent": 0})

    # then loop through each line to count votes
    for row in readable:
        # increment vote counter
        totalVotes += 1
        # find the matching candidate key, and update their vote counters
        """-----------------------"""
        
# calculate the percentage totals of each candidate
"""-----------------"""
# determine the election's winner
"""-----------------"""

# print results to console
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {totalVotes}")
print("---------------------------------")
for candidates in ballot:
    print(f"-name-: -votePercent-% (-votes-)")
print("---------------------------------")
print(f"Winner: -winner-")
print("---------------------------------")

# open output file
analysis = open(outputPath, "a")
# output results to text file
analysis.write("Election Results \n")
analysis.write("--------------------------------- \n")
analysis.write(f"Total Votes: {totalVotes} \n")
analysis.write("--------------------------------- \n")
for candidates in ballot:
    analysis.write(f"-name-: -votePercent-% (-votes-) \n")
analysis.write("--------------------------------- \n")
analysis.write(f"Winner: -winner- \n")
analysis.write("--------------------------------- \n")
analysis.close()