import numpy as np
import os
import random
import matplotlib.pyplot as plt
import datetime
from sklearn.preprocessing import PolynomialFeatures
from reading import *
import time

checkIns = fileReading()


start = time.clock()

def Regression(x,y,deg):
    coeff = np.polyfit(x, y, deg)
    print("coefficients: ", end="")
    print(coeff)

    ypred = [0]*len(x)
    for i in range(len(x)) :
        for j in range(deg+1) :
            ypred[i] =ypred[i] + coeff[j]*(float(x[i])**(deg-j))
    '''
    print("x_dates: ", end="")
    print (x)
    print("y_actual: ", end="")
    print (y)
    print("y_predicted: ", end="")
    print ([int(i) for i in ypred])
    '''
    print("x_date: y_actual: y_predicted")
    for i in range(len(x)) :
        print(str(x[i]) + ": " + str(y[i]) + ": " + str(int(ypred[i])))
    plt.scatter(x, y) 
    plt.plot(x, ypred) 
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.show() 
    
    return coeff

def predict(x, coeff, deg):
    ypred = 0
    for j in range(deg+1) :
        ypred =ypred + coeff[j]*(float(x)**(deg-j))
    print("x_date: ", end="")
    print (x)    
    print("y_predicted: ", end="")
    print(int(ypred))
    
def getDate(checkin):
    date = checkin[1]
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    year = date_time_obj.date().year
    month=str(int(float(date_time_obj.date().month)*99/12))
    if len(month)==1:
        month="0"+month
    return int(str(year) + str(month))

def inpDate(date):
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    year = date_time_obj.date().year
    month=str(int(float(date_time_obj.date().month)*99/12))
    if len(month)==1:
        month="0"+month
    return int(str(year) + str(month))
    
    
def locationCheckIns(locationId):
    checkinsLocation = []
    for checkIn in checkIns :
        try:
            if(checkIn[4] == locationId) :
                checkinsLocation.append(checkIn)
        except:
            continue 
    return checkinsLocation

def userCheckIns(userId):
    user_checkins = []
    for checkIn in checkIns :
        try:
            if(checkIn[0] == userId) :
                user_checkins.append(checkIn)
        except:
            continue 
    return user_checkins
    
def getDict(checkinsLocation):
    Dict = {}
    for checkin in checkinsLocation : 
        date=getDate(checkin)
        if date in Dict.keys() :
            Dict[date] = Dict[date] + 1
        else : 
            Dict[date] = 1
    return Dict

print("Choose an option : \n")
print("1. Predict future check-ins at a location.\n")
print("2. Predict future check-ins of a user.\n")

option = input()
print("You have selected option: " +option +"\n")

if option=="1":
    locationID = input("Please enter locationID: ")
    Dict = getDict(locationCheckIns(locationID))
elif option =="2":
    userID = input("Please enter userID: ")
    Dict = getDict(userCheckIns(userID))

print("\n")    
x = list(Dict.keys()) 
x.sort()
y = [0]*len(x)
i=0
while i<len(x):
    y[i]=Dict[x[i]]
    i = i+1
l=len(x)

coeff = Regression(x,y,2)

date = input("Enter a date to predict on: ")
xinp = inpDate(date)
predict(xinp, coeff, 2)


print('Time of execution',time.clock() - start,'seconds')
