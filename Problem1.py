# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 03:50:27 2018

@author: vysan
"""

import pandas as pd
def lines(filename,number):
    files=pd.read_csv(filename,header=0,sep=",")
    linenumbers=number-1
    return files.head(linenumbers)
print(lines('filename',number))
