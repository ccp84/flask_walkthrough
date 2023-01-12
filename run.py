import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/news")
def news():
    data = []
    with open("data/news.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("news.html", news_items=data)


@app.route("/news/<news_id>")
def archive(news_id):
    news = {}
    with open("data/news.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["news_id"] == news_id:
                news = obj
    return render_template("archive.html", news=news)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
