from flask import Blueprint, request, render_template, session, redirect

from data_base import db_session
from models.cart import Cart
from models.item import Item
from models.user import User
cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route('/shop/cart/', methods=['GET'])
def get_cart_info():
    user_login = session.get('login')
    current_user = db_session.query(User).filter_by(login=user_login).first()
    if current_user:
        cart = db_session.query(Cart).filter_by(user_login=current_user.login).all()
        return render_template('cart_page.html', cart=cart, current_user=current_user, Item=Item, db=db_session)

    return render_template('cart_page.html', current_user=current_user)


@cart_blueprint.post('/shop/cart/')
def add_items_to_cart():
    user_login = session.get('login')
    if user_login:
        current_user = db_session.query(User).filter_by(login=user_login).first()
        item_id = request.form['id']
        cart_entry = db_session.query(Cart).filter_by(user_login=current_user.login, item_id=item_id).first()

        if cart_entry:
            quantity = cart_entry.quantity + 1
            cart_entry.quantity = quantity
        else:
            db_session.add(Cart(user_login=current_user.login, item_id=item_id, quantity=1))

        db_session.commit()

        return redirect('/shop/cart')
    else:
        return redirect('/login')


@cart_blueprint.route('/shop/cart/delete', methods=['POST'])
def delete_items_from_cart():
    user_login = session.get('login')
    if user_login:
        current_user = db_session.query(User).filter_by(login=user_login).first()
        item_id = request.form['id']
        cart_entry = db_session.query(Cart).filter_by(user_login=current_user.login, item_id=item_id).first()

        if cart_entry.quantity > 1:
            quantity = cart_entry.quantity - 1
            cart_entry.quantity = quantity
        else:
            db_session.delete(cart_entry)

        db_session.commit()

        return redirect('/shop/cart')
    else:
        return redirect('/login')


@cart_blueprint.route('/shop/cart/order', methods=['POST', 'GET'])
def edit_oder_form():
    user_login = session.get('login')
    current_user = db_session.query(User).filter_by(login=user_login).first()

    cart = db_session.query(Cart).filter_by(user_login=current_user.login).all()
    price = 0
    for cart in cart:
        if cart.quantity:
            item_id = cart.item_id
            quantity = cart.quantity
            for item in db_session.query(Item).filter_by(id=item_id).all():
                price += item.price * quantity

    if request.method == 'GET':
        return render_template('order_form.html', current_user=current_user.login, price=price)
