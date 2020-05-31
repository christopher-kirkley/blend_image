import cv2 as cv
import numpy as np

from helpers import resize



file_ = 'source/4.jpg'

img = cv.imread(file_, cv.IMREAD_UNCHANGED)
img = resize(img, (500,500))
print(img.shape)
cv.imshow('image', img)
cv.waitKey(0)

