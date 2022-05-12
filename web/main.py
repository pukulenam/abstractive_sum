from email.mime import base
from flask import Flask, render_template, request, send_from_directory,url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inputNews = db.Column(db.Text, nullable=False)
    summarizedNews = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<News {self.id}>'


@app.route("/", methods=['POST','GET'])
def home():
    if request.method == 'POST':
        news_text = request.form['inputNews']

        summarized='Intinya... '+str(news_text)
        
        new_news = News(inputNews=news_text,summarizedNews=summarized)

        try:
            # return news_text
            db.session.add(new_news)
            db.session.commit()
            
            # return redirect('/')
            return render_template('index.html', news_text=news_text,summarized=summarized)
        except:
            return 'There was an issue summarizing your news'

    else:
        # tasks = News.query.order_by(News.id).all()
        return render_template('index.html')
@app.route('/submit',methods=['POST','GET'] )
def submit():
    return "<p>Hello, World!</p>"
    # return render_template('asd.html')

@app.route('/history')
def history():
    query_news=News.query.order_by(News.id.desc())

    return render_template('history.html', news=query_news)

@app.route('/export')
def export():
    basedir = os.path.abspath(os.path.dirname(__file__))
    sql_engine = create_engine(os.path.join('sqlite:///' + os.path.join(basedir, 'news.db')), echo=False)
    results = pd.read_sql_query('select * from News',sql_engine)
    results.to_csv(os.path.join(basedir, 'exported.csv'),index=False,sep=",")

    # return 'sukses'
    return send_from_directory(basedir,'exported.csv')
    
@app.route('/<int:id>')
def home_(id):
    result=News.query.get_or_404(id)

    return render_template('index.html', news=result)
    # return send_from_directory(basedir,'exported.csv')


if __name__ == "__main__":
    app.run(debug=True)


