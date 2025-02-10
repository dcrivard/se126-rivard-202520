#Derek Rivard
#Midterm lab
#2/10/2025
#program prompt- Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold a “status” value for each book. Assign each book a status value of “On Loan” or “Available” and store to the newly created list. Half of the books should be “On Loan” and the other half should be “Available” – you can decide which books hold which status as long as it is an even split between the two potential values. Once the new list is populated, process through the five lists to display all of the data to the user as well as the total number of records in the file.  
# Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice2.csv’, where each book’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay). 
# Finally, create a sequential search program that allows a user to repeatedly search the book database information stored in the lists based on the following menu: 
# Personal Library Search 
# 1.	Search by TITLE
# 2.	Search by AUTHOR
#3.	EXIT 
#For option 1: When a searched-for item is found, print all data* in the program on the specific book from the lists. If they are not found, alert the user. 
#For option 2: When a searched for item is found, print all data* in the program on all authors that match the criteria. If no one matches the searched-for criteria, alert the user.  
#The user should not be able to quit the search program unless they choose option 3, to exit. 
#*All Data to print per employee if found: 
#title, author, genre, pages, status


#imports
import csv

#functions 


#1D empty list 
title = []
author = []
genre = []
pages = []
status = []

#new list 
on_loan = 0     #output 1
available = 0   #output 2
num_records = 0 #output 3


#with open statement allows you to append the lists you have identifyied 

print(f"{'Title':8} {'Author':8} {'Genre':8} {'Pages':8} {'status':8}")
print("---------------------------------------------------------------")
with open ("midterm/books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        title.append(rec[0])
        author.append(rec[1])
        genre.append(rec[2])
        pages.append(rec[3])


        num_records += 1
for i in range(0, num_records):

    if genre[i] == 'science fiction' or genre[i] == 'horror':
        status.append("on_loan")

    elif genre[i] == 'fantasy' or genre[i] == 'mystery' or genre[i] == 'thriller':
        status.append("available")


#print statement for empty lists
print(f"INDEX #:  {'Title':10}  {'Author':10}  {'Genre':3}  {'Pages':3}  {'status':3}")
print("-------------------------------------------------------------------------------")
for i in range(0, len(title)):
    print(f"INDEX {i}:  {title[i]:10}  {author[i]:10}  {genre[i]:3}  {pages[i]:3}  {status[i]:3}")
print("-------------------------------------------------------------------------------")

#create new data file
file = open('midterm/midterm_choice2.csv', 'w')

for i in  range(0, len(status)):
    file.write(f"{title[i]},{author[i]},{genre[i]},{pages[i]},{status[i]}")

file.close


#Do your sequencial search!
print("\tWelcome to the Student Search Program")

answer = input("Would you like to start your search? [y/n]: ").lower()

while answer == "y":
    #show user search menu 
    print("\t~Search Menu~")
    print("1. Search by Title")         #one search value found
    print("2. Search by Author")      #multiple search values found
    print("3. EXIT")
    #gain search type 
    search_type = input("Enter your search type [1-3]: ")
#If title can be found
    if search_type == "1":
        print("\tTitle SEARCH~")
        found = -1
        search_last = input("Enter the Title you wish to find: ")
        for i in range(0, len(title)):
            if search_last.lower() == title[i].lower(): 
                found = i

#if can or cannot be found
        if found != -1:
            #last name FOUND!
            print(f"Your search for {search_last} was FOUND! Here is their data: ")
            print(f"{title[found]:10}  {author[found]:10}  {genre[found]:3}  {pages[found]:3}  {status[found]:3}")
        else: 
            #NOT found
            print(f"Your search for {search_last} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")

    elif search_type == "2": #Author
        print("\tauthor SEARCH")

        found = []
        search_let= input("Enter the AUTHOR you wish to find: ")

        
        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an EMPTY LIST
            #NOT found
            print(f"Your search for {search_let} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else: 
            #Author FOUND!
            print(f"Your search for {search_let} was FOUND! Here is their data: ")

            #'found' is a list populated with index locations - we loop through this list, and use found[i] (which again, holds an INDEX from our other searched-through list) to be recalled and used below
            for i in range(0, len(found)):
                print(f"{found[i]}:  {title[found[i]]:10}  {author[found[i]]:10}  {genre[found[i]]:3}  {pages[found[i]]:3}  {status[found[i]]:3}")
    elif search_type == "3": #exit
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    #build a way out of the loop - answer should be able to change value! 
    if search_type == "1" or search_type == "2":
        #when search_type == "3" the user has chosen to exit, and if they did not provide a 1, 2, or 3 to search_type then they will automatically be brought back through the loop to see the menu again
        answer = input("Would you like to search again? [y/n]: ").lower()

print("\nThanks for using the search program. Goodbye!\n")