from urllib.parse import urlparse
from helpers.database import findall, findone

def linkcheck(rawlink):
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


def getaplaylist(name):
    pl = findone(name)
    return pl["songs"]
    # songlinks = []
    # for item in pl:
    #     songlinks.append(item["songs"])
    # return songlinks


def getallplaylists():
    pl = findall()
    return pl