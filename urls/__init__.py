def create_blueprints():
    from app import db

    from .admin_route import admin_blueprint
    from .cart_route import cart_blueprint
    from .item_route import items_blueprint
    from .shop_page_route import shop_blueprint
    from .user_route import user_blueprint

    return {
        'admin': admin_blueprint,
        'cart': cart_blueprint,
        'items': items_blueprint,
        'shop': shop_blueprint,
        'user': user_blueprint,
    }
