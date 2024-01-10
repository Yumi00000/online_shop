from app import db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    text = db.Column(db.String(250))
    rating = db.Column(db.Integer)
    user_login = db.Column(db.String(50), db.ForeignKey('user.login'))


    def __init__(self, item_id, text, rating, user_login):
        self.item_id = item_id
        self.text = text
        self.rating = rating
        self.user_login = user_login

    def __repr__(self):
        return '<Feedback %r>' % self.id