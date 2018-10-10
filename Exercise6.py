#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:50:53 2018

@author: Alicia
"""
##########
#Problem1#
##########
#Using wages.csv as file referenced for Problem 1 of code
filename = "/Users/Alicia/Desktop/Fall/BIOS60318/Exercise6/wages.csv" #Filepath set as variable
file_object = open(filename,"r") #opening file

header = ""
for i in range(10):
    header+=file_object.readline() #forloop to read and print lines
    
file_object.close() #closing file
print header #Usage: print header


###########
#Problem 2#
###########
##Part 1##
filename2 = "/Users/Alicia/Desktop/Fall/BIOS60318/Exercise6/IBC_EX6/iris.csv" #filepath to read iris.csv file
import pandas as pd
data = pd.read_csv('iris.csv',header=0,sep=",")

data2 = data.iloc[-2:,-2:]
print data2 #Usage: print data2


##Part 2##
counterSet=0
counterVers=0
counterVirg=0
for value in data.iloc[:,4]:
    if value == "setosa":
        counterSet +=1
    if value == "versicolor":
        counterVers +=1
    if value == "virginica":
        counterVirg +=1

print counterSet #Usage: print counterSet
print counterVers #Usage: print counterVers
print counterVirg #Usage: print counterVirg
      

##Part 3##
data3 = data[data["Sepal.Width"] > 3.5] #Printing data in column Sepal.Width with values >3.5

print data3 #Usage: print data3


##Part 4##
data4 = data.loc[data['Species'] == "setosa"] #Finding rows with setosa under column species
data4b = data4.to_csv('setosa.csv') #exporting above rows to new .csv file 
#Usage: Above exports into 'setosa.csv' no need to run "print data4b"


##Part 5##
data5 = data.loc[data['Species'] == "virginica"]
data5a = data5.iloc[:,3]
data5avg = data5a.mean()
print data5avg #Usage: print data5avg
data5min = data5a.min()
print data5min #Usage: print data5min
data5max = data5a.max()
print data5max #Usage: print data5max
