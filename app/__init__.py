from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.landing import bp as landing_bp
    app.register_blueprint(landing_bp)

    return app
