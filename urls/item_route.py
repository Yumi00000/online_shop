from flask import Blueprint, render_template, request, session, redirect, url_for
from app import db
from models.item import Item
from models.feedback import Feedback
from models.user import User

items_blueprint = Blueprint('item', __name__)

@items_blueprint.route('/shop/items/<int:item_id>/review', methods=['GET', 'POST'])
def create_read_reviews(item_id):
    session_user = session.get('login')
    current_user = User.query.filter_by(login=session_user).first() if session_user else None

    if request.method == 'GET':
        reviews = Feedback.query.filter_by(item_id=item_id).all()
        return render_template('reviews.html', reviews=reviews, item_id=item_id, current_user=current_user)
    elif request.method == 'POST':
        review_text = request.form.get('review-text')
        rating = request.form.get('rating')
        feedback = Feedback(item_id=item_id, text=review_text, rating=rating, user=current_user)
        db.session.add(feedback)
        db.session.commit()

    return redirect(url_for('item.create_read_reviews', item_id=item_id))

@items_blueprint.route('/shop/items/<int:item_id>/review/<int:review_id>', methods=['GET', 'POST'])
def full_review(item_id, review_id):
    if request.method == 'GET':
        review = Feedback.query.filter_by(feedback_id=review_id).first()
        return render_template('full_review.html', review=review, item_id=item_id)
    elif request.method == 'POST':
        review_text = request.form.get('review')
        rating = request.form.get('rating')
        session_user = session.get('login')
        current_user = User.query.filter_by(login=session_user).first()
        feedback = Feedback.query.filter_by(feedback_id=review_id).first()
        feedback.text = review_text
        feedback.rating = rating
        feedback.user = current_user
        db.session.commit()
        return redirect(url_for('item.create_read_reviews', item_id=item_id))

@items_blueprint.route('/shop/items', methods=['GET'])
def items_page():
    session_user = session.get('login')
    current_user = User.query.filter_by(login=session_user).first() if session_user else None
    items = Item.query.all()
    return render_template('items.html', current_user=current_user, items=items)

@items_blueprint.route('/shop/items/<int:item_id>', methods=['GET'])
def get_items(item_id):
    item = Item.query.filter_by(id=item_id).first()
    reviews = Feedback.query.filter_by(item_id=item_id).all()
    return render_template('item_page.html', item=item, reviews=reviews)
