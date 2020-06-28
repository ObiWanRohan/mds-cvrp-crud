import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from config import Config
__version__ = 'v0.0.1'


db = SQLAlchemy()
migrate = Migrate()
cache = Cache()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    from app.api.v0_1 import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v0.1')

    return app
