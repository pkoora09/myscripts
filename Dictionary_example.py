# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:25:42 2019

@author: PKoora
"""

mystr = input("Enter String:")
mydict = {}

for char in mystr:
    temp = mystr.count(char)    
    mydict[char] = temp

print("dictionary:", mydict)
print("occuranaces:")
for mykey in mydict.keys():
    print(mykey,mydict[mykey])
    

    
    






