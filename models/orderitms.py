from app import db


class Orderitms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    quantity = db.Column(db.Integer, db.ForeignKey('cart.quantity'))

    def __init__(self, order_id, item_id, quantity):
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity

    def __repr__(self):
        return '<Orderitms %r>' % self.id
