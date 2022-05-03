from pymongo import MongoClient

db = MongoClient('mongodb://localhost:27017/').web_db


def findall():
    playlists = []
    for doc in db.playlists.find({}, {"_id": False}):
        playlists.append(doc)

    return playlists


def find(name):
    playlists = []
    for doc in db.playlists.find({"name": name}, {"_id": False}):
        playlists.append(doc)
    
    if len(playlists) > 0:
        return playlists
    else:
        return None