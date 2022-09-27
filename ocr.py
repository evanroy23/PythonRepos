
import os
from PIL import Image
from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\workspace\Tesseract-OCR\tesseract'
print( pytesseract.image_to_string('./2019.jpg', lang='kor+eng', config='-c preserve_interword_spaces=1 --psm 4') )