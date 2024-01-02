from flask import Blueprint, request, render_template, session, redirect

from db_requests import load_from_db, insert_data_in_db, delete_data_from_db, read_multiply_data_from_db, \
    update_data_in_db

cart_blueprint = Blueprint('cart', __name__)


@cart_blueprint.route('/shop/cart/', methods=['GET'])
def get_cart_info():
    login = session.get('login')

    current_user = load_from_db('*', 'User', {'login': login})[0][0]
    cart_id = load_from_db('user_login', 'Cart', {'user_login': current_user})
    cart = read_multiply_data_from_db('*', ['Cart', 'Item'], [('Cart.item_id = Item.id',)],
                                      {'user_login': current_user})
    return render_template('cart_page.html', cart_id=cart_id, current_user=current_user, cart=cart)


@cart_blueprint.post('/shop/cart/')
def add_items_to_cart():
    login = session.get('login')
    if login:
        current_user = load_from_db('*', 'User', {'login': login})[0][0]
        item_id = request.form.get('id')
        quantity_result = load_from_db('quantity', 'Cart', {'user_login': current_user, 'item_id': item_id})
        if quantity_result:
            quantity = quantity_result[0][0]
            update_data_in_db('Cart', {'quantity': quantity + 1}, {'user_login': current_user, 'item_id': item_id})
        else:
            insert_data_in_db('Cart', {'user_login': current_user, 'item_id': item_id, 'quantity': 1})

        return redirect('/shop/cart')
    else:
        return redirect('/login')


@cart_blueprint.route('/shop/cart/delete', methods=['POST'])
def delete_items_from_cart():
    login = session.get('login')
    current_user = load_from_db('*', 'User', {'login': login})[0][0]

    item_id = request.form.get('id')
    quantity_result = load_from_db('quantity', 'Cart', {'user_login': current_user, 'item_id': item_id})
    quantity = quantity_result[0][0]
    if quantity > 1:
        update_data_in_db('Cart', {'quantity': quantity - 1}, {'user_login': current_user, 'item_id': item_id})
    else:
        delete_data_from_db('Cart', 'item_id', item_id)
    return redirect('/shop/cart')


@cart_blueprint.route('/shop/cart/order', methods=['POST', 'GET'])
def edit_oder_form():
    login = session.get('login')
    current_user = load_from_db('*', 'User', {'login': login})[0][0]
    if request.method == 'GET':

        return render_template('order_form.html', current_user=current_user)
