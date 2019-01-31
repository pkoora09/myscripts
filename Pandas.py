# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 12:37:05 2019

@author: PKoora
"""

import pandas
import os
mydataframe=pandas.read_csv("C:/Users/pkoora.DIR/Desktop/datasets-master/nba.csv")
print(mydataframe[["Name","Team"]])

"""
for list in mydataframe["Position"]:
    print(list)
    """