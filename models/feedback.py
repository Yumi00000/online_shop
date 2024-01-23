from sqlalchemy import ForeignKey, String, Column, Integer

from data_base import Base as init_db

class Feedback(init_db):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'))
    text = Column(String(250))
    rating = Column(Integer)
    user_login = Column(String(50), ForeignKey('user.login'))


    def __init__(self, item_id, text, rating, user_login):
        self.item_id = item_id
        self.text = text
        self.rating = rating
        self.user_login = user_login

    def __repr__(self):
        return '<Feedback %r>' % self.id

