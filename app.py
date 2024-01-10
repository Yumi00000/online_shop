from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'dfgdrfttg3e4dfvb'

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///online_shop.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)

from models.cart import Cart
from models.category import Category
from models.compare import Compare
from models.feedback import Feedback
from models.item import Item
from models.item_stat import ItemsStat
from models.order import Order
from models.orderitms import Orderitms
from models.orderstatus import Orderstatus
from models.user import User
from models.waitlist import Waitlist
from models.wishlist import Wishlist

migrate = Migrate(app, db)

# Register blueprints after app creation
from urls import items_blueprint, admin_blueprint, user_blueprint, shop_blueprint, cart_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(shop_blueprint)
app.register_blueprint(cart_blueprint)

if __name__ == '__main__':
    db.create_all()
    app.run()
