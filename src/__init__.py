from flask import Flask, request
print('src init')
from src.routes.friend_routes import friend_bp
from src.routes.user_routes import user_bp



def create_app():
    app = Flask(__name__)
    print('create app')
    app.register_blueprint(friend_bp)
    app.register_blueprint(user_bp)
    return app

