import os
import csv

csvpath=os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath,) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    totalmonths=[]
    profitlosses=[]
    profitaverage=[]
    profitincrease=[]
    profitdecrease=[]


    monthlength=len(Date)

    profittotal=sum(Profit/Losses)

    profitaverage=profittotal / monthlength



    print("financial analysis")
    print("Total Months: ", monthlength)
    
