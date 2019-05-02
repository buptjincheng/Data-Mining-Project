import re
import collections
from datetime import datetime
import time
import matplotlib.pyplot as plt

def takesec(elem):
    return elem[1]
    
file1 = open("Brightkite_totalCheckins.txt","r")
checkinStrings = file1.readlines()
checkIns = []
temp = len(checkinStrings)
i = 0
while i < temp:
    checkinsSplit = re.split(r'\t+', checkinStrings[i])
    try:
        checkinsSplit[4]=checkinsSplit[4][:-1]
        checkIns.append(checkinsSplit)
    except:
        i=i+1
        continue
    i=i+1

start = time.clock()

print("Choose an option : \n")
print("1. Patterns of check-ins on a specific day.\n")
print("2. Patterns of check-ins at a specific location.\n")
print("3. Patterns of check-ins at a specific location and on a specific day.\n")


option = input()
print("You have selected option: " +option +"\n")

result_checkIns = []
if option == "1":
    # for date
    date = input("Enter date : ") 
    i = 0
    while i<temp:
        try:
            checkindate_split = checkIns[i][1].split('T')[0]
            if checkindate_split == date:
                result_checkIns.append(checkIns[i])
        except:
            i=i+1
            continue
        i = i+1
    counter=collections.Counter([row[4] for row in result_checkIns])

elif option == "2":
    location = input("Enter location id : ")
    i = 0
    while i < temp:
        try:
            if checkIns[i][4]==location:
                result_checkIns.append(checkIns[i])
        except:
            i=i+1
            continue
        i=i+1
    counter=collections.Counter([row[1].split('T')[0] for row in result_checkIns])
    
elif option == "3":
    date = input("Enter date : ")
    location = input("Enter location id : ")
    i = 0
    while i<temp:
        try:
            checkindate_split = checkIns[i][1].split('T')[0]
            if checkindate_split == date and checkIns[i][4]==location:
                result_checkIns.append(checkIns[i])
        except:
            i=i+1
            continue
        i = i+1
    for chec in result_checkIns:
        print(chec)

print('Time of execution',time.clock() - start,'seconds')

if option == "1" or option =="2":
    threshold = input("Enter threshold value : ")
    opt = 0
    if option=="2":
        print("\n")
        print("1. Show result count wise.")
        print("2. Show result in a timeline.")
        opt = input()
        print("You have selected option: " +opt +"\n")
    values = list(counter.values())
    keys = list(counter.keys())
    i = 0
    count = len(values)
    finalCheckInCount = []
    while i<count:
        if(values[i]>=int(threshold)):
            finalCheckInCount.append([keys[i],values[i]])
        i = i+1
    print("Location/Date: Count")
    if opt=="2":
         for chec in sorted(finalCheckInCount):
            print(chec[0]+": "+str(chec[1]))
         plt.xlabel("Timeline")
         plt.ylabel("Number of Check-Ins")   
         plt.plot([pt[0] for pt in finalCheckInCount],[pt[1] for pt in finalCheckInCount])
         plt.show()   
    else:
        for chec in sorted(finalCheckInCount, key=takesec, reverse =True):
            print(chec[0]+": "+str(chec[1]))
        plt.xlabel("LocationIDs")
        plt.ylabel("Number of Check-Ins")   
        plt.plot([pt[0][:5] for pt in finalCheckInCount],[pt[1] for pt in finalCheckInCount])
        plt.show()
