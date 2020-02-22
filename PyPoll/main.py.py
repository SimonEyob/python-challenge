import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    candiates=[]
    Khan=[]
    Correy=[]
    Li=[]
    O_Tooley=[]
    for row in csvreader:
        candiates.append(row[2])
    for i in range(len(candiates)):
        if i == "Khan":
            Khan.append(i)
        elif i == "Correy":
            Correy.append(i)
        elif i == "Li":
            Li.append(i)
        elif i == "O'Tooley":
            O_Tooley.append(i)
voters=len(candiates)
Khan_votes=len(Khan)
Correy_votes=len(Correy)
Li_votes=len(Li)
O_tooley_votes=len(O_Tooley)
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(voters))
print("Khan: "+ str(Khan_votes))