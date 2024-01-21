from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yumi:postgres@localhost/online_shop'
app.config['SERVER_NAME'] = '127.0.0.1:5000'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super secret key"
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from urls.__init__ import create_blueprints

blueprints = create_blueprints()

app.register_blueprint(blueprints['user'], name='user_blueprint')
app.register_blueprint(blueprints['admin'], name='admin_blueprint')
app.register_blueprint(blueprints['items'], name='items_blueprint')
app.register_blueprint(blueprints['shop'], name='shop_blueprint')
app.register_blueprint(blueprints['cart'], name='cart_blueprint')

if __name__ == '__main__':
    with app.app_context():
        app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
