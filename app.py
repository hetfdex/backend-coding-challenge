from flask import render_template, redirect, url_for
from sqlalchemy import func, or_
from unbabel_jose import app, db, uapi
from unbabel_jose.forms import TranslationForm
from unbabel_jose.models import Translation

@app.route("/", methods = ["GET", "POST"])
def index():
    translation_form = TranslationForm()

    if translation_form.validate_on_submit():
        post_translation(translation_form.to_translate.data)

    translations = get_sorted_translations()

    return render_template("index.html", translation_form = translation_form, translations = translations)

def post_translation(to_translate):
    response = uapi.post_translations(text = to_translate, target_language = "es", source_language = "en", callback_url = "localhost")

    if response:
        insert_translation(response.text, response.uid, response.status)

def get_translation(uid):
    return uapi.get_translation(uid)

def insert_translation(source_text, uid, status):
    new_translation = Translation(source_text = source_text, translated_text = "none", uid = uid, status = status)

    db.session.add(new_translation)
    db.session.commit()

def get_sorted_translations():

    update_translations()

    translations = Translation.query.order_by(func.length(Translation.translated_text)).all()

    return translations

def update_translations():
    translations_to_update = Translation.query.filter(or_(Translation.status == "requested", Translation.status == "translating")).all()

    if translations_to_update:
        for translation_to_update in translations_to_update:
            response = get_translation(translation_to_update.uid)

            if response:
                if response.status == "completed":
                    update_translation(response.uid, response.status, response.translation)
                else:
                    update_translation(response.uid, response.status)

def update_translation(uid, status, translated_text = "none"):
    translation_to_update = Translation.query.filter_by(uid = uid).first()

    if translation_to_update:
        translation_to_update.translated_text = translated_text
        translation_to_update.staus = staus

        db.session.commit()

if __name__ == '__main__':
    app.run(debug = True)
