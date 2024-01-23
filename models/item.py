from sqlalchemy import ForeignKey, Integer, Column, Float, Text, String

from data_base import Base as init_db



class Item(init_db):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(Integer, ForeignKey('items_stat.id'))
    category = Column(Integer, ForeignKey('category.id'))

    def __init__(self, name, description, price, status, category):
        self.name = name
        self.description = description
        self.price = price
        self.status = status
        self.category = category

    def __repr__(self):
        return '<Item %r>' % self.id

