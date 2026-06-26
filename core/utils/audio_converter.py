from pydub import AudioSegment
import sys
import os

def convert_to_mp3(input_file, output_file):
    try:
        audio = AudioSegment.from_file(input_file, format="webm", codec="opus")
        audio.export(output_file, format="mp3")
        print(f"[+] Conversion to MP3 completed: {output_file}\n")

        os.remove(input_file)
        print(f"[+] Removed original file: {input_file}\n")
    except Exception as e:
        print(f"[!] Error during conversion: {e}\n")

if __name__ == "__main__":
    print("[!] This file can't be executable out of the main file: app.py.\n")
    sys.exit(1)