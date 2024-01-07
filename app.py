from models.__init__ import app

from urls import items_blueprint, admin_blueprint, user_blueprint, shop_blueprint, cart_blueprint




app.secret_key = 'dfgdrfttg3e4dfvb'
app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(shop_blueprint)
app.register_blueprint(cart_blueprint)

if __name__ == '__main__':
    app.run()
