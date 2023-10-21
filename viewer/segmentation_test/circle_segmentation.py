import cv2
import numpy as np
from matplotlib import pyplot as plt

path = './frame80.png'

src = cv2.imread(path)

# kernel di smoothing 5x5
k = np.ones((5,5),np.float32)/25

# grayscale image
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Apply a smoothing kernel to make gaussian blur
# this reduce noise. Improves edge detection.
smoothed = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT)

# compute Canny edge detection for both normal and smoothed source.
# As we can see the smoothed one cathes better circle's edges
edges = cv2.Canny(gray, 100, 150, apertureSize=3)
edges_smoothed = cv2.Canny(smoothed, 100, 150, apertureSize=3)

# apply dialtion to highlight circlular areas.
dilation = cv2.dilate(edges, np.ones((2,2)), iterations=1)
dilation_smoothed = cv2.dilate(edges_smoothed, np.ones((2,2)), iterations=1)

# apply hough transform to detect circles
circles = cv2.HoughCircles(dilation, cv2.HOUGH_GRADIENT, dp=1, minDist=5, param1=150, param2=20, minRadius=10)
circles_smoothed = cv2.HoughCircles(dilation_smoothed, cv2.HOUGH_GRADIENT, dp=1, minDist=5, param1=150, param2=20, minRadius=10)

# add circles to images
for circle in circles[0,:]:
    x, y, r = circle
    center = (x,y)
    cv2.circle(gray, (int(x), int(y)), int(r), (255,0,0), cv2.FILLED)

for circle in circles_smoothed[0,:]:
    x, y, r = circle
    center = (x,y)
    cv2.circle(smoothed, (int(x), int(y)), int(r), (255,0,0), cv2.FILLED)
 
# ---------------------------- disply result ---------------------------- 
plt.subplot(231), plt.imshow(edges)#, cmap="gray")
plt.title("canny"), plt.axis("off")
plt.subplot(234), plt.imshow(edges_smoothed)#, cmap="gray")
plt.title("canny smoothed"), plt.axis("off")
plt.subplot(232), plt.imshow(dilation)#, cmap="gray")
plt.title("dilation"), plt.axis("off")
plt.subplot(235), plt.imshow(dilation_smoothed)#, cmap="gray")
plt.title("dilation smoothed"), plt.axis("off")
plt.subplot(233), plt.imshow(gray)
plt.title("detection"), plt.axis("off")
plt.subplot(236), plt.imshow(smoothed)
plt.title("detection smoothed"), plt.axis("off")
plt.show()