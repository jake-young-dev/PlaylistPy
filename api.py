import json
from bottle import Bottle, run, request, response
from PyCli.client import get
from helpers.playlist import linkcheck, playlistsplit, getallplaylists, getaplaylist

#creat bottle app
app = Bottle()

#status endpoint
@app.get("/")
def statuscheck():
    response.status = 200
    response.body = "Ya boi"
    return response

#get list of saved playlists
@app.get("/playlists")
def showplaylists():
    playlists = getallplaylists()
    response.add_header("Content-Type", "application/json")
    response.body = json.dumps(playlists)
    response.status = 200
    return response

#gets songs of playlist <name>
@app.get("/playlist/<name>")
def getplaylist(name):
    playlist = getaplaylist(name)
    response.add_header("Content-Type", "application/json")
    response.body = json.dumps(playlist)
    response.status = 200
    return response

#returns a list of songs in playlist 
@app.post("/playlist")
def playlisthandler():
    rawpl = request.body.read().decode()

    playlist = json.loads(rawpl)
    link = playlist["playlist"]
    error = linkcheck(link)

    if error != None:
        response.body = error
        response.status = 200
        return response
    
    d = get(link, None)

    if d[0] == 200:
        songs = playlistsplit(d[1])

        if len(songs) > 0:
            response.add_header("Content-Type", "application/json")
            response.body = json.dumps(songs)
        else:
            response.body = "No songs found in playlist"

    else:
        response.body = "API Client error"

    response.status = 200
    return response


run(app, host="", port=8080)