import cv2
import numpy as np
from matplotlib import pyplot as plt

path = './frame80.png'

src = cv2.imread(path)

# kernel di smoothing 5x5
k = np.ones((5,5),np.float32)/25

# grayscale image
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny_edges = cv2.Canny(gray,100,300,apertureSize = 3)

x = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3)
y = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3)
sobel_edges = cv2.addWeighted(x, 0.5, y, 0.5, 0.0)

canny_sobel = cv2.Canny(sobel_edges,100,110,apertureSize = 3)
 
plt.subplot(121), plt.imshow(canny_edges)
plt.subplot(122), plt.imshow(sobel_edges, cmap="gray")
plt.show()