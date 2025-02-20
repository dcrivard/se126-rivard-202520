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