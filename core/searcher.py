from pytubefix import YouTube
from pytubefix.cli import on_progress
import time
import sys

class AudioSearcher:
    def __init__(self, url):
        self.url = url

    def validate_url(self):
        if not self.url or self.url == "" or self.url == " ":
            print("[!] No URL provided. Exiting...\n")
            sys.exit(1)
        elif "youtube.com" not in self.url and "youtu.be" not in self.url and "music.youtube.com" not in self.url:
            print("[!] Invalid YouTube URL. Exiting...\n")
            sys.exit(1)

    def search_audio(self):
        self.validate_url()

        print(f"[+] Searching audio from URL: {self.url}")
        print()

        time.sleep(0.5)

        yt = YouTube(self.url, on_progress_callback=on_progress)
        audio_stream = yt.streams.get_audio_only()
        if audio_stream is None:
            print("[!] No audio stream found for this video.\n")
            sys.exit(1)

        print("[+] Search completed.\n")
        print(f"[+] Title: {yt.title}")
        print(f"[+] Author: {yt.author}")
        print(f"[+] Available audio streams:")
        print(f"    - itag: {audio_stream.itag}, mime_type: {audio_stream.mime_type}, abr: {audio_stream.abr}, type: {audio_stream.type}\n")