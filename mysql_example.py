# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:21:45 2019

@author: PKoora
"""

import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="pradeep")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME VARCHAR(50) NOT NULL,
         INCOME FLOAT,
         ADDRESS VARCHAR(100))"""
cursor.execute(sql)

print("table create successfully")

db.close()