import os

import requests
from flask import render_template, flash, request, redirect
from flaskdemo import app, sitemap
from werkzeug.utils import secure_filename

from flaskdemo.utils import get_node_title, get_node_alias
from flaskdemo.cv import get_timeseries

agency = 'U.S. Department of Labor'


ALLOWED_EXTENSIONS = {'pdf'}
DOL = 'U.S. Department of Labor'
AGENCIES = {
    'whd': 'Wage and Hour Division',
    'brb': 'Benefits Review Board'
}


def allowed_file(filename):
    return '.' in filename \
           and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def clean(string):
    string = string.replace('\n', ' ')
    return string


def pdf_info(filename):
    import textract
    text = textract.process(filename)
    return text.decode('utf-8')


@app.route('/cv/<state_abbr>')
def cv(state_abbr):
    data, state_name = get_timeseries(state_abbr)
    return render_template('basic.html',
                           title=agency,
                           h1=f'Coronavirus Cases in {state_name}',
                           content=data)


@app.route('/config')
def config():
    return render_template('config.html',
                           title=agency)


@app.route('/sitemap')
def get_sitemap():
    content = sitemap.html_table()
    return render_template('sitemap.html',
                           title=agency,
                           content=content)


@app.route('/upload')
def upload_form():
    return render_template('upload.html',
                           title=agency)


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            # return redirect(request.url)
            error = 'No file selected for uploading'
            return render_template('upload.html',
                                   title=agency,
                                   error=error)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            flash('File successfully uploaded')
            info = pdf_info(filepath)
            return render_template('upload.html',
                                   title=agency,
                                   info=info)
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            error = 'Error status'
            # return redirect(request.url)
            # return redirect(url_for('upload_form', error=error))
            return render_template('upload.html',
                                   title=agency,
                                   error=error)


@app.route('/')
def home():
    """Landing page."""
    return render_template('home.html',
                           title=agency)


@app.route('/demo/<path:variable>', methods=['GET'])
def demo_variable(variable):
    """Demo variable page."""
    ag = AGENCIES.get(variable)
    if not ag:
        ag = DOL
    return render_template('demo.html',
                           title=ag,
                           h1='Hello World')


@app.route('/demo')
def demo():
    """Demo page."""
    return render_template('demo.html',
                           title=agency,
                           h1='Hello World')


@app.route('/node/<int:id_>')
def node(id_):
    """Demo page."""
    content = sitemap.content(id_)
    alias = sitemap.alias(id_)
    title = sitemap.title(id_)
    return render_template('basic.html',
                           title=agency,
                           h1=title,
                           content=content)


@app.route('/drupal/<int:id_>')
def drupal(id_):
    """Demo page."""
    content = ''
    alias = get_node_alias(id_)
    title = get_node_title(id_)
    return render_template('basic.html',
                           title=agency,
                           h1=title,
                           alias=alias,
                           content=content)


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
