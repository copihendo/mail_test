# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:54:42 2017

@author: Andrey1
"""

lines = 0
FileName = input('Input file name \n')
print(FileName)
for line in open(FileName, 'r'):
    lines += 1
print(lines)