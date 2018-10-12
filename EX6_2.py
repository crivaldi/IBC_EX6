import pandas as pd
#read iris.csv into python
Iris = pd.read_csv('iris.csv')
#read the last two columns and rows
Iris.loc[148:149, 'Petal.Width':'Species']
#return counts for each unique species
unique = Iris.Species.value_counts()
#return all sepal widths greater than 3.5
Iris[Iris['Sepal.Width']>3.5]
#put setova into a new csv file
setosa = Iris[Iris.Species == 'setosa']
setosa.to_csv('setosa.csv')
#return the minimum, maximum, and mean petal length of virginica
virginica = Iris[Iris.Species == 'virginia']
Iris['Petal.Length'].min()
Iris['Petal.Length'].max()
Iris['Petal.Length'].mean()
