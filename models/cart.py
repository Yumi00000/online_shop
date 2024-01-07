from .__init__ import db


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.Integer, db.ForeignKey('user.login'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    quantity = db.Column(db.Integer)
