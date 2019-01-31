# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:23:58 2019

@author: PKoora
"""

import os
import pathlib
import shutil

"""
os.mkdir("Source")
os.mkdir("Destination")



pathlib.Path("./Source/test1.txt").touch()
pathlib.Path("./Source/test2.txt").touch()
pathlib.Path("./Source/test3.txt").touch()
pathlib.Path("./Source/test4.txt").touch()
"""

shutil.copyfile("./Source/test1.txt", "./Destination/test2.txt")


