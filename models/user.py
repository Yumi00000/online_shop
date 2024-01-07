from .__init__ import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    sure_name = db.Column(db.String(50))
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=True, nullable=False)
    mobile_number = db.Column(db.String(50), unique=True, nullable=False)
    is_super_user = db.Column(db.Boolean, default=0)
