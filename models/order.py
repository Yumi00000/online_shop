from app import db


class Order(db.Model):
    __tablename__ = 'Order'
    order_id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(50), db.ForeignKey('User.login'))
    address = db.Column(db.String(250))
    order_total_price = db.Column(db.Float)
    status = db.Column(db.String(250))

    def __init__(self, user_login, address, order_total_price, status_id):
        self.user_login = user_login
        self.address = address
        self.order_total_price = order_total_price
        self.status_id = status_id


    def __repr__(self):
        return '<Order %r>' % self.id