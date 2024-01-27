from sqlalchemy import Column, Boolean, String
from data_base import Base


class User(Base):
    __tablename__ = 'user'
    login = Column(String(50), unique=True, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    password = Column(String(250), unique=True, nullable=False)
    mobile_number = Column(String(50), unique=True, nullable=False)
    is_super_user = Column(Boolean, default=0)

    def __init__(self, name, surname, login, password, mobile_number):
        self.login = login
        self.name = name
        self.surname = surname
        self.password = password
        self.mobile_number = mobile_number

    def __repr__(self):
        return f'<User {self.login}>'
