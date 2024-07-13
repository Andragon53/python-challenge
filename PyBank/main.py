# Import modules
import os
import csv

# set file paths for data and output files
dataPath = os.path.join('Resources', 'budget_data.csv')
outputPath = os.path.join('analysis', 'data analysis.txt')

# targeted recording variables
totalMonths = 0
netTotal = 0
valueChanges = []
highProfitDate = ""
highProfitAmount = 0
highLossDate = ""
highLossAmount = 0

# open the file and parse it
with open(dataPath) as budgetFile:
    readable = csv.reader(budgetFile, delimiter=",")
    
    # read over the header
    next(readable)
    # loop through each line
    for row in readable:
        # increment month counter
        totalMonths += 1
        # record new value, and add it to the net total
        valueChanges.append(row[1])
        netTotal += int(row[1])

        # compare row value to current highest profit, update amount and date if higher
        if int(row[1]) > highProfitAmount:
            highProfitAmount = int(row[1])
            highProfitDate = str(row[0])
        # compare row value to current highest loss, update amount and date if higher
        if int(row[1]) < highLossAmount:
            highLossAmount = int(row[1])
            highLossDate = str(row[0])

# calculate change averages
changeAvg = netTotal/len(valueChanges)

# print results to console
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${changeAvg:.2f}") # Rounded to 2 decimal places
print(f"Greatest Monthly Profit: {highProfitDate} ${highProfitAmount}")
print(f"Greatest Monthly Loss: {highLossDate} ${highLossAmount}")

# open output file
analysis = open(outputPath, "a")
# output results to text file
analysis.write("Financial Analysis \n")
analysis.write("--------------------------------- \n")
analysis.write(f"Total Months: {totalMonths} \n")
analysis.write(f"Total: ${netTotal} \n")
analysis.write(f"Average Change: ${changeAvg:.2f} \n") # Rounded to 2 decimal places
analysis.write(f"Greatest Monthly Profit: {highProfitDate} ${highProfitAmount} \n")
analysis.write(f"Greatest Monthly Loss: {highLossDate} ${highLossAmount}")
analysis.close()