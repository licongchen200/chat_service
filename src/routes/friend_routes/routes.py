from . import friend_bp


@friend_bp.route('/friend')
def health():
    print('abc')
    return "ok"


