import sys
from PIL import Image
import pytesseract

sys.stdout.reconfigure(encoding="utf-8")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if len(sys.argv) < 2:
    print("No image")
    sys.exit(1)

ruta_imagen = sys.argv[1]

try:
    img = Image.open(ruta_imagen).convert("L")
    texto = pytesseract.image_to_string(img, lang="spa")
    print(texto)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)