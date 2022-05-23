from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from models import User

class LoginForm(FlaskForm):  # пишу свою форму поверх базовой формы из фласка
    username = StringField('Имя пользователя: ')
    password = PasswordField('Пароль: ')
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользоват: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    password = StringField('Пароль: ', validators=[DataRequired()])
    password_again = StringField('Повторите пароль: ', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def check_usename(self, username):
        user = User.query.filter_by(username=username.data)
        if user is not None:
            raise ValidationError('Пользователь с таким ником уже зарегистрирован')

    def check_email(self, email):
        user = User.query.filter_by(email=email.data)
        if email is not None:
            raise ValidationError('Пользователь с такой почтой уже зарегистрирован')
