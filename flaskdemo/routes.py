import os

from flask import render_template, flash, request, redirect
from flaskdemo import app
from werkzeug.utils import secure_filename

agency = 'U.S. Department of Labor'


ALLOWED_EXTENSIONS = {'pdf'}
DOL = 'U.S. Department of Labor'
AGENCIES = {
    'whd': 'Wage and Hour Division',
    'brb': 'Benefits Review Board'
}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def clean(string):
    string = string.replace('\n', ' ')
    return string


def pdf_info(filename):
    import textract
    text = textract.process(filename)
    return text.decode('utf-8')


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
            return redirect(request.url)
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
