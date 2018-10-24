#Build a basic web app with a simple input field that takes an English (EN) input translates it to Spanish (ES).
#When a new translation is requested it should add to a list below the input field
#(showing one of three status: requested, pending or translated) - (note: always request human translation)
#The list should be dynamically ordered by the size of the translated messages
#Create a scalable application.
#Have tests
#Page load time shouldnt exceed 1 second
#Unbabel's API: http://developers.unbabel.com/

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

from unbabel_jose.translations.views import translation_blueprint

app.register_blueprint(translation_blueprint, url_prefix = "/translations")

#uapi = UnbabelApi("fullstack-challenge", "9db71b322d43a6ac0f681784ebdcc6409bb83359", sandbox = in_test_mode)
#to_translate = 'This is a test'
#target_language = 'pt'
#callback_url = 'http://my_awesome_app.com/unbabel_callback/'
#uapi.post_translations(text=to_translate, target_language=target_language, callback_url=callback_url)
