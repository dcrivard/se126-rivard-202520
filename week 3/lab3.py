#---imports----------------------------------------------------------
import csv

#---functions------------------------------------------------------


#---Main executing code-------------------------------------------


#lists
id_numbers = []
ages = []
registered = []
votes = []
total_count =[]
total_regis = []
total_votes = []
num_records = 0
not_old = 0

with open("week 3/voters_202040.csv") as file:
    reader = csv.reader(file)
    next(reader) 
    
    for row in reader:
        id_numbers.append(row[0])  
        ages.append(int(row[1]))
        registered.append(row[2])  
        votes.append(row[3])    

        num_records += 1 
    
        if ages <= 18:
            not_old += 1

        elif registered == "N":
            total_count + 1

        elif votes == "N":
            total_regis += 1 

        else:
            total_votes += 1 

            




print(f"\nNumber of individuals not eligible to register: {registered}")
print(f"\nNumber of individuals who are old enough to vote but have not registered: {not_old}")
print(f"\nNumber of individuals who are eligible to vote but did not vote:{total_count}")
print(f"\nNumber of individuals who did vote{total_regis}")
print(f"\nNumber of records processed{num_records}")
