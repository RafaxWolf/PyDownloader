from pytubefix import YouTube
import urllib.request
import sys
import os

def thumbnail_downloader(url, path):
    try:
        yt = YouTube(url)

        thumb_url = yt.thumbnail_url
        if not thumb_url:
            print("[!] No thumbnail URL found for this video.\n")
            return
        
        filename = f"{yt.title}_thumbnail.jpg"
        filepath = os.path.join(path, filename)

        print(f"[+] Downloading thumbnail from URL: {thumb_url}\n")
        urllib.request.urlretrieve(thumb_url, filepath)
        print(f"[+] Thumbnail downloaded successfully: {filepath}\n")

    except Exception as e:
        print(f"[!] Error downloading thumbnail: {e}\n")

if __name__ == "__main__":
    print("[!] This file can't be executable out of the main file: app.py.\n")
    sys.exit(1)