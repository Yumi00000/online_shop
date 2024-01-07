from app import db


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.Integer, db.ForeignKey('user.login'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    quantity = db.Column(db.Integer)

    def __init__(self, user_login, item_id, quantity):
        self.user_login = user_login
        self.item_id = item_id
        self.quantity = quantity

    def __repr__(self):
        return '<Cart %r>' % self.id