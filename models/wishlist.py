from .__init__ import db


class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50), unique=True, nullable=False)
    user_login = db.Column(db.String(50), db.ForeignKey('user.login'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
