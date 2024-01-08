from flask import Blueprint, request, session, render_template, url_for, redirect

from db_requests import load_from_db, update_data_in_db, insert_data_in_db

items_blueprint = Blueprint('item', __name__)


@items_blueprint.route('/shop/items/<int:item_id>/review', methods=['GET', 'POST'])
def create_read_reviews(item_id):
    session_user = session.get('login')
    current_user = None
    if session_user:
        current_user = load_from_db('*', 'User', {'login': session_user})[0][0]
    if request.method == 'GET':
        reviews = load_from_db('*', 'feedback', {'item_id': item_id})
        return render_template('reviews.html', reviews=reviews, item_id=item_id, current_user=current_user)
    elif request.method == 'POST':
        review = request.form.get('review-text')
        rating = request.form.get('rating')
        insert_data_in_db('feedback',
                          {"item_id": item_id, 'text': review, 'rating': rating, 'user_login': current_user})

    return redirect(url_for('item.create_read_reviews', item_id=item_id))


@items_blueprint.route('/shop/items/<item_id>/review/<review_id>', methods=['GET', 'POST'])
def full_review(item_id, review_id):
    if request.method == 'GET':
        review = load_from_db('*', 'feedback', {'feedback_id': review_id})[0]
        return render_template('full_review.html', review=review, item_id=item_id)
    elif request.method == 'POST':
        review = request.form.get('review')
        rating = request.form.get('rating')
        session_user = session.get('login')
        current_user = load_from_db('*', 'User', {'login': session_user})[0][0]
        update_data_in_db('feedback',
                          {'feedback_id': review_id, 'text': review, 'rating': rating, 'user_login': current_user},
                          {'feedback_id': review_id})
        return redirect(url_for('item.create_read_reviews', item_id=item_id))


@items_blueprint.route('/shop/items', methods=['GET'])
def items_page():
    session_user = session.get('login')
    current_user = None
    if session_user:
        current_user = load_from_db('*', 'User', {'login': session_user})[0]
    items = load_from_db('*', 'Item')

    return render_template('items.html', current_user=current_user, items=items)


@items_blueprint.route('/shop/items/<int:item_id>', methods=['GET'])
def get_items(item_id):
    # item_id is now a parameter from the URL, no need to get it from form
    item = load_from_db('*', 'Item', {'id': item_id})
    review_id = load_from_db('feedback_id', 'feedback', {'item_id': item_id})
    return render_template('item_page.html', item=item, review_id=review_id)
