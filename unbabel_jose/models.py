from unbabel_jose import db

class Translations(db.Model):
    __tablename__ = "translations"

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String())
    translation = db.Column(db.String())

    def __init__(self, original):
        self.original = original

    def translate(self):
        translated = ""
        self.translation = translated

    #def __repr__(self):
        #return "{self.id} | {self.original}"
