# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:41:35 2019

@author: PKoora
"""

myvar = input("Enter a String:")
lenstr = len(myvar)
if lenstr < 5 :
    print("String is too short:", myvar)
elif lenstr > 30:
    print("String is too long:", myvar)
else:
    print("my string:", myvar)