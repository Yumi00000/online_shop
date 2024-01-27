from sqlalchemy import Column, Integer, String, ForeignKey

from data_base import Base

class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    user_login = Column(String(50), ForeignKey('user.login'))
    item_id = Column(Integer, ForeignKey('item.id'))
    quantity = Column(Integer, unique=True)

    def __init__(self, user_login, item_id, quantity):
        self.user_login = user_login
        self.item_id = item_id
        self.quantity = quantity

    def __repr__(self):
        return '<Cart %r>' % self.id
