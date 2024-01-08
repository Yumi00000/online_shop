from flask import Blueprint, render_template, request, session, redirect, url_for

from app import db
from models.cart import Cart
from models.item import Item
from models.user import User

cart_blueprint = Blueprint('cart', __name__)


@cart_blueprint.route('/shop/cart/', methods=['GET'])
def get_cart_info():
    login = session.get('login')
    current_user = User.query.filter_by(login=login).first()
    cart_id = Cart.query.filter_by(user_login=current_user.login).first()
    cart = db.session.query(Cart, Item).filter(Cart.item_id == Item.id, Cart.user_login == current_user.login).all()
    return render_template('cart_page.html', cart_id=cart_id, current_user=current_user, cart=cart)


@cart_blueprint.post('/shop/cart/')
def add_items_to_cart():
    login = session.get('login')
    if login:
        current_user = User.query.filter_by(login=login).first()
        item_id = request.form.get('id')
        cart_item = Cart.query.filter_by(user_login=current_user.login, item_id=item_id).first()

        if cart_item:
            cart_item.quantity += 1
        else:
            cart_item = Cart(user_login=current_user.login, item_id=item_id, quantity=1)
            db.session.add(cart_item)

        db.session.commit()
        return redirect(url_for('cart.get_cart_info'))
    else:
        return redirect('/login')


@cart_blueprint.route('/shop/cart/delete', methods=['POST'])
def delete_items_from_cart():
    login = session.get('login')
    current_user = User.query.filter_by(login=login).first()

    item_id = request.form.get('id')
    cart_item = Cart.query.filter_by(user_login=current_user.login, item_id=item_id).first()

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
    else:
        db.session.delete(cart_item)

    db.session.commit()
    return redirect(url_for('cart.get_cart_info'))


@cart_blueprint.route('/shop/cart/order', methods=['POST', 'GET'])
def edit_order_form():
    login = session.get('login')
    current_user = User.query.filter_by(login=login).first()

    if request.method == 'GET':
        return render_template('order_form.html', current_user=current_user)
