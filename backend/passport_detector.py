import cv2
import numpy as np
import pytesseract
from transliterate import translit, get_available_language_codes
import ner

class ExtractorOwner:
    extractor = None
    def __init__(self):
        if ExtractorOwner.extractor is None:
            ExtractorOwner.extractor = ner.Extractor()
        self.extractor = ExtractorOwner.extractor


def has_photo(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    if len(faces):
        return faces
    return None

def detect_field(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
    gradX = cv2.Sobel(blackhat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = np.absolute(gradX)
    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
    gradX = (255 * ((gradX - minVal) / (maxVal - minVal))).astype("uint8")
    gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
    thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
    thresh = cv2.erode(thresh, None, iterations=4)
    p = int(gray.shape[1] * 0.05)
    thresh[:, 0:p] = 0
    thresh[:, gray.shape[1] - p:] = 0
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        crWidth = w / float(gray.shape[1])
        
        if ar > 5 and crWidth > 0.75:
            pX = int((x + w) * 0.03)
            pY = int((y + h) * 0.03)
            (x, y) = (x - pX, y - pY)
            (w, h) = (w + (pX * 2), h + (pY * 2))
            roi = image[y:y + h, x:x + w].copy()
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            return roi
    return None

def replace_strange_symbol(s):
    s = translit(s, 'ru')
    s = s.replace('3', 'ч')
    s = s.replace('£', 'е')
    s = s.replace('6', 'г')
    s = s.replace('¢', 'й')
    return s

def extract_person(s):
    m = map(lambda x : ' '.join(map(lambda token : token.text, x.tokens)), filter(lambda x : x.type=='PER', ExtractorOwner().extractor(txt)))
    return list(m)

def symbol2space(s, c):
    return ' '.join(filter(lambda x : len(x) > 0, s.split(c)))


def has_fields(img):
    roi = detect_field(img)
    txt_main = pytesseract.image_to_string(roi)
    txt_main = symbol2space(txt_main.lower(), '<')
    txt_main = replace_strange_symbol(txt_main)
    person = ' '.join(extract_person(txt_main))
    person = symbol2space(person, ' ').split()
    if len(person) > 0 and has_photo(img):
        return person
    return None

