import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from data.Keys.db_session_keys import SqlAlchemyBase


class Keys(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'keys'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    hashed_key = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    powerful = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    who_appointed = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    phone = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    path_log = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    finished_date = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def set_key(self, password):
        self.hashed_key = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_key, password)