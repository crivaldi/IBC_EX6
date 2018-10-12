#reads the first line of a file called DNA.txt
import pandas as pn
lines = 1
data = pn.read_csv('DNA.txt', header = 0)
data.head(1)
