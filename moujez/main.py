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
    summarizer = Summarizer()
    
    a = request.args.get('a', 0, type=str)
    summarizer = Summarizer()
    # a = u"http://www.asriran.com/fa/news/332468/%D9%BE%DB%8C%D8%A7%D9%85-%D8%B3%DB%8C%D8%AF-%D9%85%D8%AD%D9%85%D8%AF-%D8%AE%D8%A7%D8%AA%D9%85%DB%8C-%D8%A8%D9%87-%DA%A9%D9%86%DA%AF%D8%B1%D9%87-%D9%8A%DA%A9-%D8%AD%D8%B2%D8%A8"
    page = Fetch(a)
    if page.service == 'iransamane':
        service = IranSamane(page.page)
    elif page.service == 'news-studio':
        service = NewsStudio(page.page)

    print "fetching content"
    content = service.fetch_content()
    print "end fetching"
    summarized = summarizer.summarize(content)
    print "end summarize"
    res = {
        'summarized': summarized,
        'title': service.fetch_title(),
        'tags': service.fetch_tags(),
    }
    return jsonify(result= res)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
