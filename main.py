from flask import Flask

app = Flask(__name__)


def urlMaker(query: str):
    # check if query is string

    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    return url


@app.get('/<query>')
def getURL(query):
    return urlMaker(query)
