from logging.config import fileConfig
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from alembic import context

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

db = SQLAlchemy()


def run_migrations_online():
    context.configure(
        url=current_app.config['SQLALCHEMY_DATABASE_URI'],
        target_metadata=db.metadata,
        compare_type=True,
        compare_server_default=True,
        compare_server_default_strict=True,
    )


run_migrations_online()
