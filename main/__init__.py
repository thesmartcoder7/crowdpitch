from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from ..config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import views, forms