import cv2 
from matplotlib import pyplot as plt
import numpy as np

src = cv2.imread('./snowy-street.jpg')
d = cv2.dilate(src, kernel=np.ones((2,2)), iterations=3) # ingrandisci la neve
e = cv2.erode(src, kernel=np.ones((2,2)), iterations=3) # elimina i fiocchi di neve

plt.subplot(131), plt.imshow(src)
plt.title('src'), plt.axis("off")
plt.subplot(132), plt.imshow(d)
plt.title('dilate'), plt.axis("off")
plt.subplot(133), plt.imshow(e)
plt.title('dilate'), plt.axis("off")

plt.show()