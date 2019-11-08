import random as rn
initList=[]
finalList=[]
elCount=0
print'List size'
listSize = input()

for elCount in range(listSize):
    initList.append(rn.randint(0,99))
    elCount+=1

elCount=element=summ=0
print initList

while elCount<len(initList):
    while element < elCount:
        summ+=initList[element]
        element+=1
    finalList.append(summ)
    elCount+=1
    summ=element=0

print finalList