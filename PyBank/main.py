# Import modules
import os
import csv

# set file path
dataPath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(dataPath, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))


'''
# open the file and parse it
with open(dataPath) as budgetFile:
    readable = csv.reader(budgetFile, delimiter=",")

    # loop through each line
    #for row in readable:
    '''