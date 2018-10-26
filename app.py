from flask import render_template
from sqlalchemy import func
from unbabel_jose import app
from unbabel_jose.forms import TranslationForm
from unbabel_jose.models import Translation
from unbabel_jose.tasks import post_translation

@app.route("/", methods = ["GET", "POST"])
def index():
    translation_form = TranslationForm()

    if translation_form.validate_on_submit():
        post_translation.delay(translation_form.to_translate.data)

    translations = get_sorted_translations()

    return render_template("index.html", translation_form = translation_form, translations = translations)

def get_sorted_translations():
    return Translation.query.order_by(func.length(Translation.translated_text)).all()

if __name__ == '__main__':
    app.run(debug = True)
