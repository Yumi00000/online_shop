from sqlalchemy import Column, String, Float, ForeignKey, Integer
from data_base import Base

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    user_login = Column(String(50), ForeignKey('user.login'))
    address = Column(String(250))
    order_total_price = Column(Float)
    status = Column(Integer)

    def __init__(self, user_login, address, order_total_price, status):
        self.user_login = user_login
        self.address = address
        self.order_total_price = order_total_price
        self.status = status

    def __repr__(self):
        return '<Order %r>' % self.id
