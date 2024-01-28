from flask import Blueprint, request, render_template, session, redirect, url_for

import data_base
from data_base import db_session

from db_requests import load_from_db, insert_data_in_db, read_multiply_data_from_db
from models import compare, item
from models.compare import Compare
from models.item import Item
from models.user import User
from models.waitlist import Waitlist
from models.wishlist import Wishlist

shop_blueprint = Blueprint('shop', __name__)


@shop_blueprint.route('/favorites')
def favorites():
    user_login = session.get('login')
    current_user = db_session.query(User).filter_by(login=user_login).first()
    if current_user:
        user_favorites = db_session.query(Wishlist).filter_by(user_login=current_user.login).all()
        return render_template('favorites.html', login=current_user.login, favorites=user_favorites, db=db_session,
                               Item=Item)
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
        return render_template('waitlist.html', current_user=current_user.login, user_waitlist=user_waitlist,
                               db=db_session,
                               Item=Item)
    # else:
    #     insert_data_in_db('waitlist', ['johndoe', 1])


from sqlalchemy.orm import joinedload


@shop_blueprint.route('/shop/compare/', methods=['GET', 'PUT'])
def compare_update():
    if request.method == 'GET':
        data_base.init_db()
        cmp_items = db_session.query(Compare, Item).join(Item, Item.id == Compare.item_id).all()
        items_list = [{**item[0].to_dict(), **item[1].to_dict()} for item in cmp_items]
        return render_template('compare_update.html', items_list=items_list)


@shop_blueprint.post('/shop/compare/')
def add_to_compare():
    data_base.init_db()
    item_id = request.form.get('item_id')
    existing_compare_item = Compare.query.filter(
        (Compare.item_id == item_id) &
        (Compare.user_login == session.get('login'))
    ).first()
    user_cmp = compare.Compare.query.distinct(compare.Compare.id).filter(
        compare.Compare.user_login == session.get('login')).all()

    if existing_compare_item:
        print(f"Item with ID {item_id} is already in the compare list.")
    else:
        new_compare_item = Compare(item_id=item_id, name='Some name', user_login=session.get('login'))
        db_session.add(new_compare_item)
        db_session.commit()
    return redirect(url_for('shop.compare_update'))
