#Exercise 06
#Alicia Susi
#Due 10/12/18
#Problem 1
import pandas

data=pandas.read_csv("wages.csv")
#Returning the top 5 lines from the file wages.csv
print("Question 1: ")
print(data.head(5))

#Problem 2
#Print last 2 rows in last 2 columns
data=pandas.read_csv("iris.csv")
row_num=data.shape[0]
col_num=data.shape[1]
print()
print("Question 2:Part 1")
print(data.iloc[row_num-2:row_num,col_num-2:col_num])

#Number of observations for each species
print()
print("Question 2:Part 2")
count=data.groupby(["Species"], sort=False).size()
print(count)

#Number of rows with Sepal.Width > 3.5
print()
print("Question 2:Part 3")
sorted_data=data.sort_values('Sepal.Width')
part3 = (sorted_data.loc[sorted_data['Sepal.Width'] > 3.5]).shape[0]
print(part3)

#setosa data moved to new csv file
print()
print("Question 2:Part 4")
part4 = (sorted_data.loc[sorted_data['Species'] == 'setosa'])
print(part4)
part4.to_csv("setosa.csv")

#Max, Min, and Mean of Petal.Length for virginica species
print()
print("Question 2:Part 5")
part5 = (sorted_data.loc[sorted_data['Species'] == 'virginica'])
print('Max is:')
print(part5['Petal.Length'].max())
print('Min is:')
print(part5['Petal.Length'].min())
print('Mean is:')
print(part5['Petal.Length'].mean())
