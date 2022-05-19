from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db= SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'


app = Flask(__name__)
db = SQLAlchemy(app)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)  

app.config['SECRET_KEY'] = '12345678'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'


from app import views

 
