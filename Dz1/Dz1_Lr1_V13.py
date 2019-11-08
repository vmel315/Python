#! /usr/bin/env python
# -*- coding: utf-8 -*-
mass = [11,12,13,14]
suff = ' '
gribCount = str(input('Введите количество грибов\n'))
num = int(gribCount[-1])
if num in range(2,5,1) and int(gribCount) not in mass:
    suff = 'а '
elif num == 1 and int(gribCount) not in mass:
    pass
else:
    suff='ов '
print 'мы нашли ' +gribCount + ' гриб' + suff + 'в лесу'