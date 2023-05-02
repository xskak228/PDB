from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):

    powerful = StringField('Уровень аккаунта', validators=[DataRequired()])
    who_appointed = StringField("Куратор ключа", validators=[DataRequired()])

    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])

    phone = StringField('Телефон', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])

    finished_date = StringField('Дата окончания действия ключа', validators=[DataRequired()])

    submit = SubmitField('Зарегистрировать ключ')