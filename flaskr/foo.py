# This is my playground file.
# <from dir flask-tutorial> flask --app flaskr run --debug


from flask import Blueprint


bp = Blueprint(
    name='foo',
    import_name=__name__,
    url_prefix='/foo'
)


@bp.route('/<placeholder>', methods=['GET'])
def one(placeholder):
    return f'This is {placeholder}.'
