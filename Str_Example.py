# -*- coding: utf-8 -*-
"""
Write a python program to accept a string from keyboard and reverse the string

@author: PKoora
"""

mystr = input("Enter String:")
mystr1=""
mylist = list(mystr)
mylist.reverse()
print("Before Reverse:", mystr)
for val in mylist:
    mystr1 = mystr1 + val
print(mystr1)
