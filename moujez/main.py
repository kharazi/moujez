from flask import Flask, render_template, request, jsonify
from src.fetch import Fetch
from services.iran_samane import IranSamane
from services.news_studio import NewsStudio
from src.summarize import Summarizer
# from mongoengine import connect


app = Flask(__name__)
# connect('moujez')


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=str)
    print a
    page = Fetch(a)
    print "service", page.service
    if page.service == 'iransamane':
        service = IranSamane(page.page)
    elif page.service == 'news-studio':
        service = NewsStudio(page.page)
    else:
        return jsonify(result='bad request')

    # resutl = service.fe
    content = service.fetch_content()
    summarizer = Summarizer()
    print "salaaaaaaaaam"
    summarizer.summariz(content)
    print "khodaaaaaafez"
    return jsonify(result= unicode("fuck"))


if __name__ == "__main__":
    app.run()
