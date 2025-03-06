#derek Rivard
#3/6/2025
#Makup lab 

#program prompt - Allow the user to accept a class name, and if the course exists: display all the students enrolled in this course (just student ID, first name, and last name). Use a new list (found_class) to store which students are enrolled in the course and use this list to display the student information back to the user. If the class does not exist, tell the user this and allow them to revisit the menu to try again. 

#import 
import csv

#empty lists
id = []
lastname = []
firstname = []
class1 = []
class2 = []
class3 = []

found_class = []
#append lists 
with open("Week 9\students.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        id.append(rec[0])
        lastname.append(rec[1])
        firstname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

for i in range(0, len(id)):
    print(f"{id[i]:5}  {lastname[i]:25}  {firstname[i]:15}  {class1[i]:20}  {class2[i]:5}  {class3[i]:25}")
print("--------------------------------------------------------------------------------")
#functions
ans = 'y'

while ans == "y":
    print("\tSEARCHING MENU")
    print("1. see all student reports") #shows all the students reports
    print("2. Search by student id") #searches by students id number
    print("3. Search by students last name") #searches by student last name 
    print("4. view a class roster [class1, class2, and class3]")#allows to look up class roster
    print("5. EXIT")

    search_type = input("\nHow would you like to search today? [1-5]: ")
        #option 5 - error
    if search_type == 5:
        print("\n\nThank you for using my program, GOODBYE!\n\n\n")
    #if the search type is wrong
        if search_type not in ["1", "2", "3", "4", "5"]:
         print("***INVALID ENTRY!***\nPlease try again")
    
    #option 1 - searching for student records
    if search_type == "1": 
        for i in range(0, len(id)):
            print(f"{id[i]:5}  {lastname[i]:25}  {firstname[i]:15}  {class1[i]:20}  {class2[i]:5}  {class3[i]:25}")
        print("--------------------------------------------------------------------------------")

    #option 2 - searching for student ids 
    elif search_type == "2":
        print('search by id')

        search = input("Enter the id you are looking for: ")

        min = 0
        max = len(id) - 1
        mid = int((min + max) / 2)
   

        print(min, max , mid, id[mid])

        #while min < max and search.lower() != id[mid].lower():
        while min < max and search.lower() != lastname[mid].lower():
            if search.lower() < id[mid].lower():
                max = mid - 1
            else:
                min = mid + 1

            mid = int((min + max) / 2)

        if search.lower() == id[mid].lower():
            print(f"we found your search for {search}, details below: ")
            print(f"{'id':12}  {'firstname':3}  {'lastname'}")
            print(f"------------------------------------------------------")
            print(f"{id[mid]:12}  {firstname[mid]:3}  {lastname[mid]}")
            print(f"---------------------------------------------------------")
        else:
            print(f"\nYour search for {search} is complete, no matches found ")
    #option 3 - searching for lastname
    elif search_type == "3":
        print('search by Last name')

        search = input("Enter the last name you are looking for: ")

        min = 0
        max = len(lastname) - 1
        mid = int((min + max) / 2)
   

        print(min, max , mid, lastname[mid])

        #while min < max and search.lower() != lastname[mid].lower():
        while min < max and search.lower() != lastname[mid].lower():
            if search.lower() < lastname[mid].lower():
                max = mid - 1
            else:
                min = mid + 1

            mid = int((min + max) / 2)

        if search.lower() == lastname[mid].lower():
            print(f"we found your search for {search}, details below: ")
            print(f"{'id':12}  {'firstname':3}  {'lastname'}")
            print(f"------------------------------------------------------")
            print(f"{id[mid]:12}  {firstname[mid]:3}  {lastname[mid]}")
            print(f"---------------------------------------------------------")
        else:
            print(f"\nYour search for {search} is complete, no matches found ")

    #option 4 - class roster
    elif search_type == "4":
        print('search by class id')
        found_class = []
        search_let = input("Enter the class you wish to find: ") #genre we are looking through all classes for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(class1)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_let == class1[i] or search_let == class2[i] or search_let == class3[i]: 
                #if performs the SEARCH - is what we're looking for here in the list?
                found_class.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
                print(f"Found a {search_let} status in INDEX {i}")
            '''
            if search_let == class1: 
                found = i
                #if performs the SEARCH - is what we're looking for here in the list?
                found_class.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
            print(f"Found a {search_let} status in INDEX {i}")
            
            if class3[i] == found_class: 
                #if performs the SEARCH - is what we're looking for here in the list?
                found_class.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
            print(f"Found a {search_let} status in INDEX {i}")
            i + 1

            '''
        if not found_class:
            print(f"Sorry, your search for the class {search_let} could not be found.")
        else:
        #class FOUND!
            print(f"Your search for {search_let} was FOUND! Here is their data: ")

                #'found' is a list populated with index locations - we loop through this list, and use found[i] (which again, holds an INDEX from our other searched-through list) to be recalled and used below
            for i in range(0, len(found_class)):
                print(f"{id[found_class[i]]:5}  {lastname[found_class[i]]:25}  {firstname[found_class[i]]:15}")


    #option 5 - end statement
    if search_type == "5":
        print("\n\nThank you for using my program, GOODBYE!\n\n\n")
        ans = "n"