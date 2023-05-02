import datetime

from flask import Flask, redirect, render_template

from data.GenerateKey import GenerateKeys
from data.Keys import db_session_keys
from data.Keys.keys import Keys
from data.MainBase import db_session_base
from data.MainBase.base import Main
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from forms.LoginForm import LoginForm
from forms.RegisterForm import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PeopleDataBase_secretkey'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=1)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session_keys.create_session()
    return db_sess.query(Keys).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session_keys.create_session()
        user = db_sess.query(Keys).filter(Keys.email == form.Email.data).first()
        if user and user.check_password(form.Key.data):
            login_user(user)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильная почта или неверный ключ!",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated and current_user.powerful <= 2:
        form = RegisterForm()
        db_sess = db_session_keys.create_session()
        if form.validate_on_submit():
            user = Keys(
                powerful=form.powerful.data,
                who_appointed=form.who_appointed.data,
                surname=form.surname.data,
                name=form.name.data,
                phone=form.phone.data,
                email=form.email.data,
                finished_date=form.finished_date.data

            )
            user.set_key(GenerateKeys())
            db_sess.add(user)
            db_sess.commit()
        return render_template("register.html", title='Регистрация ключа', form=form)
    return """У вас нет такой возможности. <a href="/">Гл. страница</a>"""


@app.route('/')
def index():
    if not current_user.is_authenticated:
        return """Привет, ты на сайте 'БД', но ты не залогинен, пожалуйста, залогинся:
        <a href="login">Войти</a>"""
    return "ТУТ ничего НЕЕЕЕТ!, покачто..."


def main():
    db_session_base.global_init("db/base.db")
    db_session_keys.global_init("db/keys.db")

    # tes_bd()

    app.run()


def tes_bd():
    keys = Keys()
    keys.powerful = 1
    keys.who_appointed = 1
    keys.surname = "TEST1"
    keys.name = "TEST2"
    keys.phone = "1(234) 567 89-10"
    keys.email = "test@mail.com"
    keys.set_key("TEST1234")
    db_sess_1 = db_session_keys.create_session()

    base = Main()
    base.key = "wWdaDA2D2daWA2809p"
    db_sess_2 = db_session_base.create_session()

    db_sess_1.add(keys)
    db_sess_2.add(base)
    db_sess_1.commit()
    db_sess_2.commit()


if __name__ == '__main__':
    main()
