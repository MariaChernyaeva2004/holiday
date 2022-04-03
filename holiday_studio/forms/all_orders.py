from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Order, create_session


def get_all_orders():
    session = create_session()
    orders = session.query(Order).all()
    return orders


class AllOrdersForm(FlaskForm):
    order_list = QuerySelectField("ЗАКАЗЫ",
                                  query_factory=get_all_orders,
                                  get_pk=lambda order: order.id,
                                  get_label=lambda order: order.title)
