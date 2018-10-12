# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 23:16:15 2018

@author: Alexis
"""

import pandas as pd
#Problem 1 
#Function creation for head
def head_function(file_desired,number_of_lines):

    with open(file_desired) as filename:
        CSV_data=pd.read_csv(filename)
        print(CSV_data[0:number_of_lines])
        return 0
#Calls the function created
head_function('iris.csv',5) #Uses input file iris.csv and the number of lines 5
#Next problem

iris_data=pd.read_csv("iris.csv") #Reads the iris.csv file and puts in dataframe

#Part 1 of Problem 2
iris_size=iris_data.shape #tells the rows of columns in the dataframe
DesiredRows=iris_size[0]-2 #want the last 2 rows
DesiredColumns=iris_size[1]-2#want the last 2 columns
Last2x2=iris_data.iloc[DesiredRows:,DesiredColumns:]#gives the last 2 rows and columns
print(Last2x2)

#Part 2 of Problem 2
ListOfSpecies=iris_data.Species.unique()#tells the unique species
SetosaRows=iris_data[iris_data.Species==ListOfSpecies[0]]#makes a df of Setosa
VersicolorRows=iris_data[iris_data.Species==ListOfSpecies[1]]#makes a df of versicolor
VirginicaRows=iris_data[iris_data.Species==ListOfSpecies[2]]#makes a df of versicolor
SetosaOccur=SetosaRows.shape[0] #gives number of occurances for each df
VersicolorOccur=VersicolorRows.shape[0]
VirginicaOccur=VirginicaRows.shape[0]
print "The number of occurances for",ListOfSpecies[0],"is" ,SetosaOccur
print "The number of occurances for",ListOfSpecies[1],"is" ,VersicolorOccur
print "The number of occurances for",ListOfSpecies[2],"is" ,VirginicaOccur

#Part 3 of Problem 2
SepalWidthGreater3_5=iris_data[iris_data['Sepal.Width']>3.5]#filter df for greater than 3.5
print "The number of rows with sepal width greater than 3.5 is" ,SepalWidthGreater3_5.shape[0]

#Part 4 of Problem 2
SetosaRows.to_csv('setosa.csv', sep=',',index=False)#Makes df to a csv file

#Part 5 of Problem 2
MeanVir=VirginicaRows['Petal.Length'].mean()
print "The petal length mean is" ,MeanVir
MaxVir=VirginicaRows['Petal.Length'].max()
print "The petal length maximum is" ,MaxVir
MinVir=VirginicaRows['Petal.Length'].min()
print "The petal length minimum is" ,MinVir