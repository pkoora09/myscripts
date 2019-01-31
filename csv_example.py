# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:14:50 2019

@author: PKoora

import csv
mycity = set()
with open("C:/Personal/Python/realestate.csv", "r")  as myobj:
    mycsv = csv.reader(myobj)
    for var in mycsv:
        mycity.add(var[1])
print(mycity)

"""


