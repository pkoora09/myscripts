# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:02:44 2019

@author: PKoora
"""

import os

from flask_example2 import app


if __name__ == '__main__':
    app.debug = False
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
