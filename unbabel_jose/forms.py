from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TranslationForm(FlaskForm):
    to_translate = StringField("Enter text to translate:", validators = [DataRequired()])
    submit = SubmitField("Translate")
