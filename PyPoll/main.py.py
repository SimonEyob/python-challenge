import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join("output", "new.txt")
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
    
voters=len(candiates)
Khan_votes=candiates.count("Khan")
Correy_votes=candiates.count("Correy")
Li_votes=candiates.count("Li")
O_tooley_votes=candiates.count("O'Tooley")
if Khan_votes >Correy_votes and Li_votes and O_tooley_votes:
    winner = "Khan"
if Correy_votes  > Khan_votes and Li_votes and O_tooley_votes:
    winner = "Correy"
if  Li_votes > Khan_votes and Correy_votes and O_tooley_votes:
    winner = "Li"
if O_tooley_votes >Correy_votes and Li_votes and Khan_votes:
    winner = "O'Tooley"

output=(f'Election Results\n'
        f'-------------------------\n'
        f'Total Votes: ({voters})\n'
        f'Khan: {round(Khan_votes/voters*100,2)}% ({Khan_votes})\n'
        f'Correy: {round(Correy_votes/voters*100,2)}"% ({Correy_votes})\n'
        f'Li: {round(Li_votes/voters*100,2)}% ({Li_votes})\n'
        f'OTooley: {round(O_tooley_votes/voters*100,2)}% ({O_tooley_votes}))\n'
        f'-------------------------\n'
        f'The winner is: "{winner}\n'
        f'-------------------------')

print(output)


#print("Election Results")
#print("-------------------------")
#print("Total Votes: " + str(voters))
#print("-------------------------")
#print("Khan: "+str(int(Khan_votes/voters*100))+"% ("+ str(Khan_votes)+")")
#print("Correy: "+str(int(Correy_votes/voters*100))+"% ("+ str(Correy_votes)+")")
#print("Li: "+str(int(Li_votes/voters*100))+"% ("+ str(Li_votes)+")")
#print("O'Tooley: "+str(int(O_tooley_votes/voters*100))+"% ("+ str(O_tooley_votes)+")")
#print("-------------------------")
#print("The winner is: "+ str(winner))
#print("-------------------------")
output_path=open('output_path','w')
output_path.write(output)
output_path.close()

    

 
    
