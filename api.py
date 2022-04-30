from urllib.parse import urlparse
import json
from bottle import Bottle, run, request, response
from PyCli.client import get
from helpers.playlist import linkcheck, playlistsplit

app = Bottle()

@app.get("/")
def statuscheck():
    response.status = 200
    response.body = "Ya boi"
    return response

@app.post("/playlist")
def playlistHandler():
    rawpl = request.body.read().decode()

    playlist = json.loads(rawpl)
    link = playlist["playlist"]
    error = linkcheck(link)

    if error != None:
        response.body = error
        response.status = 200
        return response
    
    d = get(link, None)

    songs = playlistsplit(d[1])

    if len(songs) > 0:
        response.add_header("Content-Type", "application/json")
        response.body = json.dumps(songs)
    else:
        response.body = "No songs found in playlist"

    response.status = 200
    return response


run(app, host="", port=8080)