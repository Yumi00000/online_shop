from app import db


class Items_stat(db.Model):
    __tablename__ = 'Items_stat'
    stat_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Item_stat %r>' % self.name
