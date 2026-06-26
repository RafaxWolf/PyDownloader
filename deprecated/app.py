from deprecated.downloader import download_audio
from deprecated.old_searcher import search_audio
# from core.searcher import search_audio
import signal
import os
import sys

# Signal Handler for Graceful Exit
def signal_handler(sig, frame):
    print("\n[!] Search interrupted by user. Exiting...\n")
    sys.exit(0)

# CTRL+C
signal.signal(signal.SIGINT, signal_handler)

###* PyDownloader Functions ###

# Path Verification
def existing_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

def verify_path(pre_save):
    # If no path is provided or invalid, use default "Audio" folder in current directory
    if not pre_save or not os.path.isdir(pre_save) or pre_save == "" or pre_save == "." or pre_save == "./" or pre_save == " ":
        default_path = os.getcwd() + "/Audio"

        existing_path(default_path)
        save_path = default_path

        # If valid path is provided, use it
    else:
        existing_path(pre_save)
        save_path = pre_save

    return save_path

# Display Menu
def menu_text():
    print("\n╔══════════════════════════════════════════════════════╗")
    print("║                YouTube PyDownloader                  ║")
    print("║                  Made by RafaxWolf                   ║")
    print("║                     Version 3.0                      ║")
    print("╚══════════════════════════════════════════════════════╝\n")
    print("1) Download YouTube Audio")
    print("2) Search YouTube Audio Streams")
    print("3) Exit\n")

# Menu Selector
def main_menu():
    try:
        menu_text()
        opts = int(input("[+] Select an option: "))
    except ValueError:
        print("\n[!] Invalid input. Please enter a number corresponding to the options.\n")
        return main_menu()

    return opts

# Main Execution
if __name__ == "__main__":
    while True:
        selected_opt = main_menu()
        match selected_opt:
            case 1:
                # Get user inputs
                yt_url = input("[+] Enter the YouTube video/audio URL: ").strip()
                pre_save = input("[+] Enter the directory to save the audio (default is current directory): ").strip()

                # Verify and set download path
                download_path = verify_path(pre_save)

                # Starts the downloading process
                download_audio(yt_url, download_path)
                break
            
            case 2:
                # Get user input for searching audio streams
                yt_url = input("[+] Enter the YouTube video/audio URL: ").strip()
                search_audio(yt_url)
                break
            
            case 3:
                print("\n[+] Exiting from YT PyDownloader...\n")
                break
            
            case _:
                print("\n[!] Invalid option selected. Please try again.\n")