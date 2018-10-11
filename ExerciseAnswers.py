#Loading iris.csv
import pandas as pd
iris=pd.read_csv('iris.csv')
print iris
#1 Imitate functionality of head
file=iris
x=3
file.head(x)
#or
def head(x,y):
    head=x.head(n=y)
    
    return head
head(iris,3)
#2.1 Print the last 2 rows in the last 2 columns to the Python terminal
iris.shape
iris.iloc[148:150,3:5]
#2.2 Get the number of observations for each species included in the data set
iris['Species'].value_counts()
#2.3 Rows with Sepal.Width>3.5
iris[iris['Sepal.Width']>3.5]
#2.4 Write the data for the species setosa to comma-delimited file names 'setosa.csv'
setosa=iris[iris.Species.str.contains('setosa')]
setosa
setosa.to_csv('setosa.csv')
Setosa=pd.read_csv('setosa.csv')
Setosa
#2.5 Calculate the mean, minimum, and maximum of Petal.Length for observations from virginica
virginica=iris[iris.Species.str.contains('virginica')]
virginica
virginica['Petal.Length'].mean()
virginica['Petal.Length'].min()
virginica['Petal.Length'].max()
