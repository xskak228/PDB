import datetime

import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from data.MainBase.db_session_base import SqlAlchemyBase


class Main(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'main'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    phone = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    update = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    powerful = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    who_appointed = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)


class Media(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'media'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    p_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    path = sqlalchemy.Column(sqlalchemy.String, nullable=True)