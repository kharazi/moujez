import sqlite3
import datetime
import pickle
import flask
from flask import Flask, render_template, request, jsonify
from src.fetch import Fetch
from services.iran_samane import IranSamane
from services.news_studio import NewsStudio
from services.service import Service
from src.summarize import Summarizer
# from mongoengine import connect


app = Flask(__name__)
# connect('moujez')

def connect_db():
    return sqlite3.connect("log.db")

@app.before_request
def before_request():
    flask.db = connect_db()

@app.after_request
def after_request(response):
    flask.db.close()
    return response

def query_db(query, args=(), one=False):
    cur = flask.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    flask.db.commit()
    return (rv[0] if rv else None) if one else rv


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/_add_numbers')
def add_numbers():
    summarizer = Summarizer()

    a = request.args.get('a', 0, type=str)
    summarizer = Summarizer()
    # a = u"http://www.asriran.com/fa/news/332468/%D9%BE%DB%8C%D8%A7%D9%85-%D8%B3%DB%8C%D8%AF-%D9%85%D8%AD%D9%85%D8%AF-%D8%AE%D8%A7%D8%AA%D9%85%DB%8C-%D8%A8%D9%87-%DA%A9%D9%86%DA%AF%D8%B1%D9%87-%D9%8A%DA%A9-%D8%AD%D8%B2%D8%A8"
    page = Fetch(a)
    if page.service == 'iransamane':
        service = IranSamane(page.page)
    elif page.service == 'news-studio':
        service = NewsStudio(page.page)
    else:
        service = Service(page.page)

    print "fetching content"
    content = service.fetch_content()
    # print content
    print "end fetching"
    summarized = summarizer.summarize(content)
    print "end summarize"
    res = {
        'summarized': summarized,
        'title': service.fetch_title(),
        'tags': service.fetch_tags(),
        'image': service.fetch_image(),
    }

    # For log
    log = (datetime.datetime.now(), res['title'], content, pickle.dumps(summarized)) 
    query_db('INSERT INTO log VALUES (?,?,?,?)', log)
    # 
    return jsonify(result=res)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
