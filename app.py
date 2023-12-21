import sqlite3
from urllib import request

from flask import Flask, url_for

app = Flask(__name__)


@app.post('/login')
def login():
    return 'login'


@app.post('/register')
def register():
    return 'register'


@app.get('/shop/items/<item_id>')
def get_items(item_id):
    my_db = sqlite3.connect('identifier.sqlite')
    cursor = my_db.cursor()
    cursor.execute(f'SELECT * FROM Item WHERE id = {item_id}')
    item_data = cursor.fetchall()
    return item_data


@app.route('/shop/items/<item_id>/review', methods=['POST', 'GET'])
def create_read_reviews(item_id):
    if request.methods == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM feedback WHERE id = {item_id}')
        item_reviews = cursor.fetchall()
        return item_reviews
    else:
        return f'post_review_status {item_id}'


@app.route('/shop/items/<item_id>/review/<review_id>', methods=['GET', 'PUT'])
def full_review(review_id, item_id):
    if request.methods == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM feedback WHERE item_id = {item_id} and feeedback_id = {review_id}')
        full_review = cursor.fetchall()
        return full_review
    else:
        return f'edit_review_status {review_id}'


@app.get('/shop/items/')
def items_page():
    page = request.args.get('page')
    my_db = sqlite3.connect('identifier.sqlite')
    cursor = my_db.cursor()
    cursor.execute(f'SELECT category FROM Item')
    cursor.execute(f'SELECT order_total_price FROM "Order"')
    items_page = cursor.fetchall()
    return items_page, page


@app.post('/shop/search/')
def search():
    return 'search_res'


@app.get('/shop/cart/')
def get_cart_info():
    my_db = sqlite3.connect('identifier.sqlite')
    cursor = my_db.cursor()
    cursor.execute(f'SELECT * FROM Cart')
    cart = cursor.fetchall()
    return cart


@app.route('/shop/cart', methods=['POST', 'PUT'])
def add_items_to_cart():
    item_id = request.args.get('item_id')
    amount = request.args.get('amount')
    return f'add_status/{item_id, amount}'


@app.route('/shop/cart', methods=['DELETE'])
def delete_items_from_cart():
    item = request.args.get('item')
    return f'delete_status/{item}'


@app.route('/shop/cart/order', methods=['POST', 'GET'])
def edit_oder_form():
    if request.methods == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM "Order"')
        order_form = cursor.fetchall()
        return order_form
    else:
        return 'form_status'


@app.route('/shop/favorites/<list_id>', methods=['GET', 'PUT'])
def favorites_update(list_id):
    if request.methods == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM wishlist WHERE list_id = {list_id}')
        favorites = cursor.fetchall()
        return favorites
    else:
        return f'list_status{list_id}'


@app.post('/shop/favorites/')
def favorites():
    return 'favorites'


@app.route('/shop/waitlist', methods=['GET', 'POST'])
def waitlist():
    if request.methods == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM waitlist')
        waitlist = cursor.fetchall()
        return waitlist
    else:
        return 'add_item_status'


@app.route('/shop/compare/<cmp_id>', methods=['GET', 'PUT'])
def compare_update(cmp_id):
    if request.methods == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM compare WHERE cmp_id = {cmp_id}')
        compare = cursor.fetchall()
        return compare
    else:
        return f'change_compare_status{cmp_id}'


@app.post('/shop/compare/')
def add_to_compare():
    return 'add_status'


@app.route('/admin/items', methods=['POST', 'GET'])
def items_update():
    if request.methods == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM Item')
        items = cursor.fetchall()
        return items
    else:
        return 'items_post_status'


@app.route('/admin/items/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def item_update(item_id):
    if request.methods == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM Item WHERE id = {item_id}')
        item = cursor.fetchall()
        return item
    elif request.methods == 'PUT':
        return f'change_item_info{item_id}'
    else:
        return f'delete_item_status{item_id}'


@app.get('/admin/orders')
def orders_info():
    my_db = sqlite3.connect('identifier.sqlite')
    cursor = my_db.cursor()
    cursor.execute(f'SELECT * FROM "Order"')
    orders = cursor.fetchall()
    return orders


@app.put('/admin/orders/<order_id>')
def change_order_info(order_id):
    return f'order_inf{order_id}'


@app.get('/admin/stat')
def stat():
    my_db = sqlite3.connect('identifier.sqlite')
    cursor = my_db.cursor()
    cursor.execute(f'SELECT status FROM "Order"')
    status = cursor.fetchall()
    return status


@app.put('/user')
def user():
    return 'user'


with app.test_request_context():
    print(url_for('login'))
    print(url_for('register'))
    print(url_for('get_items', item_id=123))
    print(url_for('create_read_reviews', item_id=123))
    print(url_for('full_review', item_id=123, review_id=456))
    print(url_for('items_page', category=1, order='price', page=2))
    print(url_for('search'))
    print(url_for('get_cart_info'))
    print(url_for('add_items_to_cart', item_id=54224, amount=2))
    print(url_for('add_items_to_cart', item='gun'))
    print(url_for('edit_oder_form'))
    print(url_for('edit_oder_form'))
    print(url_for('favorites_update', list_id=123))
    print(url_for('favorites_update', list_id=123))
    print(url_for('favorites'))
    print(url_for('waitlist'))
    print(url_for('waitlist'))
    print(url_for('compare_update', cmp_id=123))
    print(url_for('compare_update', cmp_id=123))
    print(url_for('add_to_compare'))
    print(url_for('items_update'))
    print(url_for('items_update'))
    print(url_for('item_update', item_id=123))
    print(url_for('item_update', item_id=123))
    print(url_for('item_update', item_id=123))
    print(url_for('orders_info'))
    print(url_for('change_order_info', order_id=789))
    print(url_for('stat'))
    print(url_for('user'))

if __name__ == '__main__':
    app.run()
