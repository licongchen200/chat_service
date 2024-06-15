from flask import Flask, request
from src.chat import get_message
from src.user import get_user
app = Flask(__name__)


@app.route('/health')
def health():
    return "ok"


@app.route('/user')
def user():
    return get_user()


@app.route('/message')
def message():
    id = request.args.get('id', default=1, type=int)
    count = request.args.get('count', default=10, type=int)
    return get_message(id, count)

if __name__ == "__main__":
    app.run(debug=True, port=8081, host='0.0.0.0')
