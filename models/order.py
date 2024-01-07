from .__init__ import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(50), db.ForeignKey('user.login'))
    address = db.Column(db.String(250))
    order_total_price = db.Column(db.Float)
    status_id = db.Column(db.Integer, db.ForeignKey('order_status.status_id'))
