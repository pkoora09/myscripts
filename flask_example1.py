# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:56:08 2019

@author: PKoora
"""

import os
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
    
    authors = os.listdir("C:/")
    rendered_html = render_template_string(html, library=library_name, authors = authors)
    return rendered_html