import cv2
import easyocr
import pytesseract
from utils.scorer import score

reader = easyocr.Reader(["en"], gpu=False)

def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.GaussianBlur(gray, (3,3), 0)

def run_ocr_pipeline(image):
    image = preprocess(image)

    texts_easy = [r[1] for r in reader.readtext(image)]
    texts_tess = pytesseract.image_to_string(image).splitlines()

    all_texts = texts_easy + texts_tess
    confidence = score(all_texts)

    return all_texts, confidence
