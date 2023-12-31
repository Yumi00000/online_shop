from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'dfgdrfttg3e4dfvb'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///identifier.sqlite'

print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register blueprints after app creation
from urls import items_blueprint, admin_blueprint, user_blueprint, shop_blueprint, cart_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(shop_blueprint)
app.register_blueprint(cart_blueprint)

if __name__ == '__main__':
    app.run()
