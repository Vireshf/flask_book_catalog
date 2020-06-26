import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_migrate import Migrate

db = SQLAlchemy()
bootstrap = Bootstrap()
bcrypt = Bcrypt()
loginmanager = LoginManager()
#loginmanager.login_view = "authentication.do_the_login_admin"
loginmanager.login_view = "authentication.do_the_login"
loginmanager.session_protection = 'strong'
# migrate = Migrate()



def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    db.init_app(app)
    # migrate.init_app(app, db)
    bootstrap.init_app(app)
    bcrypt.init_app(app)
    loginmanager.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app



