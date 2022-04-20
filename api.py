import http.client
from urllib.parse import urlparse
import json
from bottle import Bottle, run, request

app = Bottle()

@app.post("/playlist")
def playlistHandler():
    print()
    print("/playlist")
    rawpl = request.body.read().decode()

    playlist = json.loads(rawpl)
    link = urlparse(playlist["playlist"])
    host = link.hostname
    path = link.path + "?" + link.query

    if host == "None" or path == "None":
        return "That link is dogwater"
    if host != "www.youtube.com":
        return "Playlist needs to be a public or unlisted Youtube playlist"

    connection = http.client.HTTPSConnection(host, http.client.HTTPS_PORT, timeout=10)
    connection.request("GET", path)
    res = connection.getresponse()

    print(connection)
    print("Recieved playlist: " + playlist["playlist"])
    print("Requesting playlist: " + str(res.status))

    data = res.read().decode()
    songs = []
    chunks = data.split("\"")
    for line in chunks:
        if "/watch?" in line and "index" in line:
            songs.append(host + line)
    
    if len(songs) > 0:
        print("Playlist downloaded: " + str(len(songs)) + " songs")
    else:
        print("No songs found in playlist")

    connection.close()
    return songs


run(app, host="localhost", port=8080)