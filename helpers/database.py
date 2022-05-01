from pymongo import MongoClient

def test():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.web_db
    for doc in db.playlists.find({}):
        print(doc)
    # print(db.playlists.find({}))
    client.close()

def findall():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.web_db

    playlists = []
    for doc in db.playlists.find({}):
        playlists.append(doc)

    return playlists

def findone(name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.web_db
    playlists = []
    for doc in db.playlists.find({"name": name}):
        playlists.append(doc)
    
    if len(playlists) > 0:
        return playlists[0]
    else:
        return None