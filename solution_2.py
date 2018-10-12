#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:09:43 2018

@author: mlpoterek
"""

from pandas import DataFrame, read_csv
import pandas as pd

location = r'/Users/mlpoterek/Biocomp/IBC_EX6/iris.csv'
df = pd.read_csv(location)

#Print the last 2 rows in the last 2 columns
last_rows = df.tail(2)
last_cols = last_rows[['Petal.Width', 'Species']]
print(last_cols)

#Number of observations of each species
spec_count = df['Species'].value_counts()
print(spec_count)

#Rows with Sepal.Width > 3.5
sepal_rows = df[df['Sepal.Width'] > 3.5]
print(sepal_rows)

#Write the data for the species setosa to a csv file 'setosa.csv'
setosa_rows = df[df['Species']=='setosa']
setosa_rows.to_csv("setosa.csv",sep = ',', index = False)

#Mean, min, and max of 'Petal.Length' for observations from virginica
virginica_rows = df[df['Species']=='virginica']
v_mean = virginica_rows['Petal.Length'].mean()
v_min = virginica_rows['Petal.Length'].min()
v_max = virginica_rows['Petal.Length'].max()
print(v_mean, v_min, v_max)