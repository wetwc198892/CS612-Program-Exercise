tempList = [0,1] #initialize a list
#for loop to generate 
for i in range(2,100):
    tempList.append(tempList[i-1]**0.5+tempList[i-2]**1.1)
print(tempList)#print the result list
