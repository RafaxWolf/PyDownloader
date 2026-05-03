"""
Modulo PyDownloader.core.downloader\n
Este modulo proporciona funcionalidad para descargar streams de audio desde URLs de YouTube utilizando la libreria pytubefix.

Copyright (C) 2026 RafaxWolf
"""

from pytubefix import YouTube
from pytubefix.cli import on_progress
from core.utils.mp3_converter import convert_to_mp3
from core.utils.thumbnail_scrapper import thumbnail_downloader
import time
import sys
import os


def download_audio(url, path):
    print(f"[+] Downloading audio from URL: {url}")
    print(f"[+] Saving to path: {path}\n")

    time.sleep(0.05)

    yt = YouTube(url, on_progress_callback=on_progress)
    audio_stream = yt.streams.filter(only_audio=True).last()
    if audio_stream is None:
        print("[!] No audio stream found for this video.\n")
        sys.exit(1)

    if os.path.exists(yt.title):
        print("[!] Audio file already exists. Exiting to avoid overwrite.\n")
        sys.exit(1)

    print(f"    - itag: {audio_stream.itag}, mime_type: {audio_stream.mime_type}, abr: {audio_stream.abr}, type: {audio_stream.type}")

    print("[+] Downloading...\n")

    audio_stream.download(output_path=path)

    time.sleep(0.05)

    print("[+] Download finished, converting to mp3...\n")

    time.sleep(0.05)

    downloaded_file = os.path.join(path, audio_stream.default_filename)
    new_file_path = os.path.join(path, f"{yt.title}.mp3") or downloaded_file

    # convert_to_mp3(downloaded_file, new_file_path)

    print("[+] Download completed successfully.\n")
    print(f"[+] Title: {yt.title}")
    print(f"[+] Author: {yt.author}")
    print(f"[+] Saved at: {new_file_path}")
    print()

    opts = input("[+] Do you want to download the thumbnail? (y/n): ").strip().lower()

    if opts == "y":
        thumbnail_downloader(url, path)
    else:
        print("[+] Thumbnail download skipped.\n")


if __name__ == "__main__":
    print("[!] This file can't be executable out of the main file: app.py.\n")
    sys.exit(1)