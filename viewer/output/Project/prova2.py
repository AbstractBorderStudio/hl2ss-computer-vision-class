import cv2
import numpy as np

from matplotlib import pyplot as plt
from enum import Enum
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.morphology import *
from skimage.measure import label, regionprops
from skimage.color import rgb2gray
from math import sqrt
# read image
img = cv2.imread('frame0.png')

# convert img to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# do adaptive threshold on gray image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 55, 3)

blobs= blob_log(thresh, max_sigma=35, num_sigma=40, threshold=0.40)



print("A")
for circle in blobs:
                x, y, r = circle
                center = (int(x), int(y))
                
                result = cv2.circle(img, center, int(r), (255, 0,0), cv2.FILLED)


# display it
#cv2.imshow("IMAGE", img)
cv2.imshow("THRESHOLD", thresh)
#cv2.imshow("BLOB", blobs)


result1 = cv2.circle(img, (309,179), 5, (255, 0,0), cv2.FILLED)
cv2.imshow("RESULT", result1)
cv2.waitKey(0)
