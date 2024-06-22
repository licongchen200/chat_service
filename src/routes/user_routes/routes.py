from . import user_bp


@user_bp.route('/users')
def users():
    return "Hello from the user routes!"
