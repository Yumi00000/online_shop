from .__init__ import db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    text = db.Column(db.String(250))
    rating = db.Column(db.Integer(5))
    user_login = db.Column(db.String(50), db.ForeignKey('user.login'))
