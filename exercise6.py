# Answer to number 1
iris = pandas.read_csv('iris.csv')
x=3
iris.head(3)



# Answers to number 2
pwd
cd IBC_EX6

iris = pandas.read_csv('iris.csv')
print (iris)
iris.iloc[148:150,3:5]

iris ['Species'].value_counts()

iris[iris['Sepal.Width']>3.5]

pwd
cd ../
mv setosa.csv /Users/Cosmoscommander/IBC_EX6
cd CosmosCommander/IBC_EX6

setosa = pandas.read_csv('setosa.csv')

row=iris [iris.Species.str.contains('setosa')]
row
row.to_csv('setosa.csv')


virginica = iris [iris.Species.str.contains('virginica')]
virginica['Petal.Length'].mean()
virginica['Petal.Length'].min()
virginica['Petal.Length'].max()

