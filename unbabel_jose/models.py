from unbabel_jose import db

class Translation(db.Model):
    __tablename__ = "translations"

    id = db.Column(db.Integer, primary_key=True)
    source_text = db.Column(db.String(512))
    translated_text = db.Column(db.String(512))
    uid = db.Column(db.String(64))
    status = db.Column(db.String(64))

    def __init__(self, source_text, translated_text, uid, status):
        self.source_text = source_text
        self.translated_text = translated_text
        self.uid = uid
        self.status = status

    def __repr__(self):
        return "{} | {} | {} | {}".format(self.uid, self.source_text, self.translated_text, self.status).encode("utf-8")
