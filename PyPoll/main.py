import os
import csv

electiondata=os.path.join("Resources", "election_data.csv")

with open(electiondata, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(header)

    cant1 = "Diana DeGette"
    cant2 = "Raymon Anthony Doane"
    cant3 = "Charles Casper Stockham" 

#votiessss
    vote1 = 0
    vote2 = 0
    vote3 = 0

#loop de loop
    for person in csvreader:
        if person[2] == cant1:
            vote1 = vote1 + 1
        elif person[2] == cant2:
            vote2 = vote2 + 1
        elif person[2] == cant3:
            vote3 = vote3 + 1
  
#count them guys
totalv = vote1+vote2+vote3

#percentages
cant1_percent = ((vote1/totalv)*100)
cant2_percent = ((vote2/totalv)*100)
cant3_percent = ((vote3/totalv)*100)

#winner winner chicken dinner 

if vote1 > vote2 and vote1 > vote3:
    print("Charles, you big lug, you won!")
elif vote2 > vote1 and vote2 > vote3:
    print("Diana, you peach, you won!")
elif vote2 > vote1 and vote2 > vote3:
    print("Raymon, you lucky walnut, you won!")


#lemme see em 
print("Election Results ")
print("Total Votes: ", totalv)
print("Charles Casper Stockham: ", cant1_percent, "(", vote1, ")")
print("Diana DeGette:", cant3_percent, "(", vote3, ")")
print("Raymon Anthony Doane: ", cant3_percent, "(", vote3, ")")


#make the file pls

txtfile = "Poll.txt"
file_path = os.path.join("Poll.txt")
with open(txtfile, "w") as text_file:

    text_file.write("Election Results ")
    text_file.write("Total Votes: " + str(totalv))
    text_file.write("Charles Casper Stockham: " + str(cant1_percent) + str(vote1) )
    text_file.write("Diana DeGette:" + str(cant3_percent) + str(vote2) )
    text_file.write("Raymon Anthony Doane: "+ str(cant3_percent) + str(vote3) )