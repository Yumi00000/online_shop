from flask import Blueprint, request, render_template, session, redirect

from data_base import db_session

from db_requests import load_from_db, insert_data_in_db, read_multiply_data_from_db
from models.compare import Compare
from models.item import Item
from models.user import User
from models.waitlist import Waitlist
from models.wishlist import Wishlist

shop_blueprint = Blueprint('shop', __name__)


@shop_blueprint.route('/shop/search/', methods=['POST'])
def search():
    if request.method == 'POST':
        name = request.form['search']
        search_res = db_session.query(Item).filter(Item.name == name).all()
        return render_template('items.html', search_res=search_res, name=name)



@shop_blueprint.route('/favorites')
def favorites():
    user_login = session.get('login')
    current_user = db_session.query(User).filter_by(login=user_login).first()
    if current_user:
        user_favorites = db_session.query(Wishlist).filter_by(user_login=current_user.login).all()
        return render_template('favorites.html', login=current_user.login, favorites=user_favorites, db=db_session, Item=Item)
    else:
        return render_template('favorites.html', login=None, favorites=None, db=db_session, Item=Item)


@shop_blueprint.route('/shop/favorites/<list_id>', methods=['GET', 'PUT'])
def favorites_update(list_id):
    user_login = session.get('login')
    current_user = db_session.query(User).filter_by(login=user_login).first()
    if request.method == 'GET':
        user_favorites = db_session.query(Wishlist).filter_by(user_login=current_user.login, list_id=list_id).all()


@shop_blueprint.route('/shop/waitlist', methods=['GET', 'POST'])
def waitlist():
    if request.method == 'GET':
        user_login = session.get('login')
        current_user = db_session.query(User).filter_by(login=user_login).first()
        user_waitlist = db_session.query(Waitlist).filter_by(user_login=current_user.login).all()
        return render_template('waitlist.html', current_user=current_user.login, user_waitlist=user_waitlist, db=db_session,
                               Item=Item)
    # else:
    #     insert_data_in_db('waitlist', ['johndoe', 1])


@shop_blueprint.route('/shop/compare/', methods=['GET', 'PUT'])
def compare_update():
    if request.method == 'GET':
        user_login = session.get('login')
        current_user = db_session.query(User).filter_by(login=user_login).first()
        user_compare = db_session.query(Compare).filter_by(user_login=current_user.login).all()
        return render_template('compare.html', login=current_user.login, compare=user_compare, db=db_session,
                               Item=Item)
    # else:
    #     update_data_in_db('compare', {'cmp_id': 2, 'item_id': 2}, {'cmp_id': cmp_id})


@shop_blueprint.post('/shop/compare/')
def add_to_compare():
    insert_data_in_db('compare', [3, 3])
