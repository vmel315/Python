import math
count=0
mass1 = []

a=8
m=6
b=5*10**3
k=[1.6,9.1,8]
for count in range(len(k)):
    d = math.sin(k[count]/a)/math.cos(m*b)
    c = (d+0j)/((d+0j)**d+1)/(1-math.e**k[count])
    #c = d/(d**d+1)/(1-math.e**k[count])
    print c

count=0
d=0
c=0
k=a*(-0.5)*3
while count<1:
    d = math.sin(k/a)/math.cos(m*b)
    c = (d+0j)/((d+0j)**d+1)/(1-math.e**k)
    count+=1
    print c

count=0
d=0
c=0
a=2*(0.2)*2.8
k=[1.7,5,-2]
#?двойной цикл?
