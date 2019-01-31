# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:38:54 2019

@author: PKoora
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'This is my home page'

@app.route('/login')
def loginpage():
    return 'This is my Login page'

@app.route('/dashboard')
def dashpage():
    return 'This is my Dashboard page'


app.run()
