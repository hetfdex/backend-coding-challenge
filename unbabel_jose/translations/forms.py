from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TranslateForm(FlaskForm):
    textToTranslate = StringField("Enter text to translate:")
    submit = SubmitField("Submit")
