import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('C:/Users/jagan/OneDrive/Documents/testpaper.jpeg')

if img is None:
    print("Error: Could not load image")
else:
    text = pytesseract.image_to_string(img)
    print("Extracted text:")
    print(text)