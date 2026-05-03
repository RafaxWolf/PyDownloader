from ytmusicapi import YTMusic

class YTMusicScrapper:
    def __init__(self, song_name, artist_name=None):
        self.yt = YTMusic()
        self.song_name = song_name
        self.artist_name = artist_name

    def search_song(self):
        search_results = self.yt.search(self.song_name, filter='songs')

        if not search_results:
            raise ValueError("No results found.")

        first_result = search_results[0]

        song_info = {
            'title': first_result['title'],
            'artists': [artist['name'] for artist in first_result['artists']],
            'album_name': first_result['album']['name'] if 'album' in first_result else 'N/A',
            'album_id': first_result['album']['id'] if 'album' in first_result else 'N/A',
            'video_id': first_result['videoId'],
            'song_url': f"https://music.youtube.com/watch?v={first_result['videoId']}"
        }

        return song_info