from celery import Celery
from data_base import db_session
from models.item import Item
from models.order import Order
from models.orderitms import Orderitms
from models.user import User
from utills import send_email_to_user

app = Celery('task', broker='pyamqp://celeryuser:celeryuser@rabbitmq:5672//')
app.conf.broker_connection_retry_on_startup = True


@app.task
def send_email(user_login, order_id):
    user = db_session.query(User).filter_by(login=user_login).first()
    email = user.email

    order = Order.query.filter_by(id=order_id).first()
    order_total_price = order.order_total_price

    order_items = db_session.query(Item, Orderitms).join(Item, Item.id == Orderitms.item_id).where(
        Orderitms.order_id == order_id).all()
    items_name = [item[0].to_dict().get('name') for item in order_items]

    message = f'Thank you for your order nr{order_id}! Your total price is ${order_total_price}.'
    message += f'\nHere are the items in your order: {",".join(items_name)}.'

    send_email_to_user(email, message)
