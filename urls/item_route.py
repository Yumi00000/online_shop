from flask import Blueprint, request, session, render_template, url_for, redirect
from sqlalchemy import func, desc

from data_base import db_session
from models.feedback import Feedback
from models.item import Item
from models.user import User

items_blueprint = Blueprint('item', __name__)


@items_blueprint.route('/shop/items/<int:item_id>/review', methods=['GET', 'POST'])
def create_read_reviews(item_id):
    user_login = session.get('login')
    current_user = None
    if user_login:
        current_user = db_session.query(User).filter_by(login=user_login).first()
    if request.method == 'GET':
        user_reviews = db_session.query(Feedback).filter_by(user_login=current_user.login).all()
        return render_template('reviews.html', reviews=user_reviews, item_id=item_id, current_user=current_user.login,
                               Item=Item, db=db_session)
    elif request.method == 'POST':
        review_text = request.form['review-text']
        rating = request.form['rating']

        new_feedback = Feedback(text=review_text, rating=rating, user_login=current_user.login, item_id=item_id)
        db_session.add(new_feedback)
        db_session.commit()

    return redirect(url_for('item.create_read_reviews', item_id=item_id))


@items_blueprint.route('/shop/items/<item_id>/review/<review_id>', methods=['GET', 'POST'])
def full_review(item_id, review_id):
    user_login = session.get('login')
    current_user = db_session.query(User).filter_by(login=user_login).first()

    if request.method == 'GET':
        user_review = db_session.query(Feedback).filter_by(user_login=current_user.login, feedback_id=review_id).first()
        return render_template('full_review.html', review=user_review, item_id=item_id)

    elif request.method == 'POST':
        review_text = request.form['review']
        rating = request.form['rating']

        existing_review = db_session.query(Feedback).filter_by(user_login=current_user.login,
                                                               feedback_id=review_id).first()

        if existing_review:

            existing_review.text = review_text
            existing_review.rating = rating
            db_session.commit()
            return redirect(url_for('item.create_read_reviews', item_id=item_id))
        else:
            return render_template('full_review.html', error_message="Review not found.", item_id=item_id)


@items_blueprint.route('/shop/items', methods=['GET'])
def items_page():
    user_login = session.get('login')
    current_user = db_session.query(User).filter_by(login=user_login).first()

    items = db_session.query(Item).all()

    item_ratings = {}
    for item in items:
        average_rating = db_session.query(func.avg(Feedback.rating)).filter(Feedback.item_id == item.id).scalar()
        item_ratings[item.id] = average_rating

    filter_param = request.args.get('filter')
    category_param = request.args.get('category')

    if filter_param:
        filter_mappings = {
            'Lower price': Item.price,
            'Higher price': -Item.price,
            'Default': None,
        }
        order_by = filter_mappings.get(filter_param, None)

        if order_by is not None:
            items = db_session.query(Item).order_by(order_by).all()
    if category_param and category_param != 'all':
        items = db_session.query(Item).filter_by(category=category_param).all()

    return render_template('items.html', current_user=current_user, items=items, item_ratings=item_ratings)


@items_blueprint.route('/shop/items/<int:item_id>', methods=['GET'])
def get_items(item_id):
    item = db_session.query(Item).filter_by(id=item_id).all()
    review_id = db_session.query(Feedback).filter_by(item_id=item_id).first()
    return render_template('item_page.html', item=item, review_id=review_id, db=db_session)
