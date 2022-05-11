from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from ..config import ProdConfig


app = Flask(__name__)
# use from object. app.config from object
app.config['SQLALCHEMY_DATABASE_URI'] = ProdConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .main import views, forms