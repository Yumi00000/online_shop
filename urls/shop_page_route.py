from flask import Blueprint, request, render_template

from db_requests import load_from_db, insert_data_in_db, update_data_in_db

shop_blueprint = Blueprint('shop', __name__)


@shop_blueprint.post('/shop/search/')
def search():
    return 'search_res'


# @shop_blueprint.route('/shop/favorites', methods=['GET', 'POST'])
# def get_favorites():
#     login = request.form.get('login')
#     items = []  # Initialize the items variable
#     if login:
#         current_user=load_from_db('*', 'User', {'login': login})[0]
#         load_from_db( '*', 'wishlist', [('user_login', current_user[0])])
#         items = load_from_db( '*', 'wishlist', [('user_login', current_user[0])])
#     elif request.method == 'POST':
#         insert_data_in_db('wishlist', {'item_id':})
#     return render_template('favorites.html', login=login, items=items)




@shop_blueprint.route('/shop/favorites/<list_id>', methods=['GET', 'PUT'])
def favorites_update(list_id):
    if request.method == 'GET':
        load_from_db('*', 'wishlist', [('list_id', list_id)])
    else:
        update_data_in_db('wishlist', {'list_id': 2, 'list_name': 'Clothes', 'user_login': 'johndoe', 'item_id': 2},
                          {'list_id': list_id})


@shop_blueprint.route('/shop/waitlist', methods=['GET', 'POST'])
def waitlist():
    if request.method == 'GET':
        load_from_db('*', 'waitlist')
    else:
        insert_data_in_db('waitlist', ['johndoe', 1])


@shop_blueprint.route('/shop/compare/<cmp_id>', methods=['GET', 'PUT'])
def compare_update(cmp_id):
    if request.method == 'GET':
        load_from_db('*', 'compare', [('cmp_id', cmp_id)])
    else:
        update_data_in_db('compare', {'cmp_id': 2, 'item_id': 2}, {'cmp_id': cmp_id})


@shop_blueprint.post('/shop/compare/')
def add_to_compare():
    insert_data_in_db('compare', [3, 3])
