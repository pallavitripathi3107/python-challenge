# Import the os module to creaImte file path across operating system
import os

# import module for reading csv file
import csv
# Path to collect data from the Resources folder
csvpath = os.path.join ("Resources", "budget_data.csv")

outputPath = os.path.join("analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open (csvpath) as csvfile:

# csvreader hold content of delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

# read the header row and print
    csv_header = next(csvreader)
    
    RowCount = 0
    sum = 0
    greatestIncrease = 0
    greatestIncreaseMonth = ""
    greatestDecrease = 0
    greatestDecreaseMonth = ""
    changeSum = 0

# read each row of data after header
    for Row in csvreader:
        RowCount = RowCount + 1
#calculating total sum amount
        sum = sum + int(Row[1])
#calculating greatest increase in profit over the entire period
        if RowCount > 1:
            currentIncrease = int(Row[1]) - lastRowAmount
            if currentIncrease > greatestIncrease:
                greatestIncrease = currentIncrease
                greatestIncreaseMonth = Row[0]

#calculating greatest decrease in profit over the entire period
        if RowCount > 1:
            currentDecrease = int(Row[1]) - lastRowAmount
            if currentDecrease < greatestDecrease:
                greatestDecrease = currentDecrease
                greatestDecreaseMonth = Row[0]
#calculating change in profit/loss over the entire period  
            currentChange = int(Row[1]) - lastRowAmount
            changeSum = (changeSum + currentChange)
 
#saving last row amount in a variable to be used in next iteration.
        lastRowAmount = int(Row[1])

#calculating average of change in profit/loss over the entire period       
averageChange = round(changeSum / (RowCount -1), 2)

#output print
print("\nFinancial Analysis")
print("\n---------------------------")
print ("\nTotal Months: " + str(RowCount))
print("\nTotal: $" + str(sum))  
print("\nAverage Change: $" + str(averageChange))  
print("\nGreatest Increase in Profits: " + greatestIncreaseMonth + " ($" + str(greatestIncrease) + ")")
print("\nGreatest Decrease in Profits: " + greatestDecreaseMonth + " ($" + str(greatestDecrease) + ")")

with open (outputPath, "w") as outputFile:
    outputFile.write("\nFinancial Analysis\n")
    outputFile.write("\n---------------------------")
    outputFile.write("\n\nTotal Months: " + str(RowCount))
    outputFile.write("\n\nTotal: $" + str(sum))
    outputFile.write("\n\nAverage Change: $" + str(averageChange))
    outputFile.write("\n\nGreatest Increase in Profits: " + greatestIncreaseMonth + " ($" + str(greatestIncrease) + ")")
    outputFile.write("\n\nGreatest Decrease in Profits: " + greatestDecreaseMonth + " ($" + str(greatestDecrease) + ")")
    
