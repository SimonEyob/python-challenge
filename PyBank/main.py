# Module for reading CSV files
import os
import csv
from numpy import mean

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    date=[]
    profit_loses=[]
    changes=[]
    net_total=0
    
    # Read each row of data after the header
    for row in csvreader:
        date.append(str(row[0]))
        profit_loses.append(int(row[1]))
        net_total += int(row[1])
    for i in range(len(profit_loses)):
        if i==85:
           break
        else:
            changes.append(int(profit_loses[i+1])-int(profit_loses[i]))

           

print("Financial Analysis")
print("----------------------------")
print("Total Months: "+ str(len(date)))
print("Total: $"+ str(mean(net_total))) 
print("Average  Change: $"+ str(mean(changes)))
print("Greatest Increase in Profits: " + date[changes.index(int(max(changes)))+1] + " ($" + str(max(changes)) + ")") 
print("Greatest Increase in Profits: " + date[changes.index(int(min(changes)))+1] + " ($" + str(min(changes)) + ")") 