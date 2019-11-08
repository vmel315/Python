#! /usr/bin/env python
# -*- coding: utf-8 -*-
mass = [11,12,13,14]
gribCount = str(input('Введите количество грибов\n'))
num = int(gribCount[-1])
if num in range(2,5,1) and int(gribCount) not in mass:
    print'мы нашли '+gribCount+' гриба в лесу'
elif num == 1 and int(gribCount) not in mass:
    print'мы нашли ' + gribCount + ' гриб в лесу'
else:
    print'мы нашли ' + gribCount + ' грибов в лесу'
input()