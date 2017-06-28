"""
The flask application package.
"""

from flask import Flask
from flaskbasic.content_management import Content

app = Flask(__name__)
Topic_Dict = Content()

import flaskbasic.views
