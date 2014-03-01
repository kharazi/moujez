from flask import Flask, render_template, request, jsonify
# from mongoengine import connect


app = Flask(__name__)
# connect('moujez')


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    return jsonify(result=a + 4)


if __name__ == "__main__":
    app.run()
