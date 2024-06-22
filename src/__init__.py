from flask import Flask, request
print('src init')
from src.routes.friend_routes import friend_bp



def create_app():
    app = Flask(__name__)
    print('create app')
    app.register_blueprint(friend_bp)
    return app

