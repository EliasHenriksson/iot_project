from flask import Flask
from app import api_bp
from Model import db


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(api_bp, url_prefix='/api')
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run()
