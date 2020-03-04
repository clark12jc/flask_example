from flask import render_template
from flaskdemo import app

agency = 'U.S. Department of Labor'


@app.route('/')
def home():
    """Landing page."""
    return render_template('home.html',
                           title=agency)


@app.route('/demo')
def demo():
    """Demo page."""
    return render_template('demo.html',
                           title=agency,
                           h1='Page Title')


@app.route('/sidenav')
def demo_sidenav():
    """Sidenav page."""
    return render_template('demo_sidenav.html',
                           title=agency,
                           h1='Page Title')


@app.route('/login')
def login():
    """Sidenav page."""
    return render_template('login.html',
                           title=agency)
