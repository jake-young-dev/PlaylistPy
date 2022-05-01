from pymongo import MongoClient

def test():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.web_db
    print(db.playlists.find({}))
    client.close()