import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from data.MainBase.db_session_base import SqlAlchemyBase


class Main(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'main'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    key = sqlalchemy.Column(sqlalchemy.String, nullable=False)
