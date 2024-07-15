# Import modules
import os
import csv

# set file paths for data and output files
dataPath = os.path.join('Resources', 'election_data.csv')
outputPath = os.path.join('analysis', 'results.txt')

# target recording variables
totalVotes = 0
candidateList = []
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
        # increment vote counter
        totalVotes += 1
        # If the candidate is not in the candidate list...
        if row[2] not in candidateList:
            # create new entries for them in the ballot & candidate list,
            # and add a vote to the candidate's total
            ballot.append({"Name": row[2], "Votes": 1, "Percent": 0})
            candidateList.append(row[2])
        else:
            # find the candidate voted for, and update the tally
            for candidate in ballot:
                if candidate["Name"] == row[2]:
                    candidate["Votes"] = candidate["Votes"] + 1

# Set variables to hold the winner
winner = "UNKNOWN"
winningCount = 0

# for each candidate...
for candidate in ballot:
    # calculate the percentage totals of each candidate, and format correctly
    candidate["Percent"] = (candidate["Votes"] / totalVotes) * 100
    # determine if they are winning the election
    if candidate["Votes"] > winningCount:
        winningCount = candidate["Votes"]
        winner = candidate["Name"]

# print results to console
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {totalVotes}")
print("---------------------------------")
for candidate in ballot:
    print(f"{candidate["Name"]}: {candidate["Percent"]:.3f}% ({candidate["Votes"]})")
print("---------------------------------")
print(f"Winner: {winner}")
print("---------------------------------")

# open output file
analysis = open(outputPath, "a")
# output results to text file
analysis.write("Election Results \n")
analysis.write("--------------------------------- \n")
analysis.write(f"Total Votes: {totalVotes} \n")
analysis.write("--------------------------------- \n")
for candidate in ballot:
    analysis.write(f"{candidate["Name"]}: {candidate["Percent"]:.3f}% ({candidate["Votes"]}) \n")
analysis.write("--------------------------------- \n")
analysis.write(f"Winner: {winner} \n")
analysis.write("--------------------------------- \n")
analysis.close()
