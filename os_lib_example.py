# -*- coding: utf-8 -*-
"""
Progranm to list all the files and directories in the current path

@author: PKoora
"""

import os

"""
print(os.getcwd())

print(os.cpu_count())
print(os.getlogin())
mylist = os.listdir()

for myfile in mylist:
    if myfile.endswith(".py") or myfile.endswith(".txt"):
        print(myfile)

print(os.listdir("C:/"))

for myfile in mylist:
    if os.path.isdir(myfile):
        print(myfile)



os.chdir(".\Temp")
for var in range(1,101):
    mystr="dir"+str(var)
    os.mkdir(mystr)
    


os.chdir(".\Temp")
mylist = os.listdir()
for myfile in mylist:
    if myfile.endswith(".txt"):
        os.remove(myfile)



mydir = []
myfiles = []
mylist = os.listdir()
for myfile in mylist:
  
    if os.path.isdir(myfile):
        mydir.append(myfile)
        
    if os.path.isfile(myfile):
        myfiles.append(myfile)
        
        
print("files")
print(myfiles)
print("Directories")
print(mydir)

"""

#os.mkdir("backup")
for file in os.listdir():
    if os.path.isfile(file):
        if file.endswith(".py"):
            os.system('cp' + file + 'C:\Personal\Python\Examples\Programs\backup/')
        

