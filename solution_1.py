#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:05:39 2018

@author: mlpoterek
"""

def head (str, n) :
    with open (str) as my_file:
        first_lines = [next(my_file) for x in xrange(n)]        
    print(first_lines)

head("iris.csv", 2) #to call function with n=2
