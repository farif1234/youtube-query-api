from flask import Flask

app = Flask(__name__)


def youtubeQuery(query: str):
    # print(query)
    # characters not encoded = [@,#,$,%,&,=,+,;,:,,,?,/]
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    return url


def spotifyQuery(query: str):
    url = f"https://open.spotify.com/search/{query.replace(' ', '%20')}"
    return url


@app.get('/youtube/<query>')
def getYtURL(query):
    return youtubeQuery(query)


@app.get('/spotify/<query>')
def getSpURL(query):
    return spotifyQuery(query)
