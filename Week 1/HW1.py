#Derek Rivard
#1/13/2025
#Lab1

#functions
def decision(response):
    while response != "y" and response != "n":
        print("***INVALID ENTRY***")
        response = input("\t\tDo you have another number to check: ").lower()

        return response

def difference(people, max_cap):

    diff = max_cap - people

    return diff

#main code 

ppl = 100 
max = 100

ans = "y"

while ans == "y" or ans == "Y":

    name = (input("\t\tEnter the name of your meeting: "))
    numb = float(input("\t\tEnter the number of those attending meeting: "))
    capi = float(input("\t\tWhat is the room capacity: ")) 

    remain = difference(numb, capi)


    if remain >= 0:
        print(f"THIS IS LEGAL, {remain} can be added")
    else:
        print(f"This is NOT legal")



allow = difference(ppl, max)
print(allow)



#final displays


print("\n\n\t\tThank you for using the program. Goodbye.\n\n")