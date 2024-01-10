from app import db


class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(50), db.ForeignKey('user.login'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))

    def __init__(self, user_login, item_id):
        self.user_login = user_login
        self.item_id = item_id

    def __repr__(self):
        return '<Waitlist %r>' % self.id
