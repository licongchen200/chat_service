from . import friend_bp


@friend_bp.route('/friend')
def health():
    return "ok"


