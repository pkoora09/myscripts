# -*- coding: utf-8 -*-
"""
calculate upper and lower

@author: PKoora
"""
myup = 0
mylo = 0
mystr = input("Enter String:")
for char in mystr:
    if char.isupper():
        myup = myup + 1
    else:
        mylo = mylo + 1
print("Upper:", myup)
print("Lower:", mylo)
        