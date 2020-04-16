from flask import Flask
import os

from flaskdemo.sitemap import Sitemap

UPLOAD_FOLDER = '/sites/flaskdemo'

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

relpath = os.path.dirname(__file__)
filepath = os.path.join(relpath, 'brb.csv')
sitemap = Sitemap(filepath)

from flaskdemo import routes
