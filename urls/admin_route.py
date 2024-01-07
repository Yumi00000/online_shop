from flask import Blueprint, request, render_template, redirect, url_for

from app import db
from db_requests import delete_data_from_db
from models.item import Item
from models.order import Order
from models.user import User

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.get('/admin/orders')
def admin_orders():
    order = db.session.query(Order).all()
    return render_template('admin_dashboard.html', order=order)


@admin_blueprint.route('/admin/orders/<order_id>', methods=['GET'])
def get_admin_orders_info(order_id):
    order = db.session.query(Order).filter_by(order_id=order_id).first()
    return render_template('change_order_info.html', order=order)


@admin_blueprint.route('/admin/orders/<order_id>', methods=['POST'])
def update_admin_orders_info(order_id):
    order = db.session.query(Order).filter_by(order_id=order_id).first()

    if order:
        order.address = request.form['address']
        order.status = request.form['status']
        db.session.commit()

    return redirect('/admin/orders')


@admin_blueprint.route('/admin/users', methods=['GET', 'POST'])
def admin_users():
    if request.method == 'GET':
        return render_template('admin_user_page.html', users=db.session.query(User).all())
    elif request.method == 'POST':
        user_id = request.form['user_id']
        db.session.delete(db.session.query(User).filter_by(login=user_id).first())
        db.session.commit()
        return redirect(url_for('admin.admin_users'))


@admin_blueprint.route('/admin/items', methods=['GET'])
def admin_products():
    return render_template('admin_products.html', items=db.session.query(Item).all())


@admin_blueprint.route('/admin/items/new_item', methods=['POST', 'GET'])
def admin_products_new():
    if request.method == 'GET':
        return render_template('new_item.html')

    name = request.form['name']
    description = request.form['description']
    status = request.form['status']
    category_name = request.form['category']
    price = request.form['price']

    new_item = Item(name=name, price=price, description=description, status=status, category=category_name)

    db.session.add(new_item)
    db.session.commit()

    return redirect(url_for('admin.admin_products'))


@admin_blueprint.route('/admin/items/<item_id>', methods=['GET', 'POST'])
def admin_products_update(item_id):
    item = db.session.query(Item).filter_by(id=item_id).first()

    if request.method == 'GET':
        return render_template('change_item_info.html', item=item)
    elif request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        item.status = request.form['status']
        item.category = request.form['category']
        item.price = request.form['price']
        db.session.commit()
        return redirect(url_for('admin.admin_products'))


@admin_blueprint.route('/admin/items/<item_id>/delete', methods=['POST'])
def admin_products_delete(item_id):
    db.session.delete(db.session.query(Item).filter_by(id=item_id).first())
    db.session.commit()
    return redirect(url_for('admin.admin_products'))