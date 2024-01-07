from flask import Blueprint, request, render_template, session

from app import db
from db_requests import load_from_db, insert_data_in_db, read_multiply_data_from_db
from models.compare import Compare
from models.item import Item
from models.user import User
from models.waitlist import Waitlist
from models.wishlist import Wishlist

shop_blueprint = Blueprint('shop', __name__)


@shop_blueprint.post('/shop/search/')
def search():
    return 'search_res'


@shop_blueprint.route('/favorites')
def favorites():
    user_login = session.get('login')
    current_user = db.session.query(User).filter_by(login=user_login).first()
    if current_user:
        user_favorites = db.session.query(Wishlist).filter_by(user_login=current_user.login).all()
        return render_template('favorites.html', login=current_user.login, favorites=user_favorites, db=db, Item=Item)
    else:
        return render_template('favorites.html', login=None, favorites=None, db=db, Item=Item)


@shop_blueprint.route('/shop/favorites/<list_id>', methods=['GET', 'PUT'])
def favorites_update(list_id):
    user_login = session.get('login')
    current_user = db.session.query(User).filter_by(login=user_login).first()
    if request.method == 'GET':
        user_favorites = db.session.query(Wishlist).filter_by(user_login=current_user.login, list_id=list_id).all()


@shop_blueprint.route('/shop/waitlist', methods=['GET', 'POST'])
def waitlist():
    if request.method == 'GET':
        user_login = session.get('login')
        current_user = db.session.query(User).filter_by(login=user_login).first()
        user_waitlist = db.session.query(Waitlist).filter_by(user_login=current_user.login).all()
        return render_template('waitlist.html', current_user=current_user.login, user_waitlist=user_waitlist, db=db,
                               Item=Item)
    # else:
    #     insert_data_in_db('waitlist', ['johndoe', 1])


@shop_blueprint.route('/shop/compare/', methods=['GET', 'PUT'])
def compare_update():
    if request.method == 'GET':
        user_login = session.get('login')
        current_user = db.session.query(User).filter_by(login=user_login).first()
        user_compare = db.session.query(Compare).filter_by(user_login=current_user.login).all()
        return render_template('compare.html', login=current_user.login, compare=user_compare, db=db,
                               Item=Item)
    # else:
    #     update_data_in_db('compare', {'cmp_id': 2, 'item_id': 2}, {'cmp_id': cmp_id})


@shop_blueprint.post('/shop/compare/')
def add_to_compare():
    insert_data_in_db('compare', [3, 3])
