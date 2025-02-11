from flask import Flask
from ui import routes
from config import Config


def create_app() -> Flask:
    app = Flask(import_name=__name__)
    app.config.from_object(obj=Config)
    app.register_blueprint(blueprint=routes.bp)

    return app
