import pandas as pd
iris = pd.read_csv("/Users/Rachel R/Desktop/data-shell/IBC_EX6/iris.csv")
n = 5
head = iris[0:n]
print(head)
