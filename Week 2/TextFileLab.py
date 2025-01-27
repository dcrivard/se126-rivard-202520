#DereK Rivard
#W2D2 - Text file handling




#variable Dictionary:



#----Imports-----------------------------------------
import csv
#--Functions------------------------------------------
ty = []
brand = []
cpu = []
ram = []
fdisk = []
nohdd = []
twodisk = []
os = []
yr = []

#initialize a record counting variable



#connecting to the file
with open("Week 2/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)
    #Print for headers

    print(f"{'TYPE':10}   {'BRAND':10}   {'CPU':10}   {'RAM':10}   {'1st DISK':10}   {'NO HDD':10}   {'2ND DISK':10}   {'OS':10}   {'YR':10}")
    print("----------------------------------------------------------------------------------------------------------------------")

    

    for rec in file:

        if rec[0] == "D":
            ty.append("Desktop")

        else:
            ty.append("Laptop")

        if rec[1] == "DL":
            brand.append("Dell")

        elif rec[1] == "HP":
            brand.append("HP")

        elif rec[1] == "GW":
            brand.append("gateway")

        else:
            brand.append("ERROR")

        cpu.append(rec[2])
        ram.append(rec[3])
        fdisk.append(rec[4])
        nohdd.append(rec[5])

        
        if rec[5] == "1":
            twodisk.append("---")
            os.append(rec[6])
            yr.append(rec[7])

        else:
            twodisk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])





        #print(f"{ty:10}   {brand:10}   {cpu:10}   {ram:10}   {fdisk:10}   {nohdd:10}   {twodisk:10}   {os:10}   {yr:10}")


#disconnect from the file
print(f"{'TYPE':10}   {'BRAND':10}   {'CPU':10}   {'RAM':10}   {'1st DISK':10}   {'NO HDD':10}   {'2ND DISK':10}   {'OS':10}   {'YR':10}")
print("----------------------------------------------------------------------------------------------------------------------")
for i in range(0, len(ty)):
    print(f"{ty[i]:10}   {brand[i]:10}   {cpu[i]:10}   {ram[i]:10}   {fdisk[i]:10}   {nohdd[i]:10}   {twodisk[i]:10}   {os[i]:10}   {yr[i]:10}")
print("------------------------------------------------------------------------------------------------------------------")
old_desk = 0 
old_lap = 0

for i in range(0, len(yr)):

    if int(yr[i]) <= 16:
        print(f"old machine found on index {i}")
        if ty == "desktop":
            old_desk += 1

print(f"\nTOTAL 0. of desktops that need to be replaced: {old_desk}")
print(f"\nTOTAL RECORDS IN FILE: {len(ty)}\n\nThank you, Goodbye")