import os
import csv

csvpath=os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    totalmonths=[]
    profitloss=[]
    profitaverage=[]
    profitchange=[]

    for row in csvreader:
        totalmonths.append(row[0])
        profitloss.append(int(row[1]))

    monthlength=len(totalmonths)

    profittotal=sum(profitloss)

    profitaverage=profittotal / monthlength

    for i in range(len(profitloss)-1):
        profitchange.append(profitloss[i+1]-profitloss[i])
        profitincrease = max(profitchange)
        profitdecrease = min(profitchange)

    print("financial analysis ")
    print("Total Months: ", monthlength)
    print("Average Change ", profitaverage)
    print("Greatest Increase in Progress ", profitincrease)
    print("Greatest Decrease in Progress ", profitdecrease)

txtfile = "Finances.txt"
file_path = os.path.join("Finances.txt")
with open(txtfile, "w") as text_file:

    text_file.write("financial analysis ")
    text_file.write("Total Months: " + str(totalmonths))
    text_file.write("Average Change " + str(profitaverage))
    text_file.write("Greatest Increase in Progress " + str(profitincrease))
    text_file.write("Greatest Decrease in Progress " + str(profitdecrease))