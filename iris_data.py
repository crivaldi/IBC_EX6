# This script is aimed to do some simple analysis for iris dataset

import pandas as pd
data = pd.read_csv("iris.csv", delimiter = ",")


# Q1
print data.iloc[0:2,:]
print data.iloc[:,-2:]

# Q2
print pd.value_counts(data.Species)

# Q3
print data.loc[data['Sepal.Width'] > 3.5]

# Q4
setosa = data.loc[data['Species']=='setosa']
setosa.to_csv("setosa.csv")

# Q5
virginica = data.loc[data['Species']=='virginica']
vmin = virginica['Petal.Length'].min()
vmax = virginica['Petal.Length'].max()
vmean = virginica['Petal.Length'].mean()
print "Minimum, maximum and mean: "
print vmin,vmax,vmean
