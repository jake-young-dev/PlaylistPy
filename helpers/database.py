from pymongo import MongoClient

def test():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.web_db
    for doc in db.playlists.find({}):
        print(doc)
    # print(db.playlists.find({}))
    client.close()

def findallplaylists():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.web_db

    playlists = []
    for doc in db.playlists.find({}):
        playlists.append(doc['name'])

    return playlists