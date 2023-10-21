import cv2
import numpy as np
from matplotlib import pyplot as plt

path = 'test_images/solidWhiteCurve.jpg'

src = cv2.imread(path)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,150,450,apertureSize = 3)
#dilate = cv2.dilate(edges, np.ones((2,2)), iterations=1)
lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=10,minLineLength=1,maxLineGap=10)

res = src
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(res,(x1,y1),(x2,y2),(0,255,0),1)

# visualizzation

plt.subplot(121),plt.imshow(edges)
plt.title("edges"),plt.axis("off")
plt.subplot(122),plt.imshow(res)
plt.title("resoult"),plt.axis("off")

plt.show()