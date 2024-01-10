from app import db


class Order_itms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('Order.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('Item.id'))
    quantity = db.Column(db.Integer, db.ForeignKey('Cart.quantity'))

    def __init__(self, order_id, item_id, quantity):
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity

    def __repr__(self):
        return '<Order_itms %r>' % self.id
