import cv2
import math


def findContours(image) -> list:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)[1]

    contour = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    boundClients = list()
    if len(contour) <= 6 and len(contour) > 3:
        for c in contour:
            x, y, w, h = cv2.boundingRect(c)
            if w > h:
                amount = (math.floor(w/24))
                w = (math.ceil(w/amount))
                for i in range(amount):
                    boundClients.append([x+(w*i), y, w, h])
            else:
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 1)
                boundClients.append([x, y, w, h])
    boundClients.sort(key=lambda x: x[0])
    return boundClients


def crop(image, dim):
    return image[dim[1]:dim[1] + dim[3], dim[0]: dim[0] + dim[2]]
