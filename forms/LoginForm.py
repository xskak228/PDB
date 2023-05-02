from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    Email = EmailField('Почта', validators=[DataRequired()])
    Key = StringField('Ключ', validators=[DataRequired()])
    submit = SubmitField('Войти')