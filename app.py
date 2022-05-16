from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)  # подключаю настройки сайта
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


from routes import *
from models import *


if __name__ == '__main__':
    app.run()
