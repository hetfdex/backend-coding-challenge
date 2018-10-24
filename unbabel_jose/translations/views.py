from flask import render_template, redirect, url_for, Blueprint
from unbabel_jose import db
from unbabel_jose.models import Translations
from unbabel_jose.translations.forms import TranslateForm

translation_blueprint = Blueprint("translations", __name__, template_folder = "templates/translations")

@translation_blueprint.route("/translation", methods = ["GET", "POST"])
def translation():
    form = TranslateForm()

    if form.validate_on_submit():
        textToTranslate = form.textToTranslate.data
        newTranslation = Translations(textToTranslate)

        #db.session.add(newPuppy)
        #db.session.commit()

        return redirect(url_for("/"))
    return render_template("translate.html", form = form)
