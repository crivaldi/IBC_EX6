#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:12:00 2018

@author: saurylara
"""
#Import and get the first five rows from the wages file
wages = pandas.read_csv("/Users/saurylara/Desktop/wages.csv")
numlines = 5
headwages = wages[0:numlines]
print(headwages)

#Import the iris file
iris = pandas.read_csv("/Users/saurylara/IBC_EX6/iris.csv")

#Print the last 2 rows in the last two columns of the data in the iris file
tailiris = iris.iloc[148:150, 3:5]
print(tailiris)

#Get number of observations for each species in the dataset (setosa,virginica,veronica)
numSetosa = iris[iris['Species']=='setosa'].count()['Species']
print 'There are', numSetosa, 'setosa'

numvirginica = iris[iris['Species']=='virginica'].count()['Species']
print 'There are', numSetosa, 'virginica'

numveronica = iris[iris['Species']=='veronica'].count()['Species']
print 'There are', numSetosa, 'veronica'

#Get number of rows from Sepal Width that are greater than 3.5
numSepalWidth = iris[iris['Sepal.Width'] > 3.5].count()['Sepal.Width']
print 'There are', numSepalWidth, 'greater than 3.5'

#Print(datasetosa) and redirect this data to a comma-delimited file named 'setosa.csv'
dataSetosa = iris[iris['Species']=='setosa']
dataSetosa.to_csv('setosa.csv')

#Calculate the mean, maximum, and minimum of Petal Length observations for virginica
dataVirginica = iris[iris['Species']=='virginica']['Petal.Length']
maxval, minval, meanval = dataVirginica.max(), dataVirginica.min(), dataVirginica.mean()
print('Maximum value:', maxval,'Minimum Value', minval,'Mean', meanval)
