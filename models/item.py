from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, db.ForeignKey('status.id'))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))


    def __init__(self, name, description, price, status, category):
        self.name = name
        self.description = description
        self.price = price
        self.status = status
        self.category = category
    def __repr__(self):
        return '<Item %r>' % self.name