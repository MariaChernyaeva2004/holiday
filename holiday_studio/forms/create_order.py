from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FloatField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField

from models import Client, create_session


def get_all_clients():
    session = create_session()
    clients = session.query(Client).all()
    return clients


class CreateOrderForm(FlaskForm):
    title = StringField("Название заказа", validators=[DataRequired()])
    price = FloatField("Цена заказа", validators=[DataRequired()])
    describtion = StringField("Описание заказа", validators=[DataRequired()])
    client_list = QuerySelectField("Клиент",
                                   query_factory=get_all_clients,
                                   get_pk=lambda client: client.id,
                                   get_label=lambda client: client.full_name)
    submit = SubmitField("Создать")
