from app import db


class User(db.Model):
    """Описание таблицы пользователей в БД"""
    id = db.Column(db.Integer, primary_key=True)  # id - ключ таблицы, хранящий числа, используемый для идентификации
    username = db.Column(db.String(64), unique=True, index=True)  # уникальный юзернейм, по которому можно найти пользователя
    email = db.Column(db.String(120), unique=True, index=True)
    password = db.Column(db.String(256))

