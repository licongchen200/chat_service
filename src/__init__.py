from flask import Flask, request
from src.routes.friend_routes import friend_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(friend_bp)
    return app
