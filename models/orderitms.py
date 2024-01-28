from sqlalchemy import ForeignKey, Integer, Column

from data_base import Base


class Orderitms(Base):
    __tablename__ = 'orderItms'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    item_id = Column(Integer, ForeignKey('item.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'item_id': self.item_id,

        }

    def __init__(self, order_id, item_id):
        self.order_id = order_id
        self.item_id = item_id

    def __repr__(self):
        return '<Orderitms %r>' % self.id
