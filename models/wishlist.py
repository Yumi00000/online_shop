from sqlalchemy import ForeignKey, Integer, Column, String

from data_base import Base


class Wishlist(Base):
    __tablename__ = 'wishlist'
    id = Column(Integer, primary_key=True)
    list_name = Column(String(50), unique=True, nullable=False)
    user_login = Column(String(50), ForeignKey('user.login'))
    item_id = Column(Integer, ForeignKey('item.id'))


    def __init__(self, list_name, user_login, item_id):
        self.list_name = list_name
        self.user_login = user_login
        self.item_id = item_id
    def __repr__(self):
        return '<Wishlist %r>' % self.id

