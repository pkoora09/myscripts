# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:13:39 2019

@author: PKoora
"""

mystr="192.168."
for val in range(0,2):
    mystr1=mystr
    mystr1=mystr+str(val)+"."
    for val1 in range(1,11):
        mystr2=mystr1
        mystr2=mystr1+str(val1)
        print(mystr2)
        
    