from flask import Flask, jsonify, redirect, render_template, request, send_from_directory,url_for, request,make_response,abort , session, flash
import pandas as pd
import os
import json
from flask_restful import Resource, Api, reqparse
from preprocess import predict
from functools import wraps

app = Flask(__name__)
app.secret_key = 'pukulenam'
api = Api(app)


def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        f = open("key", "r")
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == f.read():
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

# API
   
class Summarize(Resource):
    @require_appkey
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('news')
        args = parser.parse_args()
        # return args.news
        try:
            
            output = predict(args.news)
            return jsonify({'summarized': output})


        except Exception as e:
            # return 'There was an issue summarizing your news : '+str(e)
            return jsonify({'message':str(e)})

        
@app.route('/')
def home():

    return '<h1>Abstractive Summarization</h1>'
    # @app.route('/api/summarize')
    # def api_page():

    #     return '<h1>API Page</h1>'

    
api.add_resource(Summarize, '/api/summarize')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))