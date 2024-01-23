from sqlalchemy import ForeignKey, Integer, Column

from data_base import Base as init_db



class Orderitms(init_db):
    __tablename__ = 'orderItms'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    quantity = Column(Integer, ForeignKey('cart.quantity'))

    def __init__(self, order_id, item_id, quantity):
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity

    def __repr__(self):
        return '<Orderitms %r>' % self.id

