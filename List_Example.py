# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:17:42 2019

@author: PKoora
"""

mylist = [5,7,8]
mylist.append(10)
print("Appended 10:", mylist)
mylist.append(20)
print("Appended 20:", mylist)
mylist.append(50)
print("Appended 50:", mylist)
mylist.extend([90,20,45,32,645,32,90,65,43,23,55,4,32,50])
print("Extended List:", mylist)
print("Unique List:", set(mylist))
mylist.remove(50)
print("Remove 50:", mylist)
mylist.sort(reverse=True)
print("Sort Elements:", mylist)
print("Converted to Tuple:", tuple(mylist))
