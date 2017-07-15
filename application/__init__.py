#!/usr/bin/env python
from flask import Flask

import config

app = Flask(__name__)
app.config.from_object(config)
app.template_folder = '../templates'
from application import views