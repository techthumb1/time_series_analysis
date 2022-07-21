from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_wtf import FlaskForm

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APP.config['SECRET_KEY'] = 'secret'
APP.config['DEBUG'] = True

# Initialize the database
DB = SQLAlchemy(APP)
MIGRATE = Migrate(APP, DB)


# Initialize the login manager
LOGIN_MANAGER = LoginManager(APP)
LOGIN_MANAGER.login_view = 'login'


# Define the User model
class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(20), unique=True)
    password = DB.Column(DB.String(60))
    is_admin = DB.Column(DB.Boolean)

    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


# Define the LoginForm
class LoginForm(FlaskForm):
    username = DB.Column(DB.String(20), unique=True)
    password = DB.Column(DB.String(60))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<LoginForm %r>' % self.username


# Define the RegisterForm
class RegisterForm(FlaskForm):
    username = DB.Column(DB.String(20), unique=True)
    password = DB.Column(DB.String(60))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<RegisterForm %r>' % self.username
