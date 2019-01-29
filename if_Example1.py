# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:46:44 2019

@author: PKoora
"""
mystr = input("Enter month:")

mywinlist = ["january", "february", "march"]
mywincount= mywinlist.count(mystr.lower())

mysumlist = ["april", "may", "june"]
mysumcount= mysumlist.count(mystr.lower())

myrainlist = ["july", "august", "september", "october"]
myraincount = myrainlist.count(mystr.lower())

if mywincount > 0:
    print("Winter")
elif mysumcount > 0:
    print("Summer")
elif myraincount > 0:
    print("Rainy")
else:
    print("It is either Nov or Dec or wrong month entered")
