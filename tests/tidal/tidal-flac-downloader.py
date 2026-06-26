import tidalapi
from pathlib import Path
from tidalapi import Quality

oauth_file = Path("tidal-oauth.json")

session = tidalapi.Session()
session.login_oauth_simple()

def tidal_scrapper(session, search_query):
    print("Scraping Tidal Library...")

    search_results = session.search(search_query, type='track', limit=10)
    first_track = search_results['tracks'][0]

    print(f"Found Track: {first_track.title} by {first_track.artist.name}")
    return first_track

if __name__ == "__main__":
    song_name = input("[+] Enter the song name: ")
    artist_name = input("[+] Enter the artist name: ")
    query = f"{song_name} {artist_name}"

    tidal_scrapper(session, query)