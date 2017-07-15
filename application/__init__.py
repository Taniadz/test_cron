#!/usr/bin/env python
from flask import Flask

import config
import os
app = Flask(__name__, static_folder='../static')
app.config.from_object(config)



app.template_folder = '../templates'
app.config['STATIC_FOLDER'] = '../static'
from application import views