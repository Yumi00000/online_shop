from sqlalchemy import String, Column, Integer, ForeignKey

from data_base import Base as init_db



class Compare(init_db):
    __tablename__ = 'compare'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'))
    item_to_compare = Column(Integer, ForeignKey('item.id'))
    user_login = Column(String(50), ForeignKey('user.login'))

    def __init__(self, item_id, item_to_compare, user_login):
        self.item_id = item_id
        self.item_to_compare = item_to_compare
        self.user_login = user_login

    def __repr__(self):
        return '<Compare %r>' % self.id

