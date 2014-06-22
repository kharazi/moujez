import sqlite3
import datetime
import pickle
import random
import flask
from sets import Set
from flask import Flask, render_template, request, jsonify, redirect
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

@app.route("/get_form", methods=['POST'])
def get_form():
    print "get"
    log_id = request.form['log_id']
    query_db(
        "INSERT INTO question_game_result VALUES (?,?,?,?,?,?,?,?)", 
        [log_id, request.form["name"], request.form["11"], request.form["12"],
        request.form["21"], request.form["22"], request.form["31"], request.form["32"]
        ]
        )
    print request.form['name']
    return redirect('/')
    

@app.route('/_add_numbers')
def add_numbers():

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
    query_db('INSERT INTO log (submitted_time, title, source, summarized_text) VALUES (?,?,?,?)', log)
    # 
    return jsonify(result=res)


@app.route('/evaluation/1')
def evaluation_1():
    random_number = random.randint(1, 1)
    news = query_db("SELECT * FROM log WHERE log_id = ?", 
        [random_number], one=True)
    questions = query_db(
        "SELECT * FROM questions_table WHERE news_id = ?",
        [random_number], one=True
        )
    print "news is", questions
    news["summarized_text"] = pickle.loads(news["summarized_text"])
    return render_template('evaluation.html', news=news, questions=questions)


@app.route('/result')
def result():
    news = query_db("SELECT * FROM question_game_result")
    return render_template('result.html', news=news)

@app.route('/keyword')
def keyword_evaluation():
    logs = query_db("SELECT * FROM log")
    precision_sum = 0
    recall_sum = 0
    counter = 0
    for log in logs:
        counter += 1
        a = Set(extract_keyword(log["source"])) 
        b = Set(extract_keyword(log["summarized_text"]))
        t = a & b
        precision = len(t) / len(b)
        recall = len(t) / len(a)
        precision_sum += precision
        recall_sum += recall

    p = precision_sum / counter
    r = recall_sum / counter
    print p, r
    return "salam"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
