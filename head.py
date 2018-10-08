# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:09:30 2018

Patricia Portmann
Exercise06 - Part 1
Python code that replcated head functionality

@author: Patricia
"""
import numpy as np

filename = raw_input("What file are you using? ")
print(type(filename))

# an array variable assigned to the file's contents, genfromtxt allows for strings
data=np.genfromtxt(filename,dtype='str')
print(type(data))

# variable to set equal to the umber of lines we want to pull from the top
endline = input("How many lines do you want to print? ")
print(type(endline))
print(data[0:endline])
# saves the data inside inflammation-01.csv into variable data