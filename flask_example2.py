# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:30:52 2019

@author: PKoora
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:56:08 2019

@author: PKoora
"""

import os
import pandas
from flask import Flask
from flask import render_template_string  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "Python"
    html = """
        <html>
            <h1>Welcome to {{library}} library!</h1>
            <ul>
                    {% for author in authors %}
                        <li>{{author}}</li>
                    {% endfor %}
            </ul>
        </html>
    """
    with open("C:/Users/pkoora.DIR/Desktop/datasets-master/nba.csv") as fobj:
        lines = fobj.readlines()    
    rendered_html = render_template_string(html, library=library_name, authors = lines)
    return rendered_html