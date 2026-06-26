from pytubefix import YouTube
from pytubefix.cli import on_progress
from core.providers.base_provider import BaseProvider
import os

class YouTubeProvider(BaseProvider):
    def supports(self, url):
        return ("youtube.com" in url
                 or "youtu.be" in url 
                 or "youtube-nocookie.com" in url
                 or "music.youtube.com" in url
        )
    
    def download(self, url: str, path: str, audio_format: str = "mp3"):
        print(f"[+] Downloading YouTube audio from URL: {url}")

        yt = YouTube(url, on_progress_callback=on_progress)
        audio_stream = yt.streams.filter(only_audio=True).last()

        if audio_stream is None:
            raise ValueError("[!] No audio stream found for this video.\n")
        
        downloaded_file = audio_stream.download(output_path=path)
        print(f"[+] Download finished.\n")
        print(f"- Title: {yt.title}")
        print(f"- Author: {yt.author}")
        print(f"- Saved at: {downloaded_file}")
        #print(f"[+] Download finished, converting to {audio_format}...\n")
    
    def search(self, url: str):
        yt = YouTube(url, on_progress_callback=on_progress)
        audio_streams = yt.streams.filter(only_audio=True)

        if not audio_streams:
            raise ValueError("[!] No audio streams found for this video.\n")
        
        print(f"[+] Available audio streams for '{yt.title}':\n")
        for stream in audio_streams:
            print(f"- itag: {stream.itag}, mime_type: {stream.mime_type}, abr: {stream.abr}, type: {stream.type}")