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
name = []

#appending lists
with open("final/golf.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        name.append(rec[0])
        distance.append(rec[1])
        wins.append(rec[2])
        majors.append(rec[3])
        cut.append(rec[4])

for i in range(0, len(distance)):
    print(f"{name[i]:5}  {distance[i]:20}  {wins[i]:25}  {majors[i]:15}  {cut[i]:5}")
print("--------------------------------------------------------------------------------")
#functions
ans = 'y'

while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Show all golfers") #show all golfers and their numbers
    print("2. Search by name")
    print("3. Search by driving distance") #searches by golfers last name 
    print("4. Search by wins")#allows to look up the percentage of fairways hit, percentage of greens hit and driving distance
    print("5. Search by majors")
    print("6. Search by did they make the cut")
    print("7. EXIT")

    search_type = input("\nHow would you like to search today? [1-8]: ")
        #option 8 - error
    if search_type == 8:
        print("\n\nThank you for using my program, GOODBYE!\n\n\n")
    #if the search type is wrong
        if search_type not in ["1", "2", "3", "4", "5", "6", "7"]:
         print("***INVALID ENTRY!***\nPlease try again")
    
    #option 1 - searching for student records
    if search_type == "1": 
        for i in range(0, len(name)):
            print(f"{name[i]:5}  {distance[i]:20}  {wins[i]:25}  {majors[i]:15}  {cut[i]:5}")
        print("--------------------------------------------------------------------------------")

    #option 2 - searching for how far the participants can hit it off the tee on average 
    elif search_type == "2": #search by name of golfer 
        print("\n~Search by name~")
        found = []  #empty list, found locations (index) will be stored if/when found
        search_let= input("Enter the golfer you wish to find: ") #genre we are looking through all golfers for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(name)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_let.lower() == name[i].lower(): 
                #if performs the SEARCH - is what we're looking for here in the list?
                found.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
                print(f"Found a {search_let} author in INDEX {i}")

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an EMPTY LIST
            #NOT found
            print(f"Your search for {search_let} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else: 
            #last name FOUND!
            print(f"Your search for {search_let} was FOUND! Here is their data: ")

            #'found' is a list populated with index locations - we loop through this list, and use found[i] (which again, holds an INDEX from our other searched-through list) to be recalled and used below
            for i in range(0, len(found)):
                print(f"{name[i]:5}  {distance[i]:20}  {wins[i]:25}  {majors[i]:15}  {cut[i]:5}")

    elif search_type == "3":
            print('search by distance')

            search = input("Enter the distance you are looking for: ")

            min = 0
            max = len(distance) - 1
            mid = int((min + max) / 2)
   

            print(min, max , mid, distance[mid])

        #while min < max and search.lower() != id[mid].lower():
            while min < max and search.lower() != distance[mid].lower():
                if search.lower() < distance[mid].lower():
                    max = mid - 1
                else:
                    min = mid + 1

            mid = int((min + max) / 2)
 
            if search.lower() == distance[mid].lower():
                print(f"we found your search for {search}, details below: ")
                print(f"{'name':12}  {'distance':3}  {'wins':3}  {'majors':3}  {'cut':3}")
                print(f"------------------------------------------------------")
                print(f"{name[i]:5}  {distance[i]:20}  {wins[i]:25}  {majors[i]:15}  {cut[i]:5}")
                print(f"---------------------------------------------------------")
            else:
                print(f"\nYour search for {search} is complete, no matches found ")