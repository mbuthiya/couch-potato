# Importing app dependencies
from flask import Flask,render_template
from flask_bootstrap import Bootstrap

# Initializations
app = Flask(__name__)
bootstrap = Bootstrap(app)

from app import views
from app import errors
