# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:06:44 2019

@author: PKoora
"""
myString = input("Enter Some String:")
print("UPPERCASE:",myString.upper())
print("Number of occurance of p:", myString.count("p"))
print("Replace python:", myString.replace("Python","Ruby"))
temp = myString.split(" ")
print("Number of words:",len(temp))
temp1 = list(myString)
print("Number of Characters:", len(temp1))

print("Remove Spaces:", myString.replace(" ",""))
