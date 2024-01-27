from sqlalchemy import Column, Integer, String

from data_base import Base



class Orderstatus(Base):
    __tablename__ = 'orderStatus'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)


    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Orderstatus %r>' % self.id

