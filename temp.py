# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:45:28 2019

@author: PKoora
"""

alist = ["google.com","unix.com","facebook.com","google.com","linkedin.com"]
unique_list = set(alist)
mylist=[]
for val in unique_list:
    mylist.append(len(val))

print(mylist)
    