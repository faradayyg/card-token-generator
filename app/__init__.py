from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
