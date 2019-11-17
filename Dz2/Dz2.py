import random as rn
import time as tm
import prettytable
import matplotlib.pyplot as plt

table = prettytable.PrettyTable(['listSize', 'bubbleSort', 'selectSort', 'insertSort'])
x=[]
y1=[]
y2=[]
y3=[]
mass1=[]
mass2=[]
mass3=[]

def bubbleSort (mass):
    print mass
    print '--------'
    for i in range(len(mass)):
        for j in range(len(mass)-1-i):
            if mass[j] > mass[j+1]:
                a = mass[j]
                mass[j] = mass[j+1]
                mass[j+1] = a
    print mass
    print '--------'

def selectSort(mass):
    print mass
    print '--------'
    for i in range(len(mass) - 1):
        m = i
        j = i + 1
        while j < len(mass):
            if mass[j] < mass[m]:
                m = j
            j = j + 1
        mass[i], mass[m] = mass[m], mass[i]
    print mass
    print '--------'

def insertSort(mass):
    print mass
    print '--------'
    for i in range(1, len(mass)):
        item_to_insert = mass[i]
        j = i - 1
        while j >= 0 and mass[j] > item_to_insert:
            mass[j + 1] = mass[j]
            j -= 1
        mass[j + 1] = item_to_insert
    print mass
    print '--------'

for N in range(50,201,50):
    x.append(N)
    min=1
    max=N
    for i in range(N):
        mass1.append(int(round(rn.random() * (max - min) + min)))
    #for i in range(N):
    #    mass2.append(int(round(rn.random() * (max - min) + min)))
    #for i in range(N):
    #    mass3.append(int(round(rn.random() * (max - min) + min)))
    mass3=mass2=mass1
    t1 = tm.time()
    bubbleSort(mass1)
    t2 = tm.time()-t1
    y1.append('%.3f'%t2)

    t3 = tm.time()
    selectSort(mass2)
    t4 = tm.time()-t3
    y2.append('%.3f'%t4)

    t5 = tm.time()
    insertSort(mass3)
    t6 = tm.time()-t5
    y3.append('%.3f'%t6)

    table.add_row([str(N),str(t2), str(t4), str(t6)])

print table
plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.show()