# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:54:57 2019

@author: PKoora
"""
mypassval = 0
mypass = input("Enter Password:")
if mypass.count("$") > 0 or mypass.count("#") > 0 or mypass.count("@") > 0:
    if len(mypass) > 5 and len(mypass) < 13:
        print("Valid Password")
    else:
        print("Password should contain atleast 6 characters and maximim 12 characters")
else:
    print("Password should contain either of $@#")
                