#Derek Rivard
#final lab
#3/3/2025

#program prompt - We here today are creating a program where we can search up golfers using sequencial search standerds to allow the user to identify a players, scores, the distance they can hit a golf ball, what percentage they ccan hit a fairway off the tee, the percentage in which they can hit a green in regulation, and lastly they can find the player off of his last name

#csv
import csv

#empty lists-----------------------------------------------
scoring = []
distance = []
fir = []
gir = []
lname = []

#appending lists
with open("final/golf.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        scoring.append(rec[0])
        distance.append(rec[1])
        fir.append(rec[2])
        gir.append(rec[3])
        lname.append(rec[4])

for i in range(0, len(scoring)):
    print(f"{scoring[i]:5}  {distance[i]:25}  {fir[i]:15}  {gir[i]:20}  {lname[i]:5}")
print("--------------------------------------------------------------------------------")
#functions

#main executing code---------------------------------------
