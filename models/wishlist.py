from app import db


class Wishlist(db.Model):
    list_id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50), unique=True, nullable=False)
    user_login = db.Column(db.String(50), db.ForeignKey('User.login'))
    item_id = db.Column(db.Integer, db.ForeignKey('Item.id'))


    def __init__(self, list_name, user_login, item_id):
        self.list_name = list_name
        self.user_login = user_login
        self.item_id = item_id
    def __repr__(self):
        return '<Wishlist %r>' % self.id
