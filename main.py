from flask import Flask

app = Flask(__name__)


def urlMaker(query: str):
    # print(query)
    # characters not encoded = [@,#,$,%,&,=,+,;,:,,,?,/]
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    return url


@app.get('/youtube/<query>')
def getURL(query):
    return urlMaker(query)
