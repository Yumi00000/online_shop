from sqlalchemy import String, Column, Integer, ForeignKey

from data_base import Base



class Compare(Base):
    __tablename__ = 'compare'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'))
    name = Column(String(32), nullable=False)
    user_login = Column(String(50), ForeignKey('user.login'))

    def __init__(self, item_id, name, user_login):
        self.item_id = item_id
        self.name = name
        self.user_login = user_login

    def __repr__(self):
        return '<Compare %r>' % self.id

