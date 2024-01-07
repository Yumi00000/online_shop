from .__init__ import db


class Waitlist(db.Model):
    user_login = db.Column(db.String(50), db.ForeignKey('user.login'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
