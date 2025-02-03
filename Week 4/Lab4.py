#Derek Rivard
#2/3/2025
#Lab 4

#promgram prompt - Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension.

#----Imports-----------------------------------
import csv
#-----functions-----------------------------------

#----main executing code-----------------------------

#lists
first = []
last = []
age = []
sname = []
House = []


#for each employee list
email = []
department = []
ext = []

#counts for departments
Dnum = 0        #total people
rd_count = 0       
market_count = 0
HR_count = 0
account_count = 0
sales_count = 0 
audit_count = 0 


with open("Week 4/got_emails.csv") as file:
    reader = csv.reader(file)


    #appending
    for row in reader:
        first.append(row[0])
        last.append(row[1])
        age.append(row[2])
        sname.append(row[3])
        House.append(row[4])

        print(row)

        #email names
        email.append(row[3] + "@westeros.net")


        if row[4] == "House Stark":
            department.append("Research & Development")
            ext.append(int(100 + Dnum))
            rd_count += 1

        if row[4] == "House Targaryen":
            department.append("Marketing")
            ext.append(int(200 + Dnum))
            market_count += 1

        if row[4] == "House Tully":
            department.append("Human Resources")
            ext.append(int(300 + Dnum))
            HR_count += 1

        if row[4] == "House Lannister":
            department.append("Accounting")
            ext.append(int(400 + Dnum))
            account_count += 1

        if row[4] == "House Baratheon":
            department.append("Sales")
            ext.append(int(500 + Dnum))
            sales_count += 1

        if row[4] == "The Night's Watch": 
            department.append("Auditing")
            ext.append(int(600 + Dnum))
            audit_count += 1

        Dnum += 1 

#print statements
print(f"research and development counter. {rd_count}")
print(f"Marketing counter. {market_count}")
print(f"Human Resources department counter. {HR_count}")
print(f"accounting counter. {account_count}")
print(f"total sales counter. {sales_count}")
print(f"auditing counter. {audit_count}")


print(f"{'first':8} {'last':10} {'email':30} {'department':23} {'ext':3}")

#for loop for printing and indexing names 
for i in range(0, len(first)):
    print(f"{first[i]:8} {last[i]:10} {email[i]:30} {department[i]:23} {ext[i]:3}")
print("-------------------------------------------------------------------")

#new data file 
file = open('Week 4/westeros.csv', 'w') #file path

for i in range(0, len(first)):
    file.write(f"{first[i]},{last[i]},{email[i]},{department[i]},{ext[i]}\n")

file.close() #create file