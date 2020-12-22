from flask import Flask
import feedparser

app = Flask(__name__)

RSS_FEED = {'mail': 'https://news.mail.ru/rss/main/74/',
            'rambler': 'https://news.rambler.ru/rss/Cheliabinsk/'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="mail"):
    feed = feedparser.parse(RSS_FEED[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1> Заголовки </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>
    </html> """.format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
