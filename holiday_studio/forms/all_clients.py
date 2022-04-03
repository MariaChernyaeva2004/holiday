from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FloatField, SelectField
from wtforms.validators import DataRequired, optional
from wtforms_sqlalchemy.fields import QuerySelectField

from models import Client, create_session


def get_all_clients():
    session = create_session()
    clients = session.query(Client).all()
    return clients


class AllClientsForm(FlaskForm):
    client_list = QuerySelectField("КЛИЕНТЫ",
                                   query_factory=get_all_clients,
                                   get_pk=lambda client: client.id,
                                   get_label=lambda client: client.full_name)