from os import getenv
from dotenv import load_dotenv

load_dotenv()
DB_PASSWORD = getenv('DB_PASSWORD')


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


APP = Flask(__name__)
APP.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
APP.config["SECRET_KEY"] = DB_PASSWORD
