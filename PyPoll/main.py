# Import the os module to creaImte file path across operating system
import os

# import module for reading csv file
import csv
# Path to collect data from the Resources folder
csvpath = os.path.join ("Resources", "election_data.csv")

# Path to file to print the output
outputPath = os.path.join("analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open (csvpath) as csvfile:

# csvreader hold content of delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

# read the header row first 
    csv_header = next(csvreader)
   
    totalVoteCount = 0
# Create a dictionary to hold candidate name (key) and values(number of votes).
    voteDict = {}

# read each row of data after header
    for Row in csvreader:
        # logic to find candidates and vote counts for each candidate and store in dictionary
        totalVoteCount = totalVoteCount + 1
        candidateName = Row[2]
        if candidateName in voteDict.keys():
            voteCount = voteDict.get(candidateName)
            voteCount = voteCount + 1
            voteDict[candidateName] = voteCount 
        else:
            voteDict[candidateName] = 1

    
# output data to file and terminal
    with open (outputPath, "w") as outputFile:

        print ("\nElection Results")
        print ("\n----------------------------")
        print ("\nTotal Votes:" + " " + str(totalVoteCount))  
        print ("\n----------------------------")

        outputFile.write("\nElection Results\n")
        outputFile.write("\n----------------------------")
        outputFile.write("\n\nTotal Votes:" + " " + str(totalVoteCount)) 
        outputFile.write("\n\n----------------------------")

        winnerVotes = 0
        winnerName = ""
        for candidate in voteDict.keys():
            votes = voteDict.get(candidate)
        
            percentageVotes = votes*100/totalVoteCount

            print("\n" + candidate + ":" + " " + str(round(percentageVotes, 3)) + "% " +  "(" + str(votes) + ")")
            outputFile.write("\n\n" + candidate + ":" + " " + str(round(percentageVotes, 3)) + "% " +  "(" + str(votes) + ")")
        
        # determine winner and votes
            if votes > winnerVotes:
                winnerVotes = votes
                winnerName = candidate

        print ("\n----------------------------")
        print ("\nWinner: " + winnerName)
        print ("\n----------------------------")

        outputFile.write("\n\n----------------------------")
        outputFile.write("\n\nWinner: " + winnerName)
        outputFile.write("\n\n----------------------------")

        

    

    
     


   
   









