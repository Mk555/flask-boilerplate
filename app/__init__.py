import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from flask_login import LoginManager


# Init objects
db = SQLAlchemy()
login_manager = LoginManager()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    # Loading module Base
    base_module = import_module('app.base.routes')
    app.register_blueprint(base_module.blueprint)
    # Loading the example module
    base_module = import_module('app.module_example.routes')
    app.register_blueprint(base_module.blueprint)
    

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def config_app(app):
    app.config.update(
        # App config
        TESTING=True,
        SECRET_KEY=b'QP=!a/n778Pk~V6/',
        # DB config
        SQLALCHEMY_DATABASE_URI='sqlite:////'+ os.path.abspath(os.getcwd()) + '/db.sqlite3',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    

def create_app():
    app = Flask(__name__, static_folder='base/static')
    config_app(app)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app