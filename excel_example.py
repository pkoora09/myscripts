# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:25:10 2019

@author: PKoora


from openpyxl import Workbook
wb = Workbook

ws = wb.active


ws['A1'] = "Name"
ws.append(["Pradeep"])
ws.append(["lalit"])

wb.save("C:/Personal/Python/myexcel.xlsx")


from openpyxl import Workbook
import csv
wb = Workbook()

ws = wb.active

with open("C:/Personal/Python/realestate.csv") as myobj:
    for line in csv.reader(myobj):
        ws.append(line)
wb.save("C:/Personal/Python/real.xlsx")

"""