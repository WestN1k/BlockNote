from flask import Flask
from flask_migrate import Migrate

from config import Config
from app.api.v1 import bp as v1_bp
from app.extentions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    migrate = Migrate(app, db)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(v1_bp, url_prefix='/api/v1/')
    return app
