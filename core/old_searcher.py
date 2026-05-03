"""
Este módulo está deprecado. Utilice **`PyDownloader.core.searcher`** en su lugar.

Módulo PyDownloader.core.old_searcher

Este módulo proporciona funcionalidad para buscar flujos de audio desde URLs de YouTube utilizando la biblioteca pytubefix.

Copyright (C) 2026 RafaxWolf
"""

from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys
import time

def search_audio(url):
    if not url or url == "" or url == " ":
        print("[!] No URL provided. Exiting...\n")
        sys.exit(1)
    elif "youtube.com" not in url and "youtu.be" not in url and "music.youtube.com" not in url:
        print("[!] Invalid YouTube URL. Exiting...\n")
        sys.exit(1)

    print(f"[+] Searching audio from URL: {url}")
    print()

    time.sleep(0.5)

    yt = YouTube(url, on_progress_callback=on_progress)
    #audio_stream = yt.streams.filter(only_audio=True,mime_type="audio/webm")
    audio_stream = yt.streams.last()
    if audio_stream is None:
        print("[!] No audio stream found for this video.\n")
        sys.exit(1)

    print("[+] Search completed.\n")
    print(f"[+] Title: {yt.title}")
    print(f"[+] Author: {yt.author}")
    print(f"[+] Available audio streams:")
    print(audio_stream)
    # print(f"    - itag: {audio_stream.itag}, mime_type: {audio_stream.mime_type}, abr: {audio_stream.abr}, type: {audio_stream.type}\n") 


if __name__ == "__main__":
    print("[!] This file can't be executable out of the main file: app.py.\n")
    sys.exit(1)