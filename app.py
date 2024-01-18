from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from urls.__init__ import register_blueprints

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        register_blueprints(app)

    if app.config.get('ENV') == 'development':
        app.run(debug=True)
