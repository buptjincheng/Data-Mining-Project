import matplotlib.pyplot as plt
import random as rand
from random import shuffle
import math
from math import sin, cos, sqrt, atan2, radians
from reading import *
import time

def EuclidDistance(x,y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

Colors = []
for i in range(100):
    Colors.append((rand.uniform(0, 1), rand.uniform(0, 1), rand.uniform(0, 1)))

print("Choose an option : \n")
print("1. Predict Clusters for single user\n")
print("2. Predict Clusters based on user's friend circle\n")

option = input()
print("You have selected option: " +option +"\n")


if option=="1":
    userID = input("Enter UserID:")
    checkIns = singleUserData(userID, fileReadingAsLocations())
elif option=="2":
    userID = input("Enter UserID:")
    checkIns = multiUserdata(userID, fileReadingAsLocations())
else: 
    print("Select from above options only.")
    exit()

print("reading data")
print("data read")

rand.seed(37)
shuffle(checkIns)

start = time.clock()

numCluster = 8
numIterations = 100

#initialise clusters
print("initialising clusters")
centers = []
clusters = []
for i in range(numCluster):
    clusters.append(set())
    
currentCluster = dict()
for i in range(len(checkIns)):
    if i < numCluster:
        x = i
    else:
        x = rand.randint(0,numCluster-1)
    currentCluster[i] = x
    clusters[x].add(i)
    

for i in range(numCluster):
    while 1:
        index = rand.randint(0,len(clusters[i])-1)
        if checkIns[index] not in centers:
            break
    centers.append(checkIns[index])


#update center
def updateCenter():
    centerChanged=0
    for i in range(len(clusters)):
        Cluster = clusters[i]
        x,y = 0,0
        for j in Cluster:
            x += checkIns[j][0]
            y += checkIns[j][1]
        if len(Cluster) > 0:
            x /= len(Cluster)
            y /= len(Cluster)
        else:
            x = math.inf
            y = math.inf
        
        if (x,y) != centers[i]:
            centers[i] = (x,y)
            centerChanged = 1
    return centerChanged

def kMeans():
    for itr in range(numIterations):
        print('Iteration',itr,'started')
        centerChanged = 0
        for i in range(len(checkIns)):
            cluster = currentCluster[i]
            distance = EuclidDistance(checkIns[i],centers[cluster])
            for j in range(len(centers)):
                d = EuclidDistance(checkIns[i],centers[j])
                if d < distance:
                    distance = d
                    cluster = j
            if currentCluster[i] != cluster:
                clusters[currentCluster[i]].remove(i)
                currentCluster[i] = cluster
                clusters[currentCluster[i]].add(i)
        
        centerChanged = updateCenter()
        
        if centerChanged == 0:
            break
    print('Number of iterations at convergence:',itr+1)

# function call and plot
kMeans()
X,Y = [],[]
for i in range(numCluster):
    X.append([])
    Y.append([])
for i in range(len(checkIns)):
    c = currentCluster[i]
    X[c].append(checkIns[i][0])
    Y[c].append(checkIns[i][1])
for i in range(numCluster):
    print(i,len(X[i]))
    plt.plot(X[i], Y[i], '+', label='C'+str(i+1), color=Colors[i])
plt.title('K-means')
plt.xlabel('Latitude --->')
plt.ylabel('Longitude --->')
plt.show()
print('Time of execution',time.clock() - start,'seconds')