from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from unbabel.api import UnbabelApi
from unbabel_jose.config import Config

app = Flask(__name__)

app.config["SECRET_KEY"] = Config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["CELERYBEAT_SCHEDULE"] = Config.CELERYBEAT_SCHEDULE
app.config["TIMEZONE"] = "UTC"

db = SQLAlchemy(app)

Migrate(app, db)

def make_celery(app):
    celery = Celery(app.import_name, broker = Config.CELERY_BROKER_URL)

    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)

uapi = UnbabelApi(username = Config.UNBABEL_USER, api_key = Config.UNBABEL_API, sandbox = True)
