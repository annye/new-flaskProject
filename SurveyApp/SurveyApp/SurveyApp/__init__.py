"""
The flask application package.

"""
import os

from flask import Flask, render_template, url_for, views
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask.ext.babel import Babel
lm = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "survey.db")
app.config['SECRET_KEY'] = 'this-is-my-secret'
app.config['PAGE_SIZE'] = 1

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)



db = SQLAlchemy(app)
lm.init_app(app)
lm.session_protection = "strong"
lm.login_view = "login"
migrate = Migrate(app, db)

from .views import *







