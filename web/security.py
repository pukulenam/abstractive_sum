from functools import wraps
from flask import request, abort


# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        key=result=Key.query.get_or_404(1)
        #if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function



# @app.route('/json/', methods=['POST'])
# @require_appkey
# def put_user():
#     return 'Posted JSON!'

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# app.run(host='127.0.0.1',port='443', debug = False/True, ssl_context=context)