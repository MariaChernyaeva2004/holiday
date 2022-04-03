from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Order, create_session


def get_all_orders():
    session = create_session()
    orders = session.query(Order).all()
    return orders


class DeleteOrderForm(FlaskForm):
    order_list = QuerySelectField("Выберите существующий заказ",
                                   query_factory=get_all_orders,
                                   get_pk=lambda order: order.id,
                                   get_label=lambda order: f'{order.id}-{order.title}')
    submit = SubmitField('Удалить')
