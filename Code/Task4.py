import time
inp_file = open("Brightkite_edges.txt","r")

start = time.clock()


def takeint(elem):
    return int(elem)

friend = {}
data = inp_file.readlines()
temp = len(data)
i = 0
while i < temp:
	line = data[i].split()
	if(line[0] not in friend.keys()):
		friend[line[0]] = set()
	friend[line[0]].add(line[1])
	i=i+1

print("Choose an option : \n")
print("1. Show all the friends of a person\n")
print("2. Find mutual friends of 2 people\n")
print("3. Give friend suggestion for a person\n")
print("4. Print friend list of all users to a file\n")

option = input()
print("You have selected option: " +option +"\n")

if option == "1":
    p_id = input("Enter person id : \n")
    f_ids = friend[p_id]
    print("The person "+ p_id + " has " + str(len(f_ids))+ " friends.\n")
    print(sorted(f_ids, key=takeint))
elif option == "2":
    p1_id = input("Enter person1 id : \n")
    p2_id = input("Enter person2 id : \n")
    mutual = friend[p1_id].intersection(friend[p2_id])
    print("For person "+p1_id + " and "+ p2_id +", Number of mutual friends are : " + str(len(mutual))+"\n")
    print(sorted(mutual, key=takeint))
elif option == "3":
    suggest_friend = {}
    p_id = input("Enter person id : \n")
    thresh = input("No. of mutual friends must be greater than : \n")
    for key in friend.keys():
        if(key!= p_id):
            if(key not in friend[p_id]):
                count = len(friend[p_id].intersection(friend[key]))
                if(count !=0):
                    suggest_friend[key] = count
    print("UserID: No. of mutual Friends")
    for key, value in sorted(suggest_friend.items(), key=lambda item: item[1],reverse=True):
        if value <= int(thresh):
            break
        print("%s: %s" % (key, value))
elif option =="4":
    out_file = open("Users_friend.txt","w")
    for key, value in friend.items():
        out_file.write(key)
        for v in sorted(value, key=takeint):
            out_file.write(" "+v)
        out_file.write("\n")
    out_file.close()
    
print('Time of execution',time.clock() - start,'seconds')
