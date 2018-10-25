from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from unbabel.api import UnbabelApi

app = Flask(__name__)

app.config["SECRET_KEY"] = "Abcde12345!"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/unbabel_translations"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

Migrate(app, db)

uapi = UnbabelApi(username = "fullstack-challenge", api_key = "9db71b322d43a6ac0f681784ebdcc6409bb83359", sandbox = True)
