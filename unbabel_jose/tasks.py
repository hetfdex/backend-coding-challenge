from sqlalchemy import or_
from unbabel_jose import db, uapi, celery
from unbabel_jose.models import Translation

@celery.task()
def post_translation(to_translate):
    response = uapi.post_translations(text = to_translate, source_language = "en", target_language = "es", callback_url = "localhost")

    if response:
        insert_translation.delay(response.text, response.uid, "requested")

@celery.task()
def insert_translation(source_text, uid, status):
    new_translation = Translation(source_text = source_text, translated_text = "none", uid = uid, status = status)

    db.session.add(new_translation)
    db.session.commit()

@celery.task()
def update_translations():
    translations_to_update = Translation.query.filter(or_(Translation.status == "requested", Translation.status == "pending")).all()

    if translations_to_update:
        for translation_to_update in translations_to_update:
            response = uapi.get_translation(translation_to_update.uid)

            if response:
                if response.status == "completed":
                    update_translation.delay(response.uid, response.status, "translated")
                elif response.status == "translating":
                    update_translation.delay(response.uid, "pending")
                else:
                    update_translation.delay(response.uid, response.status)

@celery.task()
def update_translation(uid, status, translated_text = "none"):
    translation_to_update = Translation.query.filter_by(uid = uid).first()

    if translation_to_update:
        translation_to_update.translated_text = translated_text
        translation_to_update.status = status

        db.session.commit()
