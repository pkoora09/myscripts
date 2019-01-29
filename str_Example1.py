# -*- coding: utf-8 -*-
"""
umber of digits and letters

@author: PKoora
"""

mylet = 0
mydig = 0
mystr = input("Enter String:")
for char in mystr:
    if char.isdigit():
        mydig = mydig + 1
    else:
        mylet = mylet + 1
print("Letters:", mylet)
print("Digits:", mydig)
