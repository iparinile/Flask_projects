from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)

RSS_FEED = {'mail': 'https://news.mail.ru/rss/main/74/',
            'rambler': 'https://news.rambler.ru/rss/Cheliabinsk/'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="mail"):
    feed = feedparser.parse(RSS_FEED[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
