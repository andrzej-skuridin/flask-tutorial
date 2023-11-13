# This is my playground file.
# <from dir flask-tutorial> flask --app flaskr run --debug


from flask import Blueprint


bp = Blueprint(
    name='foo',
    import_name=__name__,
    url_prefix='/foo'
)


@bp.route('/<placeholder>', methods=['GET'])
def one(placeholder=None):
    return f'This is {placeholder}.'


@bp.route('/', methods=['GET'])
def two():
    return f'This is {__name__}.'
