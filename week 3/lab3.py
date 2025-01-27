#---imports----------------------------------------------------------
import csv

#---functions------------------------------------------------------


#---Main executing code-------------------------------------------


#lists
id_numbers = []
ages = []
registered = []
votes = []

with open("week 3\class_grades.csv") as file:
    reader = csv.reader(file)
    next(reader) 
    
    for row in reader:
        id_numbers.append(row[0])  
        ages.append(row[1]) 
        registered.append(row[2])  
        votes.append(row[3])       



