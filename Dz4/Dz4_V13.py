#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Скопировать из файла F1 в файл F2 все строки, в которых более 2 слов. Определить номер слова,
# в котором больше всего гласных букв.
import os
import re
k=i=0
os.system(r'nul>F3.txt')

def fileCount(file):
    return len(open(file).readlines())

def countVowel(word,vowels='aeiouyAEIOUY'):
    return sum(1 for char in word if char in vowels)

print 'words with max count of vowels in row where count of words > 2:'
while i < fileCount('F2.txt'):
    line = open('F2.txt').read().split('\n')[i]
    result = re.findall(r'\w+', line)
    if len(result)-1>2:
        outFile = open('F3.txt','a')
        outFile.write(line+'\n')
        print(max(result, key=countVowel))
    i += 1
outFile.close()

