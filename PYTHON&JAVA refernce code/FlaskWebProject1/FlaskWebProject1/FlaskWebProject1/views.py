"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FlaskWebProject1 import application


@application.route('/')
@application.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@application.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@application.route('/about')
def about():
    """Renders the about page."""
    if request.method == 'POST' :
        if request.form['submit_button'] == 'submit' :
            pass
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@application.route('/application')
def application():
    """Renders the about page."""
    return render_template(
        'application.html',
        title='Application',
        year=datetime.now().year,
        message='Hello World!'
    )