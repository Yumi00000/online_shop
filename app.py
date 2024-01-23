from flask import Flask
from alembic.config import Config
from alembic.script import ScriptDirectory

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:5000'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yumi:postgres@db/online_shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super secret key"

alembic_script_location = "alembic"

config = Config()
config.set_main_option("script_location", alembic_script_location)
config.set_main_option("sqlalchemy.url", app.config['SQLALCHEMY_DATABASE_URI'])

script = ScriptDirectory.from_config(config)

from urls.__init__ import user_blueprint, admin_blueprint, shop_blueprint, cart_blueprint, items_blueprint


app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(shop_blueprint)
app.register_blueprint(cart_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

