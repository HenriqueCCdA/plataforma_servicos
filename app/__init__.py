import os

from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy.pool import QueuePool

from config import app_config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(engine_options={"pool_size": 10, "poolclass":QueuePool, "pool_pre_ping":True})
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.session_protection = 'strong'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)

    migrate.init_app(app, db)
    login.init_app(app)

    # diretorio para salvar os arquivos
    top_level_dir = os.path.abspath(os.curdir)
    upload_folder = top_level_dir
    app.config['UPLOAD_FOLDER'] = upload_folder

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/main')

    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app


from .models import usuario_model
