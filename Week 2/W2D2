#DereK Rivard
#W2D2 - Text file handling




#variable Dictionary:



#----Imports-----------------------------------------
import csv
#--Functions------------------------------------------
def difference(people, max_cap):
    diff = max_cap - people
    return diff



#---MAIN EXECUTING CODE----------------------------

#initial counting vars
total_rec = 0
rooms_over = 0

#-----------Connected to the file---------------------------------
print(f"\n\n{'NAME':20}     {'MAX':5}   {'PPL':5}   {'OVER':5}")
print("--------------------------------------------------------")
with open("Week 2\classLab2.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #occurs during every row in the file (text file -> 2D list!)

        #assign each field data value to a friendly var field
        name = rec[0]
        max = int(rec[1])   #all text data is read as a string, cast as a num!
        ppl = int(rec[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display rooms that are over capacity
        if remaining < 0 :
            rooms_over += 1
            print(f"{name:20}   {max:5}   {ppl:5}   {abs(remaining):5}")

            #count ALL rooms!
            total_rec += 1

#-----------Disconnected to the file------------------------------
#display final data
print(f"\nRooms currently OVER capacity: {rooms_over}")
print(f"\nTotal rooms in the file: {total_rec}")