from flask import redirect
from alembic.config import Config
from alembic.script import ScriptDirectory
import os
from urls.shop_page_route import shop_blueprint
from urls.admin_route import admin_blueprint
from urls.user_route import user_blueprint
from urls.cart_route import cart_blueprint
from urls.item_route import items_blueprint
from flask import Flask
from celery import Celery

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@172.19.0.2:5432/online_shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super secret key"
alembic_script_location = os.path.join("alembic")
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

config = Config()
config.set_main_option("script_location", alembic_script_location)
config.set_main_option("sqlalchemy.url", app.config['SQLALCHEMY_DATABASE_URI'])

script = ScriptDirectory.from_config(config)

app.register_blueprint(admin_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(cart_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(shop_blueprint)


@app.redirect
def redirect_to_shop_items():
    return redirect('/shop/items')


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
