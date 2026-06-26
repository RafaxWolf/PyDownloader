from ytmusicapi import YTMusic
import json
import signal
import sys

def signal_handler(sig, frame):
    print("\n[!] Search interrupted by user. Exiting...\n")
    sys.exit(0)

# CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Song
def searcher(song_name):
    # Song Searcher
    yt = YTMusic()

    search_results = yt.search(song_name, filter='songs')

    if not search_results:
        print("[!] Error: No results found.")
        return
    
    first_result = search_results[0]
    song_results = yt.get_song(first_result['videoId'])

    print(json.dumps(song_results, indent=4))

    # Extract song details
    song_title = first_result['title']
    artists = first_result['artists']

    # Obtener todos los artistas y separarlos con comas (excepto si ya tienen & o coma)
    song_artists = ', '.join([
        artist['name'] for artist in artists 
        if '&' not in artist['name'] and ',' not in artist['name']
    ]) or ', '.join([artist['name'] for artist in artists])
    
    album_name = first_result['album']['name'] if 'album' in first_result else 'N/A'
    album_id = first_result['album']['id'] if 'album' in first_result else 'N/A'
    video_id = first_result['videoId']
    song_url = f"https://music.youtube.com/watch?v={video_id}" 

    print("\n[+] Search completed successfully.\n")
    print(f"[+] Found song:\nTitle: {song_title}\nArtist: {song_artists}\nAlbum: {album_name}\nAlbum ID: {album_id}\nURL: {song_url}")

    # Album Searcher
    album_search_opt = input("\n[+] Buscar informacion del album? (y/n)\n>> ")
    if(album_search_opt.lower() == "y"):
        album_info = yt.get_album(album_id)

        print(json.dumps(album_info, indent=4))


    else:
        print("[+] Saliendo...")



if __name__ == "__main__":
    """ song = input("[+] Enter the song name to search: ").strip()
    artist = input("[+] Enter the artist name (optional): ").strip() """
    
    song = "Ohtami"
    artist = "Eladio Carrion"
    if artist:
        song += f" {artist}"
    searcher(song)