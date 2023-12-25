from flask import Flask, request

from db_requests import load_from_db, insert_data_in_db, update_data_in_db, delete_data_from_db

app = Flask(__name__)


@app.post('/login')
def login():
    return 'login'


@app.post('/register')
def register():
    insert_data_in_db('User', ['user2', 'John', 'Silverhand', 'pas1111', '777'])


def get_items(item_id):
    load_from_db('*', 'Item', [('id', item_id)])


@app.route('/shop/items/<item_id>/review', methods=['POST', 'GET'])
def create_read_reviews(item_id):
    if request.method == 'GET':
        load_from_db('*', 'feedback', [('item_id', item_id)])
    else:
        insert_data_in_db('feedback', [3, 2, 'Greate T-Shirt', 5, 'johndoe'])


@app.route('/shop/items/<item_id>/review/<review_id>', methods=['GET', 'PUT'])
def full_review(review_id, item_id):
    if request.method == 'GET':
        load_from_db('*', 'feedback', [('item_id', item_id), ('feedback_id', review_id)])
    else:
        update_data_in_db('feedback', {'feedback_id': 2, 'item_id': 3, 'text': 'terrible book', 'rating': 2,
                                       'user_login': 'johndoe'},
                          {'feedback_id': review_id})


@app.get('/shop/items/')
def items_page():
    load_from_db('category', 'Item')
    load_from_db('order_total_price', 'Order')


@app.post('/shop/search/')
def search():
    return 'search_res'


@app.get('/shop/cart/')
def get_cart_info():
    load_from_db('*', 'Cart')


@app.route('/shop/cart', methods=['POST', 'PUT'])
def add_items_to_cart():
    insert_data_in_db('Cart', ['johndoe', 3, 4])


@app.route('/shop/cart', methods=['DELETE'])
def delete_items_from_cart():
    delete_data_from_db('Cart', 'item_id', '1')


@app.route('/shop/cart/order', methods=['POST', 'GET'])
def edit_oder_form():
    if request.method == 'GET':
        load_from_db('*', 'Order')
    else:
        insert_data_in_db('Order', ['3', 'johndoe', '456 Oak St', '60', 'Pending'])


@app.route('/shop/favorites/<list_id>', methods=['GET', 'PUT'])
def favorites_update(list_id):
    if request.method == 'GET':
        load_from_db('*', 'wishlist', [('list_id', list_id)])
    else:
        update_data_in_db('wishlist', {'list_id': 2, 'list_name': 'Clothes', 'user_login': 'johndoe', 'item_id': 2},
                          {'list_id': list_id})


@app.post('/shop/favorites/')
def favorites():
    insert_data_in_db('wishlist', [3, 'Books Wishlist', 'johndoe', 3])


@app.route('/shop/waitlist', methods=['GET', 'POST'])
def waitlist():
    if request.method == 'GET':
        load_from_db('*', 'waitlist')
    else:
        insert_data_in_db('waitlist', ['johndoe', 1])


@app.route('/shop/compare/<cmp_id>', methods=['GET', 'PUT'])
def compare_update(cmp_id):
    if request.method == 'GET':
        load_from_db('*', 'compare', [('cmp_id', cmp_id)])
    else:
        update_data_in_db('compare', {'cmp_id': 2, 'item_id': 2}, {'cmp_id': cmp_id})


@app.post('/shop/compare/')
def add_to_compare():
    insert_data_in_db('compare', [3, 3])


@app.route('/admin/items', methods=['POST', 'GET'])
def items_update():
    if request.method == 'GET':
        load_from_db('*', 'Item')
    else:
        insert_data_in_db('Item', ['4', 'Lamborghini R2',
                                   'The Lamborghini R2 is an agricultural tractor manufactured by the Italian company Lamborghini Trattori. The R2 model is equipped with a powerful diesel engine for efficient work in the field. The tractor features a modern design and high quality workmanship, which makes it popular among farmers looking for reliable agricultural equipment.',
                                   20000000, 1, 'Tractors'])


@app.route('/admin/items/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def item_update(item_id):
    if request.method == 'GET':
        load_from_db('*', 'Item', [('id', item_id)])
    elif request.method == 'PUT':
        update_data_in_db('Item', {'price':222}, {'id':item_id})
    else:
        return f'delete_item_status{item_id}'


@app.get('/admin/orders')
def orders_info():
    load_from_db('*', 'Order')


@app.put('/admin/orders/<order_id>')
def change_order_info(order_id):
    update_data_in_db('Order', {'address':'123 Main St'}, {'order_id':order_id})

@app.get('/admin/stat')
def stat():
    load_from_db('status', 'Order')


@app.put('/user')
def user():
    update_data_in_db('User', {'name':'Danial'}, {'login':'johndoe'})


if __name__ == '__main__':
    app.run()
