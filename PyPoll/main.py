# List dependencies for os.path.join
import os
import csv

# Set total for total number of votes to zero
# Set up dictionary for total count per candidate
total = 0
candidatecount = {}

# Read in a .csv file to open the file
csvpath = os.path.join('C:/Users/adm/Desktop/bootcamp/RU-JER-DATA-PT-10-2019-U-C/Homework/03-Python Homework/PyPoll/Resources', 'election_data.csv') 

# Open the file
with open(csvpath, newline='') as csvfile:
    # Read the dataset
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header 
    csvheader = next(csvreader)

    # Create loop for each row in the dataset    
    for row in csvreader:
        # Calculate total number of votes    
        total += 1

        # Set name to the candidate's name per row
        name = row[2]
        # Set conditional statement where the candidates with the same name counts
        if name in candidatecount:
            candidatecount[name] += 1
        # If name does not match the candidate on the current row, count a new name
        else:
            candidatecount[row[2]] = 1 

    # Set the winning count number to zero        
    winningcount = 0

    # Loop candidate name in the candidate count dictionary
    for name in candidatecount:

        # Set condition where the highest counted candidate is set as winner
        if candidatecount[name] > winningcount:
            winner = name
            winningcount = candidatecount[name]

    # Print election results to terminal
    print("Election Results")
    print("----------------------")
    print(f'Total Votes: {total}')
    print("----------------------")
    for name in candidatecount:   
        print(f'{name}: {((candidatecount[name] / total) * 100):.3f}%  {candidatecount[name]}')
    print("----------------------")
    print(winner)
    print("----------------------")

    # Write the election results to a text file
    f = open('Election Results.txt', 'w+')
    f.write("Election Results\n")
    f.write("----------------------\n")
    f.write(f'Total Votes: {total}\n')
    f.write("----------------------\n")
    for name in candidatecount:   
        f.write(f'{name}: {((candidatecount[name] / total) * 100):.3f}%  {candidatecount[name]}\n')
    f.write("----------------------\n")
    f.write(f'Winner: {winner}\n')
    f.write("----------------------")