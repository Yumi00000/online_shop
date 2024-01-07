from .__init__ import db


class Compare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item_id_to_compare = db.Column(db.Integer, db.ForeignKey('item.id'))
    user_login = db.Column(db.String(50), db.ForeignKey('user.login'))
