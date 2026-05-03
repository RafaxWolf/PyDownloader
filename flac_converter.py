from pydub import AudioSegment
import signal
import glob
import sys
import os

def signal_handler(sig, frame):
    print()
    print("[!] Operacion cancelada por el usuario.")
    print("[!] Saliendo...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def list_audio_files(musicFolder, debug = False):
    extensions = (".m4a")
    musicFiles = []

    if (debug):
        print("[*] Debug Extensions: " + str(extensions))

    for ext in extensions:
        if (debug):
            print("[*] Debug Pattterns: " + ext)

        pattern = os.path.join(musicFolder, f"*{ext}")
        musicFiles.extend(glob.glob(pattern))

    print(f"[+] Canciones sin convertir en '{musicFolder}':")
    print(*musicFiles, sep="\n", end="\n")


def convert_to_flac(input_file):
    try:
        if (not ".m4a" in input_file):
            input_file = input_file+".m4a"

        print(f"[+] Converting {input_file} to FLAC format...\n")
        
        audio = AudioSegment.from_file(input_file, format="webm", codec="opus")
        output_file = os.path.splitext(input_file)[0] + ".flac"
        print(f"[+] Output FLAC file will be: {output_file}\n")

        audio.export(output_file, format="flac", parameters=[
            "-ar",
            "44100",
            "-sample_fmt",
            "s16",
            "-compression_level",
            "8"
        ])

        print(f"[+] Conversion to FLAC completed: {output_file}\n")

    except Exception as e:
        print(f"[!] Error during conversion: {e}\n")
        sys.exit(1)



if __name__ == "__main__":
    usrInput = input("[+] Ingresa la carpeta donde se encuentren los archivos de musica (m4a) a convertir: ")

    if(usrInput == "" or usrInput == " " or not os.path.isdir(usrInput)):
        print("[!] Carpeta ingresada invalida.")
        print("[!] Utilizando carpeta por defecto.")
        folder = "Audio"
    else:
        # print("[+] Carpeta encontrada.")
        folder = usrInput

    list_audio_files(folder, debug=True)
    selectedSong = input("[+] Ingrese nombre de cancion a convertir: ")
    filepath = os.path.join(folder, selectedSong)

    convert_to_flac(filepath)

