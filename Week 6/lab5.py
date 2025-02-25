#derek Rivard
#Lab 5
#2/20/2025

#program prompt - Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options.  Your program should give your user the following menu:
#Personal Library Menu
# 1.	Show All Titles – list all book data to the user alphabetically by title
# 2.	Search by Title – allow for an entire title or a title key word
# 3.	Search by Author – show all titles of the searched-for author
# 4.	Search by Genre - show all titles of the searched-for genre
# 5.	Search by Library Number – only allow for one specific library number item
# 6.	Show All Available – show all titles with status “available”
# 7.	Show All On Loan - show all titles with status “on loan”
# 8.	EXIT
# When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author, Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches should not be case sensitive.

#imports
import csv

#empty lists
library_num = []
title = []
author = []
genre = []
page = []
status = []

#total records
totalrecords = 0

#header
print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5} {'STATUS':5}")
print("--------------------------------------------------------------------------------")

#append your lists into there individual rows
with open("Week 6/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: 
        library_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        page.append(rec[4])
        status.append(rec[5])


for i in range(0, len(library_num)):
    print(f"{library_num[i]:5}  {title[i]:25}  {author[i]:15}  {genre[i]:20}  {page[i]:5}  {status[i]:25}")
print("--------------------------------------------------------------------------------")
#each title shown in order by bubble sort
for i in range(0, len(title) -1):

    for index in range(0, len(title) - 1):#inner loop

        if(title[index] > title[index + 1]):

            #if above is true, swap places!

            temp = title[index]
            title[index] = title[index + 1]
            title[index + 1] = temp

            #swap all other values
            temp = author[index]
            author[index] = author[index + 1]
            author[index + 1] = temp

            #swap library num
            temp = library_num[index]
            library_num[index] = library_num[index + 1]
            library_num[index + 1] = temp

            #swap genre
            temp = genre[index]
            genre[index] = genre[index + 1]
            genre[index + 1] = temp

            #swap page
            temp = page[index]
            page[index] = page[index + 1]
            page[index + 1] = temp

            #swap status
            temp = status[index]
            status[index] = status[index + 1]
            status[index + 1] = temp
for i in range(0, len(library_num)):
    print(f"{library_num[i]:5}  {title[i]:25}  {author[i]:15}  {genre[i]:20}  {page[i]:5}  {status[i]:25}")
#disconnected from file
ans = 'y'

while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Search by title") #searches by title
    print("2. Search by author") #binary search review
    print("3. Search by genre") #find part of a whole
    print("4. Search by Library number")
    print("5. EXIT")

    search_type = input("\nHow would you like to search today? [1-5]: ")
    if search_type == 5:
        print("\n\nThank you for using my program, GOODBYE!\n\n\n")
    #if the search type is wrong
    if search_type not in ["1", "2", "3", "4", "5"]:
         print("***INVALID ENTRY!***\nPlease try again")

#Option #1
    elif search_type == "1":
        print('search by title or title key word')

        search = input("Enter the Title you are looking for: ")

        min = 0
        max = len(title) - 1
        mid = int((min + max) / 2)
   

        print(min, max , mid, title[mid])

        #while min < max and search.lower() != title[mid].lower():
        while min < max and search.lower() != title[mid].lower():
            if search.lower() < title[mid].lower():
                max = mid - 1
            else:
                min = mid + 1

            mid = int((min + max) / 2)

        if search.lower() == title[mid].lower():
            print(f"we found your search for {search}, details below: ")
            print(f"{'TITLE':12}  {'AUTHOR':3}  {'GENRE'}")
            print(f"------------------------------------------------------")
            print(f"{title[mid]:12}  {author[mid]:3}  {genre[mid]}")
            print(f"---------------------------------------------------------")
        else:
            print(f"\nYour search for {search} is complete, no matches found ")

    elif search_type == "2": #search by author
        print("\n~Search by author~")
        found = []  #empty list, found locations (index) will be stored if/when found
        search_let= input("Enter the author you wish to find: ") #genre we are looking through all students for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(author)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_let.lower() == author[i].lower(): 
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
                print(f"{library_num[i]:5}  {title[i]:25}  {author[i]:15}  {genre[i]:20}  {page[i]:5}  {status[i]:25}")

    elif search_type == "3": #search by genre
        print("\n~Search by genre~")
        found = []  #empty list, found locations (index) will be stored if/when found
        search_let= input("Enter the Genre you wish to find: ") #genre we are looking through all students for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(genre)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_let.lower() in genre[i].lower(): 
                #if performs the SEARCH - is what we're looking for here in the list?
                found.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
                print(f"Found a {search_let} genre in INDEX {i}")

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
                print(f"{library_num[found[i]]:5}  {title[found[i]]:25}  {author[found[i]]:15}  {genre[found[i]]:20}  {page[found[i]]:5}  {status[found[i]]:25}")


    elif search_type == "4": #search for library number
        search = input("\nWhat Library number are you searching for?:  ")
        for i in range(0, len(library_num)):
            if library_num[i] == search:
                print(f"{library_num[i]:5}  {title[i]:25}  {author[i]:15}  {genre[i]:20}  {page[i]:5}  {status[i]:25}")
                print("-------------------------------------------------------------------------------------------")

        else:
            if i == len(library_num):
                print("search not found")

    elif search_type == "4":
        print("\n~Search by status~")
        found = []  #empty list, found locations (index) will be stored if/when found
        search_let= input("Enter the status you wish to find: ") #genre we are looking through all students for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(status)):
            #for loop performs the SEQUENCE - from start through end of list items

            if status[i] == 'avaliable': 
                #if performs the SEARCH - is what we're looking for here in the list?
                found.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
                print(f"Found a {search_let} status in INDEX {i}")
                i + 1
        else: 
            #last name FOUND!
            print(f"Your search for {search_let} was FOUND! Here is their data: ")

            #'found' is a list populated with index locations - we loop through this list, and use found[i] (which again, holds an INDEX from our other searched-through list) to be recalled and used below
            for i in range(0, len(found)):
                print(f"{library_num[found[i]]:5}  {title[found[i]]:25}  {author[found[i]]:15}  {genre[found[i]]:20}  {page[found[i]]:5}  {status[found[i]]:25}")

#last option to user
    elif search_type == "5":
        print(f"\nYou have chosen to EXIT")
        ans = "N"