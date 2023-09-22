# Module 3 Challenge

## Problem
We have solved two problems in this challenge namely PyPoll and PyBank. In PyPoll, our task was to read election data from a csv file to determine the polling result and the final winner. In the PyBank, our task was to read budget data from a csv file to calculate profit/loss statistics.

## Location of source

### PyBank

* **PyBank code file:** PyBank/main.py

* **PyBank output:** PyBank/analysis/output.txt

* **PyBank resource:** PyBank/Resources/budget_data.csv

### PyPoll

* **PyPoll code file:** PoPoll/main.py

* **PyPoll output:** PyPoll/analysis/output.txt

* **PyPoll resource:** PyPoll/Resources/election_data.csv

## Explanation of code

In both of the problems we read data from the CSV file and apply logic to get the final result. 

In PyPoll, we used dictionary to keep track of candidates and their votes. The solution can be applied to any new CSV file as well with same format to get the required outcome.

In PyBank, we used different variables to determine certain statistics from the provided csv file. Example: greatest increase in profit, greatest decrease in profit, average change etc.


## Learnings

* Using List and Dictionary data structures to solve problems. In PyPoll, we made sure that the solution does not require change even if new candidates are introduced. In both problems, we used list data structures to read the row data from csv files

* Reading CSV file using csvReader and looping through the entire data to solve the problem.

* Writing output to Terminal and an output file.

* Understanding absolute and relative path concepts.

* Using string concatenation to print the required outputs.
