#Derek Rivard
#final lab
#3/3/2025

#program prompt - We here today are creating a program where we can search up golfers using sequencial search standerds to allow the user to identify a player by the distance they can hit a golf ball, how many tournament wins they have, the number of majors won, whtherh or not they made the cut this week and lastly their last names

#csv
import csv

#empty lists-----------------------------------------------
#number of yards per shot off the tee
distance = []
#overall career wins
wins = []
#overall career wins in a major championship
majors = []
#if they made it to the weekend for this weeks tournament (the Arnold Palmer)
cut = []
#last name
lname = []

#appending lists
with open("final/golf.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        distance.append(rec[0])
        wins.append(rec[1])
        majors.append(rec[2])
        lname.append(rec[3])
        cut.append(rec[4])

for i in range(0, len(distance)):
    print(f"{distance[i]:5}  {wins[i]:25}  {majors[i]:15}  {lname[i]:20}  {cut[i]:5}")
print("--------------------------------------------------------------------------------")
#functions
ans = 'y'

while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Show all golfers") #show all golfers and their numbers
    print("2. Search by driving distance") #searches by golfers last name 
    print("4. Search by wins")#allows to look up the percentage of fairways hit, percentage of greens hit and driving distance
    print("5. Search by majors")
    print("6. Search by lname")
    print("7. Search by did they make the cut")
    print("8. EXIT")

    search_type = input("\nHow would you like to search today? [1-8]: ")
        #option 8 - error
    if search_type == 8:
        print("\n\nThank you for using my program, GOODBYE!\n\n\n")
    #if the search type is wrong
        if search_type not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
         print("***INVALID ENTRY!***\nPlease try again")
    
    #option 1 - searching for student records
    if search_type == "1": 
        for i in range(0, len(distance)):
            print(f"{distance[i]:5}  {wins[i]:25}  {majors[i]:15}  {lname[i]:20}  {cut[i]:5}")
        print("--------------------------------------------------------------------------------")
