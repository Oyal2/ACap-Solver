import numpy as np
import urllib
import cv2
from PIL import Image
import os
from tensorflow import expand_dims
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model
from amazoncaptcha.utils import findContours, crop


class AmazonCaptchaSolver():
    def __init__(self):
        self.model = load_model(os.path.join(
            os.path.dirname(__file__), "expectedModel.hdf5"))
        self.letters = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'J',
                        'K', 'L', 'M', 'N', 'P', 'R', 'T', 'U', 'X', 'Y']

    def getCaptchaImage(self, url):
        if len(url) == 0:
            return ""
        resp = urllib.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image

    def predict(self, img: Image):
        image = Image.fromarray(img)
        image = image.resize((227, 227))
        img_array = img_to_array(image)
        img_array = expand_dims(img_array, 0)
        predictions = self.model.predict(img_array)[0]
        return self.letters[np.argmax(predictions)]

    def solve(self, Url=None, Image=None):
        if Image is None:
            Image = self.getCaptchaImage(Url)

        contours = findContours(image=Image)
        finalAnswer = ""
        for contour in contours:
            newImage = crop(Image, contour)
            prediction = self.predict(newImage)
            finalAnswer += prediction
        return finalAnswer
