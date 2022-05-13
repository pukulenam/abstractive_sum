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

        # summarized='Intinya... '+str(news_text)
        
        # new_news = News(inputNews=news_text,summarizedNews=summarized)

        try:
            # return news_text
            # db.session.add(new_news)
            # db.session.commit()
            
            
            # return render_template('index.html', news_text=news_text,summarized=summarized)
            

            # Test AI Platform 

            
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "pukulenam-test-24bfaa30d863.json" # Ask JSON file to achmad nofandi
            PROJECT = "pukulenam-test" # change for your GCP project
            REGION = "us-central1" # change for your GCP region (where your model is hosted)
            MODEL = 'test'

            payload=[news_text]
            output = predict_json(PROJECT,REGION,MODEL,payload)
            str_output = ' '.join(map(str, output))
            new_news = News(inputNews=news_text,summarizedNews=str_output)
            db.session.add(new_news)
            db.session.commit()
            return render_template('index.html',news_text=news_text,summarized=str_output)


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

import googleapiclient.discovery
import json
from google.api_core.client_options import ClientOptions

service = googleapiclient.discovery.build('ml', 'v1')

def predict_json(project, region, model, instances, version=None):
    """Send json data to a deployed model for prediction.

    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        region (str): regional endpoint to use; set to None for ml.googleapis.com
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to tensors.
        version: str, version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the
            model.
    """
    # Create the ML Engine service object.
    # To authenticate set the environment variable
    # GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
    prefix = "{}-ml".format(region) if region else "ml"
    api_endpoint = "https://{}.googleapis.com".format(prefix)
    client_options = ClientOptions(api_endpoint=api_endpoint)
    service = googleapiclient.discovery.build(
        'ml', 'v1', client_options=client_options)
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']


if __name__ == "__main__":
    app.run(debug=True)


