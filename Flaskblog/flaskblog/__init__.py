from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users. login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    app.app_context().push()
    mail.init_app(app)

    from flaskblog.users.routes import users
    app.register_blueprint(users)
    from flaskblog.posts.routes import posts
    app.register_blueprint(posts)
    from flaskblog.main.routes import main
    app.register_blueprint(main)

    return app
