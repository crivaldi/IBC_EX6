# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:09:30 2018

Patricia Portmann
Exercise06 - Part 1
Python code that replicates head functionality

@author: Patricia
"""  
# defines a function head
def headPython (str, n) :
    with open (str) as filename: # opens passed in string as filename
        lines = [next(filename) for x in xrange(n)]
    print(lines)

headPython("iris.csv", 5)
#calls the function, passes the string "iris.csv" and the number 5
