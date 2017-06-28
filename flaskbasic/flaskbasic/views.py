"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flaskbasic import app
from flaskbasic.content_management import Content

Topic_Dict = Content()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        a = Topic_Dict,
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.errorhandler(404)
def pagenotfound(e):
    return render_template("404.html")