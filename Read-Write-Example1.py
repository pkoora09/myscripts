# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:51:16 2019

@author: PKoora


import datetime

myobj = open("C:\Personal\Python\even.txt","w")
for var in range(500,300,-2):
    mytime = datetime.date.today()
    myobj.write(str(mytime)+":"+str(var)+"\n")

myobj.close()



import datetime
import os

myobj = open("C:\Personal\Python\listfiles.txt","w")
mylist = os.listdir()
for var in mylist:
    mytime = datetime.date.today()
    myobj.write(str(mytime)+":"+str(var)+"\n")
    
myobj.close()

"""






