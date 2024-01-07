from app import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(50), db.ForeignKey('user.login'))
    address = db.Column(db.String(250))
    order_total_price = db.Column(db.Float)
    status_id = db.Column(db.Integer, db.ForeignKey('order_status.status_id'))

    def __init__(self, user_login, address, order_total_price, status_id):
        self.user_login = user_login
        self.address = address
        self.order_total_price = order_total_price
        self.status_id = status_id


    def __repr__(self):
        return '<Order %r>' % self.id