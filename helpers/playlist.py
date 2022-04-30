from urllib.parse import urlparse

def linkcheck(rawlink): #returns str's host, error
    link = urlparse(rawlink)
    host = link.hostname
    path = link.path + "?" + link.query

    if host == None or path == None:
        #bad link
        return "That link is dogwater"
    if host != "www.youtube.com":
        #not yt
        return "Playlist needs to be public or unlisted YouTube playlist"
    
    return None


def playlistsplit(pl):
    songs = []
    chunks = pl.split("\"")

    for line in chunks:
        if "/watch?" in line and "index" in line:
            songs.append("https://www.youtube.com" + line)

    return songs