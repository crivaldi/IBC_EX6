# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:38:14 2018

Exercise06 Part 2: uses the data from iris.csv to do a couple different tasks

@author: Patricia
"""

import pandas
# pandas contains a DataFrame structure that can handle multiple data types
# numpy can only handle integers

data=pandas.read_csv("iris.csv") # data loaded into a data frame var "data" from iris.csv

# prints the last two rows in the last two columns
print("Part 1: Last two rows in the last two columns")
last2rows=data.tail(n=2)
last2rowcol=last2rows.iloc[:,3:]
print(last2rowcol)

# gets the number of observations for each species in the data
print("Part 2: species count")
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

# gets rows with sepal lengths > 3.5, only prints the row number
# in order to print the whole row use the commented out "print(data.iloc[x,:])"
print("Part 3: Rows in iris.csv with Sepal lengths greater than 3.5 ")
for x in range(totalrows):
    if data.iloc[x,1]>3.5:
        print'row: ',x
        # print(data.iloc[x,:])
        
# writes the data for the species "setosa" into a comma delimited file 
# named setosa.csv
setosa=pandas.DataFrame(columns=['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width','Species'])
for x in range(totalrows):
    if data.iloc[x,4]=="setosa":
        setosa.loc[x]=data.iloc[x,:]

setosa.to_csv('setosa.csv',header=True,index=False,sep=",")
print("Part 4: setosa.csv is made")
# header=True so that the headings for the olumns of the DataFrame are added to the .csv file
# uses the sorted data and saves it in a .csv file with comma as delimiter

# Calculate the mean, minimum, and maximum Petal.Length for virginica observations
print("Part 5:")
virginicaList=list() # declares a list of virginica Petal.Length
for x in range(totalrows):
    if data.iloc[x,4]=="virginica":
        virginicaList.append(data.iloc[x,2]) # adds Petal.Length to list

#virginicaSum=virginicaList.sum()
#virginicaLength=virginicaList.len()
virginicaMean=sum(virginicaList)/len(virginicaList)
virginicaMin=min(virginicaList)
virginicaMax=max(virginicaList)
print"The mean petal length for virginica species is:",virginicaMean
print"The minimum petal length for virginica species is:",virginicaMin
print"The maximum petal length for virginica species is:",virginicaMax