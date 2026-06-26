from PIL import Image
import glob, os

img_folder = "img"
extensions = ("*.jpg", "*.jpeg", "*.webp")

img_files = []

for ext in extensions:
    pattern = os.path.join(img_folder, ext)
    img_files.extend(glob.glob(pattern))

print(f"Contenido en {img_folder}:\n{img_files}")

select_img = input("[+] Ingrese nombre de imagen: ")
file_name, file_ext = os.path.splitext(select_img)

file_path = os.path.join(img_folder, select_img)

img = Image.open(file_path).convert("RGB")
img.save(f"./{img_folder}/{file_name}.png", "png")