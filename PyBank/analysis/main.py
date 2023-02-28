import os
import csv

csvpath = os.path.join("..", "Resources", "budget.csv")

with open(budget_data.csv,) as csvfile:
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
