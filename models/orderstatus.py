from app import db


class Orderstatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Orderstatus %r>' % self.id
