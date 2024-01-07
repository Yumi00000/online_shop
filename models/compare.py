from app import db


class Compare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item_to_compare = db.Column(db.Integer, db.ForeignKey('item.id'))
    user_login = db.Column(db.String(50), db.ForeignKey('user.login'))

    def __init__(self, item_id, item_to_compare, user_login):
        self.item_id = item_id
        self.item_to_compare = item_to_compare
        self.user_login = user_login

    def __repr__(self):
        return '<Compare %r>' % self.id
