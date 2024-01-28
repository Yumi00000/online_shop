from sqlalchemy import String, Column, Integer, ForeignKey

from data_base import Base


class Compare(Base):
    __tablename__ = 'compare'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'))
    name = Column(String(32), nullable=False)
    user_login = Column(String(50), ForeignKey('user.login'))

    def to_dict(self):
        return {
            'id': self.id,
            'user_login': self.user_login,
            'name': self.name,
            'item_id': self.item_id}

    def __repr__(self):
        return '<Compare %r>' % self.id
