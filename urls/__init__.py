
def register_blueprints(app):
    from .admin_route import admin_blueprint
    from .cart_route import cart_blueprint
    from .item_route import items_blueprint
    from .shop_page_route import shop_blueprint
    from .user_route import user_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(items_blueprint)
    app.register_blueprint(shop_blueprint)
    app.register_blueprint(cart_blueprint)
