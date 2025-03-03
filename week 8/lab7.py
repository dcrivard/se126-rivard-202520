#Derek Rivard
#Lab 7
#3/3/2025

#program prompt - Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary based on the following menu

#import-----------------------------------------------------------------
import csv

#main executing code-----------------------------------------------------
#library
words = {
    "python" : "a popular programming language created by Guido van Rossum",
    "documentation" : "programming comments; notes within code which explain what the code does"
}

definitions = []


with open("week 8/words.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #add each record's data as a new key + value pair from the text file
        #key --> rec[0]  ; value --> rec[1]
        words.update({rec[0] : rec[1]})
        #when using .update() --> pass {'key' : value}

        definitions.append(rec[0])

#disconnect from file 
print(f"\n{'WORD':6}\t{'DEF'}")
print("-" * 50)
for key in words:
    #for every key (and value) pair found within the 'words' definition 
    print(f"{key:6}\t{words[key]}")
print("-" * 50)

ans = "y"
while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Search by Word") #searches by word
    print("2. Or add a Word") #Adding word to library 
    print("3. EXIT")
    search_type = input("\nWhat do you want? [1-3]: ")
    #SEQUENTIAL SEARCH FOR A WORD 
    if search_type == "1":
        search = input("\nEnter the WORD you are looking for: ")
        found = 0

        for key in words:
            if search.lower() == key.lower():
            #store the found title's location in the dictionary --> 
                found = key

        if found != 0:
            print(f"\nKEY:{found:6}\tTITLE:{words[found]}")
        else:
            print(f"\nYour search for {search} came up empty :[")


#type() returns the class type of the data passed to it
    if type(words) is list:
        print("'Words' is a LIST")    

#add word to list
    if search_type == "2":
        new_word = input("\n\nWhat word would you like to add?: ")
        new_def = input("\n\nWhat defintion would you like to add to this word?: ")
        #words.update({rec[0] : rec[1]})
        words.update({new_word : new_def})
        print(f"\n{'WORD':6}\t{'DEF'}")
        print("-" * 50)
        for key in words:
        #for every key (and value) pair found within the 'words' definition 
            print(f"{key:6}\t{words[key]}")
        print("-" * 50)

#Search type BYE
    if search_type == "3":
        print("\n\nThank you for using my program, GOODBYE!\n\n\n")
        ans = "n"