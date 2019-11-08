#! /usr/bin/env python
# -*- coding: utf-8 -*-
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
print'-------------------------'
print initList

print '1 or 2'
'''
1 - с учетом новых значений
2 - без учета новых значений
'''
opt=input()

#-----LR4
if opt==1:
    print'1 - с учетом новых значений'
    elCount=1
    while elCount<len(initList):
        while element < elCount:
            summ+=initList[element]
            element+=1
        initList.pop(elCount)
        initList.insert(elCount,summ)
        elCount+=1
        summ=element=0
    print initList
elif opt==2:
    print '2 - без учета новых значений'
    elCount=1
    summbuf=initList[0]
    while elCount<len(initList):
        summbuf+=initList[elCount]
        currentSumm = summbuf - initList[elCount]
        initList.pop(elCount)
        initList.insert(elCount,currentSumm)
        elCount+=1
    print initList
