from flask import Blueprint, request, render_template, session

from db_requests import load_from_db, insert_data_in_db, update_data_in_db, read_multiply_data_from_db

shop_blueprint = Blueprint('shop', __name__)


@shop_blueprint.post('/shop/search/')
def search():
    return 'search_res'


@shop_blueprint.route('/shop/favorites', methods=['GET', 'POST'])
def get_favorites():
    login = session.get('login')
    current_user = load_from_db('*', 'User', {'login': login})[0][0]
    print(current_user)
    favorites = read_multiply_data_from_db('*', ['wishlist', 'Item'], [('wishlist.item_id = Item.id',)],
                                           {'user_login': current_user})
    print(favorites)
    return render_template('favorites.html', login=login, favorites=favorites)


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
        login = session.get('login')
        current_user = load_from_db('*', 'User', {'login': login})[0][0]
        print(current_user)
        waitlist = read_multiply_data_from_db('*', ['waitlist', 'Item'], [('waitlist.item_id = Item.id',)],
                                              {'user_login': current_user})
        print(waitlist)
        return render_template('waitlist.html', login=login, waitlist=waitlist)
    else:
        insert_data_in_db('waitlist', ['johndoe', 1])


@shop_blueprint.route('/shop/compare/', methods=['GET', 'PUT'])
def compare_update():
    if request.method == 'GET':
        login = session.get('login')
        current_user = load_from_db('*', 'User', {'login': login})[0][0]
        compare = read_multiply_data_from_db('*', ['compare', 'Item'],
                                             [('compare.item_id = Item.id', 'compare.item_to_compare = Item.id')],
                                             {'user_login': current_user})
        print(compare)
        return render_template('compare.html', login=login, compare=compare)
    # else:
    #     update_data_in_db('compare', {'cmp_id': 2, 'item_id': 2}, {'cmp_id': cmp_id})


@shop_blueprint.post('/shop/compare/')
def add_to_compare():
    insert_data_in_db('compare', [3, 3])
