from urllib.parse import urlparse
import json
from bottle import Bottle, run, request, response
from PyCli.client import get

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
    link = urlparse(playlist["playlist"])
    host = link.hostname
    path = link.path + "?" + link.query

    if host == None or path == None:
        response.body = "That link is dogwater"
        response.status = 200
        return response
    if host != "www.youtube.com":
        response.body = "Playlist needs to be a public or unlisted YouTube playlist"
        response.status = 200
        return response
    
    d = get(playlist["playlist"], None)
    data = d[1]

    songs = []
    chunks = data.split("\"")
    for line in chunks:
        if "/watch?" in line and "index" in line:
            songs.append("https://" + host + line)

    if len(songs) > 0:
        response.add_header("Content-Type", "application/json")
        response.body = json.dumps(songs)
    else:
        response.body = "No songs found in playlist"

    response.status = 200
    return response


run(app, host="", port=8080)