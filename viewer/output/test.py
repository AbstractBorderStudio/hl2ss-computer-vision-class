import numpy as np
import cv2
from matplotlib import pyplot as plt 

path = 'test.txt'

# data = np.loadtxt(path, dtype=np.uint16)

# cv2.imshow("gne", data/np.max(data))
# cv2.waitKey(0)

path = 'imgs/frame0.png'
im = cv2.imread(path)
plt.imshow(im/255)
plt.show()
