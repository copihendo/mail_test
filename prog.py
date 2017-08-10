# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:54:42 2017

@author: Andrey1
"""

string = 0
Name = input('Input file name \n')
print(Name)
for line in open(Name, 'r'):
    string += 1
print(string)