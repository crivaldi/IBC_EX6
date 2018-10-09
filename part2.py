# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:38:14 2018

Exercise06 Part 2: uses the data from iris.csv to do a couple different tasks

@author: Patricia
"""

import pandas
# pandas contains a DataFrame structure that can handle multiple data types
# numpy can only handle integers

data=pandas.read_csv("iris.csv") # data loaded into var "data" from iris.csv

# prints the last two rows in the last two columns
last2rows=data.tail(n=2)
last2rowcol=last2rows.iloc[:,4:]
print(last2rowcol)
  
# gets the number of observations for each species in the data
totalrows=data.shape[0]
# loop through rows
setosa_count=0
versicolor_count=0
virginica_count=0
for x in range(totalrows):
    if data.iloc[x,4]=="setosa":
        setosa_count += 1
    else: 
        if data.iloc[x,4]=="versicolor":
            versicolor_count += 1
        else: 
            if data.iloc[x,4]=="virginica":
                virginica_count += 1

print("setosa count is: ")
print(setosa_count)
print("versicolor count is: ")
print(versicolor_count)
print("virginica count is: ")
print(virginica_count)        

# gets rows with sepal lengths > 3.5
print("Rows with Sepal lengths greater than 3.5: ")
for x in range(totalrows):
    if data.iloc[x,1]>3.5:
        print("row number: ",x)
        print(data.iloc[x,:])
        

# writes the data for the species "setosa" into a comma delimited file 
# named setosa.csv
setosa=pandas.DataFrame(columns=['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width','Species'])
print(setosa)
for x in range(totalrows):
    if data.iloc[x,4]=="setosa":
        setosa.loc[x]=data.iloc[x,:]

setosa.to_csv('setosa.csv',header=False,index=False,sep=" ")
# uses the sorted data and saves it in a .csv file with space as delimiter
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
