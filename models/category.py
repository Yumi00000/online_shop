from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


    def __init__(self, name, description=None):
        self.name = name


    def __repr__(self):
        return '<Category %r>' % self.id
