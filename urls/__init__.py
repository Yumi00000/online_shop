from flask import Blueprint

admin_blueprint = Blueprint('admin', __name__)
cart_blueprint = Blueprint('cart', __name__)
items_blueprint = Blueprint('item', __name__)
shop_blueprint = Blueprint('shop', __name__)
user_blueprint = Blueprint('user', __name__)
