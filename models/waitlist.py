from sqlalchemy import ForeignKey, Integer, Column, String

from data_base import Base as init_db



class Waitlist(init_db):
    __tablename__ = 'waitlist'
    id = Column(Integer, primary_key=True)
    user_login = Column(String(50), ForeignKey('user.login'))
    item_id = Column(Integer, ForeignKey('item.id'))

    def __init__(self, user_login, item_id):
        self.user_login = user_login
        self.item_id = item_id

    def __repr__(self):
        return '<Waitlist %r>' % self.id

