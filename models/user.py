from app import db


class User(db.Model):

    login = db.Column(db.String(50), unique=True, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    password = db.Column(db.String(250), unique=True, nullable=False)
    mobile_number = db.Column(db.String(50), unique=True, nullable=False)
    is_super_user = db.Column(db.Boolean, default=0)

    def __init__(self, name, surname, login, password, mobile_number):
        self.login = login
        self.name = name
        self.surname = surname
        self.password = password
        self.mobile_number = mobile_number

    def __repr__(self):
        return f'<User {self.login}>'

