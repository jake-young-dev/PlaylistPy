import http.client
from urllib.parse import urlparse

userlink = "https://www.youtube.com/playlist?list=PL5WG4doTSrXSzrzgMa2HiLdqOnlBynVEH"


#SCRIPT START

playlist = urlparse(userlink)
if playlist.hostname == "" or playlist.query == "":
    print("That link was dogwater")
    exit()
if playlist.hostname != "www.youtube.com":
    print("Link needs to be a youtube playlist")
    exit()
host = playlist.hostname
path = playlist.path + "?" + playlist.query

connection = http.client.HTTPSConnection(playlist.hostname, http.client.HTTPS_PORT, timeout=10)
connection.request("GET", path)
res = connection.getresponse()

print()
print(connection)
print()
print("Recieved playlist: " + userlink)
print("Requesting playlist: " + str(res.status))

data = res.read().decode()
songs = []
chunks = data.split("\"")
for line in chunks:
    if "/watch?" in line and "index" in line:
        songs.append(host + line)

if len(songs) > 0:
    print("Playlist downloaded: " + str(len(songs)) + " songs")
    print()
else:
    print("No songs found in playlist")
    print()

connection.close()

print()
print("PLAYLIST")
print("***********************************")
for i, song in enumerate(songs):
    print(str(i) + ": " + song)
print("***********************************")








# import http.client

# conn = http.client.HTTPSConnection('www.youtube.com', http.client.HTTPS_PORT, timeout=10)
# print(conn)

# conn.request("GET", '/playlist?list=PL5WG4doTSrXSzrzgMa2HiLdqOnlBynVEH')
# res = conn.getresponse()
# data = res.read().decode()
# print(str(res.status))

# playlist = data.split('"')
# for song in playlist:
#     if "/watch?" in song and "index" in song:
#         print(song)


#faster and easier lol
# import requests

# res = requests.get("https://www.youtube.com/playlist?list=PL5WG4doTSrXSzrzgMa2HiLdqOnlBynVEH")
# test = str(res.content).split('"')
# for link in test:
#     if '/watch?' in link and "index" in link:
#         print(link)