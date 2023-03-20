from app.api.v1 import bp


@bp.route('get_test/')
def test():
    return 'hello v1'
