from flask import Flask
from .routes import animal_blueprint
from .errors import register_error_handlers


def create_app():
    app = Flask(__name__)
    app.register_blueprint(animal_blueprint, url_prefix='/api')
    register_error_handlers(app)
    return app
