from flask import Flask, jsonify, redirect, render_template, request, send_from_directory,url_for, request,make_response,abort , session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import os
import googleapiclient.discovery
import json
import requests
from google.api_core.client_options import ClientOptions
from flask_restful import Resource, Api, reqparse
import secrets
from flask_marshmallow import Marshmallow
from functools import wraps
from datetime import datetime   
from difflib import SequenceMatcher

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.secret_key = 'pukulenam'
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inputNews = db.Column(db.Text, nullable=False)
    summarizedNews = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<News {self.id}>'


class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    masterPassword = db.Column(db.String, nullable=False)
    apiKey = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Key {self.id}>'

class NewsSchema(ma.Schema):
   class Meta:
        fields = ('id', 'inputNews', 'summarizedNews')
    

@app.route("/", methods=['POST','GET'])
def home():
    if request.method == 'POST':
        news_text = request.form['inputNews']

        try:
            # caching news from db before call predict endpoint
            query_news=News.query.order_by(News.id)

            for _news in query_news:
                compare = SequenceMatcher(None, _news.inputNews, news_text)
                if compare.ratio() > 0.95:
                    return render_template('index.html',news_text=news_text,summarized=_news.summarizedNews)

            # call predict endpoint
            url = "https://predictapi-ntklgukjta-uc.a.run.app/api/summarize"

            payload = json.dumps({
            "news": news_text
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            json_data = json.loads(response.text)
            new_news = News(inputNews=news_text,summarizedNews=json_data["summarized"])
            db.session.add(new_news)
            db.session.commit()
            return render_template('index.html',news_text=news_text,summarized=json_data["summarized"])


        except Exception as e:
            return 'There was an issue summarizing your news : '+str(e)

    else:
        return render_template('index.html')


@app.route('/history')
def history():
    query_news=News.query.order_by(News.id)

    return render_template('history.html', news=query_news,status='')

@app.route('/export', methods=['POST'])
def export():


    list_id = request.form.getlist('list_array[]')
    if len(list_id)<1:
        query_news=News.query.order_by(News.id)
        flash('You have to check the news that you want to export',"danger")
        return render_template('history.html',news=query_news)
    else:
        try:
            basedir = os.path.abspath(os.path.dirname(__file__))
            dir = os.path.join(basedir,'exported')
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
                
            sql_engine = create_engine(os.path.join('sqlite:///' + os.path.join(basedir, 'news.db')), echo=False)
            query= 'SELECT * FROM News WHERE id IN ('+(','.join([str(elem) for elem in list_id]))+')'
            results = pd.read_sql_query(query,sql_engine)
            name = 'exported/'+datetime.now().strftime('%d-%m-%Y %H.%M ')+'news.csv'
            results.to_csv(os.path.join(basedir,name),index=False,sep=",")
            return send_from_directory(basedir, name)   
        except:

            basedir = os.path.abspath(os.path.dirname(__file__))
            sql_engine = create_engine(os.path.join('sqlite:///' + os.path.join(basedir, 'news.db')), echo=False)
            query= 'SELECT * FROM News WHERE id IN ('+(','.join([str(elem) for elem in list_id]))+')'
            results = pd.read_sql_query(query,sql_engine)
            name = 'exported/'+datetime.now().strftime('%d-%m-%Y %H.%M ')+'news.csv'
            results.to_csv(os.path.join(basedir,name),index=False,sep=",")
            return send_from_directory(basedir, name)   
       



@app.route('/<int:id>')
def home_(id):
    result=News.query.get_or_404(id)

    return render_template('index.html', news=result,state='view')

@app.route('/delete/<int:id>')
def delete(id):
    try:
        result=News.query.get_or_404(id)
        db.session.delete(result)
        db.session.commit()  
        flash('News deleted successfully',"success")
        return redirect('/history')
    except Exception as e:
        # return 'There was an issue deleting your news : '+str(e)
        query_news=News.query.order_by(News.id)
        flash(str(e),"danger")
        return render_template('history.html', status=str(e),news=query_news)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method=='GET':
        try:
            result=News.query.get_or_404(id)
            
            return render_template('index.html', state='edit',news=result)
        except Exception as e:
            flash(str(e),"danger")
            query_news=News.query.order_by(News.id)    
            return render_template('history.html', status=str(e),news=query_news)

    else:
        result=News.query.get_or_404(id)
        news_text = request.form['inputNews']
        summarized_news = request.form['outputNews']
        result.inputNews=news_text
        result.summarizedNews=summarized_news
        try:
            db.session.commit()
            flash('Changes saved successfully',"success")
            return redirect('/history')
        except Exception as e:    
            return 'There was an issue updating your news : '+str(e)






def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        key=Key.query.get_or_404(1)
        #if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key.apiKey:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

def require_passkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        key=Key.query.get_or_404(1)
        #if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key.masterPassword:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

# API

class Security(Resource):


    @require_passkey
    def put(self):
        query = Key.query.get_or_404(1)
        query.apiKey=secrets.token_hex(16)
        db.session.commit()
        return jsonify({'key':query.apiKey})

    # def post(self):
    #     try:
    #         newKey = Key(masterPassword='pukulenam',apiKey=secrets.token_hex(16))
    #         db.session.add(newKey)
    #         db.session.commit()
    #         return {'status' : 'Success'}
    #     except Exception as e:
    #         return {'status': str(e)}
    
class Summarize(Resource):
    @require_appkey
    def get(self):
        query_news=News.query.order_by(News.id)
        news = NewsSchema(many=True).dump(query_news)
        return jsonify({'history': news})

    @require_appkey
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('news')
        args = parser.parse_args()

        try:

            # caching news from db before call predict endpoint
            query_news=News.query.order_by(News.id)

            for _news in query_news:
                compare = SequenceMatcher(None, _news.inputNews, args.news)
                if compare.ratio() > 0.95:
                    return jsonify({'summarized': _news.summarizedNews})

            # call predict endpoint
            url = "https://predictapi-ntklgukjta-uc.a.run.app/api/summarize"

            payload = json.dumps({
            "news": args.news
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            json_data = json.loads(response.text)
            new_news = News(inputNews=args.news,summarizedNews=json_data["summarized"])
            db.session.add(new_news)
            db.session.commit()
        
            return jsonify({'summarized': json_data["summarized"]})


        except Exception as e:
            # return 'There was an issue summarizing your news : '+str(e)
            return jsonify({'message':str(e)})
        

    
api.add_resource(Security, '/api/security')
api.add_resource(Summarize, '/api/summarize')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


