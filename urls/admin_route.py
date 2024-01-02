from flask import Blueprint, request, render_template, redirect, url_for

from db_requests import load_from_db, update_data_in_db, insert_data_in_db, delete_data_from_db

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.get('/admin/orders')
def admin_orders():
    orders = load_from_db('*', 'Order')
    item_id = load_from_db('*', 'order_itms', )
    return render_template('admin_dashboard.html', orders=orders, item_id=item_id)


@admin_blueprint.route('/admin/orders/<order_id>', methods=['GET', 'POST'])
def change_admin_orders_info(order_id):
    if request.method == 'GET':
        load_from_db('*', 'Order', {'order_id': order_id})
        return render_template('change_order_info.html', order_id=order_id)
    elif request.method == 'POST':
        address = request.form.get('address')
        status = request.form.get('status')
        update_data_in_db('Order', {'address': address, 'status': status}, {'order_id': order_id})
        return redirect(url_for('admin.admin_orders'))


@admin_blueprint.route('/admin/users', methods=['GET', 'POST'])
def admin_users():
    if request.method == 'GET':
        return render_template('admin_user_page.html', users=load_from_db('*', 'User'))
    elif request.method == 'POST':
        user_id = request.form.get('user_id')
        delete_data_from_db('User', 'login', user_id)
        return redirect(url_for('admin.admin_users'))


@admin_blueprint.route('/admin/items', methods=['GET'])
def admin_products():
    return render_template('admin_products.html', items=load_from_db('*', 'Item'))


@admin_blueprint.route('/admin/items/new_item', methods=['POST','GET'])
def admin_products_new():
    if request.method == 'GET':
        return render_template('new_ittem.html', item=request.form.get('id'))
    name = request.form.get('name')
    description = request.form.get('description')
    status = request.form.get('status')
    category = request.form.get('category')
    price = request.form.get('price')
    insert_data_in_db('Item', {'name': name, 'price': price, 'description': description, 'status': status,
                               'category': category})
    return redirect(url_for('admin.admin_products'))


@admin_blueprint.route('/admin/items/<item_id>', methods=['GET', 'POST'])
def admin_products_update(item_id):
    if request.method == 'GET':
        return render_template('change_item_info.html', items=load_from_db('*', 'Item', {'id': item_id}))
    elif request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        status = request.form.get('status')
        category = request.form.get('category')
        price = request.form.get('price')
        update_data_in_db('Item', {'name': name, 'price': price, 'description': description, 'status': status,
                                   'category': category}, {'id': item_id})
        return redirect(url_for('admin.admin_products'))

@admin_blueprint.route('/admin/items/<item_id>/delete', methods=['POST'])
def admin_products_delete(item_id):
    delete_data_from_db('Item', 'id', item_id)
    return redirect(url_for('admin.admin_products'))