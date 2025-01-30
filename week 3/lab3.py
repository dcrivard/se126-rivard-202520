#Derek Rivard
#lab3

#program prompt - Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.


#---imports----------------------------------------------------------
import csv

#---functions------------------------------------------------------


#---Main executing code-------------------------------------------


#lists
id_numbers = []
ages = []
registered = []
votes = []


#what am i doing here: expanding on lists to clarfiy the language to help me

not_old = 0         #output #1
not_regis = 0       #output #2
total_regis = 0     #output #3
total_votes = 0     #output #4
num_records = 0     #output #5

#what am i doing here: connecting csv file forcing this tp read it
with open("week 3/voters_202040.csv") as file:
    reader = csv.reader(file)

    
    for row in reader:
        #what am i doing here: appending top rows and including num_records on the bottom
        id_numbers.append(row[0])  
        ages.append(int(row[1]))
        registered.append(row[2])  
        votes.append(row[3])    

        num_records += 1 



     

print(f"{'id_numbers':10}   {'ages':10}   {'registered':10}    {'votes':10}")
print("-------------------------------------------------------------------------")

#what am i doing here: neatly keeping all my if statements in a for loop and listing them to add them in num_records
for i in range(0, num_records):

    #what am i doing here: seperating the if statements so that the computer can tell them apart
    if ages[i] < 18:
        not_old += 1 

    if ages[i] >= 18 and registered[i] == "N":
        not_regis += 1

    if ages[i] >= 18 and registered[i] == "Y" and votes[i] == "N":
        total_regis += 1 

    if votes[i] == "Y":
        total_votes += 1


            
#what am i doing here: adding what goes in the rows and outlining what they are for so that the user and myself can understand
print(f"\nNumber of individuals not eligible to register: {not_old}")
print(f"\nNumber of individuals who are old enough to vote but have not registered: {not_regis}")
print(f"\nNumber of individuals who are eligible to vote but did not vote:{total_regis}")
print(f"\nNumber of individuals who did vote{total_votes}")
print(f"\nNumber of individuals in the file: {num_records}")