#Derek Rivarrd
#lab 6
#2/24/2025

#program prompt - After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.

#imports----------------------------------------------------------------------------------------

#functions---------------------------------------------------------------------------------------

#main executing code-----------------------------------------------------------------------------
#start with 1d lists
seatA = ["A", "A", "A", "A", "A", "A", "A"]
seatB = ["B", "B", "B", "B", "B", "B", "B"]
seatC = ["C", "C", "C", "C", "C", "C", "C"]
seatD = ["D", "D", "D", "D", "D", "D", "D"]


#print seats
def display():
    for i in range(len(seatA)):
        print(f"{i+1}  {seatA[i]}  {seatB[i]}  {seatC[i]}  {seatD[i]}")

ans = "y"
while ans == "y":
    display()
    #get data from user
    Row = int(input("Enter row number[1-7]: "))
    seat = input("enter seat type[A/B/C/D]: ")

    if seat.upper() == "A":
        if seatA[Row - 1] != "X":
            seatA[Row - 1] = "X"

        else:
            print(f"Sorry, seat {Row}{seat} is taken")

    if seat.upper() == "B":
        if seatB[Row - 1] != "X":
            seatB[Row - 1] = "X"

        else:
            print(f"Sorry, seat {Row}{seat} is taken")

    if seat.upper() == "C":
        if seatC[Row - 1] != "X":
            seatC[Row - 1] = "X"

        else:
            print(f"Sorry, seat {Row}{seat} is taken")

    if seat.upper() == "D":
        if seatD[Row - 1] != "X":
            seatD[Row - 1] = "X"

        else:
            print(f"Sorry, seat {Row}{seat} is taken")

    display()

    #get new value for 'ans' --> ask user if they want to reserve another seat
    ans = input("Do you want that again? Y/N: ").lower()
    if ans == "N":
        print(f"Bye!")

