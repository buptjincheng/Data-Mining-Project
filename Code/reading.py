import re
import collections
def fileReading():
	file1 = open("Brightkite_totalCheckins.txt","r")
	checkinStrings = file1.readlines()
	checkIns = []
	temp = len(checkinStrings)
	i = 0
	while i < temp:
		checkinsSplit = re.split(r'\t+', checkinStrings[i])
		checkinsSplit[-1] = checkinsSplit[-1].strip()
		checkIns.append(checkinsSplit)
		i=i+1
	return checkIns

def fileReadingAsLocations():
	file1 = open("Brightkite_totalCheckins.txt","r")
	checkinStrings = file1.readlines()
	checkInsLocations = {}
	temp = len(checkinStrings)
	i = 0
	while i < temp:
		checkinsSplit = re.split(r'\t+', checkinStrings[i])
		try:
			if checkinsSplit[0] not in checkInsLocations:
				checkInsLocations[checkinsSplit[0]] = []
			checkInsLocations[checkinsSplit[0]].append((float(checkinsSplit[2]), float(checkinsSplit[3])))
		except:
			i=i+1
			continue
		i=i+1
	return checkInsLocations


def singleUserData(userID, checkIns):
	coordinate_list = list(set(checkIns[userID]))
	return coordinate_list


def multiUserdata(userID, checkIns):
	file1 = open("Brightkite_edges.txt", "r")
	friend={}
	line  = file1.readline()
	while(line):
		data = line.split()
		friend[data[0]] =set()
		for i in range(1,len(data)):
			friend[data[0]].add(data[i])
		line=file1.readline()
	friends = friend[userID]
	coordinate_list = list(set(checkIns[userID]))
	for person in friends:
		if person in checkIns.keys():
			checkPoint = list(set(checkIns[person]))
			coordinate_list = coordinate_list + checkPoint
	return list(set(coordinate_list))
  