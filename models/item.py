from .__init__ import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
