#---imports----------------------------------------------------------
import csv

#---functions------------------------------------------------------


#---Main executing code-------------------------------------------


#lists
id_numbers = []
ages = []
registered = []
votes = []

with open("week 3/voters_202040.csv") as file:
    reader = csv.reader(file)
    next(reader) 
    
    for row in reader:
        id_numbers.append(row[0])  
        ages.append(row[1]) 
        registered.append(row[2])  
        votes.append(row[3])    




print(f"\nNumber of individuals not eligible to register: {registered}")
print(f"\nNumber of individuals who are old enough to vote but have not registered.")
print(f"\nNumber of individuals who are eligible to vote but did not vote.")
print(f"\nNumber of individuals who did vote.")
print(f"\nNumber of records processed.")
