# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:37:13 2018

@author: Rachel R
"""

pwd
cd desktop
cd data-shell
ls
cd IBC_EX6

#Question 1 
import pandas as pd    
iris = pd.read_csv("/Users/Rachel R/Desktop/data-shell/IBC_EX6/iris.csv")
n = 5
head = iris[0:n]
print(head)

#Question 2
#Print the last 2 rows and last 2 columns of iris.csv to the python terminal
tail = iris.iloc[148:150, 3:5]
print(tail)

#Get the number of observations for each species included in the dataset
observations = iris["Species"].value_counts()
print(observations)

#Get rows with Sepal.Width > 3.5
Sepalwidth = iris.loc[iris['Sepal.Width'] > 3.5]
print(Sepalwidth)
    
#Write the data for the species setosa to a comma delimited file
setosa = iris[iris["Species"]=="setosa"]
setosa.to_csv("setosa.csv")
import pandas
pandas.read_csv("setosa.csv")

#Calculate mean, min, max, of Petal.Length for observations from virginica
import numpy
Virginica = iris[iris['Species']=='virginica']['Petal.Length']
maxval, minval, meanval = numpy.max(Virginica), numpy.min(Virginica), numpy.mean(Virginica)

print('maximum value', maxval)
print('minimum value', minval)
print('mean value', meanval)   
