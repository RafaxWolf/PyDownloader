import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

def searcher(query):

    with open("config.json", 'r') as file:
        data = json.load(file)

        clientid = data["CLIENTID"]
        secret = data["CLIENT_SECRET"]
    
    print(clientid + " " + secret)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(clientid, secret))
    
    results = sp.search(query, 10)

    

if __name__ == "__main__":
    print("==== Spotify PyScrapper ====")
    print()
    song_name = input("[+] Ingrese nombre de la cancion: ")
    artist_name = input("[+] Ingrese nombre del artista: ")

    song_query = song_name + artist_name

    searcher(song_query)