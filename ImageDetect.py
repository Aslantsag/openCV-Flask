import cv2
import pytesseract


class ImageDetect:

    def __init__(self, image):
        self.image = cv2.imread('upload/' + image)
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def detect_faces(self, image):
        faces_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faces_db.detectMultiScale(self.gray_image, 1.1, 19)
        for x, y, w, h in faces:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.imwrite('static/' + image, self.image)

    def detect_eyes(self, image):
        eyes_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        eyes = eyes_db.detectMultiScale(self.gray_image, 1.1, 19)
        for x, y, w, h in eyes:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.imwrite('static/' + image, self.image)

    def detect_text(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(gray)
        return text
