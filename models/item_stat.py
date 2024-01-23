from sqlalchemy import String, Integer, Column

from data_base import Base as init_db


class ItemsStat(init_db):
    __tablename__ = 'items_stat'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ItemsStat %r>' % self.id
