from sqlalchemy import String, Column, Integer

from data_base import Base as init_db



class Category(init_db):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)


    def __init__(self, name, description=None):
        self.name = name


    def __repr__(self):
        return '<Category %r>' % self.id

